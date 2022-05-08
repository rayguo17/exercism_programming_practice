

def dict_modify(dict,key):
    dict["kiki"]=1
    dict[key].append("haha")
    

match = {}
if not "haha" in match:
    match["haha"]=[]
print(match["haha"])
dict_modify(match,"haha")
print(match)

line = "hahahahahha\n"
line = line[0:-1]
print(line)
a="""haha
klklk"""
print(a)