import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version

server = 'smtp.mail.ru'
user = 'frezar@mail.ru'
password = 'ntkyc7r20711212'

recipients = ['frezar2007@gmail.com', ]
sender = 'frezar@mail.ru'
subject = 'Test'
test_css = """
.mail {
    width: 100% !important;
    background: gray !important;
}

h1,p{
    text-align: center !important;
}

.table {
    background-color: red !important;
    padding: 20px !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
}
.table__item {
    text-align: center;
    flex-basis: 50%;
    padding: 20px;
    background-color: #fff;
    margin: 0 10px;
}"""
test = """ <div class="mail">
        <div class="mail__wrapper">
            <h1>привет Юрка</h1>
            <p>кажется научился применять стили к письмам</p>
            <p>и засовывать в них файлы</p>
            <div class="table">
                <div class="table__item">Lorem ipsum dolor sit amet consectetur adipisicing.</div>
                <div class="table__item">Lorem ipsum dolor sit amet consectetur adipisicing.</div>
            </div>
        </div>
    </div>"""
text = 'Текст сообщения  <b>bold</b>  <h1>h1</h1> test'
html = '<html><head><style>' + test_css + ' </style></head><body>' + test + '</body></html>'

filepath = "test.jpg"
basename = os.path.basename(filepath)
filesize = os.path.getsize(filepath)

msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = f'{sender} <' + sender + '>'
msg['To'] = ', '.join(recipients)
msg['Reply-To'] = sender
msg['Return-Path'] = sender
msg['X-Mailer'] = 'Python/' + (python_version())

part_text = MIMEText(text, 'plain')
part_html = MIMEText(html, 'html')
part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
part_file.set_payload(open(filepath, "rb").read())
part_file.add_header('Content-Description', basename)
part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
encoders.encode_base64(part_file)

msg.attach(part_text)
msg.attach(part_html)
msg.attach(part_file)

mail = smtplib.SMTP_SSL(server)
mail.login(user, password)
mail.sendmail(sender, recipients, msg.as_string())
mail.quit()
