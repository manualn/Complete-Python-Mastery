from pathlib import Path

# path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()
# print(path.stat())

from time import ctime

path = Path("ecommerce/__init__.py")
print(path.stat().st_ctime)
print(ctime(path.stat().st_ctime))


path.read_bytes()

# with open("__init__.py", "r") as file:

# print(path.read_text())

path.write_text("...")
path.write_bytes("...")

source = Path("ecommerce/__init__.py")
target = Path()/"__init__.py"

# target.write_text(source.read_text())

import shutil

shutil.copy(source, target)