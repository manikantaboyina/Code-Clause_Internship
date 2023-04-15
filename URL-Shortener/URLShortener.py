import pyshorteners as s

Copied_Url=input("Please Paste Your URL HERE : ")
Shorten_Url = s.Shortener().tinyurl.short(Copied_Url)
print("Shorten URl: ",Shorten_Url)


 
