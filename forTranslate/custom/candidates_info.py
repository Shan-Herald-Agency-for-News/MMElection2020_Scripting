# -*- coding: UTF-8 -*-
import json
import os

def saveFilterToText(fileName, fileDir, value):

	dirPath = "candidateInfo/"

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

def _condidates_id_filter():
	with open('shan_state_region_Candidates.json') as jFile:

		data = json.load(jFile)
		candidates_id = []

		for d in data['data']:
			candidates_id.append(d['id'])

		if not candidates_id:
			print("candidates_id is Empty")
		else:
			saveFilterToText("candidates_id", "custom", candidates_id)

_condidates_id_filter()

def _condidates_name_filter():
	with open('shan_state_region_Candidates.json') as jFile:

		data = json.load(jFile)
		attr = []
		candidates_name = []

		for d in data['data']:
			attr = d['attributes']
			candidates_name.append(attr['name'])
			

		if not candidates_name:
			print("candidates_name is Empty")
		else:
			saveFilterToText("candidates_name", "custom", candidates_name)

_condidates_name_filter()

def _condidates_image_filter():
	with open('shan_state_region_Candidates.json') as jFile:

		data = json.load(jFile)
		attr = []
		candidates_image = []

		for d in data['data']:
			attr = d['attributes']
			candidates_image.append(attr['image'])
			

		if not candidates_image:
			print("Candidates Id is Empty")
		else:
			saveFilterToText("candidates_image", "custom", candidates_image)

_condidates_image_filter()

def _condidates_constituencyId_filter():
	with open('shan_state_region_Candidates.json') as jFile:

		data = json.load(jFile)
		attr = []
		candidates_constituencyId = []

		for d in data['data']:
			attr = d['attributes']['constituency']
			candidates_constituencyId.append(attr['id'])
			

		if not candidates_constituencyId:
			print("candidates_constituencyId is Empty")
		else:
			saveFilterToText("candidates_constituencyId", "custom", candidates_constituencyId)

_condidates_constituencyId_filter()

def _condidates_constituencyTownship_filter():
	with open('shan_state_region_Candidates.json') as jFile:

		data = json.load(jFile)
		constituency = []
		attr = []
		candidates_constituencyTownship = []

		for d in data['data']:
			constituency = d['attributes']['constituency']
			attr = constituency['attributes']
			candidates_constituencyTownship.append(attr['township'])
			

		if not candidates_constituencyTownship:
			print("candidates_constituencyTownship is Empty")
		else:
			saveFilterToText("candidates_constituencyTownship", "custom", candidates_constituencyTownship)

_condidates_constituencyTownship_filter()

def _condidates_constituencyHouse_filter():
	with open('shan_state_region_Candidates.json') as jFile:

		data = json.load(jFile)
		constituency = []
		attr = []
		candidates_constituencyHouse = []

		for d in data['data']:
			constituency = d['attributes']['constituency']
			attr = constituency['attributes']
			candidates_constituencyHouse.append(attr['house'])
			

		if not candidates_constituencyHouse:
			print("candidates_constituencyHouse is Empty")
		else:
			saveFilterToText("candidates_constituencyHouse", "custom", candidates_constituencyHouse)

_condidates_constituencyHouse_filter()

def _condidates_partyId_filter():
	with open('shan_state_region_Candidates.json') as jFile:

		data = json.load(jFile)
		attr = []
		candidates_partyId = []

		for d in data['data']:
			attr = d['attributes']['party']

			if not attr:
				candidates_partyId.append(None)
			else:
				candidates_partyId.append(attr['id'])
				
			

		if not candidates_partyId:
			print("candidates_partyId is Empty")
		else:
			saveFilterToText("candidates_partyId", "custom", candidates_partyId)

_condidates_partyId_filter()

