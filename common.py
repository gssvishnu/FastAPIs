import json 
import os

def ReadJSON(FullFilePath):
    if os.path.exists (FullFilePath):
        json_data = open (FullFilePath).read()
        return json.loads(json_data)
    return {}
    
def WriteJSON (data, FullFilePath):
    with open(FullFilePath, 'w') as fp:
        json.dump(data, fp, sort_keys=True, indent=2)