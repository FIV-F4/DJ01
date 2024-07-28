from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def data(request):
    date_html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Текущая дата и время</title>
    </head>
    <body>
        <h1>Текущая дата и время:</h1>
        <p id="datetime"></p>
        <script>
            document.getElementById('datetime').innerText = new Date().toLocaleString();
        </script>
    </body>
    </html>
    """
    return HttpResponse(date_html)

def test(request):
    test_html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Тест</title>
    </head>
    <body>
        <h1>Простой тест</h1>
        <form>
            <p>Какой сейчас год?</p>
            <input type="radio" id="2023" name="year" value="2023">
            <label for="2023">2023</label><br>
            <input type="radio" id="2024" name="year" value="2024">
            <label for="2024">2024</label><br>
            <input type="radio" id="2025" name="year" value="2025">
            <label for="2025">2025</label><br>
            <button type="button" onclick="checkAnswer()">Проверить ответ</button>
        </form>
        <p id="result"></p>
        <script>
            function checkAnswer() {
                var year = document.querySelector('input[name="year"]:checked').value;
                if (year == "2024") {
                    document.getElementById('result').innerText = "Правильно!";
                } else {
                    document.getElementById('result').innerText = "Неправильно, попробуйте ещё раз.";
                }
            }
        </script>
    </body>
    </html>
    """
    return HttpResponse(test_html)