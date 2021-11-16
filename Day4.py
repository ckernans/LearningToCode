# ...
# The plan today is to learn how to search for strings from text and ...
# ... apply evaluative conditions to the text based on those strings.
# Learn more at: https://ckernans.com/day-4-is-this-text-happy-or-sad/

def Text_Type(text):
    happy_words = ["happy", "good", "thankful", "nice"] # Defining what words are in a "happy" text.
    sad_words = ["sad", "mean", "bad", "ungrateful"] # Defining what wards are in a "sad" text.
    happy_words_count = 0
    sad_words_count = 0

    for a in happy_words:
        if a in text:
            happy_words_count = happy_words_count + 1
        else:
            pass
            # happy_words_count = 0 ... started with this... but what is the problem?

    for b in sad_words:
        if b in text:
            sad_words_count = sad_words_count + 1
        else:
            pass

    if happy_words_count > sad_words_count:
        print("This is a happy text.")
    elif sad_words_count > happy_words_count:
        print("This is a sad text")
    else:
        print("This text is neither happy nor sad")

Text_Type("Hello happy")




