from googletrans import Translator 

translator = Translator()

text = input("What text do you want to translate? ")

print(" ")

print("What is your source language?")

print(" ")

print("Language Name	Language Code")
print("Afrikaans	af")
print("Irish	    ga")
print("Albanian	sq")
print("Italian	it")
print("Arabic	ar")
print("Japanese	ja")
print("Azerbaijani	az")
print("Kannada	kn")
print("Basque	eu")
print("Korean	ko")
print("Bengali	bn")
print("English	en")
print("French	fr")
print("German	de")
print("Tamil	ta")
print("Telugu	te")
print("Gujarati	gu")
print("Hindi	hi")
print("Urdu	ur")
print("Hungarian	hu")
print("Vietnamese	vi")
print("Icelandic")
print("Welsh	cy")
print("Indonesian	id")
print("Yiddish	yi")

print(" ")

source_language = str(input("Choose your source language code from the above list "))

dest_language = str(input("Choose your destination language code from the above list "))

converted_text = translator.translate(text,src=source_language,dest=dest_language)

print(converted_text.text)