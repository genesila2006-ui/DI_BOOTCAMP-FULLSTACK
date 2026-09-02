import asyncio
import googletrans # type: ignore

async def translate_words():
    translator = googletrans.googletrans.Translator()
    french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
    
    # Translate all words from French to English
    translations = await translator.translate(french_words, src='fr', dest='en')
    
    # Build dictionary matching original words to translated text
    result = {original: trans.text for original, trans in zip(french_words, translations)}
    print(result)

# Execute async function
asyncio.run(translate_words())
# Synchronous Solution (Alternative / Standard deep_translator)
# If you prefer a synchronous approach without asyncio, you can iterate through the list individually with googletrans or use deep_translator:

import asyncio

translator = googletrans.googletrans.Translator()
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

# Helper to run translation synchronously in standard scripts
result = {
    word: asyncio.run(translator.translate(word, src='fr', dest='en')).text 
    for word in french_words
}

print(result)
# Output:

# JSON
{"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}