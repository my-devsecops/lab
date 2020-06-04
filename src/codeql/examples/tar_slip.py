import tarfile
import os.path

with tarfile.open('archive.zip') as tar:
    #BAD : This could write any file on the filesystem.
    for entry in tar:
        tar.extract(entry, "/tmp/unpack/")

    # GOOD: Check that entry is safe
    for entry in tar:
        if os.path.isabs(entry.name) or ".." in entry.name:
            raise ValueError("Illegal tar archive entry")
        tar.extract(entry, "/tmp/unpack/")
