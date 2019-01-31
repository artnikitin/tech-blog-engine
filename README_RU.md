# Личный техблог с админ-страницей для редактирования постов

Минималистичная версия [clean blog theme](https://github.com/BlackrockDigital/startbootstrap-clean-blog) от BlackRockDigital с кастомным движком на Flask. 

Размещен на [timnikitin.com](https://timnikitin.com).

## С чего начать

Эти инструкции позволят скачать копию проекта и запустить его на локальной машине для разработки и тестирования.

### Установка пакетов

Проект работает на Python 3. Для установки остальных модулей и библиотек, запустите:

```
$ pip install -r requirements.txt
```

### Запуск приложения

Скачайте репозиторую вручную или запустите:

```
$ git clone https://github.com/artnikitin/tech-blog-engine.git
$ cd tech-blog-engine
$ export FLASK_APP=application.py
$ flask run
```

## Использование

### Домашняя страница


![Alt text](static/img/blog_home.png?raw=true)

### Страница поста


![Alt text](static/img/blog_post.png?raw=true)

### Комментарии


**Для комментариев использована библиотека Disqus**

![Alt text](static/img/blog_comments.png?raw=true)

**а для использования математических символов в посте [MathJax](https://www.mathjax.org), javascript библиотека для отображения LaTeX кода в браузере**

![Alt text](static/img/blog_math.png?raw=true)

### Архив

![Alt text](static/img/blog_archive.png?raw=true)

### Панель управления

**Вы можете получить доступ к админ-странице сайта через /admin. Логин:**

![Alt text](static/img/blog_login.png?raw=true)

**Редактор постов:**

![Alt text](static/img/blog_admin.png?raw=true)

**Во время сессии вы можете как редактировать посты,**

![Alt text](static/img/blog_modifypost.png?raw=true)

**так и создавать новые**

![Alt text](static/img/blog_newpost.png?raw=true)

**В качестве WYSIWYG-редактора постов использована библиотека [TinyMCE](https://www.tiny.cloud). Url постов формируются динамически с использованием regex.**

## Стек

* Python 3.5
* Flask
* Jinja2
* SQLite3, SQLAlchemy

## Авторы

* **Артем Никитин** - [artnikitin](https://github.com/artnikitin)

## Лицензия

MIT License.
