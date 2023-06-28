from translatepy.translators import DeeplTranslate
translater = DeeplTranslate()
# from translatepy.translators.google import GoogleTranslate
# translater = GoogleTranslate()

def translate_content(content, to='English'):
    res = translater.translate(content, to)
    return res.result