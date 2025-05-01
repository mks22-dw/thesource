def get_chars_after(s, key, n):
    start  = s.find(key)
    return s[start : start+n]

def get_words_after(s, key,  n):
    words = s.split()
    start = words.index(key)
    words = words[start : start+n]
    return ' '.join(words)

def get_chapter(s, chapter):
    chapter_mark = 'CHAPTER ' + chapter + '.\n'
    start = s.find(chapter_mark)
    s = s[start + len(chapter_mark):]
    end_mark = 'CHAPTER'
    if (chapter == 'XII'):
        end_mark = 'THE END'
    end = s.find(end_mark)
    return s[:end]


f = open("data/alice.txt")
text = f.read()
f.close()

print("char after test:")
print( get_chars_after(text, 'Rabbit-Hole', 100) )
print("\nwords after test:")
print( get_words_after(text, 'Rabbit-Hole', 10) )
print("\nchapter test:")
print( get_chapter(text, 'XI') )
