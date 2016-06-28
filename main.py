from interface import Interface
import sys
import traceback
import smtplib


def mail(trace):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    info = open('info.txt', 'r')
    login_info = [x.strip('\n') for x in info.readlines()]
    server.login(login_info[0], login_info[1])

    msg = traceback.format_exc(trace)
    server.sendmail("crappyoats@gmail.com", "vilmin2@illinois.edu", msg)
    server.quit()


if __name__ == '__main__':
    try:
        interface = Interface()
        interface.start()
    except:
        ex_type, ex, tb = sys.exc_info()
        mail(tb)
        del tb
