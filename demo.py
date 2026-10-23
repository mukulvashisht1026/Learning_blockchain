"""Explicit offline demonstration; run from this repository root."""
import json

import hashlib
blocks = []
previous = '0' * 64
for height, value in enumerate(['genesis', 'Alice pays Bob 5', 'Bob pays Carol 2']):
    digest = hashlib.sha256(f'{height}:{previous}:{value}'.encode()).hexdigest()
    blocks.append({'height': height, 'previous_hash': previous, 'data': value, 'hash': digest})
    previous = digest
assert blocks[1]['previous_hash'] == blocks[0]['hash']
result = {'mode': 'educational local hash chain; no consensus or currency', 'blocks': blocks}

print(json.dumps(result, indent=2, sort_keys=True))
