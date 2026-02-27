import smtplib, os, time
from email.mime.text import MIMEText
from email.header import Header

try:
    import pyperclip
    correctimport = True
except Exception:
    correctimport = False

smtp_server = "smtp.gmail.com"
smtp_port = 587

sender = input('Input your account\n')
app_password = input('app password(not password)\n')

def pasteornot():
    global yesno
    yesno = ''
    if correctimport:
        yesno = ' or pastee to paste'

pasteornot()

reciever = input('to who do you want to send?\n')

def send():
    global correctimport
    global yesno
    print(f'Please write the body(write stope to stop{yesno}.)')
    print('Do not use Ctrl + v to paste:')
    _body = ''
    while True:
        line = input('>')
        if line == "stope":
            break
        elif line == 'pastee':
            if correctimport:
                _body += str(pyperclip.paste()) + '\n'
            else:
                _body += line + '\n'
        else:
            _body += line + '\n'

    msg = MIMEText(_body, "plain", "utf-8")
    msg["From"] = Header("Python Sender", "utf-8")
    msg["To"] = Header(input('How you want to call him?\n>'), "utf-8")
    msg["Subject"] = Header(input('what is the subject of email:'), "utf-8")

    try:
        server = smtplib.SMTP(smtp_server, smtp_port, timeout = max(20, int(len(_body) / 50) + 20))
        server.starttls()
        server.login(sender, app_password)
        server.sendmail(sender, [reciever], msg.as_string())
        server.quit()
        print("sent!")
    except smtplib.SMTPAuthenticationError:
        print('Failed...Please check the app password')
    except Exception as _:
        print(f'Error: {_}. Not sent')

while True:
    if reciever.count("@") == 1 and "." in reciever and 6 < len(reciever) < 30:
        send()
        break
    else:
        print('Bad input')
        reciever = input('to who do you want to send?')
time.sleep(5)
os.system('cls')
print('Goodbye!')
time.sleep(5)
os.system('cls')
