from pathlib import Path


IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.tif', '.svg', '.heic', '.heif', '.ico', '.raw', '.cr2', '.nef')
VIDEO_EXTENSIONS = ('.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.mpg', '.mpeg', '.3gp', '.3g2', '.ogv', '.vob', '.qt')
DOCUMENT_EXTENSIONS = ('.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods', '.odp', '.rtf', '.txt', '.csv', '.md', '.pages')
ARCHIVE_EXTENSIONS = ('.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.tgz', '.zipx', '.iso', '.cab', '.dmg', '.pkg', '.z', '.apk')


def handle_extension(files: list[Path]) -> dict[Path, str]:
    file_extensions: dict[str, tuple[str, ...]] = {"Images": IMAGE_EXTENSIONS, "Videos": VIDEO_EXTENSIONS, "Documents": DOCUMENT_EXTENSIONS, "Archives": ARCHIVE_EXTENSIONS}

    files_folders: dict[Path, str] = {}

    for file in files:
        for key, value in file_extensions.items():
            if file.suffix.lower() in value:
                files_folders[file] = key
                break
            else:
                files_folders[file] = ''

    return files_folders


def handle_folder(path: str) -> None:
    folder_path = Path(path)

    if folder_path.is_dir():
        files = [f for f in folder_path.iterdir() if f.is_file()]

        folders = handle_extension(files)

        for file, folder in folders.items():
            if folder:
                path_to_folder = Path(folder_path / folder)

                if not path_to_folder.is_dir():
                    path_to_folder.mkdir(parents=True, exist_ok=True)

                file.move_into(path_to_folder)
                print(f"{file.name} moved to {folder}")
                    
            else:
                print(f"{file.name} could not be moved - file extension not supported")
    else:
        print('No folder found')


def handle_actions() -> bool:
    user_input = input('Enter folder to organize (q to quit program): ')

    if user_input == 'q':
        return True

    handle_folder(user_input)
    return False


if __name__ == '__main__':
    while True:
        has_quit = handle_actions()

        if has_quit:
            break