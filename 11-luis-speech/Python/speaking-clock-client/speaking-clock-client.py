from dotenv import load_dotenv
import os
import json
from datetime import datetime, timedelta, date
from dateutil.parser import parse as is_date

# Import namespaces
import azure.cognitiveservices.speech as speech_sdk
from playsound import playsound


def main():

    try:
        # Get Configuration Settings
        load_dotenv()
        lu_app_id = os.getenv('LU_APP_ID')
        lu_prediction_region = os.getenv('LU_PREDICTION_REGION')
        lu_prediction_key = os.getenv('LU_PREDICTION_KEY')

        # Configure speech service and get intent recognizer if you have a working microphone
        speech_config = speech_sdk.SpeechConfig(
            subscription=lu_prediction_key, region=lu_prediction_region)
        audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
        print("Speak now...")
        recognizer = speech_sdk.intent.IntentRecognizer(
            speech_config, audio_config)

        # Configure speech service and get intent recognizer if you need to use an audio file
        # audioFile = 'time-in-london.wav'
        # playsound(audioFile)
        # speech_config = speech_sdk.SpeechConfig(
        #     subscription=lu_prediction_key, region=lu_prediction_region)
        # audio_config = speech_sdk.AudioConfig(filename=audioFile)
        # recognizer = speech_sdk.intent.IntentRecognizer(
        #     speech_config, audio_config)

        # Get the model from the AppID and add the intents we want to use
        model = speech_sdk.intent.LanguageUnderstandingModel(app_id=lu_app_id)
        intents = [
            (model, "GetTime"),
            (model, "GetDate"),
            (model, "GetDay"),
            (model, "None")
        ]
        recognizer.add_intents(intents)

        # Process speech input
        intent = ''
        result = recognizer.recognize_once_async().get()
        if result.reason == speech_sdk.ResultReason.RecognizedIntent:
            intent = result.intent_id
            print("Query: {}".format(result.text))
            print("Intent: {}".format(intent))
            json_response = json.loads(result.intent_json)
            print("JSON Response:\n{}\n".format(
                json.dumps(json_response, indent=2)))

            # Get the first entity (if any)
            entity_type = ''
            entity_value = ''
            if len(json_response["entities"]) > 0:
                entity_type = json_response["entities"][0]["type"]
                entity_value = json_response["entities"][0]["entity"]
                print(entity_type + ': ' + entity_value)

            # Apply the appropriate action
            if intent == 'GetTime':
                location = 'local'
                # Check for entities
                if entity_type == 'Location':
                    location = entity_value
                # Get the time for the specified location
                print(GetTime(location))

            elif intent == 'GetDay':
                date_string = date.today().strftime("%m/%d/%Y")
                # Check for entities
                if entity_type == 'Date':
                    date_string = entity_value
                # Get the day for the specified date
                print(GetDay(date_string))

            elif intent == 'GetDate':
                day = 'today'
                # Check for entities
                if entity_type == 'Weekday':
                    # List entities are lists
                    day = entity_value
                # Get the date for the specified day
                print(GetDate(day))

            else:
                # Some other intent (for example, "None") was predicted
                print('You said {}'.format(result.text))
                if result.text.lower().replace('.', '') == 'stop':
                    intent = result.text
                else:
                    print('Try asking me for the time, the day, or the date.')

        elif result.reason == speech_sdk.ResultReason.RecognizedSpeech:
            # Speech was recognized, but no intent was identified.
            intent = result.text
            print("I don't know what {} means.".format(intent))
        elif result.reason == speech_sdk.ResultReason.NoMatch:
            # Speech wasn't recognized
            print("Sorry. I didn't understand that.")
        elif result.reason == speech_sdk.ResultReason.Canceled:
            # Something went wrong
            print("Intent recognition canceled: {}".format(
                result.cancellation_details.reason))
            if result.cancellation_details.reason == speech_sdk.CancellationReason.Error:
                print("Error details: {}".format(
                    result.cancellation_details.error_details))

    except Exception as ex:
        print(ex)


def GetTime(location):
    time_string = ''

    # Note: To keep things simple, we'll ignore daylight savings time and support only a few cities.
    # In a real app, you'd likely use a web service API (or write  more complex code!)
    # Hopefully this simplified example is enough to get the the idea that you
    # use LU to determine the intent and entitites, then implement the appropriate logic

    if location.lower() == 'local':
        now = datetime.now()
        time_string = '{}:{:02d}'.format(now.hour, now.minute)
    elif location.lower() == 'london':
        utc = datetime.utcnow()
        time_string = '{}:{:02d}'.format(utc.hour, utc.minute)
    elif location.lower() == 'sydney':
        time = datetime.utcnow() + timedelta(hours=11)
        time_string = '{}:{:02d}'.format(time.hour, time.minute)
    elif location.lower() == 'new york':
        time = datetime.utcnow() + timedelta(hours=-5)
        time_string = '{}:{:02d}'.format(time.hour, time.minute)
    elif location.lower() == 'nairobi':
        time = datetime.utcnow() + timedelta(hours=3)
        time_string = '{}:{:02d}'.format(time.hour, time.minute)
    elif location.lower() == 'tokyo':
        time = datetime.utcnow() + timedelta(hours=9)
        time_string = '{}:{:02d}'.format(time.hour, time.minute)
    elif location.lower() == 'delhi':
        time = datetime.utcnow() + timedelta(hours=5.5)
        time_string = '{}:{:02d}'.format(time.hour, time.minute)
    else:
        time_string = "I don't know what time it is in {}".format(location)

    return time_string


def GetDate(day):
    date_string = 'I can only determine dates for today or named days of the week.'

    weekdays = {
        "monday": 0,
        "tuesday": 1,
        "wednesday": 2,
        "thusday": 3,
        "friday": 4,
        "saturday": 5,
        "sunday": 6
    }

    today = date.today()

    # To keep things simple, assume the named day is in the current week (Sunday to Saturday)
    day = day.lower()
    if day == 'today':
        date_string = today.strftime("%m/%d/%Y")
    elif day in weekdays:
        todayNum = today.weekday()
        weekDayNum = weekdays[day]
        offset = weekDayNum - todayNum
        date_string = (today + timedelta(days=offset)).strftime("%m/%d/%Y")

    return date_string


def GetDay(date_string):
    # Note: To keep things simple, dates must be entered in US format (MM/DD/YYYY)
    try:
        date_object = datetime.strptime(date_string, "%m/%d/%Y")
        day_string = date_object.strftime("%A")
    except:
        day_string = 'Enter a date in MM/DD/YYYY format.'
    return day_string


if __name__ == "__main__":
    main()
