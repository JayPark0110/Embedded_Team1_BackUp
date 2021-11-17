import imaplib
import email
from email.header import decode_header, make_header

#This code is only for daum.net

def imap_daum(id, pw, num_mails):
    server = imaplib.IMAP4_SSL('imap.daum.net')
    server.login(id, pw)
    rv, data = server.select()
    recent_no = data[0]

    mailList = []

    for i in range(num_mails):
        mail_no = str(int(recent_no.decode('utf-8'))- i).encode('utf8')
        rv, fetched = server.fetch(mail_no, '(RFC822)')
        message = email.message_from_bytes(fetched[0][1])

        date = make_header(decode_header(message.get('Date')))
        tokenList = str(date).split(' ')

        date = tokenList[2] +" "+tokenList[1] +", "+ tokenList[4][:5]
        fr = make_header(decode_header(message.get('From')))
        subject = make_header(decode_header(message.get('subject')))

        mailList.append([date,str(fr),str(subject)])
    return mailList