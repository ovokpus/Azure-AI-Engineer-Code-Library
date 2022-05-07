@echo off

rem Set values for your Language Understanding app
set app_id=9873c716-ec7c-40a0-8be3-f2aeb1cd5d5f
set endpoint=https://ovo-luis.cognitiveservices.azure.com/
set key=75f9c5c8bd524dc398a729d396a986df

rem Get parameter and encode spaces for URL
set input=%1
set query=%input: =+%

rem Use cURL to call the REST API
curl -X GET "%endpoint%/luis/prediction/v3.0/apps/%app_id%/slots/production/predict?subscription-key=%key%&log=true&query=%query%"