#A program that can take the HTML code that embeds a YouTube video onto a website and parse it to determine and return the video's URL.

import re


def main():
    link = parse(input("HTML: "))
    print(link)

def parse(s):
    try:
        matches = re.search(r'^<iframe (?:width="560" height="315" )?src="https?://(?:www\.)?youtube\.com/embed/(.+)"(?: title="Youtube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen)?></iframe>', s, re.IGNORECASE)
        if matches:
            link = (f"https://youtu.be/{matches.group(1)}")
            return link
    except:
        pass


if __name__ == "__main__":
    main()