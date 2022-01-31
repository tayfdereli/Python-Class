# Python-Class

**[Hw1]** 

>- 50 soruluk, 4 yanlışın 1 doğruyu götürdüğü sınavda öğrencinin inputlarla girilen doğru yanlış sayısına göre aldığı puanı hesaplayan programı yazınız. 

>Ogrenci sınıfı diye bir sınıf tanımlanacak. Bu sınıfın içinde ogrenciAdı, ogrenciSoyadı, ogrenciSınıf’ı değişkenleri bulunacak. Bu sınıftan nesne oluşturulurken bu bilgiler parametre olarak verilecek.  

>Soru diye bir sınıfınız olacak. Bu sınıfın NetSayısı(...) ve Hesapla(...) diye iki fonksiyon olacak. 

> NetSayısı fonksiyonu doğru ve yanlış sayısını parametre olarak alıp öğrencinin kaç neti olduğunu bulur.

>  Hesapla fonksiyonu net sayısını parametre olarak alıp öğrencinin puanını hesaplayacak. Her net 2 puan. 

>  En sonunda öğrenci bilgileri ve puanı console gösterilecek.

**[HW2]**

>- Insan isimli bir sınıf tanımlayınız. Bütün constructor parametreleri default değerlere sahip olacak, default contructor (__init__) içinde belirlenecek. 

>  Bu değerler; ad,soyad,yas,ulke,sehir olacak.

>Ek olarak yetenekler isimli bir boş dizi init fonksiyonu içinde tanımlanacak.

>-kisi_bilgileri isimli fonksiyon ile init fonksiyonu içinde belirlenen kisi bilgileri return’le dönülecek.

>- yetenek_ekle isimli fonksiyon ile init fonksiyonu içinde belirlenen yetenekler dizisine yetenekler eklenecek

-Bu classtan belirtilen bilgileri içeren bir nesne tanımlayın.

>-Tanımlanan nesneye yetenek ekleyin. (Bisiklete binmek, Python vs.)

>kisi_bilgileri fonksiyonu ile bu bilgileri gösterin.

[Hw3]
>- WebPush isimli bir class tanımlayınız.   WebPush class’ı send_push  isimli bir fonksiyona sahip olsun ve bu fonksiyon çağırıldığı zaman ‘Push gönderildi!’ yazısı gösterilsin.

>Platform, optin, global_frequency_capping, start_date, end_date, language, push_type isimli özniteliklere sahip olsun. optin değeri boolean değer alsın. 

>TriggerPush, BulkPush, SegmentPush, PriceAlertPush, InstockPush isimli classlar tanımlayınız. 

>Bu class’lar WebPush classından miras alsın.Miras alan classlar ana classtan farklı olarak aşağıdaki değişkenlere sahip olsun:

![image](https://user-images.githubusercontent.com/93590132/151860333-15f24a71-9793-41f2-b254-208954285429.png)




>discountPrice(price_info, discount_rate) - Bu method üründe yapılan indirimi    hesaplayacak ve return ile geri döndürecek.

>stockUpdate() - Bu method stock bilgisini güncelleyip return ile geri döndürecek. Örneğin oluşturulan nesnenin stock bilgisi true ile false, false ise true yapacak. 

>Bütün push çeşitlerinden nesne oluşturup, methodlarını varsa kullanılmalı ve ana classta bulunan send_push methodu çağırılmalı.

