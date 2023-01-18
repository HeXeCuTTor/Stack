import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

class Email:
    def __init__(self):
        self.GMAIL_SMTP = "smtp.gmail.com"
        self.GMAIL_IMAP = "imap.gmail.com"
        self.login = 'login@gmail.com'
        self.password = 'qwerty'
        self.subject = 'Subject'
        self.recipients = ['vasya@email.com', 'petya@email.com']
        self.message = 'Message'
        self.header = None

    def send_message(self):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))
        ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()
        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, msg.as_string())
        ms.quit()
        return
    #send end

    #recieve
    def recieve(self):
        mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result_data = mail.uid('search', None, criterion)
        assert result_data[0], 'There are no letters with current header'
        latest_email_uid = result_data[0].split()[-1]
        result_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = result_data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message
    #end recieve


if __name__ == '__main__':
    send = Email.send_message()
    recieve = Email.recieve()