import argparse
import json
import tempfile
import os
from pathlib import Path

def Parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", type = str)
    parser.add_argument("--value", type = str)
    return parser.parse_args()

def ReadFromFile(storage_path) -> dict:
    if not os.path.isfile(Path(storage_path)):
        return {}
    with open(storage_path, 'r') as f:
        line = f.read()
        if(len(line) > 0):
            return json.loads(line)
        
def WriteToFile(my_dict, storage_path, key, value):
    with open(storage_path, 'w+') as f:            
        my_dict.setdefault(key, [])
        my_dict[key].append(value)
        f.write(json.dumps(my_dict))  
         
def PutToFile(storagepath, key, value):
    my_dict = ReadFromFile(storagepath)
    WriteToFile(my_dict, storagepath, key, value)
            
def GetData(storagepath, key):
    my_dict = ReadFromFile(storagepath)
    return my_dict.get(key, [])
    
def main():
    args = Parse()
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    
    if (args.key and args.value):
        PutToFile(storage_path, args.key, args.value)
    elif args.key and not args.value :
        print(*GetData(storage_path, args.key), sep = ', ')
        
main()
