# conkatatonate.py
import random
from collections import Counter

stopwords = [
    "i", "a", "the", "am", "an", "and", "to", "in", "of", "on",
    "for", "it", "is", "you", "me", "my", "we", "us", "our",
    "they", "them", "their", "he", "she", "him", "her", "im", "i'm",
    "so", "your", "when", "this", "will", "but", "when", "that", "all",
    "have", "no", "o", "oh", "come", "now", "see", "with", "it's", "from",
    "be", "are", "here", "one", "if", "what", "not", "say", "was", "had",
    "out", "through", "time", "go", "way", "at", "let", "as", "by", "back",
    "like", "find", "how", "into", "can", "long", "there", "away", "can't",
    "couldn't", "would", "wouldn't", "cannot", "did", "only", "could", "where",
    "just", "still", "words", "over", "do", "hear", "take", "behind", "saw",
    "you're", "more", "been", "who", "has", "coming", "know", "then", "left",
    "try", "something", "somewhere", "someone", "up"
]

# read in lyrics
with open("data/lyrics.txt", "r") as f:
    words = f.read().lower().split()

# filter words
filtered_words = [w for w in words if w not in stopwords]

# count frequency
counts = Counter(filtered_words)

# show the 10 most common
print("Most common Katatonia words:")
for word, freq in counts.most_common(20):
    print(word, "→", freq)

print("\n--- ConKATATONated Corpus ---")

# remix mode: chain the top N words into a bleak line
N = 20  # number of words to chain together
top_words = [w for w, _ in counts.most_common(N)]

# randomize order for chaotic effect
random.shuffle(top_words)

# concatenate into a Katatonic string
katatonated_line = " ".join(top_words)

print(katatonated_line)