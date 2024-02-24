from gtts import gTTS


def text_to_speech(text):
    tts = gTTS(text, lang='en', tld='co.in')
    tts.save('result.mp3')
    