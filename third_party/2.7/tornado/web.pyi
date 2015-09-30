# Stubs for tornado.web (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from tornado import httputil

MIN_SUPPORTED_SIGNED_VALUE_VERSION = ... # type: Any
MAX_SUPPORTED_SIGNED_VALUE_VERSION = ... # type: Any
DEFAULT_SIGNED_VALUE_VERSION = ... # type: Any
DEFAULT_SIGNED_VALUE_MIN_VERSION = ... # type: Any

class RequestHandler:
    SUPPORTED_METHODS = ... # type: Any
    application = ... # type: Any
    request = ... # type: Any
    path_args = ... # type: Any
    path_kwargs = ... # type: Any
    ui = ... # type: Any
    def __init__(self, application, request, **kwargs): ...
    def initialize(self): ...
    @property
    def settings(self): ...
    def head(self, *args, **kwargs): ...
    def get(self, *args, **kwargs): ...
    def post(self, *args, **kwargs): ...
    def delete(self, *args, **kwargs): ...
    def patch(self, *args, **kwargs): ...
    def put(self, *args, **kwargs): ...
    def options(self, *args, **kwargs): ...
    def prepare(self): ...
    def on_finish(self): ...
    def on_connection_close(self): ...
    def clear(self): ...
    def set_default_headers(self): ...
    def set_status(self, status_code, reason=None): ...
    def get_status(self): ...
    def set_header(self, name, value): ...
    def add_header(self, name, value): ...
    def clear_header(self, name): ...
    def get_argument(self, name, default=..., strip=True): ...
    def get_arguments(self, name, strip=True): ...
    def get_body_argument(self, name, default=..., strip=True): ...
    def get_body_arguments(self, name, strip=True): ...
    def get_query_argument(self, name, default=..., strip=True): ...
    def get_query_arguments(self, name, strip=True): ...
    def decode_argument(self, value, name=None): ...
    @property
    def cookies(self): ...
    def get_cookie(self, name, default=None): ...
    def set_cookie(self, name, value, domain=None, expires=None, path='', expires_days=None, **kwargs): ...
    def clear_cookie(self, name, path='', domain=None): ...
    def clear_all_cookies(self, path='', domain=None): ...
    def set_secure_cookie(self, name, value, expires_days=30, version=None, **kwargs): ...
    def create_signed_value(self, name, value, version=None): ...
    def get_secure_cookie(self, name, value=None, max_age_days=31, min_version=None): ...
    def get_secure_cookie_key_version(self, name, value=None): ...
    def redirect(self, url, permanent=False, status=None): ...
    def write(self, chunk): ...
    def render(self, template_name, **kwargs): ...
    def render_string(self, template_name, **kwargs): ...
    def get_template_namespace(self): ...
    def create_template_loader(self, template_path): ...
    def flush(self, include_footers=False, callback=None): ...
    def finish(self, chunk=None): ...
    def send_error(self, status_code=500, **kwargs): ...
    def write_error(self, status_code, **kwargs): ...
    @property
    def locale(self): ...
    @locale.setter
    def locale(self, value): ...
    def get_user_locale(self): ...
    def get_browser_locale(self, default=''): ...
    @property
    def current_user(self): ...
    @current_user.setter
    def current_user(self, value): ...
    def get_current_user(self): ...
    def get_login_url(self): ...
    def get_template_path(self): ...
    @property
    def xsrf_token(self): ...
    def check_xsrf_cookie(self): ...
    def xsrf_form_html(self): ...
    def static_url(self, path, include_host=None, **kwargs): ...
    def require_setting(self, name, feature=''): ...
    def reverse_url(self, name, *args): ...
    def compute_etag(self): ...
    def set_etag_header(self): ...
    def check_etag_header(self): ...
    def data_received(self, chunk): ...
    def log_exception(self, typ, value, tb): ...

def asynchronous(method): ...
def stream_request_body(cls): ...
def removeslash(method): ...
def addslash(method): ...

class Application(httputil.HTTPServerConnectionDelegate):
    transforms = ... # type: Any
    handlers = ... # type: Any
    named_handlers = ... # type: Any
    default_host = ... # type: Any
    settings = ... # type: Any
    ui_modules = ... # type: Any
    ui_methods = ... # type: Any
    def __init__(self, handlers=None, default_host='', transforms=None, **settings): ...
    def listen(self, port, address='', **kwargs): ...
    def add_handlers(self, host_pattern, host_handlers): ...
    def add_transform(self, transform_class): ...
    def start_request(self, server_conn, request_conn): ...
    def __call__(self, request): ...
    def reverse_url(self, name, *args): ...
    def log_request(self, handler): ...

class _RequestDispatcher(httputil.HTTPMessageDelegate):
    application = ... # type: Any
    connection = ... # type: Any
    request = ... # type: Any
    chunks = ... # type: Any
    handler_class = ... # type: Any
    handler_kwargs = ... # type: Any
    path_args = ... # type: Any
    path_kwargs = ... # type: Any
    def __init__(self, application, connection): ...
    def headers_received(self, start_line, headers): ...
    stream_request_body = ... # type: Any
    def set_request(self, request): ...
    def data_received(self, data): ...
    def finish(self): ...
    def on_connection_close(self): ...
    handler = ... # type: Any
    def execute(self): ...

class HTTPError(Exception):
    status_code = ... # type: Any
    log_message = ... # type: Any
    args = ... # type: Any
    reason = ... # type: Any
    def __init__(self, status_code, log_message=None, *args, **kwargs): ...

class Finish(Exception): ...

class MissingArgumentError(HTTPError):
    arg_name = ... # type: Any
    def __init__(self, arg_name): ...

class ErrorHandler(RequestHandler):
    def initialize(self, status_code): ...
    def prepare(self): ...
    def check_xsrf_cookie(self): ...

class RedirectHandler(RequestHandler):
    def initialize(self, url, permanent=True): ...
    def get(self): ...

class StaticFileHandler(RequestHandler):
    CACHE_MAX_AGE = ... # type: Any
    root = ... # type: Any
    default_filename = ... # type: Any
    def initialize(self, path, default_filename=None): ...
    @classmethod
    def reset(cls): ...
    def head(self, path): ...
    path = ... # type: Any
    absolute_path = ... # type: Any
    modified = ... # type: Any
    def get(self, path, include_body=True): ...
    def compute_etag(self): ...
    def set_headers(self): ...
    def should_return_304(self): ...
    @classmethod
    def get_absolute_path(cls, root, path): ...
    def validate_absolute_path(self, root, absolute_path): ...
    @classmethod
    def get_content(cls, abspath, start=None, end=None): ...
    @classmethod
    def get_content_version(cls, abspath): ...
    def get_content_size(self): ...
    def get_modified_time(self): ...
    def get_content_type(self): ...
    def set_extra_headers(self, path): ...
    def get_cache_time(self, path, modified, mime_type): ...
    @classmethod
    def make_static_url(cls, settings, path, include_version=True): ...
    def parse_url_path(self, url_path): ...
    @classmethod
    def get_version(cls, settings, path): ...

class FallbackHandler(RequestHandler):
    fallback = ... # type: Any
    def initialize(self, fallback): ...
    def prepare(self): ...

class OutputTransform:
    def __init__(self, request): ...
    def transform_first_chunk(self, status_code, headers, chunk, finishing): ...
    def transform_chunk(self, chunk, finishing): ...

class GZipContentEncoding(OutputTransform):
    CONTENT_TYPES = ... # type: Any
    MIN_LENGTH = ... # type: Any
    def __init__(self, request): ...
    def transform_first_chunk(self, status_code, headers, chunk, finishing): ...
    def transform_chunk(self, chunk, finishing): ...

def authenticated(method): ...

class UIModule:
    handler = ... # type: Any
    request = ... # type: Any
    ui = ... # type: Any
    locale = ... # type: Any
    def __init__(self, handler): ...
    @property
    def current_user(self): ...
    def render(self, *args, **kwargs): ...
    def embedded_javascript(self): ...
    def javascript_files(self): ...
    def embedded_css(self): ...
    def css_files(self): ...
    def html_head(self): ...
    def html_body(self): ...
    def render_string(self, path, **kwargs): ...

class _linkify(UIModule):
    def render(self, text, **kwargs): ...

class _xsrf_form_html(UIModule):
    def render(self): ...

class TemplateModule(UIModule):
    def __init__(self, handler): ...
    def render(self, path, **kwargs): ...
    def embedded_javascript(self): ...
    def javascript_files(self): ...
    def embedded_css(self): ...
    def css_files(self): ...
    def html_head(self): ...
    def html_body(self): ...

class _UIModuleNamespace:
    handler = ... # type: Any
    ui_modules = ... # type: Any
    def __init__(self, handler, ui_modules): ...
    def __getitem__(self, key): ...
    def __getattr__(self, key): ...

class URLSpec:
    regex = ... # type: Any
    handler_class = ... # type: Any
    kwargs = ... # type: Any
    name = ... # type: Any
    def __init__(self, pattern, handler, kwargs=None, name=None): ...
    def reverse(self, *args): ...

url = ... # type: Any

def create_signed_value(secret, name, value, version=None, clock=None, key_version=None): ...
def decode_signed_value(secret, name, value, max_age_days=31, clock=None, min_version=None): ...
def get_signature_key_version(value): ...
