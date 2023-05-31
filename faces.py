#A simple program that can convert input into an emoticon.

def main():
    emoji = input("Please type an emoticon: ").upper()
    emoji = convert(emoji)
    print(emoji)

def convert(emoji):
    emoji = emoji.replace(":)", "🙂")
    emoji = emoji.replace(":(", "🙁")
    emoji = emoji.replace(";)", "😉")
    emoji = emoji.replace("XD", "😂")
    emoji = emoji.replace("XP", "😛")
    emoji = emoji.replace(";P", "😜")
    return emoji

main()