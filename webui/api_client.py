# Этот код должен быть интегрирован в компоненты Dash
import requests

# URL API для аутентификации и получения токена
AUTH_URL = "http://localhost:8000/auth/token"

# Функция для отправки запроса на аутентификацию
def get_auth_token(username, password):
    response = requests.post(AUTH_URL, data={'username': username, 'password': password})
    if response.status_code == 200:
        return response.json()['access_token']
    return None

# URL API для создания задачи расчета предсказаний
PREDICTION_URL = "http://localhost:8000/predict/create"

# Функция для отправки запроса на создание задачи предсказания
def create_prediction_task(token, user_input):
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(PREDICTION_URL, headers=headers, json={'input_data': user_input})
    if response.status_code == 200:
        return response.json()['task_id']
    return None
