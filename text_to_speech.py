from gtts import gTTS
import os
import time

# Text to speech
"""Application to convert text to speech."""

name = "                                                         Text to speech        "
print(name)
print("""
""")

time.sleep(2)

print("""This is the text to speech project by Amey.
In this program, you can type what you want and the default music player on 
your computer will open. Then, what you typed will play.""")
print("_____________________________________________________________________________")

time.sleep(5)

text = input("""Please enter the text below-
""")
language = 'en'

speech = gTTS(text=text, lang=language, slow=False)
speech.save('text.mp3')

os.system("Start text.mp3")

time.sleep(4)

print("Hope you enjoyed it!")

time.sleep(2)

print("Thank you!")
