# Ayo Belanja
E-commerce terbaik untuk segala kalangan umur

- [Profile](#profile)
- [Deployment](#deployment)
- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)

## Profile

Nama    : Anthony Edbert Feriyanto  
NPM     : 2306165654  
Kelas   : PBP C  

## Deployment

Tautan aplikasi PWS: [http://anthony-edbert-ayobelanja.pbp.cs.ui.ac.id](http://anthony-edbert-eshoppbp.pbp.cs.ui.ac.id)

# Tugas 2
## Pertanyaan dan Jawaban

1. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

    **Jawab:**

    1. Membuat direktori baru dengan nama `eshop-pbp`.
    2. Membuat berkas `requirements.txt` dan menambahkan dependencies berikut:
        ```
        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3
        ```
       Lalu, menjalankan perintah `pip install -r requirements.txt`.
    3. Membuat proyek dengan perintah:
        ```bash
        django-admin startproject mental_health_tracker .
        ```
    4. Menambahkan baris berikut pada `eshop-pbp/eshop-pbp/settings.py`:
        ```python
        ALLOWED_HOSTS = ["localhost", "127.0.0.1", "anthony-edbert-eshoppbp.pbp.cs.ui.ac.id"]
        ```
    5. Membuat berkas `.gitignore`.
    6. Membuat aplikasi bernama `main` dengan perintah:
        ```bash
        python manage.py startapp main
        ```
    7. Melakukan routing agar proyek dapat menjalankan aplikasi `main` dengan menambahkan kode berikut pada `urls.py`:
        ```python
        from django.contrib import admin
        from django.urls import path, include
        from main import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('main.urls')),
            path('', views.show_main, name='show_main'),
        ]
        ```
    8. Membuat model `Product` pada `models.py` dengan atribut `name`, `price`, dan `description`:
        ```python
        from django.db import models

        class ProductEntry(models.Model):
            name = models.CharField(max_length=255)
            price = models.IntegerField()
            description = models.TextField()
        ```
    9. Membuat fungsi `show_main` pada `views.py` untuk mengembalikan response dari atribut-atribut model `Product`:
        ```python
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
        ```
    10. Menambahkan routing untuk menghubungkan `views.py` di `main` pada `urls.py`:
        ```python
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
        ```
    11. Membuat file `add_products.py` untuk manajemen produk yang akan ditampilkan:
        ```python
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
        ```
    12. Membuat template `main.html` untuk menampilkan model yang dimiliki:
        ```html
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
        ```
    13. Melakukan deployment pada PWS (Pacil Web Service).

2. **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.**

    **Jawab:**
    ![Django Flow Chart](https://github.com/anthef/eshop-pbp/blob/main/flow_chart/flow_chart.jpg)
    
    Dalam aplikasi web Django, ketika seorang user mengirimkan request melalui browser, permintaan tersebut diterima oleh server dan pertama-tama dipetakan ke file `urls.py`. Di sini, Django memeriksa pola URL yang telah didefinisikan untuk menentukan ke mana request tersebut harus diarahkan. Biasanya, request tersebut akan diteruskan ke fungsi atau kelas yang sesuai di dalam `views.py`. `views.py` bertanggung jawab untuk menjalankan logika aplikasi, termasuk memutuskan apakah perlu berinteraksi dengan database melalui `models.py`. Jika interaksi dengan database diperlukan, seperti membaca atau menulis data, `views.py` akan mengakses `models.py` untuk melakukannya. Setelah semua proses selesai, `views.py` akan merender template yang terdiri dari file HTML, CSS, dan JavaScript untuk menampilkan antarmuka pengguna (UI).

3. **Jelaskan fungsi git dalam pengembangan perangkat lunak!**

    **Jawab:**

    1. **Collaboration:** Git memungkinkan pengerjaan proyek secara bersamaan dengan developer lain, mirip dengan Google Drive.
    2. **Backup File:** Git dapat menjadi tempat penyimpanan file atau product management, memudahkan penggunaan backup file.
    3. **Deployment:** Git memudahkan developer dalam melakukan 'push' dan 'pull' dalam 'production server'.
    4. **Version Control:** Git membantu dalam melihat historikal pengerjaan proyek, seperti pengeditan terakhir dan siapa yang mengerjakan.

4. **Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

    **Jawab:**

    Django sering dipilih untuk pengenalan pengembangan perangkat lunak karena:

    - **Struktur MVT:** Memudahkan pemahaman struktur yang terorganisir.
    - **Fitur Bawaan:** Memiliki autentikasi, pengelolaan database, dan manajemen admin yang memungkinkan pemula fokus pada konsep dasar.
    - **ORM:** Memudahkan interaksi dengan database tanpa menulis SQL mentah.
    - **Keamanan:** Menyediakan mekanisme keamanan terhadap ancaman umum.
    - **Pengembangan Cepat:** Mendukung pengembangan cepat dan aplikasi yang kompleks.
    - **Komunitas dan Dokumentasi:** Dokumentasi kuat dan komunitas besar mendukung pembelajaran.

5. **Mengapa model pada Django disebut sebagai ORM?**

    **Jawab:**

    Model pada Django disebut ORM (Object Relational Mapping) karena berfungsi sebagai penghubung antara model atau objek dalam kode Python dengan tabel dalam database relasional. ORM membantu aplikasi lebih portabel dan mendukung berbagai jenis relasi antar tabel.

## Checklist Tugas

- [x] Membuat sebuah proyek Django baru.
- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.
- [x] Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.
- [x] Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut:
  - `name`
  - `price`
  - `description`
- [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
- [x] Membuat sebuah _routing_ pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.
- [x] Melakukan _deployment_ ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- [x] Membuat sebuah `README.md` yang berisi tautan menuju aplikasi PWS yang sudah di-_deploy_, serta jawaban dari beberapa pertanyaan berikut:
  - Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).
  - Buatlah bagan yang berisi _request client_ ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.
  - Jelaskan fungsi `git` dalam pengembangan perangkat lunak!
  - Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
  - Mengapa model pada Django disebut sebagai _ORM_?

# Tugas 3

## Screenshot Postman
![JSON](https://github.com/anthef/eshop-pbp/blob/main/screenshot_post/json.png)
![XML](https://github.com/anthef/eshop-pbp/blob/main/screenshot_post/xml.png)
![JSON_ID](https://github.com/anthef/eshop-pbp/blob/main/screenshot_post/json_id.png)
![XML_ID](https://github.com/anthef/eshop-pbp/blob/main/screenshot_post/xml_id.png)

## Pertanyaan dan Jawaban 
1. **Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

    **Jawab:**
    
    Data delivery sudah menjadi pondasi vital dalam pengimplementasian sebuah plaform. Data delivery berfungsi sebagai jembatan ataupun infrastruktur yang memungkinkan berbagai elemen platform untuk berkomunikasi secara seamless. Data pada berbagai elemen, seperti dari server ke klien ataupun sebaliknya, dari database ke user interface dapat mengalir dengan lancar, aman, dan tepat waktu. Tanpa adanya data delivery, maka setiap elemen pada platform akan terisolasi. Hal itu menyebabkan fungsionalitas dari suatu platform akan menjadi tidak sesuai harapan. Selain itu, data delivery yang baik dapat meningkatkan skalabilitas dan memungkinkan platform untuk beradaptasi dengan cepat dengan perubahan kebutuhan dan menangani lonjakan lalu lintas data.

2. **Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**

    **Jawab:**

    Menurut saya, dalam hal format pertukaran data yang umum digunakan, saya memilih JSON untuk digunakan. Banyak aspek yang memengaruhi JSON lebih populer dari XML, seperti:

    - **Kesederhanaan** JSON memiliki sintaks yang lebih sederhana. Tidak seperti XML, JSON tidak memerlukan suatu tag pembuka ataupun penutup. Dari segi struktur, JSON memiliki struktur yang mirip dengan object dan array dalam JavaScript
    - **Ukuran File** JSON umumnya menghasilkan file dengan ukuran lebih kecil dbandingkan XML karena tidak memerlukan tag penutup
    - **Parsing yang lebih cepat** JSON dapat di parse menjadi objek JavaScript dengan sangat cepat
    - **Struktur data yang lebih fleksibel** JSON mendukung tipe data, seperti array dan object nested dengan lebih alami
    - **Popularisasi dalam API** Banyak API yang menggunakan JSON karena kemudahan dalam penggunaanya

    Walaupun XML menawarkan beberapa fitur tambahan seperti mendukung namespace dan skema yang lebih kuat untuk validasi, JSON lebih populer karena lebih ringkas dan mudah dalam pengimplementasiannya.
    
3. **Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?**

    **Jawab:**

4.  **Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

    **Jawab:**

5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

    **Jawab:**


## Checklist Tugas
- [x] Membuat input `form` untuk menambahkan objek model pada app sebelumnya.
- [x] Tambahkan 4 fungsi `views` baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
- [x] Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.
- [x] Menjawab beberapa pertanyaan berikut pada `README.md` pada root folder.
  - [x] Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
  - [x] Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
  - [x] Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
  - [x] Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
  - [x] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
-  [x] Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md`.
- [x] Melakukan `add`-`commit`-`push` ke GitHub.