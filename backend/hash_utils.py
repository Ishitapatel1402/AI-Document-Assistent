import hashlib


def generate_file_hash(file_path):
    """
    Generates an MD5 hash for a file.
    """

    md5 = hashlib.md5()

    with open(file_path, "rb") as f:

        while chunk := f.read(4096):
            md5.update(chunk)

    return md5.hexdigest()