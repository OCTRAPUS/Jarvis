import requests
import json

class ec2MetaData():
    def __init__(self):
        self.session = ""
        self.TOKEN_TTL_SECONDS = 180
        self.service_url = "http://169.254.169.254/latest/"
        self.metadata_url = f"{self.service_url}meta-data/"
        self.TOKEN_HEADER = "X-aws-ec2-metadata-token"
        self.TOKEN_HEADER_TTL = "X-aws-ec2-metadata-token-ttl-seconds"
        self.TOKEN = ""
        self.get_session()
        self.meta_data_keys = list()

    def get_session(self):
        token_response = requests.put(
            f"{self.service_url}api/token",
            headers={self.TOKEN_HEADER_TTL: str(self.TOKEN_TTL_SECONDS)},
            timeout=5.0,
        )
        if token_response.status_code != 200:
            token_response.raise_for_status()
        self.TOKEN = token_response.text

    def get_url(self, key=None):
        if key is None:
            return f"{self.metadata_url}"
        else:
            return f"{self.metadata_url}{key}"

    def get_meta_data_keys(self, key=None):
        url = self.get_url(key)
        headers = {self.TOKEN_HEADER: self.TOKEN}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            resp = response.text.split('\n')
            self.meta_data_keys = resp
        else:
            print(f"error{response.text}")

    def fetch_key_data(self, key):
        url = self.get_url(key)
        headers = {self.TOKEN_HEADER: self.TOKEN}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text

    def get_meta_data(self):
        self.get_meta_data_keys()
        data_dict = dict()
        data_dict.update({
            'ami-id':self.fetch_key_data('ami-id')

        })
        for key in self.meta_data_keys:
            data = self.fetch_key_data(key)
            data_dict.update({key: data})
        print(data_dict)

