# 📝 Smart Contract Generator

Generate Solidity Smart Contracts Using Natural Language.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Testing Methods](#testing-methods)
- [Design Rationale](#design-rationale)
- [Screenshots](#screenshots)

## Introduction

This project provides a web interface to generate Solidity smart contracts from natural language descriptions. It leverages OpenAI's GPT-4 API to generate code based on user input and offers predefined templates for common contract types such as ERC-20 tokens and voting systems.

## Features

- Generate Solidity smart contracts from text descriptions.
- Supports predefined contract types (ERC-20 Token, Voting System).
- Custom contract generation using GPT-4.
- Download generated contracts as `.sol` files.

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- Streamlit
- OpenAI API Key

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/smart-contract-generator.git
    cd smart-contract-generator
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up your OpenAI API Key:
    - For Unix-based systems:
        ```sh
        export OPENAI_API_KEY="your-openai-api-key"
        ```
    - For Windows:
        ```cmd
        set OPENAI_API_KEY=your-openai-api-key
        ```

5. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

## Usage

1. Open your web browser and navigate to the URL provided by Streamlit (typically `http://localhost:8501`).
2. Select the contract type from the sidebar.
3. Enter a description of your smart contract scenario.
4. Click the "Generate Smart Contract" button.
5. Review the generated Solidity code.
6. Download the generated smart contract using the download button.

## Testing Methods

### Unit Testing

Unit tests are provided to validate the functionality of the smart contract generation. To run the tests, use the following command:

```sh
pytest tests/
```

### Solidity Syntax Validation

The generated Solidity code is validated for syntax correctness using `solc`. Ensure you have the Solidity compiler installed and run:

```sh
python test_solidity.py
```

## Design Rationale

The primary design goal of this project was to create a user-friendly interface for generating Solidity smart contracts. Key considerations include:

- **Simplicity:** The interface is straightforward, allowing users to generate contracts with minimal input.
- **Flexibility:** Supports predefined contract types and custom contract generation using natural language input.
- **Extensibility:** The modular design enables easy addition of new contract templates and features.

## Screenshots

### Main Interface

![Main Interface](screenshots/main_interface.png)

### Generated Contract

![Generated Contract](screenshots/generated_contract.png)

### Download Button

![Download Button](streamlit-app-2025-03-13-15-03-53.webm)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) guide for more details.

## Acknowledgments

- OpenAI for providing the GPT-4 API.
- Streamlit for the amazing web framework.
