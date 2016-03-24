import os
import sys

for dirname, dirnames, filenames in os.walk(sys.argv[1]):
  for filename in filenames:
    if filename.endswith(sys.argv[2]):
      print(os.path.join(dirname, filename))
