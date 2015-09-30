# Stubs for requests.api (Python 3)

import typing

from .models import Response

def request(method: str, url: str, **kwargs) -> Response: ...
def get(url: str, **kwargs) -> Response: ...
def options(url: str, **kwargs) -> Response: ...
def head(url: str, **kwargs) -> Response: ...
def post(url: str, data=None, json=None, **kwargs) -> Response: ...
def put(url: str, data=None, **kwargs) -> Response: ...
def patch(url: str, data=None, **kwargs) -> Response: ...
def delete(url: str, **kwargs) -> Response: ...
