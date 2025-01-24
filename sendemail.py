import smtplib

SENDER_EMAIL= '' # emailofthesender@example.org
SENDER_PASSWORD='testeMAIL' #his password

def send_email(receiver_email, subject, body):
    message= f"Subject: {subject}\n \n {body}"
    
    with smtplib.SMTP('example.org',587) as server: #replace example.org by your smtp server
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email,message)
        

