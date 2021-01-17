import eel
import smtplib

@eel.expose
def send_message(login, password, subject, message_text, send_to):
	smtp_server = "smtp.gmail.com"
	port = 587

	server = smtplib.SMTP(smtp_server, port)
	server.starttls()

	server.login(login, password)

	msg = f"Subject: {subject}\n\n{message_text}"

	server.sendmail(login, send_to, msg)

	server.quit()

eel.init("web")
eel.start("main.html", size=(800, 800))