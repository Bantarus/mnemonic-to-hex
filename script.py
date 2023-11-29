# Function to convert mnemonic to binary
def mnemonic_to_binary(mnemonic, wordlist):
    words = mnemonic.split()
    return ''.join(format(wordlist.index(word), '011b') for word in words)

# Function to convert binary to hexadecimal
def binary_to_hex(binary_str):
    return hex(int(binary_str, 2))[2:].upper()  # [2:] to remove the '0x' prefix, and upper() for uppercase

# Load the BIP39 word list
with open('C:\\Users\\bodio\\ARCHETHIC\\NFT COLLECTION\\cli-generator-archethic\\bip39_wordlist.txt', 'r') as file:
    wordlist = [word.strip() for word in file.readlines()]

# Your mnemonic phrase
mnemonic = "flush dune result that coconut relax fiction various slab proof gun hero shine above trial cigar spoil carbon plunge juice decline boring fox forget"

# Convert mnemonic to binary
binary_str = mnemonic_to_binary(mnemonic, wordlist)

# Convert binary to hex
hex_str = binary_to_hex(binary_str)

print("Hexadecimal String:", hex_str)
