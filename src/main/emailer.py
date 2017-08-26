import smtplib


def get_emails():
    emails = {}
    try:
        emails_file = open('emails.txt', 'r')

        for email_line in emails_file:
            email_line = email_line.strip()
            if email_line != '':
                (email, name) = email_line.split(',')
                emails[email] = name.strip()
    except FileNotFoundError as err:
        print(err)
    return emails

def send_emails(emails, forecast):
    server = smtplib.SMTP('smtp.google.com', '587')
    server.starttls()
    password = input('Enter password')
    from_email = input('Enter your Gmail email id from which you want to send email')
    server.login(from_email, password)

    for to_email, name in emails.items():
        message = 'Subject: Weather Forecast\n'
        message += 'Hi ' + name + '!\n\n'
        message += forecast
        server.sendmail(from_email, to_email, message)

    server.quit()
