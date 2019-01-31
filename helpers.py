#!usr/bin/python
# -*- coding: utf-8 -*-
import re
from functools import wraps
from unidecode import unidecode
from flask import request, url_for, session, redirect

def slugify(title):
    """ Makes a url-valid string
        from blog title including
        non-Latin words """

    # ванна - vanna
    url = unidecode(title).lower()
    # убираем ' вместо мягкого знака
    url = re.sub(r"\'", "", url)
    # заменяем !:,":,": на пробелы
    url = re.sub(r"\W+", " ", url)
    # меняем пробелы на - (how-to-use-rubber-duck)
    url = re.sub(r"\s", "-", url)
    # убираем trailing signs (how- how)
    url = re.sub(r"\W$", "", url)
    # убираем знаки в начале строки (-how how)
    url = re.sub(r"^\W", "", url)
    return url

def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.11/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect(url_for("login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function