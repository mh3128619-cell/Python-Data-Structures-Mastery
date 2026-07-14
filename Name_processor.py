names = ["ali", "bob", "anna", "charlie", "ed", "alex"]

processed_names = [name.upper() if name.lower().startswith('a') else name.capitalize() for name in names if len(name) > 3]

print("Resulting names:", processed_names)
