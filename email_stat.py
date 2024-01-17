import imaplib
from datetime import datetime


gmail_username = input("Enter your Gmail email address: ")
gmail_password = input("Enter your email password (special for applications): ")

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(gmail_username, gmail_password)

def get_count_of_emails(id, folder_code):
    mail.select(folder_code)

    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)

    if id == 'inbox' or id == 'sent' or id == 'drafts' or id == 'flagged':
        search_criteria = f'(SINCE {start_date.strftime("%d-%b-%Y")}) (BEFORE {end_date.strftime("%d-%b-%Y")})'
    elif id == 'unseen':
        search_criteria = f'(UNSEEN) (SINCE {start_date.strftime("%d-%b-%Y")}) (BEFORE {end_date.strftime("%d-%b-%Y")})'
    elif id == 'i_sent_to_me':
        search_criteria = f'(SINCE {start_date.strftime("%d-%b-%Y")} BEFORE {end_date.strftime("%d-%b-%Y")} FROM {gmail_username} TO {gmail_username})'

    status, messages = mail.search(None, search_criteria)

    message_ids = messages[0].split()

    result.append([id,len(message_ids)])


email_codes = []
for i in mail.list()[1]:
    line = i.decode().split(' "/" ')
    email_codes.append(line)


result = []

get_count_of_emails('inbox', email_codes[0][1])
get_count_of_emails('sent', email_codes[5][1])
get_count_of_emails('drafts', email_codes[8][1])
get_count_of_emails('flagged', email_codes[6][1])
get_count_of_emails('unseen', email_codes[0][1])
get_count_of_emails('i_sent_to_me', email_codes[5][1])

print(result)

mail.close()
mail.logout()