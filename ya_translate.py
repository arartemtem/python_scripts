import json
import requests

api_key = 'trnsl.1.1.20170325T072008Z.efcdb38a4a5a6507.a37fbdba88fed8c6cf2fb72b2323f0be49280539'    # your api key here


def translate(langs):
    def wrapper(text_to_translate):
        lang = langs(text_to_translate)
        tr_link = 'https://translate.yandex.net/api/v1.5/tr.json/translate?lang={}&text={}&key={}'.format(lang, text_to_translate, api_key)
        translate_request = requests.get(tr_link)
        recived_translation = translate_request.json()
        translation = recived_translation['text']
        return translation[:2]
    return wrapper


@translate
def lang_detection(text_to_translate):
    det_link = 'https://translate.yandex.net/api/v1.5/tr.json/detect?hint=en,de&text={}&key={}'.format(text_to_translate, api_key)
    detect_request = requests.get(det_link)
    recived_json = detect_request.json()
    text_lang = recived_json['lang']
    if text_lang == 'en':
        return 'en-ru'
    elif text_lang == 'ru':
        return 'ru-en'
    else:
        print('error')

endless_loop = 1
while endless_loop == 1:
    text = input('text to translate: ')
    result = lang_detection(text)
    print('translated text: ', *result)
