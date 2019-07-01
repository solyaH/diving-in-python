import argparse
import json
import os
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()
print(tempfile.gettempdir())
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
datastore=None
with open(storage_path, 'r') as f:
    try: 
         datastore = json.load(f)
    except ValueError: 
         datastore = {}
         
if args.val==None:
    print(', '.join(datastore[args.key]))
elif args.key!=None:
    with open(storage_path, 'w') as f:
        try: 
            datastore[args.key].append(args.val)
            datastore.update(datastore)
        except KeyError: 
            entry={}
            entry[args.key]=[]
            entry[args.key].append(args.val)
            datastore.update(entry)
    
        json.dump(datastore, f)
        print("Done")

