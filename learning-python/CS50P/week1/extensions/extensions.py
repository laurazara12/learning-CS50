def get_media_type(file_name):
    file_extension = file_name.lower().split('.')[-1] if '.' in file_name else ''

    mime_types = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }

    if file_extension in mime_types:
        return mime_types[file_extension]
    else:
        return 'application/octet-stream'

def main():
    file_name = input("Enter the name of the file: ").strip().lower()
    media_type = get_media_type(file_name)

    print(media_type)

if __name__ == "__main__":
    main()
