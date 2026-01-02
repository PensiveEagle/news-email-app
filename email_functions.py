import smtplib, ssl

def send_email( message: str, sender_addr: str, sender_pass: str, receiver_addr: str, host: str = "smtp.gmail.com", port: int = 465 ) -> None:
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_addr, sender_pass)
        server.sendmail(sender_addr, receiver_addr, message)