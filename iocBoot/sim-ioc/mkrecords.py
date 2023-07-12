#!/usr/bin/env python3

import argparse
import random
import json

parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int, dest='NUM', required=True, help='Number of records to generate')
args = parser.parse_args()

def digital_rand() -> str:
    return str(random.randint(1,2))

def analog_rand() -> str:
    return str(random.random() * 24)

templates = {
    'digital': {
        'SIMM': 'YES',
        'ONAM': 'ON',
        'ZNAM': 'OFF',
        'VAL': digital_rand
    },
    'analog': {
        'SIMM': 'YES',
        'EGU': 'volts',
        'EGUL': '0',
        'EGUF': '24',
        'VAL': analog_rand
    }
}

fp = open('records.db', 'w')
recs = []

for i in range(1, args.NUM):
    rec = random.choice(['bi', 'bo', 'ai', 'ao'])
    m = {}
    match rec:
        case 'bi':
            m = templates['digital'].copy()
        case 'bo':
            m = templates['digital'].copy()
        case 'ai':
            m = templates['analog'].copy()
        case 'ao':
            m = templates['analog'].copy()
    m['VAL'] = m['VAL']()

    fp.write(f'record({rec}, "rec:{i}"){{\n')
    for field in m.keys():
        fp.write(f'\tfield("{field}", "{m[field]}")\n')
    fp.write("}\n\n")
    recs.append(f'rec:{i}')

fp.close()

with open('records.json', 'w') as fp:
    json.dump(recs, fp)