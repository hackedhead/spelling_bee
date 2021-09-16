import argparse

parser = argparse.ArgumentParser(description='Find Spelling Bee words')

parser.add_argument("required_letter", metavar="center", help="The center (required) letter")
parser.add_argument("other_letters",metavar="letter", nargs=6, help="The 6 surrounding (optional) letters")

args = parser.parse_args()

print(f"The center letter {args.required_letter.upper()}, and other letters {[x.upper() for x in args.other_letters]}")

words = set()
with open("words_alpha.txt", "r") as wordfile:
    for word in wordfile:
        if len(word) > 4:
            words.add(word.strip().upper())

print(f"Loaded {len(words)} words")

found = set()

game_letters = set(args.other_letters)
game_letters.add(args.required_letter)
for word in words:
    if args.required_letter in word:
        word_letters = set([x for x in word])
        if word_letters.issubset(game_letters):
            found.add(word)

for word in sorted(list(found), key=lambda x: (1/len(x), x)):
    print(word)
