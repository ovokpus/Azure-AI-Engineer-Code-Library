from dotenv import load_dotenv
from datetime import datetime
import os

# Import namespaces
import azure.cognitiveservices.speech as speech_sdk
from playsound import playsound


def main():
    try:
        global speech_config
        global translation_config

        # Get Configuration Settings
        load_dotenv()
        cog_key = os.getenv('COG_SERVICE_KEY')
        cog_region = os.getenv('COG_SERVICE_REGION')

        # Configure translation
        translation_config = speech_sdk.translation.SpeechTranslationConfig(
            cog_key, cog_region)
        translation_config.speech_recognition_language = "en-US"
        translation_config.add_target_language('fr')
        translation_config.add_target_language('es')
        translation_config.add_target_language('hi')
        print('Ready to translate from',
              translation_config.speech_recognition_language)

        # Configure speech
        speech_config = speech_sdk.SpeechConfig(cog_key, cog_region)

        # Get user input
        targetLanguage = ''
        while targetLanguage != 'quit':
            targetLanguage = input(
                '\nEnter a target language\n fr = French\n es = Spanish\n hi = Hindi\n Enter anything else to stop\n').lower()
            if targetLanguage in translation_config.target_languages:
                Translate(targetLanguage)
            else:
                targetLanguage = 'quit'

    except Exception as ex:
        print(ex)


def Translate(targetLanguage):
    translation = ''

    # Translate speech if you have a working microphone
    audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
    translator = speech_sdk.translation.TranslationRecognizer(
        translation_config, audio_config)
    print("Speak now...")
    result = translator.recognize_once_async().get()
    print('Translating "{}"'.format(result.text))
    translation = result.translations[targetLanguage]
    print(translation)

    # Translate speech using audio input from a file
    # audioFile = 'station.wav'
    # playsound(audioFile)
    # audio_config = speech_sdk.AudioConfig(filename=audioFile)
    # translator = speech_sdk.translation.TranslationRecognizer(
    #     translation_config, audio_config)
    # print("Getting speech from file...")
    # result = translator.recognize_once_async().get()
    # print('Translating "{}"'.format(result.text))
    # translation = result.translations[targetLanguage]
    # print(translation)
    # Synthesize translation
    voices = {
        "fr": "fr-FR-HenriNeural",
        "es": "es-ES-ElviraNeural",
        "hi": "hi-IN-MadhurNeural"
    }
    speech_config.speech_synthesis_voice_name = voices.get(targetLanguage)
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)
    speak = speech_synthesizer.speak_text_async(translation).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)


if __name__ == "__main__":
    main()
