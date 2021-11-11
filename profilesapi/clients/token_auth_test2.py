import requests


def client():
    # data = {
    #     'username': 'test',
    #     'email': 'test@rest.com',
    #     'password1': 'Blind101',
    #     'password2': 'Blind101'
    # }

    # response = requests.post(
    #     'http://127.0.0.1:8000/api/rest-auth/registration/',
    #     data=data
    # )

    headers = {'Authorization': 'Token d41b21b9305e86b120a30379952b97d5e8a7f9da'}

    response = requests.get(
        'http://127.0.0.1:8000/api/profiles/',
        headers=headers
    )

    print('Status Code:', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ ==  '__main__':
    client()