from flask import Flask, redirect
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <style>
            body { font-family: Arial; text-align: center; margin-top: 50px; background: #1a1a2e; color: white; }
            h1 { color: #00d4ff; }
            .menu { margin-top: 30px; }
            a { display: inline-block; margin: 15px; padding: 15px 30px; background: #16213e; border: 2px solid #00d4ff; 
                color: #00d4ff; text-decoration: none; border-radius: 8px; font-size: 18px; cursor: pointer; }
            a:hover { background: #00d4ff; color: #1a1a2e; }
        </style>
    </head>
    <body>
        <h1>🎭 Добро пожаловать в тайный мир!</h1>
        <p>Выбери одно из трёх чудес:</p>
        <div class="menu">
            <a href="/coin">🪙 Бросок монетки</a><br>
            <a href="/password">🔐 Генератор пароля</a><br>
            <a href="/message">🧙 Тайное послание</a>
        </div>
    </body>
    </html>
    '''

@app.route('/coin')
def coin():
    result = random.choice(['🪙 Орел!', '🪙 Решка!'])
    return f'''
    <html>
    <head>
        <style>
            body {{ font-family: Arial; text-align: center; margin-top: 50px; background: #1a1a2e; color: white; }}
            h1 {{ color: #00d4ff; }}
            .result {{ font-size: 48px; margin: 30px; }}
            a {{ color: #00d4ff; text-decoration: none; }}
        </style>
    </head>
    <body>
        <h1>Ты нашёл тайную страницу!</h1>
        <div class="result">{result}</div>
        <p><a href="/">← Вернуться в меню</a> | <a href="/coin">🔄 Бросить ещё раз</a></p>
    </body>
    </html>
    '''

@app.route('/password')
def password_gen():
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
    return f'''
    <html>
    <head>
        <style>
            body {{ font-family: Arial; text-align: center; margin-top: 50px; background: #1a1a2e; color: white; }}
            h1 {{ color: #00d4ff; }}
            .password {{ font-size: 32px; background: #16213e; padding: 20px; margin: 30px auto; 
                         width: fit-content; border-radius: 8px; color: #00ff00; font-family: monospace; }}
            a {{ color: #00d4ff; text-decoration: none; }}
        </style>
    </head>
    <body>
        <h1>🔐 Генератор пароля</h1>
        <div class="password">{password}</div>
        <p><a href="/">← Вернуться в меню</a> | <a href="/password">🔄 Новый пароль</a></p>
    </body>
    </html>
    '''

@app.route('/message')
def message():
    messages = [
        'Ты молод! Перед тобой открывается бесконечность! 🧙',
        'Магия вокруг... Нужно только верить! ✨',
        'Загадка: что быстрее - мысль или свет? 🤔',
        'Добро пожаловать в мир магии! Ты не один здесь... 🌙',
        'Секрет: все мы сделаны из звёзд! 🌟'
    ]
    return f'''
    <html>
    <head>
        <style>
            body {{ font-family: Arial; text-align: center; margin-top: 50px; background: #1a1a2e; color: white; }}
            h1 {{ color: #00d4ff; }}
            .message {{ font-size: 28px; background: #16213e; padding: 40px; margin: 30px auto; 
                        width: fit-content; border-radius: 8px; color: #ffff00; }}
            a {{ color: #00d4ff; text-decoration: none; }}
        </style>
    </head>
    <body>
        <h1>🧙 Тайное послание</h1>
        <div class="message">{random.choice(messages)}</div>
        <p><a href="/">← Вернуться в меню</a> | <a href="/message">🔄 Новое послание</a></p>
    </body>
    </html>
    '''

@app.route('/secret')
def secret():
    return redirect('/')

if __name__ == '__main__':
    app.run()





