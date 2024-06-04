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
    print(origin+"-->>"+country)
    result = None
    try:
        result = translator.translate(origin, supported_language[country]).text 
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
