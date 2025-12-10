# Project Overview

This project is a graphical user interface (GUI) tool for ADB (Android Debug Bridge) and Fastboot commands. It's written in Python and uses the `customtkinter` library to provide a user-friendly interface for interacting with Android devices.

The application allows users to execute a wide range of ADB and Fastboot commands without using the command line. All commands are run in separate threads to keep the GUI responsive.

# Building and Running

## Prerequisites

- Python 3.x
- ADB and Fastboot binaries installed and accessible in your system's PATH.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/parrots-14/ADB-GUI-Tool.git
    cd ADB-GUI-Tool
    ```

2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the application

```bash
python init.py
```

# Development Conventions

- The application is structured into three main modules:
    - `src/GUI.py`: Handles the user interface.
    - `src/ADB.py`: Manages the logic for executing commands.
    - `src/commands.py`: Contains the raw ADB and Fastboot commands.
- Commands are executed in separate threads to prevent the GUI from freezing.
- The UI is built with `customtkinter` for a modern look and feel.
