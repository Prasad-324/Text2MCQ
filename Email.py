import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import re

def send_email(keyword_sentence_list,keywords_distractors_list,email):
    
    a=[]
    b=[]
    index=1
    import random
    for key in keywords_distractors_list:
        sentence = keyword_sentence_list[key][0]
        pattern = re.compile(key, re.IGNORECASE)
        output = pattern.sub( " _______ ", sentence)
        a.append(output)
        choices = [key.capitalize()] + keywords_distractors_list[key]
        top4choices = choices[:4]
        random.shuffle(top4choices)
        optionchoices = ['a','b','c','d']
        for idx,choice in enumerate(top4choices):
            b.append(choice)
        index = index + 1
        
    c={}
    for i in range(len(a)):
        c[str(a[i])] = [str(b[4*i]) + "," + str(b[4*i+1])+","+str(b[4*i+2])+","+str(b[4*i+3])]
        
    EMAIL_ADDRESS = 'prasadquizmail999@gmail.com'
    EMAIL_PASSWORD = 'quizmail999'
        
    recipients = ["prasaddeva5432@gmail.com"]
    sender = "prasadquizmail999@gmail.com"
    subject = 'This is mail from Deva'
    body = json.dumps(c, indent=4) #changed code line

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    msg.attach(MIMEText(body, 'plain'))

    smtp = smtplib.SMTP('smtp.gmail.com',587) 
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    smtp.sendmail(EMAIL_ADDRESS,'prasaddeva5432@gmail.com',msg.as_string())