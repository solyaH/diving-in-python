import argparse
import json
import os
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--val')
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
data_store = None
with open(storage_path, 'r') as f:
    try:
        data_store = json.load(f)
    except ValueError:
        data_store = {}

if __name__ == '__main__':
    if args.val is None:
        print(', '.join(data_store[args.key]))
    elif args.key is not None:
        with open(storage_path, 'w') as f:
            try:
                data_store[args.key].append(args.val)
                data_store.update(data_store)
            except KeyError:
                entry = {}
                entry[args.key] = []
                entry[args.key].append(args.val)
                data_store.update(entry)

            json.dump(data_store, f)
            print('Done')
