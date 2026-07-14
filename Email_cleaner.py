emails = ["  Ali@gmail.com", "sarah@yahoo.com ", "KHALED@outlook.com", "nora@live.net", "   omar@gmail.com"]

cleaned_emails = [email.strip().lower() for email in emails if email.strip().lower().endswith('.com')]

print(cleaned_emails)
