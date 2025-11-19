import smtplib
from email.mime.text import MIMEText
import os

def enviar():
    # Credenciales desde los GitHub Secrets
    email_user = os.environ["EMAIL_USER"]
    email_pass = os.environ["EMAIL_PASS"]

    # Destinatario
    destino = "carloserenestoavalos1975@gmail.com"

    # Crear el mensaje
    msg = MIMEText("Hola Carlos, este es un correo automático enviado cada 1 hora desde GitHub Actions 🎉")
    msg["Subject"] = "Correo automático (GitHub Actions)"
    msg["From"] = email_user
    msg["To"] = destino

    # Enviar usando Gmail (SMTP SSL)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(email_user, email_pass)
        server.sendmail(email_user, destino, msg.as_string())

    print("Correo enviado exitosamente.")

if __name__ == "__main__":
    enviar()
