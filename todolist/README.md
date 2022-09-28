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
    - Melakukan routin aplikasi yang telah dibuat sebelumnya ke `urls.py` yang ada pada `project_django`
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