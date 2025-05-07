from pprint import pprint
# Returns a new string that is s with all punctuation removed.
# s.replace(a, b) will replace all occurrences of substring a in s with the new string, b.
# We will define punctuation as any non-letter, non-number, and non-whitespace character in a string. Look at the full text to Alice in Wonderland to find examples.
# The one exception is the apostrophe. We will keep it so that contracted words like isn’t remain.
# For consistency you can use the following definition of punctuation:
#     punctuation = """.,!?"()“”_-:—;"""


def remove_punctuation(s):
    punctuation = """.,!?"()“”_‘-:—;"""
    for p in punctuation:
        s = s.replace(p, ' ')
    return s

def word_counts(s):
    counts = {}
    s = s.lower()
    s = remove_punctuation(s)
    s = s.split()
    for word in s:
        if word in counts:
            counts[word]+= 1
        else:
            counts[word] = 1
    return counts

tobe = 'To be or not to be,\nthat is the question!'
counts = word_counts(tobe)
print(counts)

def remove_commons(d, common):
    for word in common:
        if word in d:
            d.pop(word)


common = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i']
counts = word_counts(tobe)
remove_commons(counts, common)
print(counts)

f = open("data/alice.txt")
text = f.read()
f.close()

counts = word_counts(text)
remove_commons(counts, common)
print(counts)
