from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from lxml import etree
from django.http import HttpResponse
from PIL import Image
from .models import TranscribedText
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)
import subprocess
import os
import cv2
import pytesseract
import speech_recognition as sr
from pydub import AudioSegment

minioClient = Minio('play.min.io',
                    access_key='Q3AM3UQ867SPQQA43P2F',
                    secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                    secure=True)


def analyze_apk(request):
    if request.method == 'POST':
        apk_file = request.FILES['apk']
        fs = FileSystemStorage()
        filename = fs.save(apk_file.name, apk_file)
        uploaded_file_url = fs.url(filename)
        apk_path = fs.path(filename)

        # Save the uploaded file to Minio
        try:
            minioClient.fput_object('my-bucket', filename, apk_path)
        except ResponseError as err:
            print(err)

        # Extract the source files using apktool
        subprocess.run(['java', '-jar', 'apktool_2.7.0.jar', 'd', apk_path])

        # Analyze the extracted files to determine if the app is localized
        def read_strings_xml(file_path):
            tree = etree.parse(file_path)
            root = tree.getroot()
            localization_issues = []
            for child in root:
                if 'translatable' in child.attrib and child.attrib['translatable'] == 'false':
                    localization_issues.append({'name': child.attrib['name'], 'issue': 'Not Translatable'})
                if child.text is None or child.text.strip() == '':
                    localization_issues.append({'name': child.attrib['name'], 'issue': 'No Text'})
            return localization_issues

        # Usage
        strings_xml_file = 'path/to/extracted/res/values/strings.xml'
        localization_issues = read_strings_xml(strings_xml_file)

        # Provide suggestions on how to add localization and generate a new APK
        # ...

        return render(request, 'analyze.html', {'uploaded_file_url': uploaded_file_url, 'localization_issues': localization_issues})

    return render(request, 'analyze.html')

def extract_images_from_apk(apk_path):

    # Extract the images from the extracted source files
    res_dir = os.path.join(apk_path, 'res')
    drawables_dir = os.path.join(res_dir, 'drawable')
    images = []
    for filename in os.listdir(drawables_dir):
        file_path = os.path.join(drawables_dir, filename)
        try:
            text = extract_text_from_image(file_path)
            minioClient.fput_object('my-bucket', 'images/' + filename, file_path)
        except ResponseError as err:
            print(err)

    return images, text

def extract_text_from_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Extract the text from the image using tesseract
    text = pytesseract.image_to_string(image)

    return text

def transcribe_audio(request):
    # Load the audio file using pydub
    audio_file = AudioSegment.from_file("path_to_audio_file", format="format_of_audio_file")

    # Convert the audio file to raw audio data
    raw_audio_data = audio_file.raw_data

    # Pass the raw audio data to the SpeechRecognition library
    r = sr.Recognizer()
    audio = sr.AudioData(raw_audio_data)

    # Use the recognize_google() method to transcribe the audio file
    text = r.recognize_google(audio)
    # transcribe audio code
    transcribed_text = "transcribed text from audio file"

    # save transcribed text to database
    TranscribedText.objects.create(text=transcribed_text)

    return HttpResponse("Audio transcribed and text saved to database")