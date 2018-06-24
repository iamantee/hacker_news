import requests

class HTML_Utils(object):

    def __init__(self):
        self._response = None 

    def get_response(self, url):
        self._response = requests.get(url)


    @property
    def response(self):
        return self._response

    @response.setter
    def responese(self, value):
        self._response = value


if __name__ == '__main__':
    import os

    url = 'https://en.wikipedia.org/wiki/Dilophosaurus'
    file_path = './data/test/web_page_content.html'
    html_utils = HTML_Utils()

    html_utils.get_response(url)

    if os.path.exists(os.path.dirname(file_path)) == False:
        try:
            os.makedirs(os.path.dirname(file_path))
        except OSError as ex:
            raise ex

    with open(file_path, 'w') as content_file:
        content_file.write(str(html_utils.responese.__dict__))

