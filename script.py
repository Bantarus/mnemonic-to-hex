import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Path to the wordlist file, assuming it's in the same directory as the script
wordlist_path = os.path.join(script_dir, 'bip39_wordlist.txt')


# Function to convert mnemonic to binary
def mnemonic_to_binary(mnemonic, wordlist):
    words = mnemonic.split()
    return ''.join(format(wordlist.index(word), '011b') for word in words)

# Function to convert binary to hexadecimal
def binary_to_hex(binary_str):
    return hex(int(binary_str, 2))[2:].upper()  # [2:] to remove the '0x' prefix, and upper() for uppercase

# Load the BIP39 word list
with open(wordlist_path, 'r') as file:
    wordlist = [word.strip() for word in file.readlines()]

# Your mnemonic phrase
mnemonic = "your_24_word_mnemonic_phrase_here"

# Convert mnemonic to binary
binary_str = mnemonic_to_binary(mnemonic, wordlist)

# Convert binary to hex
hex_str = binary_to_hex(binary_str)

print("Hexadecimal String:", hex_str)
