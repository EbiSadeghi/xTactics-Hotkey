# Xtactics-Hotkey
## Project Status
- **Status**: Complete
![Complete](https://img.shields.io/badge/status-Complete-brightgreen)

**Xtactics-Hotkey** is a Python script designed to enhance the gaming experience for **Xtactics** by providing convenient hotkeys. Utilizing the `pyautogui` library, this script automates certain actions in the game, allowing players to perform tasks more efficiently.

## Features

- **Hotkeys**: 
  - Press **Q** to click the maximum option and confirm.
  - Press **W** to delete an item.
  - Press **P** to exit the script.

## Requirements

- Python 3.x
- Libraries:
  - `pyautogui`
  - `keyboard`

You can install the required libraries using the provided `requirements.txt` file.

## Installation

1. Clone the repository or download the script file.
2. Ensure you have Python installed on your system.
3. Install the required libraries by running:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes:

   ```
   pyautogui==0.9.53
   keyboard==0.13.5
   ```

## Usage

1. Run the script using Python:

   ```bash
   python xtactics_hotkey.py
   ```

2. While playing **Xtactics**, use the following hotkeys:
   - **Q**: Clicks the maximum option and confirms the action.
   - **W**: Deletes an item after navigating through the options.
   - **P**: Exits the script.

## Code Explanation

- The script sets up the environment for GUI automation.
- It defines functions to handle specific actions in the game:
  - `click_max_then_ok()`: Automates the process of selecting the maximum option and confirming it.
  - `click_delete()`: Automates the deletion process.
- A separate thread listens for key presses to trigger these actions.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository and submit a pull request.

---

Feel free to customize any sections further to better fit your project's specifics or your personal preferences!
