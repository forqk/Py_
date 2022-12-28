import argparse
import json
import tempfile
import os
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("--key", type = str)
parser.add_argument("--value", type = str)

args = parser.parse_args()

my_dict = dict()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if os.path.isfile(Path(storage_path)):
    with open(storage_path, 'r') as f: 
        my_dict = json.loads(f.read())
            

with open(storage_path, 'w') as f:    
    if args.key and args.value:
        my_dict.setdefault(args.key, [])
        my_dict[args.key].append(args.value)
        f.write(json.dumps(my_dict))  
             
    if args.key and not args.value: # считал и ничего не записал обратно, после этой строчки очищается файл.
        print("--value empty")
        if args.key not in my_dict:
            print(None)
            
