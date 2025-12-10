# ADB GUI Tool

**Warning:** This tool has the potential to brick your phone if not used carefully. Proceed with caution.

A user-friendly graphical interface for ADB (Android Debug Bridge) and Fastboot commands, designed to simplify interaction with your Android device without the need for a terminal.

![App Screenshot](https://imgur.com/a/msSYeJF)

## What is this?

This is a Python-based GUI tool that allows you to execute common ADB and Fastboot commands through a simple point-and-click interface. It's an alternative to the command line for managing your Android device. All commands are run in separate threads, so the GUI remains responsive while commands are executing.

## Project Structure
The project is organized as follows:
- **`init.py`**: The main entry point for the application.
- **`src/GUI.py`**: Defines the graphical user interface.
- **`src/ADB.py`**: Handles the logic for executing ADB and Fastboot commands.
- **`src/commands.py`**: Contains the raw ADB and Fastboot commands.

## Features

This tool implements a wide range of ADB and Fastboot functionalities:

### ADB Scripting
- **Reboot:** Reboots the phone normally.
- **Reboot Recovery:** Reboots the phone into recovery mode.
- **Reboot Fastboot:** Reboots the phone into fastboot mode.
- **Reboot Bootloader:** Reboots the phone into bootloader mode.
- **Get State:** Prints the current state of the phone (e.g., recovery, device).
- **Get Serial Number:** Prints the device's serial number.
- **ADB Root:** Grants ADB root access.

### ADB Debugging & Server Management
- **Logcat:** Provides a continuous log of device activity. Stop by pressing `Ctrl + C` in the console where the app is running.
- **Start ADB Server:** Initiates the ADB server.
- **Kill ADB Server:** Terminates the ADB server, which can help resolve connection issues.
- **Reconnect Host:** Forces the host to reconnect to ADB.
- **Reconnect Device:** Forces the device to reconnect to ADB.
- **Reconnect Offline:** Resets and reconnects offline devices.
- **View Devices:** Lists currently connected ADB devices.

### ADB App Installation & File Transfer
- **Install APK:** Installs an APK file. Use the first argument entry box for the path to the APK on your PC.
- **Push:** Pushes a file from your computer to the device. Use the first argument for the PC file path and the second argument for the destination path on the Android device.
- **Pull:** Pulls a file from the device to your computer. Use the first argument for the file path on the device.
- **Remount:** Remounts the device's filesystem.
- **Sideload:** Sideloads ZIP files onto the device. Ensure your device is in sideload mode (you can check its state with "Get State").
- **Uninstall App:** Uninstalls an application. Use the first argument entry box for the package name.
- **List Packages:** Lists all installed packages on the device.
- **Get Android Version:** Retrieves the Android version of the connected device.

### Fastboot Basics
- **Devices:** Shows devices currently connected in fastboot mode.
- **Reboot:** Reboots the device to the system.
- **Reboot to Recovery:** Reboots the device to recovery mode.

### Fastboot Bootloader Locking / Unlocking
- **Unlock Bootloader:** Unlocks the bootloader, allowing unsigned firmware to be flashed. **Caution: This will factory reset your device.**
- **Lock Bootloader:** Locks the bootloader, enabling signature checks for firmware. **Ensure your device is completely back to stock before running this.**
- **Critical Unlock Bootloader:** Unlocks critical bootloader partitions.
- **Critical Lock Bootloader:** Locks critical bootloader partitions.

## Installation

### Prerequisites

*   Python 3.x
*   ADB and Fastboot binaries installed and accessible in your system's PATH. You can download the latest platform tools from the official Android developer website: [https://developer.android.com/studio/releases/platform-tools](https://developer.android.com/studio/releases/platform-tools).

### Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/parrots-14/ADB-GUI-Tool.git
    cd ADB-GUI-Tool
    ```

2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: If you are on a non-Windows OS and encountered issues with `customtkinter` in a previous setup attempt, ensure you follow these steps for a clean install.*

## Usage

1.  **Enable USB Debugging on your Android device:**
    *   Go to `Settings` > `About phone`.
    *   Tap on `Build number` seven times to enable `Developer options`.
    *   Go back to the `Settings` menu, find `Developer options`, and enable `USB debugging`.
    *   You may also need to authorize your computer when prompted on your phone.

2.  **Connect your Android device to your computer via a USB cable.**

3.  **Run the application:**
    Open your terminal or command prompt in the `ADB-GUI-Tool` directory and execute:
    ```bash
    python init.py
    ```
    The application GUI will launch, and any command outputs will be displayed in the terminal where you launched the script.

## Dependencies

*   `tkinter` (built-in Python GUI library)
*   `customtkinter` (for modern GUI elements)

## Troubleshooting

-   **"Waiting for device" / "Device not found"**:
    *   Ensure your device is plugged in correctly and that USB Debugging is enabled (see Usage section for instructions).
    *   Verify that you have authorized your computer on your phone when prompted.
    *   Check if your ADB drivers are correctly installed on your computer.

-   **"ADB server error"**:
    *   This usually indicates an outdated ADB server.
    *   **For Windows:** Delete any existing ADB binaries in the project directory (if any were copied there) and ensure that your system's PATH points to the up-to-date platform tools downloaded from the Android developer website.
    *   **For Linux (Debian-based):** You might need to update your platform tools: `sudo apt-get install android-sdk-platform-tools`.
    *   **For Linux (Fedora-based):** `sudo dnf install android-tools`.

## Contributing

Contributions are highly appreciated! If you have suggestions for new features, improvements, or bug fixes, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/YourFeature`).
6.  Open a Pull Request.


## License

This project is licensed under the [MIT License](LICENSE).
