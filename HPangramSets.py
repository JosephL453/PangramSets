alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
letters = set()
input = input("Give Input")
for i in input:
    letters.add(i)
if alphabet.intersection(letters) == alphabet:
    print("It is a pangram")
else: 
    print("It is not a pangram.")