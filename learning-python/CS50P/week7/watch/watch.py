import re

def main():
    input_html = input("HTML: ").strip()
    youtu_be_url = parse(input_html)

    if youtu_be_url:
        print(f"Converted youtu.be URL: {youtu_be_url}")
    else:
        print("No YouTube URL found in the input HTML.")

def parse(s):
    pattern = r"(https?://youtu.be/|https?://(?:www\.)?youtube\.com/embed/)([a-zA-Z0-9]+)"
    match = re.search(pattern, s)

    if match:
        video_id = match.group(2)
        youtu_be_url = f"https://youtu.be/{video_id}"
        return youtu_be_url
    else:
        return None

if __name__ == "__main__":
    main()
