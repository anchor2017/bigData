# load text
filename1 = 'amazon-titles.txt'
filename2 = 'google-names.txt'
file = open(filename1, "r", "utf8")
text = file.read()
file.close()

# split into words by white space
words = text.split()

# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]

print(stripped[:100])
