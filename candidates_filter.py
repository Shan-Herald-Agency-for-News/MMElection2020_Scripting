# -*- coding: UTF-8 -*-
import json

shanRegionPartiesID = [38, 16, 2, 5, 73, 124, 27, 122, 112, 15, 56, 110, 32,
                       114, 66, 57, 81, 71, 7, 3, 12, 68, 69, 4, 128, 89, 60, 93, 116, 25, 125, 61]
filterData = []
count = 0


with open('candidates.json') as jFile:
    data = json.load(jFile)

    for d in data['data']:

        attr = d['attributes']
        party = attr['party']

        if party != None:
            partyID = int(party['id'])
            for i in shanRegionPartiesID:
                if partyID == i:
                    filterData.append(d)
                    count = count + 1

    with open('shanRegionCandidates.json', 'w') as write_file:
        json.dump({"data": filterData}, write_file)
    print('finished ...')
    print(count)
