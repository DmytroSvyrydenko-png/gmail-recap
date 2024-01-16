import imaplib

gmail_username = input("Enter your Gmail email address: ")
gmail_password = input("Enter your email password (special for applications): ")

mail = imaplib.IMAP4_SSL("imap.gmail.com")

mail.login(gmail_username, gmail_password)

mail.select("INBOX")

search_criteria = '(ALL)'

status, messages = mail.search(None, search_criteria)

message_ids = messages[0].split()

print(len(message_ids))