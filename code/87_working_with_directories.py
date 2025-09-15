from pathlib import Path
path = Path("ecommerce")
#path.exists()
#path.mkdir()
#path.rmdir()
#path.rename("ecommerce 2")

#print(path.iterdir())

for p in path.iterdir():
    print(p)


paths = [p for p in path.iterdir()]
print(paths)

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

path.glob("*.py")

py_files = [p for p in path.glob("*.py")]
print(py_files)


py_files = [p for p in path.rglob("*.py")]
print(py_files)