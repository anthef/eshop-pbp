# Ayo Belanja
E-commerce terbaik untuk segala kalangan umur

- [Profile] (#Profile)
- [Deployment] (#Deployment)
- [Pertanyaan dan Jawaban] (#Pertanyaan-dan-Jawaban)
- [Checklist Tugas] (#Checklist_Tugas)

## Profile

Nama    : Anthony Edbert Feriyanto
NPM     : 2306165654
Kelas   : PBP C

## Deployment

tautan aplikasi PWS : http://anthony-edbert-eshoppbp.pbp.cs.ui.ac.id

## Pertanyaan dan Jawaban

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    **_Jawab_**:
    1. Membuat direktori baru dengan nama 'eshop-pbp'

    2. Membuat suatu berkas bernama 'requirements.txt' dan menambahin beberapa dependencies, seperti:
    '''
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    '''
    Lalu menginput 'pip install -r requirements.txt'

    3.Setelah itu, saya membuat proyek dengan perintah 'django-admin startproject mental_health_tracker .'

    4. Menambahkan code 
    '''python
    ALLOWED_HOSTS = ["localhost", "127.0.0.1","anthony-edbert-eshoppbp.pbp.cs.ui.ac.id"]
    '''
    ke 'eshop-pbp/eshop-pbp/settings.py

    5. Membuat .gitignore

    6. Pada proyek 'eshop-pbp', melakukan pembuatan aplikasi bernama main dengan perintah:
    '''python
    python manage.py startapp main
    '''

    7. Melakukan routing agar proyek bisa menjalankan aplikasi main
    '''python
    from django.contrib import admin
    from django.urls import path,include
    from main import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
        path('',views.show_main,name='show_main'),
    ]
    '''

    8. Lalu, saya membuat model 'Product' untuk aplikasi main di 'models.py' yang memiliki atribut 'name','price', dan 'description'.
    '''python
    from django.db import models

    class ProductEntry(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
    '''

    9. Lalu, saya membuat fungsi 'show_main' pada 'views.py' untuk mengembalikan response dari atribut-atribut 'model Product' yang sudah dibuat.
    '''python
    from django.shortcuts import render
    from .models import ProductEntry  

    def show_main(request):
        products = ProductEntry.objects.all()

        seen = set()
        unique_products = []
        for product in products:
            if product.name not in seen:
                unique_products.append(product)
                seen.add(product.name)

        context = {
            'npm': '2306165654',
            'name': 'Anthony Edbert Feriyanto',
            'class_name': 'PBP C',  
            'products': unique_products  
        }

        return render(request, "main.html", context)
    '''

    10. Selanjutnya saya membuat routing untuk menghubungkan 'views.py' di 'main' pada 'urls.py'
    '''python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    '''

    11. Membuat 'add_products.py' untuk manajemen product yang akan ditampilkan lebih baik
    '''python
    from django.core.management.base import BaseCommand
    from main.models import ProductEntry

    class Command(BaseCommand):
        help = 'Add sample products to the database'

        def handle(self, *args, **kwargs):
            product1 = ProductEntry(name="Laptop", price=1200, description="A high-performance laptop.")
            product1.save()

            product2 = ProductEntry(name="Smartphone", price=800, description="A latest model smartphone.")
            product2.save()

            product3 = ProductEntry(name="Computer", price=1000, description="A latest model computer.")
            product3.save()

            self.stdout.write(self.style.SUCCESS('Successfully added products'))
    '''

    12. Membuat 'main.html'untuk menampilkan model yang dimiliki
    """python
    <!DOCTYPE html>
    <html>
    <head>
        <title>Main Page</title>
    </head>
    <body>
        <h1>Welcome, {{ name }}</h1>
        <p>NPM: {{ npm }}</p>
        <p>Class: {{ class_name }}</p> 

        <h2>Product List</h2>
        <ul>
            {% for product in products %}
                <li>{{ product.name }} - ${{ product.price }}<br>{{ product.description }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """

    13. Melakukan deploymeny pada PWS(Pacil Web Service)
 
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    **_Jawab_**:        
   
3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

    **_Jawab_**:
    1. Collaboration:
        Git memungkinkan pengerjaan proyek secara bersamaan dengan developer lain. Git berfungsi seperti Google Drive
    2. Backup File-File yang berkaitan dengan pembuatan project:
        Git bisa menjadi wadah untuk file atau product management. Hal ini dapat mempermudah developer atau user dalam menggunakan backup file yang udah diupload di git. 
    3. Deployment
        Git memudahkan developer dalam melakukan 'push' dan 'pull' dalam 'production server'
    4. Version Control
        Git dapat membantu dalam melihat historikal pengerjaan project, seperti terakhir kali pengeditan, siapa yang terakhir mengerjakan, dan lainnya. 

    
4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

   **_Jawab_**:
    Django sering dijadikan pilihan untuk pengenalan pengembangan perangkat lunak karena beberapa alasan penting. Framework ini mengikuti arsitektur Model-View-Template (MVT), yang membantu pemula memahami pentingnya struktur yang terorganisir dalam pengembangan aplikasi web. Django dilengkapi dengan banyak fitur bawaan seperti autentikasi, pengelolaan database, dan manajemen admin, yang memungkinkan pemula fokus pada belajar konsep dasar tanpa perlu memikirkan konfigurasi kompleks. Selain itu, Django menawarkan ORM bawaan yang memudahkan interaksi dengan database tanpa menulis SQL mentah, sekaligus menyediakan mekanisme keamanan yang melindungi dari ancaman umum seperti CSRF, SQL injection, dan XSS.

    Selain fitur-fitur tersebut, Django dirancang untuk mendukung pengembangan cepat (rapid development) dan dapat menangani aplikasi web yang kompleks dan besar, yang memberikan pemahaman tentang pengelolaan aplikasi yang skalabel. Kesederhanaan dan struktur yang jelas memudahkan pemula untuk memahami konsep dasar seperti routing, templating, dan manajemen database tanpa terbebani oleh kode yang berlebihan. Ditambah dengan dokumentasi yang kuat dan komunitas yang besar, Django menawarkan lingkungan yang ideal bagi pemula untuk belajar dan berkembang dalam pengembangan perangkat lunak.
    
5. Mengapa model pada Django disebut sebagai ORM?

    **_Jawab_**:
    Django disebut ORM (Object Relational Mapping) karena Django berfungsi sebagai penghubung antara model atau objek dalam kode Python dengan tabel dalam database relasional. Django mendukung berbagai jenis relasai antar tabel, seperti One-to-One, Many-to-One, dan Many-to-Many. Selain itu Django ORM membuat aplikasi lebih portabel karena tidak tergantung pada database tertentu, seperti SQLite ke PostgreSQL.

## Checklist Tugas

-   [x] Membuat sebuah proyek Django baru.
-   [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.
-   [x] Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.
-   [x] Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut.
    -   `name`
    -   `price`
    -   `description`
-   [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
-   [x] Membuat sebuah _routing_ pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
-   [x] Melakukan _deployment_ ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
-   [x] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi PWS yang sudah di-_deploy_, serta jawaban dari beberapa pertanyaan berikut.
    -   Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).
    -   Buatlah bagan yang berisi _request client_ ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
    -   Jelaskan fungsi `git` dalam pengembangan perangkat lunak!
    -   Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    -   Mengapa model pada Django disebut sebagai _ORM_?