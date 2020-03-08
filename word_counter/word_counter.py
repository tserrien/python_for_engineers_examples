#purposeful experimental deviation from the original code to play around a bit

import sys
import pprint
from operator import itemgetter

#f = open("bird.txt", "r")
#lines = []
#words = []
#ranking = {}
#data = f.read()

def break_lines(data):
    sep_lines = []
    sep_lines = data.split("\n")
    #print("Original lenght of lines: ",len(sep_lines), end="")
    #remove empty lines
    for l in sep_lines:
        if not l:
            sep_lines.remove(l)
    #print(". New length of lines: ",len(sep_lines))
    return sep_lines


def sep_words(lines):
    wordslist = []
    spec = [",", "?", "!", "."]

    for i in lines:
        wordslist += i.split(" ")

    for j in range(len(wordslist)):
        wordslist[j] = wordslist[j].lower()
        for k in spec:
            if wordslist[j][-1] == k:
                wordslist[j] = wordslist[j][:-1]
            if wordslist[j][0] == k:
                wordslist[j] = wordslist[j][1:]
    return wordslist

#lines = break_lines(data)
#words = sep_words(lines)

#print(words)

#print(f"\nFile contains {len(lines)} lines and {len(words)} words\n")

#print("Sorting...")
def sort_words(words):
    sorted_ranking = {}
    words.sort()
    for i in range(len(words)):
        if i== 0:
            #print(f"Word '{words[i]}' appears {words.count(words[i])} time(s)")
            sorted_ranking[words[i]] = words.count(words[i])
        elif words[i] != words[i-1]:
            #print(f"Word '{words[i]}' appears {words.count(words[i])} time(s)")
            sorted_ranking[words[i]] = words.count(words[i])

    return sorted_ranking

#ranking = sort_words(words)
#print(ranking)
#print(f"code appears {ranking.get('code')} times")
#f.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python word_count.py <file>")
        exit(1)

    filename = sys.argv[1]

    f = open(filename, "r")
    data = f.read()

    file_lines = break_lines(data)
    file_words = sep_words(file_lines)

    print("The file has",len(file_lines),"lines")
    print("The file has",len(file_words),"words")
    yn = input("Want to see the words? (y/n)\n>>> ")
    if yn == 'y' or yn =="Y":
        pprint.pprint(sort_words(file_words))
    f.close()
