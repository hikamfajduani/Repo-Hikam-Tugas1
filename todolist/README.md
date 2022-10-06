### Link Menuju Aplikasi Heroku : https://hikam-tugas2-django.herokuapp.com/todolist/

### Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
`{% csrf_token %}` merupakan sebuah CSRF atau biasa disebut dengan *Cross Site Request Forgery* yang dimana merupakan sebuah *protection* bawaan dari *Django* yang menjaga website dari serangan dari luar atau *Hacker*. CSRF ini memiliki token yang relatif unik, hal ini dikarenakan tiap user dari website tersebut yang login memiliki token sendiri dimana setiap token pada setiap user berbeda-beda. Hal ini agar memastikan bahwa user yang login memanglah pemilik dari akun tersebut. 
  
### Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }})`? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Dalam pembuatan `<form>` penggunaan generator seperti `{{ form.as_table }})` sebenarnya tidak diharuskan atau kita tetap dapat membuat sebuah `<form>` tanpa menggunakan generator tersebut.
Selain itu, untuk pembuatan *form* itu sendiri yang dibuat secara manual dapat dilakukan dengan membuat sebuah tag yaitu <input> yang memiliki *attribute* name dan type yang sama dan sesuai dengan *form* pada server Django.

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Proses dari alur data submisi oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML dimulai ketika user menekan tombol `Create` dari `Form`. Ketika proses ini dilakukan, akan memicu permintaan HTTP ke server. Lalu setelah itu proses atau tindakan yang terjadi pada langkah sebelumnya akan memetakan permintaan ke URL yang ada pada `urls.py`. Hal ini dilakukan untuk meneruskan permintaan ke fungsi tertentu yang telah ada dan ditentukan di `views.py`. Ketika tindakan sebelumnya sama dengan URL nya, namun dengan metode HTTP yang berbeda, maka akan atau dapat mengontrol aliran berdasarkan metode permintaan tersebut. Selain itu, untuk meng-*handle* terkait yang di definisikan pada `views.py`, data dari permintaan akan diivalidasi menggunakan formulir Django. Ketika terdapat *case* dimana data tidak valid, maka server akan mengirimkan *message* yang berisi sebuah kesalahan. Disisi lain, ketika data valid, maka permintaan akan disimpan ke dalam database. Lalu, akan ditampilkan ke laman `HTML` ketika server merespons dengan `HTTP redirect` ke url yang bersangkutan.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Langkah pertama yang dilakukan adalah mengaktifkan virtual environtment di terminal.
- Selanjutnya, membuat sebuah aplikasi baru dengan menggunakan `python manage.py startapp wishlist`.
- Melakukan routing aplikasi yang telah dibuat sebelumnya ke `urls.py` yang ada pada `project_django`
- Menambahkan komponen pada Models.py di aplikasi django yang telah dibuat sebelumnya dengan isi sebagai berikut.
    ```
    class IsiTodolist(models.Model):
        user = models.ForeignKey(to=User, on_delete=models.CASCADE)
        todo_date = models.TextField()
        todo_title = models.TextField()
        todo_description = models.TextField()
        is_finished = models.BooleanField(default=False)
    ```
- Melakukan migrasi dengan menggunakan `python manage.py makemigrations` dan `python manage.py migrate`
- Membuat fungsi-fungsi seperti `show_todolist`, `register`, `login_user`, `logout_user`, `create`, lalu untuk fungsi seperti `create` dan `show_todolist` diberikan `@login_required(login_url='/todolist/login/')` agar untuk mengakses lamannya diperlukan persyaratan login.
- Membuat file `HTML` yaitu `login.html`, `register.html`, `todolist.html`, `create.html`
- Melakukan routing pada `urls.py` yang ada pada `todolist`
- Melakukan `push` dan `deploy` ke `Github` dan `Heroku`
- Membuat dua akun pengguna dan tiga *dummy data*

![image](https://user-images.githubusercontent.com/96283916/192886953-14e1e576-2d65-4c63-bdb6-5a8dfdc3dc43.png)
![image](https://user-images.githubusercontent.com/96283916/192887873-3cf79022-f08a-4bc6-810b-6daa6de43f43.png)

# Tugas 5
### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Perbedaan dari Inline, Internal dan External CSS dapat ditinjau dari beberapa aspek yaitu lokasi dan scope atau jangkauannya. Untuk lokasi Inline sendiri berada di dalam elemen dengar atrr `<style>`, untuk Internal yaitu berapa di dalam `HTML` dengan tag `style`, sedangkan untuk External sendiri yaitu berada di dalam bagian `css` yang di-import dengan tag `<tag>`. Selain itu untuk aspek scope atau jangkauannya yaitu untuk Inline memiliki jangkauan hanya untuk elemen-elemen yang digunakannya, untuk Internal yaitu untuk satu halaman saja sedangkan untuk External adalah setiap halaman yang melakukan import.

Adapun kelebihan dan kekurangan dari masing-masing style adalah untuk Inline sendiri kelebihannya adalah dapat digunakan untuk melimit ke suatu elemen tertentu saja, tetapi, tagnya akan terlihat cukup tidak beraturan. Hal ini dikarenakan style dicampur dengan HTML. Sedankan untuk Internal CSS memiliki kelebihan dimana dapat dilimit juga untuk suatu halaman tertentu, tetapi akan tidak efisien ketika terdapat perulangan untuk halaman lain. Selain itu untuk External CSS kelebihannya yaitu dapat digunakan untuk berbagi style ke beberapa halaman sekaligus, akan tetapi, cukup menyulitkan untuk melakukan debugnya. 

### Jelaskan tag HTML5 yang kamu ketahui.
- `<header>` tag ini seperti dengan namanya yaitu header adalah suatu tag yang biasa digunakan sebagai header suatu website. Header ini biasanya terletak di bagian paling atas html.
- `<nav>` tag ini dapat disebut sebagai Navigation Bar dimana digunakan sebagai mevigasi menu utama sebuah halaman web. Biasanya digunakan untuk menggabungkan beberapa link dari daftar isi ataupun link menuju halaman sebelum ataupun sesudah. Selain itu, navbar biasanya terletak di bagian paling atas.
- `<aside>` merupakan sebuah elemen tag yang dimana adalah elemen tambahan. Aside ini merupakan elemen yang ditempatkan di sisi lain halaman HTML. Biasanya terletak di sisi kanan maupun sisi kiri bahkan sisi bawah dari konten utama pada halaman HTML.
- `<section>` merupakan sebuah tag yang merepresentasikan sebuah bagian dari dokumen maupun aplikasi. Element ini juga digunakan untuk mengelompokkan konten/dokumen menjadi beberapa bagian berdasarkan tema atau pokok pikiran masing-masing.
- `<article>` merupakan sebuah tag yang digunakan untuk memberi mark up sebuah konten independen, yaitu elemen yang dapat berdiri sendiri sebagai sebuah konten utuh yang tidak terikat dengan konten lain.
- `<footer>` merupakan sebuah elemen yang merepresentasikan catatan kaki atau catatan pada bagian akhir halaman atau bagian bawah halaman.

### Jelaskan tipe-tipe CSS selector yang kamu ketahui.
- Selector class, contohnya seperti `.class` adalah selektor yang memilih elemen berdasarkan nama class yang diberikan.
- Selector ID, contohnya seperti `#header` adalah selektor yang hampir mirip dengan selector class namun ini bersifat cukup unik yaitu hanya dapat digunakan oleh satu elemen saja.
- Selector tag, contohnya seperti `<p>` adalah selektor yang akan memilih elemen berdasarkan nama tagnya.
- Universal selector, contohnya yaitu `*` adalah selektor yang dapat digunakan ke semua elemen pada jangkauan scope tertentu

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Menggunakan repositori tugas sebelumnya.
- Membuat beberapa file atau class CSS yang akan digunakan untuk memodifikasi html.file nya.
- Membuat juga sebuah card yang nantinya akan digunakan untuk membungkus login form, register form, create form, hingga task task yang di create.
- Setelah membuat class, lalu memodifikasi file html dengan memasukkan fungsi-fungsi tersebut ke file html masing-masing lalu di sesuaikan, dimulai dari login.html, register.html, create.html, dan juga todolist.html
- Mengkreasikan warna, posisi dan elemen di website semenarik dan sekreatif mungkin.
- Menambahkan hover atau animasi yang responsif ke dalam beberapa elemen untuk mendapatkan bonus.
- Mendeploy aplikasi local ke heroku agar dapat diakses oleh orang lain.
