import re

toplevel = []
narrower = dict()
p = re.compile('^<http://wescml.org/def/avpcc/((\d\d)\d*)([\.]*)(\d*)>')
with open('ids.txt') as f:
    content = f.readlines()

    for i in content:
        i=i.strip()
        narrower[i] = [];


    for i in content:
       i=i.strip()
       m = p.match(i)
       #print i + " --> " + str(m.group(1,2,4) )
       if(m.group(1) == m.group(2)):
          toplevel.append(i)

       else:
          if(m.group(3)):
             arr = narrower['<http://wescml.org/def/avpcc/'+str(m.group(1))+'>']
             arr.append(i)
          else:
             arr = narrower['<http://wescml.org/def/avpcc/'+str(m.group(2))+'>']
             arr.append(i)


for key in narrower:
   if(len(narrower[key]) > 0):
      print key + " skos:narrower " + ','.join(narrower[key]) + "\n. \n"
