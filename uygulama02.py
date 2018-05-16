Toplamsaniye= input("saniye girin:")
print ("yıl:",int(int(Toplamsaniye)/31104400))
x= int(Toplamsaniye)%31104400
print ("ay:",int(int(x)/2592000))
y = int(x)%2592000
print ("gün:",int(int(y)/86400))
z = int(y)%86400
print ("saat:",int(int(z)/3600))
v = int(z)%3600
print ("dakika:",int(int(v)/60))
w = int(v)%60
print ("saniye:",w)