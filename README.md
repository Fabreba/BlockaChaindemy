# BlockaChaindemy
# Academic Records Management System on Blockchain

Welcome to the Academic Records Management System on Blockchain, a project built using Python, Solidity, and Brownie. This system allows for secure and transparent storage of academic records and diplomas using blockchain technology, with RBAC (Role-Based Access Control) implemented to ensure only authorized personnel can manage and validate records.

## Overview

The main objective of this project is to provide a decentralized and tamper-proof solution for academic records management, improving the integrity and accessibility of these records. It utilizes smart contracts to store and manage the data and includes an RBAC system to differentiate between different user roles.

## Features

- **Blockchain Storage**: Academic records are stored on the Ethereum blockchain, ensuring transparency and data integrity.
- **RBAC**: Role-Based Access Control allows specific roles (e.g., student, registrar, verifier) to access and manage the data appropriately.
- **Python & Solidity**: The core is developed using Python and Solidity, with Brownie as the framework to simplify the smart contract development process.

## Project Structure

- `contracts/`: Contains the Solidity smart contracts that implement the academic records system and the RBAC logic.
- `scripts/`: Python scripts for deploying, testing, and managing the smart contracts.
- `tests/`: Test cases implemented to ensure the correctness and security of the system.
- `brownie-config.yaml`: Configuration file for the Brownie framework.

## Requirements

- [Python](https://www.python.org/)
- [Node.js](https://nodejs.org/)
- [Brownie](https://eth-brownie.readthedocs.io/)
- An Ethereum development environment like [Ganache](https://trufflesuite.com/ganache/)

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/academic-records-management-blockchain.git
    cd academic-records-management-blockchain
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Start an Ethereum development network (e.g., Ganache).

4. Compile the smart contracts:
    ```bash
    brownie compile
    ```

5. Deploy the contracts to the local blockchain:
    ```bash
    brownie run scripts/deploy.py
    ```

6. Execute tests to verify the functionality:
    ```bash
    brownie test
    ```

## How It Works

### Smart Contracts

- **AcademicRecords.sol**: Manages the storage and retrieval of academic records and diplomas.
- **RBAC.sol**: Implements Role-Based Access Control to differentiate between roles and authorize specific actions.

### User Roles

- **Student**: Can view their own academic records and request verification.
- **Registrar**: Manages the addition and verification of academic records.
- **Verifier**: Verifies the authenticity of academic records.

## Contributing

Contributions are welcome! Please follow the steps below:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your branch to your forked repository.
5. Create a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

