# Project Installation Instructions

This guide will help you set up and install the project on your system.

## Prerequisites

Before running the installation script, make sure you have the following installed and configured:

- **Python 3**  
  Ensure Python 3 is installed and available in your PATH. You can check with:
  ```bash
  python3 --version
  ```

- **WireGuard**  
    You need a configured WireGuard setup with:

    - Private key
    - IP address

    Replace the placeholders in the provided configuration file with your actual WireGuard private key and IP address before running the installation.

    ```bash
    webari.conf
    ```

## Installation

1. **Make the installation script executable:**  
    ```bash
    sudo chmod +x ./install.sh
    ```
2. **Run the installation script:**  
    ```bash
    ./install.sh
    ```

### The script will:
- Install all necessary dependencies (WireGuard itself)
- Create an application/service that will automatically run at system startup.
