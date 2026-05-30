import zipfile
import os


def compress_file(file_path):

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    filename = os.path.basename(file_path)
    zip_name = os.path.splitext(filename)[0] + ".zip"

    output_path = os.path.join(output_dir, zip_name)

    with zipfile.ZipFile(
        output_path,
        'w',
        zipfile.ZIP_DEFLATED
    ) as zipf:

        zipf.write(file_path, arcname=filename)

    return output_path