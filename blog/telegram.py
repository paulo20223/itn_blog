import requests
from blog.models import Settings


class Bot:

    def __init__(self):
        try:
            self.bot_token = Settings.objects.get(name='bot_token').value
            self.bot_chats_id = Settings.objects.get(name='bot_chats_id').value
        except Settings.DoesNotExist:
            pass

    def send_message(self, message):
        url_message = 'https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text={2}'.format(self.bot_token,
                                                                                                self.bot_chats_id,
                                                                                                message)
        response = requests.get(url_message)
        return response.text

    def send_photo(self, url):
        url_photo = 'https://api.telegram.org/bot{0}/sendPhoto'.format(self.bot_token)
        response = requests.post(url=url_photo, data={'chat_id': self.bot_chats_id, 'photo': url})
        return response.text

    def send_photo_with_message(self, url, message):
        url_photo = 'https://api.telegram.org/bot{0}/sendPhoto'.format(self.bot_token)
        response = requests.post(url=url_photo, data={'chat_id': self.bot_chats_id, 'photo': url, 'caption': message})
        return response.text
