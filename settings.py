from urllib3 import make_headers

REQUEST_KWARGS={
    'proxy_url': 'http://194.124.48.185:8000',
    'urllib3_proxy_kwargs': {
        'proxy_headers': make_headers(proxy_basic_auth='ZtkhvB:q5FyzN')
                            }
                }

API_KEY = "911611551:AAEhkAQPoueOzwZJfe4N8YtC4OXpFGgltiw"

CLARIFAI_API_KEY = "48fc9760e715466a8748f89169104af5"

MONGO_LINK = "mongodb+srv://telegrambot:394935@cluster0-yocf3.mongodb.net/mybot?retryWrites=true&w=majority"

MONGO_DB = "mybot"
