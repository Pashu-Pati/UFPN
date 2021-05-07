from translate import Translator
translator= Translator(from_lang="russian",to_lang="english")
translation = translator.translate("как поживаешь чувак")
import pyperclip
##pyperclip.copy('The text to be copied to the clipboard.')
spam = pyperclip.paste()
print (spam, translation)
