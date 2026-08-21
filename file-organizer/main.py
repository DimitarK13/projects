from pathlib import Path


IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.tif', '.svg', '.heic', '.heif', '.ico', '.raw', '.cr2', '.nef')
VIDEO_EXTENSIONS = ('.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.mpg', '.mpeg', '.3gp', '.3g2', '.ogv', '.vob', '.qt')
DOCUMENT_EXTENSIONS = ('.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods', '.odp', '.rtf', '.txt', '.csv', '.md', '.pages')
ARCHIVE_EXTENSIONS = ('.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.tgz', '.zipx', '.iso', '.cab', '.dmg', '.pkg', '.z', '.apk')


def handle_extension(file: Path) -> str:
    file_extensions: dict[str, tuple[str, ...]] = {"Images": IMAGE_EXTENSIONS, "Videos": VIDEO_EXTENSIONS, "Documents": DOCUMENT_EXTENSIONS, "Archives": ARCHIVE_EXTENSIONS}

    for key, value in file_extensions.items():
        if file.suffix.lower() in value:
            return key
        
    return ''


def handle_folder(path: str) -> None:
    folder_path = Path(path)

    if folder_path.is_dir():
        files = [f for f in folder_path.iterdir() if f.is_file()]

        for file in files:
            folder = handle_extension(file)

            if folder:
                path_to_folder = Path(folder_path / folder)

                path_to_folder.mkdir(parents=True, exist_ok=True)

                file.move_into(path_to_folder)
                print(f"{file.name} moved to {folder}")
                    
            else:
                print(f"{file.name} could not be moved - file extension not supported")
            
    else:
        print('No folder found')


    

if __name__ == '__main__':
    while True:
        user_input = input('Enter folder to organize (q to quit program): ')
        
        if user_input == 'q':
            break
    
        handle_folder(user_input)