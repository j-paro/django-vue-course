import requests


def client():
    # credentials = {'username': 'justin', 'password': 'Blind101'}

    # response = requests.post(
    #     'http://127.0.0.1:8000/api/rest-auth/login/',
    #     data=credentials
    # )

    headers = {'Authorization': 'Token 13b9d722cab503e8bc81283bcbb38bf4f5086442'}

    response = requests.get(
        'http://127.0.0.1:8000/api/profiles/',
        headers=headers
    )

    print('Status Code:', response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ ==  '__main__':
    client()