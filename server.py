#!/usr/bin/env python
# coding=utf-8

from flask import Flask, request

from saferproxyfix import SaferProxyFix

app = Flask(__name__)

app.wsgi_app = SaferProxyFix(app.wsgi_app)


@app.route('/')
def get_requester_ip():
    return request.remote_addr


if __name__ == '__main__':
    params = {'host': '0.0.0.0',
              'port': 8081}
    app.run(**params)
