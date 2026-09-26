# todo: добавьте во Flask маршруты для страниц (endpoint)
# - О компании
# - Контакты
# - Список постов

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <h1>Hello World!</h1>
    <p>Добро пожаловать на наш сайт.</p>
    <p><a href="/about">О компании</a> | 
       <a href="/contacts">Контакты</a> | 
       <a href="/posts">Список постов</a></p>
    """

@app.route('/about')
def about():
    return """
    <h1>О компании</h1>
    <p>СТЦ.</p>
    <p><a href="/">← На главную</a></p>
    """

@app.route('/contacts')
def contacts():
    return """
    <h1>Контакты</h1>
    <p>📧 Email: info@example.com</p>
    <p>📞 Телефон: +7 (999) 123-45-67</p>
    <p>📍 Адрес: Санкт-Петербург</p>
    <p><a href="/">← На главную</a></p>
    """

@app.route('/posts')
def posts():
    posts_list = [
        "Docker для начинающих",
        "Курсы повышения квалификации 'Программирование на языке Python'"
    ]
    
    html = "<h1>Список постов</h1><ul>"
    for post in posts_list:
        html += f"<li>{post}</li>"
    html += "</ul>"
    html += '<p><a href="/">← На главную</a></p>'
    
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)