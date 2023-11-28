import os

def count_words(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            words = content.split()
            num_words = len(words)
            print(f"The file \"{file_path}\" contains {num_words} words.")
    except FileNotFoundError:
        print(f"Error: The file \"{file_path}\" was not found.")
    except PermissionError:
        print(f"Error: The file \"{file_path}\" was not accessible.")
    except Exception as e:
        print(f"Error: {e}")

current_directory = os.path.dirname(__file__)
file_path = os.path.join(current_directory, 'Assets', 'text_file.txt')
count_words(file_path)