import smtplib
from random import randint
from app.core.settings import MAIL, MAIL_PASSWORD


async def generate_code_message(email: str):
    smtp_obj = smtplib.SMTP(f'smtp.mail.ru', 587)
    smtp_obj.starttls()
    smtp_obj.login(MAIL, MAIL_PASSWORD)
    code = randint(10000, 99999)
    smtp_obj.sendmail(MAIL, email, f"Confirm code - {code}")
    smtp_obj.quit()
    return code
