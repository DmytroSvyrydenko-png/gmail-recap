import imaplib
from datetime import datetime


gmail_username = input("Enter your Gmail email address: ")
gmail_password = input("Enter your email password (special for applications): ")

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(gmail_username, gmail_password)

mail.select("INBOX")

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

search_criteria = f'(SINCE {start_date.strftime("%d-%b-%Y")}) (BEFORE {end_date.strftime("%d-%b-%Y")})'

status, messages = mail.search(None, search_criteria)

message_ids = messages[0].split()

print(len(message_ids))