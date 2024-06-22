from googletrans import Translator

## 언어지원
"""
english : en
chinese : zh-CN
arabic : ar
spanish : es
french : fr
korean : ko
japanese : ja
"""

supported_language = {
    'english' : 'en',
    'chinese' : 'zh-CN',
    'arabic' : 'ar',
    'spanish' : 'es',
    'french' : 'fr',
    'korean' : 'ko',
    'japanese' : 'ja'
}

def translate(origin: str, country: str):
    translator = Translator()
<<<<<<< HEAD
    print(country, supported_language.keys())
    if country in supported_language.keys():
        print(origin+"-->>"+country)
    
=======
    # print(origin+"-->>"+country)
>>>>>>> 756504c9e95f1c82e0dae31b5b69ac40a539e408
    result = None
    try:
        result = translator.translate(origin, supported_language[country]).text
        print(result)
        return result
    except:
        return result
    
def translate_bio(origin: str):
    translator = Translator()
    result = None
    try:
        result = translator.translate(origin, supported_language['korean']).text 
        return result
    except:
        return result
    
# print(text_translate('hello', 'korean'))
# print(text_translate('你好', 'korean'))
# print(text_translate('مرحبا', 'korean'))
# print(text_translate('El sol brilla en el cielo azul.', 'korean'))
# print(text_translate('Bonjour', 'korean'))
# print(text_translate('안녕하세요', 'korean'))
# print(text_translate('こんにちは', 'korean'))
