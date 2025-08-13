import os
import string

def to_roman(num):
    val_map = [
        (1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'),
        (100, 'c'), (90, 'xc'), (50, 'l'), (40, 'xl'),
        (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'),
        (1, 'i')
    ]
    roman_num = ''
    for val, numeral in val_map:
        while num >= val:
            roman_num += numeral
            num -= val
    return roman_num

def create_main_folder():
    while True:
        folder_name = input("Enter the name of the main folder to create: ")
        if os.path.exists(folder_name):
            print(f"❌ The folder '{folder_name}' already exists. Please try a different name.")
        else:
            os.mkdir(folder_name)
            print(f"✅ Folder '{folder_name}' created successfully!")
            return folder_name

def get_subfolder_preferences(main_folder_name):
    while True:
        create_subfolders = input(f"\nDo you want to create subfolders inside '{main_folder_name}'? (yes/no): ").lower()
        if create_subfolders.startswith('n'):
            return None, None, None
        if create_subfolders.startswith('y'):
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    while True:
        try:
            count = int(input("How many subfolders do you want to create? "))
            if count > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number (e.g., 5).")

    while True:
        print("\nChoose a naming style for the subfolders:")
        print("  1. Numbers (e.g., 1, 2, 3, ...)")
        print("  2. Letters (e.g., a, b, c, ...)")
        print("  3. Roman Numerals (e.g., i, ii, iii, ...)")
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice in ['1', '2', '3']:
            return count, choice, main_folder_name
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def create_subfolders(count, choice, main_folder_name):
    if count is None:
        print("Ok, no subfolders created. Exiting...")
        return

    print(f"\nCreating {count} subfolders...")
    for i in range(1, count + 1):
        subfolder_name = ""
        if choice == '1':
            subfolder_name = str(i)
        elif choice == '2':
            if i > 26:
                print("Cannot create more than 26 subfolders with the letter naming style. Stopping.")
                break
            subfolder_name = string.ascii_lowercase[i-1]
        elif choice == '3':
            subfolder_name = to_roman(i)

        full_path = os.path.join(main_folder_name, subfolder_name)
        os.mkdir(full_path)

    print("✅ All subfolders created successfully!")

def main():
    main_folder = create_main_folder()
    count, choice, folder = get_subfolder_preferences(main_folder)
    create_subfolders(count, choice, folder)

if __name__ == "__main__":
    main()
