# Folder and Subfolder Creator

This Python script helps you create a main folder and optional subfolders with different naming styles:
- **Numbers** (1, 2, 3, …)
- **Letters** (a, b, c, …)
- **Roman Numerals** (i, ii, iii, …)

---

## Features

- Prevents overwriting existing folders.
- Lets you choose whether or not to create subfolders.
- Allows three different naming styles for subfolders.
- Simple and interactive command-line interface.

---

## Requirements

- Python 3.x
- No external libraries needed (uses only built-in `os` and `string` modules).

---

## How to Use

1.  Save the code as a Python file (e.g., `file_organizer.py`).
2.  Open your terminal or command prompt and navigate to the directory where you saved the file.
3.  Run the script with the following command:
    ```bash
    python fileorganizer.py
    ```
4.  Follow the on-screen prompts:
    - Enter the name of the main folder.
    - Choose whether to create subfolders.
    - If yes, specify the quantity and naming style.

---

## Example Usage

Here is an example of how the script runs:

```
Enter the name of the main folder to create: Projects
✅ Folder 'Projects' created successfully!

Do you want to create subfolders inside 'Projects'? (yes/no): yes
How many subfolders do you want to create? 5

Choose a naming style for the subfolders:
  1. Numbers (e.g., 1, 2, 3, ...)
  2. Letters (e.g., a, b, c, ...)
  3. Roman Numerals (e.g., i, ii, iii, ...)
Enter your choice (1, 2, or 3): 2

Creating 5 subfolders...
✅ All subfolders created successfully!
```

### Resulting Folder Structure

The example above would create the following directory structure:

```
Projects/
├── a/
├── b/
├── c/
├── d/
└── e/
