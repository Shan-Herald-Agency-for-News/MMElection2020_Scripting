# -*- coding: UTF-8 -*-
import json
import os

shanRegionPartiesID = [38, 16, 2, 5, 73, 124, 27, 122, 112, 15, 56, 110, 32,
                       114, 66, 57, 81, 71, 7, 3, 12, 68, 69, 4, 128, 89, 60, 93, 116, 25, 125, 61]

candidates_attributes = []
parties_attributes = []
parties = []


def shanStateRegionCandidate():
    with open('shan_state_regionCandidates.json') as jFile:

        data = json.load(jFile)

        for d in data['data']:
            candidates_attributes.append(d['attributes'])


def shanStateRegionParty():
    with open('shanRegionParties.json') as jFile:
        data = json.load(jFile)

        for d in data['data']:
            parties_attributes.append(d['attributes'])
            parties.append(d)


def _candidates_attributes_filter(attr_name, filePath):

    # open and read json file
    shanStateRegionCandidate()

    attr_value = []
    filterDuplicate = []

    for d in candidates_attributes:
        attr_value.append(d[attr_name])

    [filterDuplicate.append(x) for x in attr_value if x not in filterDuplicate]

    if not filterDuplicate:
        print("Empty")
    else:
        saveFilterToText(attr_name, filePath, filterDuplicate)

def _candidates_name_filter(party, filePath):
    shanStateRegionCandidate()

    attr = []
    filter = []

    for d in candidates_attributes:
        for i in d['party']['attributes']:
            if i['abbreviation'] == party:
                attr.append(d['attributes']['name'])
    if not attr:
        print("Empty")
    else:
        saveFilterToText(party, filePath, attr)


def _parties_attributes_filter(attr_name, filePath):

    # open and read json file
    shanStateRegionParty()
    attr_value = []
    filterDuplicate = []

    for d in parties_attributes:
        attr_value.append(d[attr_name])

    [filterDuplicate.append(x) for x in attr_value if x not in filterDuplicate]

    if not filterDuplicate:
        print("Empty")
    else:
        saveFilterToText(attr_name, filePath, filterDuplicate)

def _parties_filter(attr_name, filePath):

    shanStateRegionParty()

    attr_value = []

    for d in parties:
        attr_value.append(d[attr_name])

    if not attr_value:
        print("Empty")
    else:
        saveFilterToText(attr_name, filePath, attr_value)


def _constituency_filter(attr_name, filePath):

    # open and read json file
    shanStateRegionCandidate()

    attr_value = []
    filterDuplicate = []

    for d in candidates_attributes:
        attr = d["constituency"]
        attr_value.append(attr["attributes"][attr_name])

    [filterDuplicate.append(x) for x in attr_value if x not in filterDuplicate]

    if not filterDuplicate:
        print("Empty")
    else:
        saveFilterToText("constituency_"+attr_name, filePath, filterDuplicate)


def saveFilterToText(fileName, fileDir, value):

    dirPath = "forTranslate/" + fileDir

    if not os.path.exists(dirPath):
        os.mkdir(dirPath)

    filePath = os.path.join(dirPath, fileName+".txt")
    f = open(filePath, "w")
    str1 = ''

    for ele in value:
        str1 += str(ele) + "\n"

    f.write(str1)
    f.close()
    print("Finished ...")


# _candidates_attributes_filter('education', 'candidates')
# _candidates_attributes_filter('ethnicity', 'candidates')
# _candidates_attributes_filter('gender', 'candidates')
# _candidates_attributes_filter('religion', 'candidates')
# _candidates_attributes_filter('work', 'candidates')
# _candidates_attributes_filter('representing_ethnicity', 'candidates')
# _constituency_filter("name", 'constituency')
# _constituency_filter("state_region", 'constituency')

# _parties_attributes_filter('member_count', 'parties')
# _parties_attributes_filter('leaders_and_chairmen', 'parties')
# _parties_attributes_filter('region', 'parties')
# _parties_attributes_filter('name_burmese', 'parties')
# _parties_attributes_filter('name_english', 'parties')
# _parties_attributes_filter('abbreviation', 'parties')
# _parties_attributes_filter('flag_image', 'parties')
_parties_filter('id', 'parties')
