import pywhatkit


class Mailsender:
    def __init__(self, sender, destiny):
        self.sender = sender
        self.destiny = destiny

    def whats_msg(self, msg, hour, minute):
        pywhatkit.sendwhatmsg(self.destiny, msg, hour, minute)
        print('Message sended...')


"""mailsender = Mailsender(123123, "+5583991279296",)
mailsender.whats_msg("olá", 8, 25)"""
