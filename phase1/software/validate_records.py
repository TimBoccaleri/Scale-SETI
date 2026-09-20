#!/usr/bin/env python3
import argparse, json, pathlib, sys
try:
    import jsonschema
except Exception:
    raise SystemExit('Install jsonschema: python -m pip install jsonschema')

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--schema',required=True)
    p.add_argument('--record',required=True)
    a=p.parse_args()
    schema=json.loads(pathlib.Path(a.schema).read_text())
    record=json.loads(pathlib.Path(a.record).read_text())
    jsonschema.Draft202012Validator(schema).validate(record)
    print('VALID')
if __name__=='__main__': main()
