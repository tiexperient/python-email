import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email():
    remetente = "celia.megatronn@gmail.com"
    senha = ""
    destinatario = "celia.megatronn@gmail.com"
    assunto = "Relatório de Vendas atual"
    corpo = "Este é o corpo de um email automático"

    # Criar mensagem
    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = assunto
    mensagem.attach(MIMEText(corpo, "plain"))

    try:
        # Conectar ao servidor SMTP do Gmail
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatario, mensagem.as_string())
        servidor.quit()
        print("Email enviado com sucesso")
    except smtplib.SMTPAuthenticationError as e:
        print("Erro de autenticação:", e)
    except Exception as e:
        print("Erro ao enviar email:", e)

enviar_email()