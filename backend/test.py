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

def text_translate(origin: str, country: str) -> str:
    translator = Translator()
    try:
        result = translator.translate(origin, supported_language[country])
        return result.text
    except:
        return ""
    
# print(text_translate('hello', 'korean'))
# print(text_translate('你好', 'korean'))
# print(text_translate('مرحبا', 'korean'))
# print(text_translate('El sol brilla en el cielo azul.', 'korean'))
# print(text_translate('Bonjour', 'korean'))
# print(text_translate('안녕하세요', 'korean'))
# print(text_translate('こんにちは', 'korean'))

"""
1. db에서 꺼내온 메시지들
상대방이 보낸 것들을 나의 fluent 조회해서 번역하고 서버에서 concat하고 보내주기.

2. 소켓 통해서 들어오느것들
프론트에서 concat해야함

내가 보냄.


상대방이 보냄.
"""