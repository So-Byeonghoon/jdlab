import sys

if not len(sys.argv)==4:
  print './sed FROM_WORD TO_WORD IN_FILE'
  sys.exit(1)

file = open(sys.argv[3], 'r')

while True:
  line = file.readline()
  if not line:
    break
  print line.replace(sys.argv[1], sys.argv[2])

file.close()
