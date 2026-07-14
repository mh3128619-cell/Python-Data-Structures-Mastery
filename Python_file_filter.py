files = ["script.py", "data.csv", "main.py", "image.png", "test.py"]

py_files = list(file.upper() for file in files if file.endswith(".py"))

print(py_files)
