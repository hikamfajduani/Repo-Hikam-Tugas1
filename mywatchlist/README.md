### Link menuju aplikasi heroku : https://hikam-tugas2-django.herokuapp.com/mywatchlist/html/

## Jelaskan perbedaan antara JSON, XML, dan HTML!
- `JSON` atau biasa disebut dengan `JavaScript Object Notation` merupakan sebuah format yang *syntactically* identik dengan sebuah kode untuk membuat object `JavaScript`. Oleh karena itu, karena memiliki similiaritas dengan `JavaScript` maka ketika terdapat sebuah aplikasi yang di buatkan format `JSON` -nya, maka dapat dengan mudah di konversi menjadi object `JavaScript` asli dari data-datanya.*Syntax* dari `JSON` itu sendiri merupakan penurunan dari *syntax* dari notasi objek `JavaScript`, namun dalam hal ini, `JSON` hanya berupa *text*. Kode untuk membaca data `JSON` oun dapat ditulis dalam bahasa pemrograman apapun. 
- `XML` atau biasa disebut dengan `Extensible Markup Language` merupakan sebuah dokumen yang biasa digunakan untuk menyederhanakan sebuah pertukaran maupun penyimpanan sebuah data. Dokumen `XML` ini juga perlu memiliki *root element*. Dalam *syntax*-nya sendiri, XML tidak memotong *whitespace* dan hal ini berbeda dengan *syntax* `HTML` dimana dia memotong beberapa *whitespace* menjadi satu *whitespace*
- `HTML` atau biasa disebut dengan `Hyper Text Transfer Protocol Requests & Responses` merupakan sebuah bahasa *markup* standar untuk sebuah dokumen yang biasa digunakan atau dirancang untuk ditampilkan nanti di browser. *Markup Language* itu sendiri adalah sebuah sistem untuk menandai sebuah dokumen yang menunjukkan struktur logisnya, seperti sebuah paragraf. dan juga memberikan sebuah instruksi untuk tata letaknya pada halaman, khususnya untuk transmisi dan tampilan elektronik.

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
*Data delivery* diperlukan untuk pengimplementasian sebuah *platform* dimana kita perlu mengirimkan sebuah data dari satu `stack` ke `stack` lainnya. Data yang di transfer ini, bentuknya dapat beragam, contohnya adalah format data yang umum digunakan, atau juga digunakan pada implementasi tugas 3 kali ini yaitu `HTML`, `XML`, dan `JSON`. 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Membuat `django-app` baru dari repository tugas sebelumnya dengan nama `mywatchlist` dengan perintah python `manage.py startapp wishlist`.
- Mendaftarkan `django-app` baru tersebut ke dalam variabel `INSTALLED_APPS` yang berapa di folder `project_django` di file `settings.py` seperti berikut.
```
INSTALLED_APPS = [
    ...,
    'wishlist',
]
```
- Memodifikasi `models.py` yang berada di folder `mywatchlist` seperi berikut.
```
class WatchlistFilm(models.Model):
    film_watched = models.BooleanField(max_length=50)
    film_title = models.TextField()
    film_rating = models.IntegerField()
    film_release = models.TextField()
    film_review = models.TextField()
 ```
 - Melakukan persiapan migrasi skema model ke dalam *database* Django lokal dengan perintah `python manage.py makemigrations`
 - Menerapkan skema model ke dalam *database* Django lokal dengan perintah `python manage.py migrate`
 - Membuat folder baru dengan nama `fixtures` di folder aplikasi `mywatchlist` lalu membuat sebuah berkas bernama `initial_watchlist_data.json`, lalu isi dari file tersebut adalah data film-film yang kita buat seperti berikut.
 ```
 [
    {
        "model":"mywatchlist.watchlistfilm",
        "pk":1,
        "fields":{
            "film_watched": true,
            "film_title":"Kimi no Nawa",
            "film_rating": 5,
            "film_release": "7 Desember 2016",
            "film_review": "endingnya sangat menggantung"
        }
},
{
        "model":"mywatchlist.watchlistfilm",
        "pk":2,
        "fields":{
            "film_watched": false,
            "film_title":"Fifty Shades of Grey",
            "film_rating": 4,
            "film_release": "13 Februari 2015",
            "film_review": "awas matanya ternodai"
        }
    },
    {
        "model":"mywatchlist.watchlistfilm",
        "pk":3,
        "fields":{
            "film_watched": true,
            "film_title":"Scout Guide to the Zombie Apocalypse",
            "film_rating": 5,
            "film_release": "30 Oktober 2015",
            "film_review": "Film zombie tapi komedi"
        }
    },
    {
        "model":"mywatchlist.watchlistfilm",
        "pk":4,
        "fields":{
            "film_watched": true,
            "film_title":"High and Low",
            "film_rating": 4,
            "film_release": "22 Oktober 2015",
            "film_review": "Membuat jiwa tawuran meronta-ronta"
        }
    },
    {
        "model":"mywatchlist.watchlistfilm",
        "pk":5,
        "fields":{
            "film_watched": true,
            "film_title":"Money Heist",
            "film_rating": 5,
            "film_release": "2 Mei 2017",
            "film_review": "Mengasah otak, professor pinter banget"
        }
    },
    {
        "model":"mywatchlist.watchlistfilm",
        "pk":6,
        "fields":{
            "film_watched": false,
            "film_title":"Mencuri Raden Saleh",
            "film_rating": 5,
            "film_release": "25 Agustus 2022",
            "film_review": "Cast nya bintang besar semua"
        }
    },
    {
        "model":"mywatchlist.watchlistfilm",
        "pk":7,
        "fields":{
            "film_watched": false,
            "film_title":"Peaky Blinders",
            "film_rating": 4,
            "film_release": "12 September 2013",
            "film_review": "dingin banget cuyy"
        }
    },
    {
        "model":"mywatchlist.watchlistfilm",
        "pk":8,
        "fields":{
            "film_watched": true,
            "film_title":"Ruroni Kenshin",
            "film_rating": 4,
            "film_release": "25 Agutus 2012",
            "film_review": "Adegan action samurainya keren"
        }
    },
    {
        "model":"mywatchlist.watchlistfilm",
        "pk":9,
        "fields":{
            "film_watched": true,
            "film_title":"The Conjuring",
            "film_rating": 5,
            "film_release": "26 Juli 2013",
            "film_review": "Film horror pertama yang saya tonton, vibesnya menyeramkan"
        }
    },
    {
        "model":"mywatchlist.watchlistfilm",
        "pk":10,
        "fields":{
            "film_watched": true,
            "film_title":"Saw",
            "film_rating": 4,
            "film_release": "29 Oktober 2004",
            "film_review": "Tidak disarankan kalo phobia darah, filmnya sangat sadis"
        }
    }
        
]
 ```
 - Memasukkan data ke dalam database Django lokal dengan perintah `python manage.py loaddata initial_watchlist_data.json`
 - Kita sudah bisa mulai untuk melakukan implementasi views dasar, dimulai dengan membuat fungsi yang menerima parameter request dan me-*return* `render(request, "watchlist.html")`. Selain itu fungsi ini akan berfungsi untuk memanggil fungsi *query* ke model database dan menyimpan hasil *query* ke dalam sebuah variable. Berikut merupakan fungsinya.
 ```
 def show_watchlist(request):
    data_watchlist = WatchlistFilm.objects.all()
    context = {
    'watchlist_film': data_watchlist,
    'nama': 'Hikam Fajduani'
    }
    return render(request, "watchlist.html", context)
 ```
 - Setelah itu, kita perlu membuat folder dengan nama `templates` yang dimana folder tersebut akan menyimpan berkas `html` yang telah di inisiasi di *step* sebelumnya sebagai return. Maka dari itu, kita akan membuat folder `watchlist.html` seperti berikut.
 ```
 {% extends 'base.html' %}

 {% block content %}

  <h1>Assignment 3 PBP/PBD</h1>

  <h5>Name: </h5>
  <p>Hikam Fajduani</p>

  <h5>Student ID: </h5>
  <p>2106634250</p>

  <table>
    <tr>
      <th>Watched</th>
      <th>Title</th>
      <th>Rating</th>
      <th>Release Date</th>
      <th>Review</th>
    </tr>
    {% comment %} Add the data below this line {% endcomment %}
    {% for watchlist in watchlist_film %}
      <tr>
          <th>{{watchlist.film_watched}}</th>
          <th>{{watchlist.film_title}}</th>
          <th>{{watchlist.film_rating}}</th>
          <th>{{watchlist.film_release}}</th>
          <th>{{watchlist.film_review}}</th>
      </tr>
    {% endfor %}
  </table>

 {% endblock content %}
```
- Melakukan routing terhadap fungsi `views` sehingga nantinya halaman `HTML` dapat ditampilkan di browser.
- Menghubungkan models dengan views dan template
- Melakukan data delivery, menggunakan data data yang umum seperti `HTML`, `XML`, dan `JSON`
- Mengembalikan data dalam bentuk `XML` dengan membuat fungsi . Isi dari fungsinya adalah.
 ```
def show_xml(request):
    data = WatchlistFilm.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
- Mengembalikan data dalam bentuk `JSON` dengan membuat fungsi .Isi dari fungsinya adalah.
```
def show_json(request):
    data = WatchlistFilm.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
 ```
 - Melakukan deployment ke `heroku` dengan melakukan *push* ke repository tugas sebelumnya.
 
 # Mengecek Postman
 
 ## HTML
 ![image](https://user-images.githubusercontent.com/96283916/191568593-9c00028f-37cc-4158-87e7-21d0a6cb9f6b.png)

## XML
![image](https://user-images.githubusercontent.com/96283916/191568705-90c3fcb2-aca5-4f97-82c3-7c74b9afa417.png)

## JSON
![image](https://user-images.githubusercontent.com/96283916/191568821-561c54a9-4fde-4ad4-a5c1-5efb745565f1.png)

 Terima kasih atas perhatiannya.
 
 Salam hangat,
 
 Hikam Fajduani
