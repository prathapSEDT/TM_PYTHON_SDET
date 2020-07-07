data="Mytransactionid70848672145875424isgeneratedsucessfully"
mytemp=""
for x in range(0,len(data)):
    if (str(data[x:x+1]).isalpha() and str(data[x+1:x+2]).isdigit()) or (str(data[x:x+1]).isdigit() and str(data[x+1:x+2]).isalpha()):
        mytemp=mytemp+str(data[x:x+1])+"@"
    else:
         mytemp=mytemp+str(data[x:x+1])
pos1=mytemp.find("@")+1
pos2=mytemp.rfind("@")

print(mytemp[pos1:pos2])