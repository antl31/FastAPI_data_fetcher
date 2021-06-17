import json
from contextlib import contextmanager

import requests
from requests.exceptions import HTTPError

from api.app.errors import FakeAPIError
from api.app import config

settings = config.get_settings()


@contextmanager
def handle_request():
    try:
        yield
    except requests.RequestException as e:
        raise FakeAPIError(e)
    except Exception as e:
        raise FakeAPIError(e)


class FakeAPI:
    def __init__(self):
        self.BASE_URL = settings.fake_api_url
        self.API_KEY = settings.fake_api_secret_key
        self.timeout = 30

    def _handle_response(self, response):
        try:
            response.raise_for_status()
            return response.json()
        except HTTPError as e:
            raise FakeAPIError(e)
        except json.decoder.JSONDecodeError:
            return response.text

    def get_books(self):
        with handle_request():
            params = {"api-key": self.API_KEY}
            resp = requests.get(
                f"{self.BASE_URL}/svc/books/v3/lists/current/hardcover-fiction.json",
                params=params,
                timeout=self.timeout,
            )
        try:
            result = self._handle_response(resp)
        except FakeAPIError:
            return None
        return result["results"]["books"]
