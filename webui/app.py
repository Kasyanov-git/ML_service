import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from api_client import get_auth_token

# Инициализация приложения Dash
app = dash.Dash(__name__)

# Определение макета приложения
app.layout = html.Div([
    dcc.Store(id='session', storage_type='session'),
    html.H1("Приложение для предсказаний"),
    html.Div([
        html.Div("Имя пользователя:"),
        dcc.Input(id="username", type="text", placeholder="Введите имя пользователя"),
        html.Div("Пароль:"),
        dcc.Input(id="password", type="password", placeholder="Введите пароль"),
        html.Button('Войти', id='login-button'),
    ]),
    html.Div(id="prediction-inputs", style={"display": "none"}),
    html.Div(id="prediction-results")
])

# Callback для обработки входа в систему
@app.callback(
    Output('prediction-inputs', 'style'),
    [Input('login-button', 'n_clicks')],
    [State('username', 'value'), State('password', 'value')]
)
def login(n_clicks, username, password):
    if n_clicks and username and password:
        # Здесь должна быть логика аутентификации и получения токена
        return {"display": "block"}
    return {"display": "none"}

# Callback функция для входа в систему
@app.callback(
   Output('session', 'data'),
   Input('login-button', 'n_clicks'),
   State('username', 'value'),
   State('password', 'value')
)
def login(n_clicks, username, password):
   if n_clicks:
       token = get_auth_token(username, password)
       if token:
           return {'token': token}
       # Обработка ошибки аутентификации
   return {}

# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)




