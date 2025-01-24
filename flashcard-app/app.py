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
my_flashcards = {}
#class to store the english and translation:
class Flashcards:
    def __init__(self, english, translation):
        self.__english = english
        self.__translation = translation
    #getter methods for the private variables:
    def get_english(self):
        return self.__english
    def get_translation(self):
        return self.__translation
    #override the __str__ method for the object:
    def __str__(self):
        return f"{self.__english}: {self.__translation}"
    #to check to see if flashcards are the same (override so doesn't compare addresses):
    def __eq__(self, other):
        if isinstance(other, Flashcards):
            return self.__english == other.__english

#will be the main function that is run: 
def welcome():
    print("Welcome to flashcard frenzy!\nThis program generates flashcards just for you- so you can study what you want, without wasting time on topics that don't interest you")
    menu()
#to print the menu and get user's selection
def menu():
    print("\nPlease make a selection from the options below: ")
    getOption()
    
#to get user's selection:
def getOption():
    seeOptions() #prints out the options (good on multiple entries)
    ans = int(input("Enter a number 1 through 5: "))
    #entry by user out of scope
    while ans>5 or ans<0:
        ans = int(input("Invalid entry. Please enter a number 1 through 5. To see options, enter 6: "))
        if (ans == 6):
            seeOptions()
            ans = int(input("Now enter your selection (1-5): "))
    #valid entry has been made:
    if ans == 1:
        addflash()
    elif ans == 2:
        removeflash()
    elif ans ==3:
        showflash()
    elif ans ==4:
        testflash()
    else:
        exit()

#prints out options for selections: 
def seeOptions():
    print("\nMENU:  \n1. Add flashcard to your set \n2. Remove a flashcard from your set \n3. See your language flashcard set\n4. Test Yourself \n5. Quit")

#to add a flashcard to the flashcard set
def addflash():
    #get the language they want to generate a flashcard for: 
    language = input("\nWhat language would you like to translate the word to? ").lower()
    #if the language is not a valid language for the Translator:
    while language not in languages.keys():
        language = input("\nInvalid entry. Please check your spelling or try learning another language. \nWhat language would you like to translate the word to?: ").lower()
    #if this is our first flashcard for the language --> establish the flashcard language set:
    if language not in my_flashcards.keys():
        my_flashcards[language] = []
    #get the language code from the languages dictionary
    language_code = languages[language]
    #create the translator object that'll be used to generate the transition:
    translator= Translator(to_lang=language_code)
    #get the desired text in english:
    text= input("What text would you like to translate: ")
    #use the translator object to get the translation:
    translation = translator.translate(text)
    #add the flashcard to the flashcard set
    newfc = Flashcards(text, translation)
    
    #what if we are creating a flashcard that already exists! don't want to add it again
    if newfc in my_flashcards[language]:
        print("Already added flashcard! Try adding a new word.")
    else: #we are adding a new flashcard that doesn't exist
        my_flashcards[language].append(newfc)
        
        print(f"\nYou have typed: \"{text}\", which translates to: \"{translation}\" in {language}")
        print("We have added the flashcard to your deck!")
    getOption()
    
#to see the flashcards currently in the language set:
def showflash():
    #get the language that user wants to see:
    language = input("\nWhat language would you like to review? ").lower()
    #invalid language entry:
    while language not in languages.keys():
        language = input("\nInvalid language entered. Please check your spelling or make sure it is an accepted language: ").lower()
    #no flashcards in our flashcard set for this language:
    if language not in my_flashcards:
        print("You do not have any flashcards in this language. Add some and come back later! \n")
    #there are flashcards in this language set (get all of them):
    entry = my_flashcards[language]
    #print out each flaschard in there
    print("\nYour flashcards: ")
    for fc in entry:
        print(fc) #fc is flashcard object --> overrides str to print eng and translation
    
    getOption()
    
welcome()
    