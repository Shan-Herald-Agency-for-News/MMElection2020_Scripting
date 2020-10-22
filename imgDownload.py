import json
import requests
import os
import shutil


def partyCandidates_imgDownloads():
    image_url = ""
    filename = ""
    filepath = ""

    with open('shanRegionCandidates.json') as jFile:
        data = json.load(jFile)

        for d in data['data']:
            attr = d['attributes']
            image_url = attr['image']
            filename = filename.join([attr['name'], "_", d['id'], ".jpg"])
            filepath = os.path.join("candidatesImg", filename)

            r = requests.get(image_url, stream=True)

            if r.status_code == 200:
                r.raw.decode_content = True

                with open(filepath, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)

                print("Image successfully Downloaded: ", filename)
                image_url = ""
                filename = ""
                filepath = ""
            else:
                print("Image Couldn\'t be retreived")


def shanStateCandidates_imgDownloads():
    image_url = ""
    filename = ""
    filepath = ""

    with open('shan_state_regionCandidates.json') as jFile:
        data = json.load(jFile)

        for d in data['data']:
            attr = d['attributes']
            image_url = attr['image']
            filename = filename.join([attr['name'], "_", d['id'], ".jpg"])
            filepath = os.path.join(
                "candidatesImg/shanStateRegionCandidates", filename)

            r = requests.get(image_url, stream=True)

            if r.status_code == 200:
                r.raw.decode_content = True

                with open(filepath, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)

                print("Image successfully Downloaded: ", filename)
            else:
                print("Image Couldn\'t be retreived", filename)

            image_url = ""
            filename = ""
            filepath = ""


shanStateCandidates_imgDownloads()
