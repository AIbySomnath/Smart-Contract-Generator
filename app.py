import os
import openai
import streamlit as st

# Set your OpenAI API key here
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("📝 Smart Contract Generator")
st.subheader("Generate Solidity Smart Contracts Using Natural Language")

# Sidebar for contract type selection
st.sidebar.title("Settings")
contract_type = st.sidebar.selectbox(
    "Select Contract Type",
    ["ERC20 Token", "Voting System", "Custom"],
)

st.sidebar.write("Describe your smart contract use case below.")

# User Input
scenario = st.text_area(
    "Describe Your Smart Contract Scenario",
    "Example: Create a voting contract where each voter can vote once for a specific candidate."
)


def generate_solidity_code(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Generate a Solidity smart contract for: {prompt}",
            max_tokens=200
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)


if st.button("Generate Smart Contract"):
    if not scenario.strip():
        st.warning("⚠️ Please provide a valid contract description.")
    else:
        if contract_type == "ERC20 Token":
            solidity_code = """
            // SPDX-License-Identifier: MIT
            pragma solidity ^0.8.0;

            contract Token {
                string public name = "Sample Token";
                string public symbol = "SMT";
                uint256 public totalSupply = 1000000;

                mapping(address => uint256) public balances;

                constructor() {
                    balances[msg.sender] = totalSupply;
                }

                function transfer(address to, uint256 amount) public {
                    require(balances[msg.sender] >= amount, "Not enough tokens");
                    balances[msg.sender] -= amount;
                    balances[to] += amount;
                }

                function burn(uint256 amount) public {
                    require(balances[msg.sender] >= amount, "Not enough tokens");
                    balances[msg.sender] -= amount;
                    totalSupply -= amount;
                }
            }
            """
        elif contract_type == "Voting System":
            solidity_code = """
            // SPDX-License-Identifier: MIT
            pragma solidity ^0.8.0;

            contract Voting {
                struct Candidate {
                    string name;
                    uint256 votes;
                }

                Candidate[] public candidates;
                mapping(address => bool) public hasVoted;

                function addCandidate(string memory name) public {
                    candidates.push(Candidate(name, 0));
                }

                function vote(uint256 candidateIndex) public {
                    require(!hasVoted[msg.sender], "Already voted");
                    candidates[candidateIndex].votes += 1;
                    hasVoted[msg.sender] = true;
                }
            }
            """
        else:
            solidity_code = generate_solidity_code(scenario)

        st.success("✅ Smart Contract Generated!")
        st.code(solidity_code, language="solidity")

        # Download button
        st.download_button(
            "⬇️ Download Smart Contract",
            solidity_code,
            file_name="smart_contract.sol",
            mime="text/plain",
        )