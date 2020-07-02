from translate import Translator

translator= Translator(to_lang="ger")
my_file = open('TranslateMe.txt')
text = my_file.read()
translation = translator.translate(text)
print(translation)
