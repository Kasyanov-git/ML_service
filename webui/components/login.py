import dash_html_components as html
import dash_core_components as dcc

def login_component():
    return html.Div([
        dcc.Input(id="username", type="text", placeholder="Введите имя пользователя"),
        dcc.Input(id="password", type="password", placeholder="Введите пароль"),
        html.Button('Войти', id='login-button'),
    ])
