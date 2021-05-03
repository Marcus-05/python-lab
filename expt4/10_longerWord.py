list = ["musher", "aba", "bib", "python"]

n = int(input("Enter the value of n : "))

words = []
for word in list :
    if len(word) > n:
        words.append(word)
print(words)
