import time
from googletrans import Translator
from googletrans.constants import LANGUAGES
translator = Translator()
count = 1
phrase = input('give a sentence to translate it to all languages : ')
for lang in LANGUAGES.keys():
    trans = translator.translate(phrase, src='en', dest=lang).text    
    #transback =  translator.translate(trans, src=lang, dest='en').text # to convert back to eng 
    print(f'{count}) {lang} ---> {trans}')
    count += 1 
