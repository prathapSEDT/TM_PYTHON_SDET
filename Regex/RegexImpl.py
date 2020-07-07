import re
data="my email id : firstname12.lastname345@abc.com"

pattern="[a-z\d]*\.[a-z\d]*\@[a-z]*\.in|[a-z\d]*\.[a-z\d]*\@[a-z]*\.com|[a-z\d]*\.[a-z\d]*\@[a-z]*\.net"

# pos1=re.search(pattern=pattern,string=data).start()
# pos2=re.search(pattern=pattern,string=data).end()
# print(data[pos1:pos2])

print(re.findall(pattern=pattern,string=data))