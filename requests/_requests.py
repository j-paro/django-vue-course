import sys
import requests


if __name__ == '__main__':
    payload = {'access_key': '45a70dc23344db4c80691df95b90f8df'}
    response = requests.get(
        'http://api.exchangeratesapi.io/v1/latest',
        params=payload
    )

    if response.status_code != 200:
        sys.stderr.write(f"Error: Response: {response.json()}\n")
        exit(1)
    
    data = response.json()
    print(data)