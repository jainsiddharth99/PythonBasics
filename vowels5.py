vowels = ['a', 'e', 'i', 'o', 'u']
word = input("type a word to check: ")
found = {}
for letter in word:
    if letter in vowels:
        found.setdefault(letter,0)  #initializing the value of each letter found in the word that is in vowels
        found[letter] +=1
for k,v in sorted(found.items()):
    print(k,'was found',v,'times')

