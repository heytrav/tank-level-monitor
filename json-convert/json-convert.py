import sys
import re
import json

for line in sys.stdin:
    x = re.compile(r'^(?P<timestamp>[^\s]+)\s+[^,]+,\d,(?P<tank>[^,]+),(?P<volume>[^,]+).*')
    m = x.search(line)
    data = {"timestamp": m.group('timestamp'), "tank": m.group('tank'), "volume": m.group('volume') }
    print(json.dumps(data))
