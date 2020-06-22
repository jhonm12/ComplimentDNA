file = open('rosalind_revc.txt', 'r')
fullSet = file.read()

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

print(reversedComp)
