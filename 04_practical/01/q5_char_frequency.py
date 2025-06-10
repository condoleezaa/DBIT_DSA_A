# q5_char_frequency.py

def count_char_freq(text):
    freq = {}
    for char in text:
        if char != ' ':
            freq[char] = freq.get(char, 0) + 1
    return freq


if __name__ == "__main__":
    text = "data structures and algorithms"
    frequencies = count_char_freq(text)
    for char, count in frequencies.items():
        print(f"{char}: {count}")
