# This program is intended to intake a novel DNA sequence and then output it's complementary strand

# Comment out below to test a smaller sample strand for accuracy.
file = open('rosalind_revc.txt', 'r')
fullSet = file.read()

# The following line was used to test a smaller DNA strand, since it wasn't apparent whether the code was
# fullSet = "AAAACCCGGT"

reversedComp = ""

for letter in fullSet[::-1]:
    if letter == 'A':
        reversedComp += 'T'
    elif letter == 'T':
        reversedComp += 'A'
    elif letter == 'C':
        reversedComp += 'G'
    elif letter == 'G':
        reversedComp += 'C'

print("Original DNA Sequence: ")
print(fullSet)
print("Complementary DNA Sequence: ")
print(reversedComp)
