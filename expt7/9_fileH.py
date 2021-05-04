# 9.Python program to count the frequency of words in a file.
def word_count(fname):
        with open(fname) as f:
            unsortedwords = f.read().split()
            wordlist = []
            wordfreq = {}
            for word in unsortedwords:
                if wordlist.count(word) == 0:
                    wordlist.append(word)
                else :
                    continue
       
        for word in wordlist:
            wordfreq[word] = unsortedwords.count(word)
        print(wordfreq)

if __name__ == '__main__':
    word_count('test.txt')