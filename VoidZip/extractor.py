import zipfile
import os


def extract_file(zip_path):

    extract_folder = os.path.join(
        "output",
        os.path.splitext(os.path.basename(zip_path))[0]
    )

    os.makedirs(extract_folder, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_folder)

    return extract_folder