def vowel(letter):
    if letter in "aeiou":
        return 1
    else:
        return 0


def recursion(sentence):
    if len(sentence)==0:
        return 0
    elif vowel(sentence[0])==1:
        return 1 + recursion(sentence[1:])
    elif vowel(sentence[0])==0:
        return 0 + recursion(sentence[1:])


sentence=input("message: ")

print("Number of vowels",recursion(sentence))
