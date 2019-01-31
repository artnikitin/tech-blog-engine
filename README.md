# Tech blog engine

A modified minimalistic version of the [clean blog theme](https://github.com/BlackrockDigital/startbootstrap-clean-blog) from BlackRockDigital with customly built Flask engine. 

Hosted on [timnikitin.com](https://timnikitin.com).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Be sure to install Python3. For other modules and libraries run:

```
$ pip install -r requirements.txt
```

### Installing

Download the repository manually or run:

```
$ git clone https://github.com/artnikitin/tech-blog-engine.git
$ cd tech-blog-engine
$ export FLASK_APP=application.py
$ flask run
```

## Usage

### Home page

![Alt text](static/img/blog_home.png?raw=true)

### Post page

![Alt text](static/img/blog_post.png?raw=true)

### Comments 

**Comments are powered by Disqus**

![Alt text](static/img/blog_comments.png?raw=true)

**and math notation is running on [MathJax](https://www.mathjax.org) – a fancy javascript engine for enterpreting LaTeX in browsers**

![Alt text](static/img/blog_math.png?raw=true)

### Archive

![Alt text](static/img/blog_archive.png?raw=true)

**You can access admin dashboard via /admin url. Login:**

![Alt text](static/img/blog_login.png?raw=true)

**Dashboard:**

![Alt text](static/img/blog_admin.png?raw=true)

**During admin session you can modify old posts**

![Alt text](static/img/blog_modifypost.png?raw=true)

**or create new ones**

![Alt text](static/img/blog_newpost.png?raw=true)

**The post editing process is powered by [TinyMCE](https://www.tiny.cloud) WYSIWYG html editor. Post url's are created dynamically using regex.**

## Built With

* Python 3.5
* Flask
* Jinja2
* SQLite3, SQLAlchemy

## Authors

* **Tim Nikitin** - [artnikitin](https://github.com/artnikitin)

## Licence

MIT License.

