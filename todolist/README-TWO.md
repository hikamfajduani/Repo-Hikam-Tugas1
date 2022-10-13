## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming merupakan proses jalan dan pengerjaan sebuah program yang sequential, yaitu berdasarkan antrian eksekusi program. Oleh karena itu pada dasarnya hampir semua bahasa pemrograman merupakan synchronous programming. Sedangkan asynchronous programming merupakan sebuah proses jalan dan pengerjaan sebuah program yang proses jalannya bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. 

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma *Event-driven programming* merupakan sebuah paradigma yang dimana entitas berinteraksi sedara tidak langsung, yaitu dengan pengiriman sebuah pesan melalui sebuah perantara. Contoh penerapannya yang digunakan pada tugas kali ini adalah pada penerapan metode `AJAX POST` yang mana *end point/todolist/add* merupakan perntara komunikasi antara `jquery` dengan fungsi yang terdapat pada `views.py`.

## Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan *asynchronus programming* pada `AJAX` di tugas kali ini adalah, sesuai dengan nama dari `AJAX` yaitu `Asynchronous JavaScript And XML` dimana kita bisa melakukan *asynchronus programming* dimana kita tidak perlu mereload suatu page untuk menambahkan todolist baru. Hal yang perlu dilakukan hanya memunculkan sebuah modal yang kali ini digunakan menggunakan `bootstrap` lalu menambahkan task pada modal tersebut. Karena itu, kita tidak perlu berpindah *page* dan hanya menambahkan di ajax tersebut. Lalu task akan langsung bertambah di halaman tersebut. Implementasi itulah yang merupakan sebuah *asynchronus programming* dimana terjadi lebih dari satu proses sekaligus.

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

