# Импортируем классы Flask: само приложение и render_template,
# который подставляет переменные в HTML-шаблоны
from flask import Flask, render_template

# Создаём приложение. __name__ — имя текущего файла,
# по нему Flask находит папки templates/ и static/
app = Flask(__name__)


# Главная страница: URL "/" открывает index.html
@app.route("/")
def main_page():
    return render_template('index.html')


# Страница первого поста — трек «Авторитет в прах»
@app.route("/blog/1")
def blog_post_1():
    return render_template('post_1.html')


# Страница второго поста (названия функций приведены к единому стилю)
@app.route("/blog/2")
def blog_post_2():
    return render_template('post_2.html')


# Страница «Обо мне» — биография и анонс концерта
@app.route("/about")
def about_page():
    return render_template('about_me.html')


@app.route("/concerts")
def concerts_page():
    return render_template('concerts.html')

# Запуск сервера. debug=True включает автоперезагрузку
# при изменении кода и подробные ошибки в браузере
if __name__ == "__main__":
    app.run(debug=True)
