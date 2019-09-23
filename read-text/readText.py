
f = open("file.txt","r")

lines = f.read().split("\n")

for x in lines:
  words = x.split("=")
  '''
  if len(words) >2 :
    print(x)
    '''
  print("\""+words[0]+"\":\""+words[1]+"\",")

f.close()