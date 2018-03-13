erkekismi= input("Bir erkek ismi giriniz:")
kadınismi= input("Bir kadın ismi giriniz:")
satır= int(input("satır sayısı giriniz...Maksimum 1o satır yazdırılabilir.."))



sarkı = ["Ben senin en çok gülüşünü sevdim"," " + kadınismi+ " " ,"Sevindiren içimde umut çiçekleri açtıran","Unutturur bana birden acıları, güçlükleri","Dünyam aydınlanır sen güldüğün zaman" ," " + erkekismi+ " ", "Ben senin en çok sevgi dolu yüreğini sevdim"," " + kadınismi+ " ", "Ben senin en çok bana yansımanı sevdim", " " + erkekismi+ " ", "Bende yeniden var olmanı, benimle bütünleşmeni","Mertliğini, yalansızlığını, dupduruluğunu sevdim"," " + erkekismi+" ", "Ben seni sevdim"," "+ erkekismi+" ","ben seni sevdim"]

for olusturulacak_sarkı in sarkı[:satır]:
    print(olusturulacak_sarkı)

if satır  > 10:
    print("Satır sayısını fazla girdiniz. En fazla 10 satır giriniz... ")

