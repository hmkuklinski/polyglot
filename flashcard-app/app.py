from translate import Translator

languages= {
    "afrikaans": "af",
    "arabic": "ar", "albanian": 'sq', "armenian": "hy", "azerbaijani": 'az', "bengali": 'bn', "bosnian": 'bs', "bulgarian": 'bg',
    "catalan": 'ca', 'chinese(simplified)': 'zh', "chinese(traditional)": 'zh-TW', "croatian": 'hr', "czech": 'cs',
    "danish": 'da', "dutch": 'nl', "esperanto": 'eo', "estonian": 'et', "filipino": 'tl', 'finnish': 'fi', "french": 'fr',
    "hawaiian": 'haw', "hebrew": 'he', "hindi": 'hi', "hmong": 'hmn', 'hungarian': 'hu', "icelandic":'is', 'indonesian': 'id',
    'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'korean': 'ko', 'kurdish': 'ku', 'lao': 'lo', 'latin': 'la', 'lithuanian': 'lt',
    'macedonian': 'mk', 'malay': 'ms', 'mongolian': 'mn', 'nepali': 'ne', 'norwegian': 'no', 'persian': 'fa', 'polish': 'pl',
    'portuguese': 'pt', "punjabi": 'pa', "romanian": 'ro', "russian": 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'slovak': 'sk',
    'somali': 'so', 'spanish':'es', 'swahili': 'sw', 'swedish':'sv', 'tagalog': 'tl', 'thai':'th', 'turkish': 'tr', 'ukrainian': 'uk', 'vietnamese':'vi'
}

def welcome():
    print("welcome to flashcard frenzy! This program generates flashcards just for you- so you can study what you want, without wasting time on topics that don't interest you")
    menu()
def menu():
    print("Please make a selection from the options below: ")
    print("1. Add flashcard to your set \n2. Remove a flashcard from your set \n3. Study your flashcards \n4. Test Yourself \n5. Quit")


language = input("What language would you like to translate the word to? ").lower()
while language not in languages.keys():
    language = input("What language would you like to translate the word to?: ").lower()

language_code = languages[language]
translator= Translator(to_lang=language_code)
text= input("What text would you like to translate: ")
translation = translator.translate(text)
print(translation)