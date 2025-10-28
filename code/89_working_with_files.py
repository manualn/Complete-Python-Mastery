from pathlib import Path
from zipfile import ZipFile

#zip = ZipFile("files.zip", "w")

#for path in Path("ecommerce").rglob("*.*"):
    #zip.write(path)

#zip.close()

with ZipFile("files.zip", "w") as zip:
    for path in Path("ecommerce").rglob("*.*"):
        zip.write(path)


with ZipFile("files.zip") as zip:
    print(zip.namelist())
    zip.getinfo("ecommerce/__init__.py")

    # lets store it in another variable called info.
    info = zip.getinfo("ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)

    # New to extract all files from all zip files
    zip.extractall("extract")