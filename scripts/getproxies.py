#!/opt/homebrew/bin/python3
import requests

rtype = input('HTTP/https :') or 'http'
country = input('2-Letter Country-Code: ') or 'CN'
print(rtype)
print(country)
def send_request():

    try:
        response = requests.get(
            url="https://www.proxy-list.download/api/v1/get",
            params={
                "type": rtype,
                "anon": "elite",
                "country": country,
            },
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

send_request()
