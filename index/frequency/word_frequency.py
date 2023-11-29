import os
from collections import Counter

def analyze_word_frequency(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: The file \"{file_path}\" was not found.")
    except Exception as e:
        print(f"Error: {e}")

    # Convert text file to array of words
    text = remove_punctuation(text)
    words = text.lower().split()
    word_freq = count_frequencies(words)
    return word_freq

def remove_punctuation(text):
    punctuation_chars = ".,;:'\"!?()[]{}"
    for char in punctuation_chars:
        text = text.replace(char, '')
    return text

def count_frequencies(words):
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    sorted_word_freq = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True))
    return sorted_word_freq

def generate_report(word_freq):
    report = "Word Frequency Analysis:\n"
    report += "{:<15} {:<10}\n".format("Word", "Frequency")
    report += "-" * 25 + "\n"
    for word, frequency in word_freq.items():
        report += "{:<15} {:<10}\n".format(word, frequency)
    return report

if __name__ == "__main__":
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, '..', 'Assets', 'text_file.txt')

    try:
        word_freq = analyze_word_frequency(file_path)
        report = generate_report(word_freq)
        print(report)
    except FileNotFoundError:
        print(f"Error: The file \"{file_path}\" was not found.")
    except Exception as e:
        print(f"Error: {e}")