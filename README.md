## Link Aplikasi Heroku : https://hikam-tugas2-django.herokuapp.com/katalog/

# Buatlah bagan yang berisi *request client* ke web aplikasi berbasis *Django* beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan `berkas html`;

![Bagan](https://user-images.githubusercontent.com/96283916/190233504-2314aa6d-0b63-4796-ae97-b02ce86f8819.png)

Berikut merupakan penjelasan mengenai `urls.py`, `views.py`, `models.py`, dan `berkas html`. Pertama `urls.py` merupakan sebuah file yang berfungsi melakukan *routing* untuk permintaan yang masuk dari user. Lalu untuk `views.py` merupakan sebuah file yang berfungsi menjadi inti logika aplikasi dari jalannya proses permintaan yang masuk. Setelah itu `models.py` merupakan sebuah objek yang abstrak dari *database* dan juga konfigurasinya. Terakhir yaitu `berkas html` merupakan sebuah program yang menjadi alat untuk menampilkan atau memvisualisasikan apa aplikasi lakukan ke *user*. 

Kemudian alur dari bagan yang telah saya buat adalah sebagai berikut. Ketika ada permintaan yang masuk dari user, maka akan diterima terlebih dahulu oleh *URLconf* atau `urls.py`. Setelah itu, maka *URLconf* atau `urls.py` ini akan menyerahkan atau meneruskan permintaan dari *user* ini ke *Views* atau `views.py` untuk di proses dan didefinisikan. Ketika permintaan dari *user* tersebut memerlukan sebuah data atau *database*, maka *Views* akan menyerahkan input tersebut terlebih dahulu ke dalam *Model* atau `models.py`. `views.py` akan memanggil *query* ke *models* lalu melakukan pertukaran data di *database*, dan setelah itu akan dikembalikan kembali hasil *query*nya ke `views.py`. Setelah itu maka `views.py` akan mengembalikan kembali atau melanjutkan proses menyerahkan *input* dan memetakannya ke dalam *template* yang dalam hal ini merupakan `berkas html`. Lalu akhirnya, data dari `berkas html` yang sudah di visualisasikan tersebut akan dikembalikan lagi ke *user* sebagai *output* atau respon aplikasi. 

# Jelaskan kenapa menggunakan *virtual environment*? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*?

Dalam pembuatan sebuah web berbasis Django, *virtual environment* berfungsi sebagai sebuah fitur yang akan memisahkan antara pengaturan, *file*, *package*, dan *dependencies* yang sudah diinstall untuk setiap projek Django, sehingga ketika kita ingin membuat sebuah aplikasi lebih dari satu, maka *file-file* maupun *package* dan sebagainya yang ada akan semakin rapih dan baik karena semua *file* dari aplikasi yang berbeda tersebut tidak akan terhubung atau mempengaruhi antar satu sama lain. Selain itu, kita tetap dapat membuat sebuah aplikasi web berbasis Django tanpa menggunakan *virutal environment* ini. Dapat dilakukan dengan meng-*install* sebuah *libraries* secara global. Namun alangkah baiknya memang untuk mempertimbangkan menggunakan *virtual environment* atau *env* agar *file-file* yang ada tertata rapih. 

# Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

1. Melakukan *cloning* dari repositori github yang diambil dari *template* yang sudah disediakan kedalam file lokal dengan menggunakan perintah `git clone <URL_REPOSITORI>`.
2. Masuk ke dalam file repositori lokal yang di *clone* tersebut lalu menjalankan *command prompt* dari file tersebut. Setelah itu kita perlu membuat *virtual environment* dengan perintah `python -m venv env` lalu mengaktifkannya dengan perintah yang sesuai untuk *windows* yaitu `env\Scripts\activate.bat` 
3. Menginstall *dependencies* untuk menjalankan projek Django tersebut dengan melakukan perintah `pip install -r requirements.txt`
4. Mengecek projek Django yang telah dibuat tadi dengan perintah `python manage.py runserver lalu membuka http://localhost:8000`
5. Melakukan persiapan migrasi terlebih dahulu dengan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi dari skema model ke dalam *database* Django lokal.
6. Menerapkan skema model tersebut ke *database* Django lokal dengan menggunakan atau menjalankan perintah `manage.py migrate`
7. Memasukkan data yang ada dari *user* ke dalam *database* Django lokal tersebut dengan menggunakan perintah `python manage.py loaddata initial_catalog_data.json`
8. Membuat fungsi `show_katalog` di file `views.py` seperti berikut: 
```
     def show_katalog(request):
     return render(request, "katalog.html")
``` 
9. Mengimport kode `urls.py` ke folder katalog seperti berikut:
```
     from django.urls import path
     from katalog.views import show_katalog

     app_name = 'katalog'

     urlpatterns = [
        path('', show_katalog, name='show_katalog'),
     ]
 ```    
10. Pada `katalog.html`, kita perlu menambahkan kode-kode seperti berikut yang sesuai dengan yang ada pada `models.py`
 ```
    {% for barang in list_barang %}

    <tr>

       <th>{{barang.item_name}}</th>

       <th>{{barang.item_price}}</th>

       <th>{{barang.item_stock}}</th>

       <th>{{barang.description}}</th>

       <th>{{barang.rating}}</th>

       <th>{{barang.item_url}}</th>

    </tr>
   ``` 
11. Menambah aplikasi katalog ke `urls.py` pada folder `project_django`, yaitu dengan cara memodifikasi variabel `urlpatterns` dengan menambah kode berikut:
 ```
      path('katalog', include('katalog.urls')),
 ```  
12. meng-*import* *models* ke dalam `views.py` dengan cara sebagai berikut:
```
      from katalog.models import CatalogItem
```      
13. Memodifikasi fungsi `show_katalog` dengan menambahkan kode berikut:
```
      data_barang_katalog = CatalogItem.objects.all()
      context = {
         'list_barang': data_barang_katalog,
         'nama': 'Hikam Fajduani'
      }
```      
 14. Setelah itu, *return* pada fungsi `show_katalog` juga di modifikasi dengan menambahkan *context* seperti berikut:
``` 
      return render(request, "katalog.html", context)
```     
 15. Setelah semuanya selesai dilakukan di repositori lokal, maka setelah itu kita melakukan *push* ke dalam repositori pribadi GitHub sebelumnya dengan cara `git add .` - `git commit -m "pesan"` - `git pull` - `git push`
 16. Untuk mengetes hasil yang telah dibuat sebelumnya, maka coba lakukan `python manage.py runserver` pada *cmd* lalu membuka *link* `http://localhost:8000/katalog/` di *browser*.
 17. Ketika hasil di *browser* sudah sesuai seperti yang diinginkan, maka langkah terakhir yaitu men*deploy* aplikasi menggunakan heroku agar dapat membagikan hasil kerja menjadi *public* dan dapat diakses oleh orang lain.
 18. Langkah pertama yaitu membuka heroku di *browser*, lalu setelah *login*, pada menu utama pada bagian *New*, lakukan *Create new app* untuk membuat file aplikasi heroku baru dan menamai aplikasi tersebut sesuai keinginan.
 19. Setelah itu, masuk ke *Account settings* untuk menyalin *API KEY* dari akun heroku kita.
 20. Kemudian, kembali ke repositori GitHub sebelumnya dan masuk ke bagian *settings* dan pada *Secret* pilih bagian *action*.
 21. Buat dua variable atau repository secret yaitu `HEROKU_API_KEY` dan `HEROKU_APP_NAME` yang berisi *API KEY* yang telah disalin sebelumnya dari heroku dan juga nama dari aplikasi kita yang sebelumnya telah dibuat di heroku.
 22. Setelah itu, tetap pada GitHub dan masuk ke bagian *Action* dan melakukan *Re-Run* atas *workflow* yang gagal. Setelah *workflow* berhasil di *Run** maka itu menandakan bahwa aplikasi sudah di *deploy*.
 23. Terakhir melakukan pengecekan dengan membuka link `https://<nama-aplikasi-heroku>.herokuapp.com`

 Maka, aplikasi yang telah dibuat sudah bisa diakses oleh publik melalui link yang sudah ada.
   
 Terima Kasih

```
 Salam hangat,
 
 Hikam
```
