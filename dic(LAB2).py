cgpa={}
cgpa ["rafay"]=3.5
cgpa ["ali"]=2
cgpa ["khan"]=3.5

for k in cgpa.keys():
    if(cgpa[k]<2.5 ):
       print("no degree's",k)
    else:
         print("degree awaded",k)