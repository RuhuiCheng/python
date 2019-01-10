#args
import sys
for item in sys.argv:
    print(item)
#env  
import os
print(os.environ.get('mgdb_url'))
