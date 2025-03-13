import subprocess


def validate_solidity_code(solidity_code):
    with open("temp_contract.sol", "w") as f:
        f.write(solidity_code)

    try:
        result = subprocess.run(["solc", "--strict-assembly", "temp_contract.sol"], capture_output=True, text=True)
        return result.returncode == 0, result.stdout + result.stderr
    finally:
        subprocess.run(["rm", "temp_contract.sol"])


# Example usage
solidity_code = """
pragma solidity ^0.8.0;

contract MyToken {
    string public name = "MyToken";
    string public symbol = "MTK";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1000000 * (10 ** uint256(decimals));
    mapping(address => uint256) public balanceOf;

    constructor() {
        balanceOf[msg.sender] = totalSupply;
    }

    function transfer(address to, uint256 value) public returns (bool) {
        require(balanceOf[msg.sender] >= value, "Insufficient balance");
        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;
        return true;
    }

    function burn(uint256 value) public returns (bool) {
        require(balanceOf[msg.sender] >= value, "Insufficient balance");
        totalSupply -= value;
        balanceOf[msg.sender] -= value;
        return true;
    }
}
"""

is_valid, output = validate_solidity_code(solidity_code)
if is_valid:
    print("The Solidity code is valid.")
else:
    print("The Solidity code is invalid.")
    print(output)