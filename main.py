import requests
import argostranslate.package
import argostranslate.translate

from_code = "en"
to_code = "ja"

translatedText = argostranslate.translate.translate(requests.get("http://numbersapi.com/random/trivia").text, from_code, to_code)
print(translatedText)

with open("readme.md", mode="w", encoding="utf-8") as f:
  f.wright(translatedText)
