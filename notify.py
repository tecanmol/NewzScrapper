import requests

def send_notification(contents):
    requests.post("https://ntfy.sh/personal_newz_scrapper0808",
    data=contents.encode(encoding='utf-8'))
