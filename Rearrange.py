import re, random
words = (re.sub(r'([^A-Za-z\s]|_)+', '', str(eval(input("Enter Sentence"))))).split() #Gets string input and strips of everything except alphabetic characters and space, then converts to list
for i in range(0, len(words)):
    letters = list(str(words[i]))
    if len(letters)  > 2:
        store = [letters[0], letters[-1]]
        del letters[0]
        del letters[-1]
        random.shuffle(letters)
        letters.insert(0, str(store[0]))
        letters.append(str(store[1]))
        words[i] = str(''.join(letters))
print((" ".join(map(str, words))))