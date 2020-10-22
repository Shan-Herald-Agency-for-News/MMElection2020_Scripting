import json
import requests
import os
import shutil

partyInfoFile = "shanRegionParties.json"


def flag_imageDownload():
    image_url = ""
    filename = ""
    filepath = ""

    with open(partyInfoFile) as jFile:
        data = json.load(jFile)

        for d in data['data']:
            attr = d['attributes']
            image_url = attr['flag_image']
            filename = filename.join(
                [attr['name_english'], "_", d['id'], ".jpg"])
            filepath = os.path.join("party/flag", filename)

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


def policy_download():
    file_url = ""
    filename = ""
    filepath = ""

    with open(partyInfoFile) as jFile:
        data = json.load(jFile)

        for d in data['data']:
            attr = d['attributes']
            file_url = attr['policy']
            filename = filename.join(
                [attr['name_english'], "_", d['id'], ".pdf"])
            filepath = os.path.join("party/policy", filename)

            r = requests.get(file_url, stream=True)

            if r.status_code == 200:
                r.raw.decode_content = True

                with open(filepath, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)

                print("Image successfully Downloaded: ", filename)
                file_url = ""
                filename = ""
                filepath = ""
            else:
                print("Image Couldn\'t be retreived")


partyInfoFile = "shanRegionParties.json"


def seal_imageDownload():
    image_url = ""
    filename = ""
    filepath = ""

    with open(partyInfoFile) as jFile:
        data = json.load(jFile)

        for d in data['data']:
            attr = d['attributes']
            image_url = attr['seal_image']
            filename = filename.join(
                [attr['name_english'], "_", d['id'], ".jpg"])
            filepath = os.path.join("party/seal", filename)

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


# seal_imageDownload()
# flag_imageDownload()
# policy_download()
