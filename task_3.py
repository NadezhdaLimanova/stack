import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Post:
    def __init__(self, login: str, password: str, message: str,
                 subject: str, gmail_smtp: str, gmail_imap: str):
        self.login = login
        self.password = password
        self.message = message
        self.subject = subject
        self.gmail_smtp = gmail_smtp
        self.gmail_imap = gmail_imap


    def send_message(self):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))

        ms = smtplib.SMTP(self.gmail_smtp, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())
        ms.quit()


    def receive_mail(self):
        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result_data = mail.uid('search', None, criterion)
        assert data[0] == 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


if __name__ == "__main__":

    gmail_smtp = "smtp.gmail.com"
    gmail_imap = "imap.gmail.com"

    login = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    header = None