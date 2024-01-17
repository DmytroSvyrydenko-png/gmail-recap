import imaplib
from datetime import datetime
import smtplib
from email.message import EmailMessage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

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

def get_count_of_leaks(gmail_username):
    service = Service()
    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=option)

    url = "https://monitor.mozilla.org/"
    driver.get(url)
    time.sleep(2)

    find = driver.find_element(By.ID, 'scan-email-address')
    find.send_keys(gmail_username)
    time.sleep(1)

    find = driver.find_element(By.CLASS_NAME, 'button.primary')
    find.click()
    time.sleep(4)

    find = driver.find_element(By.CLASS_NAME, 'breach-result-count')
    count = find.get_attribute("textContent")
    current_url = driver.current_url

    result.append(['data breaches', count, current_url])

email_codes = []
for i in mail.list()[1]:
    line = i.decode().split(' "/" ')
    email_codes.append(line)


result = []
content = []
text = ""


content.append(f"Hello, {gmail_username}!")
content.append("It's time to take stock of the passing year.")
content.append("Let's go!")


content.append(" ")
content.append(" ")
get_count_of_emails('inbox', email_codes[0][1])
if result[0][1] == 0:
    content.append("Looks like someone forgot they have mail!")
    content.append(f"Here's how many letters you got: {result[0][1]}")
elif 0 < result[0][1] <= 200:
    content.append("The year 2023 is a time of meditation and calm!")
    content.append(f"Here's how many letters you got: {result[0][1]}")
else:
    content.append("The year 2023 is a mix of highlights and networking!")
    content.append(f"Here's how many letters you got: {result[0][1]}")


content.append(" ")
content.append(" ")
get_count_of_emails('sent', email_codes[5][1])
if result[1][1] == 0:
    content.append("You didn't send your letters to anyone this year.")
    content.append("But who says quantity is more important than quality?!")
    content.append("We are sure you are an interesting conversationalist. Perhaps next year there will be more reasons to communicate!")

elif 0 < result[1][1] <= 15:
    content.append("There was a special connection between you and your recipients!")
    content.append(f"You have sent {result[1][1]} letters. It's hard to imagine how much emotion you gave them!")

else:
    content.append("You've been very active socializing this year!")
    content.append(f"You've sent as many as {result[1][1]} letters this year. Your letters have made this year unforgettable.")


content.append(" ")
content.append(" ")
get_count_of_emails('drafts', email_codes[8][1])
if result[2][1] == 0:
    content.append("You are a person of courage and determination, you have absolutely no drafts!")
    content.append("Why waste time on drafts when your every word is a work of art?")

else:
    content.append("Drafts are your creative workshop.")
    content.append(f"You left {result[2][1]} letters in your drafts. Next year, give them a chance to see the light of day!")


content.append(" ")
content.append(" ")
get_count_of_emails('flagged', email_codes[6][1])
if result[3][1] == 0:
    content.append("You haven't flagged any emails, but who says that's a bad thing?")
    content.append("Perhaps for you, every letter is a diamond in the collection!")
else:
    content.append("You have room in your heart for a few favorites.")
    content.append("You're a romantic!")
    content.append(f"You've flagged {result[3][1]} letters.")


content.append(" ")
content.append(" ")   
get_count_of_emails('unseen', email_codes[0][1])
if result[4][1] == 0:
    content.append("Your manners and politeness are impressive!")
    content.append("You are so attentive to each letter that you left none unread.")
else:
    content.append("Unread emails are a little bit of time saved.")
    content.append(f"We hope no one takes offense that you didn't read  {result[4][1]} letters.")


content.append(" ")
content.append(" ")     
get_count_of_emails('i_sent_to_me', email_codes[5][1])
if result[5][1] == 0:
    content.append("Surprisingly, you haven't written a single letter to your favorite self in 2023. Never forget about yourself!")
else:
    content.append("We've noticed that you like to talk to yourself. Do you often need an expert opinion?")
    content.append(f"The number of love letters sent to yourself: {result[5][1]}")


content.append(" ")
content.append(" ")
get_count_of_leaks(gmail_username)
content.append(f"We found that {gmail_username} was exposed in {result[6][1]} data breaches.")
if result[6][1] == '⁨0⁩':
    content.append("Congratulations! You clearly take great care of your safety!")
else:
    content.append(f"It's sad, check out the information on the website Mozilla Monitor {result[6][2]}")

content.append(" ")
content.append(" ")
content.append("It was a lot of fun!")
content.append("That's all for now, but we're not saying goodbye!")
content.append("See you at this time next year?")

for i in content:
    text = text + i + "\n"


mail.close()
mail.logout()


gmail_server = "smtp.gmail.com"
gmail_port = 587

my_server = smtplib.SMTP(gmail_server, gmail_port)
my_server.ehlo()
my_server.starttls()

my_server.login(gmail_username, gmail_password)
msg = EmailMessage()
msg.set_content(text)

msg['Subject'] = 'THE GMAIL RECAP 2023'
msg['From'] = gmail_username
msg['To'] = gmail_username

my_server.send_message(msg)
print('The GMAIL RECAP 2023 was sent to your inbox!')