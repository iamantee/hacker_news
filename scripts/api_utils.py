import requests

class API_Utils(object):
    """ This class is used as utilities of Hacker News API """

    _API_REQUEST_URL_PATTERN = 'https://hacker-news.firebaseio.com/{0}/{1}.json'

    def __init__(self, version='v0', interface_type='', print_style=''):
        self._version = version
        self._interface_type = interface_type
        self._print_style = print_style

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        self._version = value

    @property
    def interface_type(self):
        return self._interface_type

    @interface_type.setter
    def interface_type(self, value):
        self._interface_type = value

    @property
    def print_style(self):
        return self._print_style

    @print_style.setter
    def print_style(self, value):
        self._print_style = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def response(self):
        return self._response

    @response.setter
    def url(self, value):
        self._response = value

    @property
    def api_response(self):
        return self._api_response

    @api_response.setter
    def api_response(self, value):
        self._api_response = value


    def construct_api_request(self):
        self._url = API_Utils._API_REQUEST_URL_PATTERN.format(self._version, self._interface_type)

        if(not self._print_style):
            self._url += '?print=' + self._print_style

    def call_api(self):
        if(not self._url):
            self._api_response = requests.get(self._url)

    def write_response_data(self, file_path):
        if(not self._api_response):
            with open(file_path, 'w') as data_file:
                data_file.writelines(self._api_response.json())


if __name__ == '__main__':
    hacker_news_api_utils = API_Utils('v0', 'topstories', 'pretty')

    hacker_news_api_utils.construct_api_request()
    hacker_news_api_utils.call_api()
    hacker_news_api_utils.write_response_data('api_response.json')
