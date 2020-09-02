import json
from urllib.parse import urljoin
from urllib.request import Request, urlopen


class MX3Client(object):
    
    URL_ROOT = "https://api.mx3.app/v1/"
    
    def __init__(self, token):
        self.token = token
    
    def _request(self, url, data=None, method=None):
        url = urljoin(MX3Client.URL_ROOT, url)
        request = Request(
            url,
            method=('POST' if data else 'GET') if method is None else method,
            data=json.dumps(data).encode('utf-8') if data else None,
            headers={
                'User-Agent': 'MX3Client/py',
                'Authorization': 'Token {}'.format(self.token),
                'Content-Type': 'application/json',
            }
        )
        with urlopen(request) as response:
            data = json.load(response)
            if not data['status']:
                raise MX3ClientException(data)
            return data
    
    def get_users(self):
        return self._request('users')['data']
    
    def get_user(self, id):
        return self._request('users/{}'.format(id))['data']
    
    def update_users(self, data):
        return self._request('users', data)['user_id']
    
    def update_user(self, id, data):
        self._request('users/{}'.format(id), data)
    
    def delete_user(self, id):
        self._request('users/{}'.format(id), method='DELETE')
    
    def get_measurements(self):
        return self._request('measurements')['data']


class MX3ClientException(Exception):
    
    def __init__(self, data):
        super(MX3ClientException, self).__init__("API call failed")
        self.data = data

