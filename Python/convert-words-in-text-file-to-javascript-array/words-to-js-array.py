words = []

# open JS file for writing
fileJs = open('words.js', 'w')

# read words file and transform all words into a JS array string
fileTxt = open('words.txt', 'r')
words = fileTxt.readlines()

fileJs.write("words = [\n")
count = 0
for w in words:
  count += 1
  fileJs.write('  "' + w.strip() + '", \n')

fileJs.write("];\n")

fileTxt.close()
fileJs.close()
