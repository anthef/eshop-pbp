# Ayo Belanja
E-commerce terbaik untuk segala kalangan umur

- [Profile](#profile)
- [Deployment](#deployment)
- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)
- [Tugas 4](#tugas-4)
- [Tugas 5](#tugas-5)
- [Tugas 6](#tugas-6)

## Profile

Nama    : Anthony Edbert Feriyanto  
NPM     : 2306165654  
Kelas   : PBP C  

## Deployment

Tautan aplikasi PWS: [http://anthony-edbert-ayobelanja.pbp.cs.ui.ac.id](http://anthony-edbert-ayobelanja.pbp.cs.ui.ac.id)

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
    ![Django Flow Chart](https://github.com/anthef/eshop-pbp/blob/main/static_file/flow_chart/flow_chart.jpg)
    
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

    Method `is_valid()` berperan penting dalam proses validasi data yang diinput oleh pengguna. Method ini berfungsi untuk memeriksa apakah data yang disubmit melalui form sudah memenuhi semua aturan validasi, seperti apakah semua field yang required sudah diisi, apakah format data sudah sesuai, atau apakah data sudah memenuhi batasan khusus yang telah didefinisikan. Jika semua data valid, maka `is_valid()` akan mengembalikan `True` dan jika ada yang tidak valid, akan mengembalikan `False`. Selain itu, jika validasi gagal, Django sendiri akan mengisi dictionary `form.errors` dengan pesan error untuk setiap field yang tidak valid. Selain itu, method ini juga membantu mencegah data yang tidak valid atau berbahaya masuk ke dalam sistem untuk melindungi aplikasi dari potensi bug atau serangan keamanan.


4.  **Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

    **Jawab:**

    Cross-Site Request Forgery Token merupakan suatu token untuk melindungi aplikasi dari serangan Cross Site Request Forgery. Dengan adanya `csrf_token`, dapat memastikan bahwa request POST berasal dari situs yang sah dan mencegah modifikasi data yang tidak sah melalui request palsu. Tanpa adanya `csrf_token`, penyerang akan membuat suatu request palsu menggunakan nama pengguna yang sudah terotentikasi, mengubah data-data sensitif, ataupun informasi pribadi pengguna bisa terekspos dan termanipulasi.

    Jika suatu website tidak memiliki `csrf_token`, maka penyerang akan membuat situs web berbahaya atau memodifikasi situ yang sudah ada. Lalu, pengguna yang sudah login ke aplikasi Django akan tanpa sadar mengakses situs berbahaya tersebut. Setelah itu, situs berbahaya akan memuat form tersembunyi yang mengirim request ke aplikasi Django. Setelah itu, penyerang akan memanfaatkan cookies sesi yang valid dari pengguna. Request palsu akan terlihat sah karena berasal dari browser pengguna yang sudah terotentikasi. Tanpa adanya `csrf_token`, server tidak dapat membedakan request yang sah dan yang palsu. 

    Django menghasilkan token unik untuk setiap sesi pengguna. Token ini disertakan dalam setiap form sebagai field tersembunyi. Saat form disubmit, Django akan memeriksa kecocokan token. Jika token berbeda, maka request akan ditolak. Dengan itu, keamanan website akan terjaga.


5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

    **Jawab:**
    1. Membuat `base.html` untuk menjadi page utama dalam website
    ```python
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            {% block meta %} {% endblock meta %}
        </head>
        <body>
            {% block content %} {% endblock content %}
        </body>
    </html>
    ```

    2. Menambahkan `BASE_DIR` pada `settings.py` agar project mengenali html yang akan menjadi template utama
    ```python
    'DIRS': [BASE_DIR / 'templates'],
    ```

    3. Menambahkan atribut `time` dan `id` pada model product
    ```python
    from django.db import models
    import uuid

    class ProductEntry(models.Model):
        id = models.UUIDField(primary_key=True,default = uuid.uuid4, editable=False)
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        time = models.DateField(auto_now_add=True)

        def __str__(self):
            return self.name
    ```

    4. Membuat `forms.py` untuk mendeklarasikan atribut-atribut dari model yang membutuhkan input dari user
    ```python
    from django.forms import ModelForm
    from .models import ProductEntry

    class ProductEntryForm(ModelForm):
        class Meta:
            model = ProductEntry
            fields=['name','price','description']
    ```

    5. Membuat method `create_name_entry` untuk mengambil input user sesuai dengan `forms.py`
    ```python
    def create_name_entry(request):
        form = ProductEntryForm(request.POST or None)
        if form.is_valid() and request.method == 'POST':
            form.save()
            return redirect('main:show_main')
        context={'form':form}
        return render(request,'create_name_entry.html',context)
    ```

    6. Membuat method `show_main` untuk menampilkannya di `main.html`
    ```python
    def show_main(request):
        products = ProductEntry.objects.all()

        context = {
            'npm': '2306165654',
            'name': 'Anthony Edbert Feriyanto',
            'class_name': 'PBP C',
            'shop_name':'Ayo Belanja',  
            'product_entry' : products
        }

        return render(request, "main.html", context)
    ```

    7. Membuat method `delete_product_entry` untuk menghapus input yang sudah masuk ke database sesuai dengan keinginan pengguna
    ```python
    def delete_product_entry(request, id):
        if request.method == 'POST':
            product = get_object_or_404(ProductEntry, id=id)
            product.delete()
            return redirect('main:show_main')
        return redirect('main:show_main')
    ```

    8. Membuat `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id` untuk menampilkan response back dari input user
    ```python
    def show_xml(request):
        data = ProductEntry.objects.all()
        return HttpResponse(serializers.serialize("xml",data),content_type='application/xml')

    def show_json(request):
        data = ProductEntry.objects.all()
        return HttpResponse(serializers.serialize("json",data),content_type='application/json')

    def show_xml_by_id(request, id):
        data = ProductEntry.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = ProductEntry.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

    9. Melakukan routing di dari method yang sudah dibuat di `urls.py`
    ```python
    from django.urls import path
    from main.views import show_main,create_name_entry,show_xml,show_json,show_xml_by_id,show_json_by_id,delete_product_entry

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-name-entry', create_name_entry, name='create_name_entry'),
        path('xml/',show_xml,name='show_xml'),
        path('json/',show_json,name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
        path('delete/<uuid:id>/', delete_product_entry, name='delete_product_entry'),
        ]
    ```

    10. Membuat `create_name_entry.html` untuk tampilan ketika web ingin meminta input dari pengguna
    ```python
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add Product Entry</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Product Entry" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
    ```
    
    11. Membuat `main.html` untuk menampilkan product dari hasil input pengguna
    ```python
        {% extends 'base.html' %}
        {% block content %}
        <!DOCTYPE html>
        <html>
        <head>
            <title>Main Page</title>
        </head>
        <body>
            <h1>Welcome to {{ shop_name }} by {{ name }}</h1>
            <p>NPM: {{ npm }}</p>
            <p>Class: {{ class_name }}</p> 

            {% if not product_entry %}
            <p>Belum ada data product pada AyoBelanja.</p>
            {% else %}
            <table>
            <tr>
                <th>Product Name</th>
                <th>Time</th>
                <th>Description</th>
                <th>Price</th>
                <th>Actions</th>
            </tr>

            {% for product in product_entry %}
            <tr>
                <td>{{ product.name }}</td>
                <td>{{ product.time }}</td>
                <td>{{ product.description }}</td>
                <td>{{ product.price }}</td>
                <td>
                    <form action="{% url 'main:delete_product_entry' product.id %}" method="POST" style="display:inline;">
                        {% csrf_token %}
                        <button type="submit">Delete</button>
                    </form>
                </td>
            </tr>
            {% endfor %}
            </table>
            {% endif %}

            <br />

            <a href="{% url 'main:create_name_entry' %}">
                <button>Add New Product Entry</button>
            </a>
        </body>
        </html>
        {% endblock content %}
    ```

## Screenshot Postman
| Response   | Screenshot |
|------------|------------|
| JSON       | ![JSON](https://github.com/anthef/eshop-pbp/blob/main/static_file/screenshot_post/json.png) |
| XML        | ![XML](https://github.com/anthef/eshop-pbp/blob/main/static_file/screenshot_post/xml.png) |
| JSON_ID    | ![JSON_ID](https://github.com/anthef/eshop-pbp/blob/main/static_file/screenshot_post/json_id.png) |
| XML_ID     | ![XML_ID](https://github.com/anthef/eshop-pbp/blob/main/static_file/screenshot_post/xml_id.png) |


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

# Tugas 4
## Pertanyaan dan Jawaban

1. **Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`**

    **Jawab:**

    Perbedaan antara `HttpResponseRedirect()` dan `redirect()` adalah `HttpResponseRedirect()` merupakan class yang berasal dari `django.http` sedangkan `redirect` adalah fungsi shortcut yang berasal dari `django.shortcuts`. Selain itu dari segi fleksibilitas, `HttpResponseRedirect()` memerlukan URL lengkap atau path relatif tetapi, `redirect` lebih fleksibel karena parameter function dapat menerima berbagai jenis function.

    `HttpResponseRedirect()` hanya menerima URL string, sedangkan `redirect` dapat menerima argumen berupa nama URL pattern, URL relatif, URL absolut, model object, view name dengan argumen.

    `HttpResponseRedirect()` berguna disaat kita membutuhkan kontrol penuh terhadap URL atau ketika bekerja dengan external URL atau generate URLs secara dinamis. Sedangkan,`redirect` berguna ketikan kita membutuhkan suatu fungsi untuk bekerja dengan view name, model objects. `redirect` dalam mengurangi reduces boilerplate code.

    Conton pengunaan `HttpResponseRedirect`:
    ```python
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect('/new-path/')
    ```

    Contoh pengunaan `redirect`:
    ```python
    from django.shortcuts import redirect
    return redirect('home')  
    ```

2. **Jelaskan cara kerja penghubungan model `Product` dengan `User`!**

    **Jawab:** 

    Dalam Django, model `Product` biasanya dihubungkan dengan model `User` menggunakan Foreign Key. Dengan adanya Foreign Key, setiap `Product` dapat terhubung ke pengguna tertentu yang telah login.

    Contoh model `Product`:
    ```python
    from django.db import models
    import uuid
    from django.contrib.auth.models import User

    class ProductEntry(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        id = models.UUIDField(primary_key=True,default = uuid.uuid4, editable=False)
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        time = models.DateField(auto_now_add=True)

        def __str__(self):
            return self.name
    ```

    Cara kerja dalam menghubungkannya adalah dengan setiap kali pengguna membuat entry product, entry tersebut akan dikaitkan dengan `user` yang login. Lalu ForeignKey akan bermanfaat untuk membuat relasi many-to-one antara `Product` dengan `User`. Many-to-one memiliki arti bahwa setiap `user` dapat memiliki lebih dari satu entry `Product`. Lalu parameter `on_delete=models.Cascade` memiliki arti apabila `user` dihapus, maka semua entri `Product` yang berkaitan dengan `user` akan dihapus.


3. **Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**

    **Jawab:**

    Authentication adalah proses untuk memverifikasi identitas seorang pengguna, biasanya dilakukan melalui kredensial seperti nama pengguna dan kata sandi. Proses ini bertujuan untuk memastikan bahwa pengguna yang mencoba mengakses suatu sistem atau layanan adalah benar-benar orang yang berwenang.

    Authorization adalah proses untuk menentukan apa yang diizinkan dilakukan oleh pengguna yang telah terautentikasi, seperti mengakses sumber daya tertentu atau melakukan tindakan-tindakan tertentu dalam sistem. Setelah identitas pengguna diverifikasi melalui proses autentikasi, otorisasi berfungsi sebagai langkah berikutnya untuk mengatur hak akses dan peran pengguna di dalam sistem tersebut. Misalnya, seorang pengguna yang memiliki hak administrator dapat mengakses dan mengelola seluruh data atau konfigurasi sistem, sementara pengguna biasa mungkin hanya memiliki akses terbatas, seperti melihat atau mengedit data tertentu. Otorisasi juga dapat mencakup pengaturan izin yang lebih rinci, seperti menentukan apakah pengguna dapat menambahkan, menghapus, atau memodifikasi informasi. 

    Ketika seorang pengguna melakukan login, autentikasi dilakukan dengan memverifikasi kredensial pengguna, seperti nama pengguna dan kata sandi. Jika kredensial tersebut valid, sistem, seperti Django, akan membuat sesi untuk pengguna tersebut dan menandai mereka sebagai pengguna yang telah terautentikasi. Artinya, proses autentikasi berfungsi untuk memastikan bahwa identitas pengguna adalah benar dan sesuai dengan informasi yang tersimpan di dalam sistem.

    Namun, autentikasi berbeda dari otorisasi. Autentikasi hanya memverifikasi siapa pengguna tersebut, sedangkan otorisasi adalah proses yang menentukan apa saja yang diizinkan untuk dilakukan oleh pengguna tersebut setelah berhasil terautentikasi. Misalnya, setelah login (autentikasi), pengguna mungkin diizinkan (otorisasi) untuk mengakses halaman profil mereka, tetapi mereka mungkin tidak diizinkan untuk mengakses halaman administratif yang hanya dapat diakses oleh pengguna dengan hak istimewa tertentu.

    Django Implementation :
    Authentication di Django ditangani melalui sistem otentikasi bawaan (`django.contrib.auth`). Built-in sistem tersebut akan memverifikasi kredensial pengguna menggunakan metode seperti `authenticate()` dan `login()`.

    Authorization dikelola melalui izin dan grup. Setelah otentikasi, Django memeriksa izin pengguna (misalnya, menggunakan `user.has_perm()`) untuk menentukan apakah mereka berwenang untuk melakukan tindakan tertentu.

4. **Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**

    **Jawab:**

    Django mengingat pengguna yang telah login melalui session-based authentication. Setelah pengguna berhasil login, Django menciptakan sesi yang menyimpan status autentikasi pengguna. Sesi ini diidentifikasi oleh session ID yang disimpan di dalam cookie pada browser pengguna. Setiap kali pengguna berinteraksi dengan server, cookie yang mengandung session ID dikirimkan kembali ke server. Django menggunakan session ID ini untuk mengambil data sesi dari server dan memastikan bahwa pengguna tersebut masih dalam status login. Django tidak menyimpan informasi sensitif seperti password di dalam cookie. Hanya session ID yang disimpan di browser, sementara data sesi sebenarnya tersimpan aman di server.

    Kegunaan lain dari cookies :
      - Preferensi Pengguna: Cookies dapat menyimpan preferensi seperti pengaturan bahasa atau tema, yang memudahkan personalisasi pengalaman pengguna di sesi berikutnya.
      - Pelacakan: Cookies sering digunakan untuk tujuan analitik, seperti melacak perilaku pengguna di situs web, atau untuk menyimpan item di keranjang belanja.
      - Token Autentikasi: Dalam beberapa mekanisme autentikasi yang stateless, seperti JWT (JSON Web Tokens), cookies digunakan untuk menyimpan token autentikasi.
    
    Serta, tidak semua cookies aman. Jika tidak ditangani dengan baik, cookies dapat menjadi vektor serangan, terutama jika mereka mengandung informasi sensitif yang tidak dienkripsi. 

    Oleh karena itu, Django mendukung berbagai pengaturan untuk meningkatkan keamanan cookie, di antaranya:
      - HttpOnly: Mencegah JavaScript di sisi klien untuk mengakses cookie, yang dapat mengurangi risiko serangan cross-site scripting (XSS).
      - Secure: Memastikan bahwa cookie hanya dikirim melalui koneksi HTTPS, sehingga melindunginya dari penyadapan pada koneksi yang tidak aman.
      - SameSite: Membatasi pengiriman cookie dalam permintaan lintas situs, yang membantu mencegah serangan cross-site request forgery (CSRF).


5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

    **Jawab:**

    1. Membuat form register menggunakan `UserCreationForm` dari `django.contrib.auth.forms` di `views.py` aplikasi `main`
    ```python
    def register(request):
        form = UserCreationForm()
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)
    ```

    2. Membuat page HTML sederhananya untuk `register.html` di dalam direktori `templates/main`
    ```python
    {% extends 'base.html' %}
    {% block meta %}
    <title>Register</title>
    {% endblock meta %}
    {% block content %}
    <div class="login">
    <h1>Register</h1>
    <form method="POST">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input type="submit" name="submit" value="Daftar" /></td>
        </tr>
        </table>
    </form>
    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    </div>
    {% endblock content %}
    ```

    3. Menambahkan function `urls.py`
    ```python
    path('register/', register, name='register'),
    ```

    4. Membuat form login menggunakan `AuthenticationForms` dari `django.contrib.auth.forms` dan method `authenticate` dan `login` dari `django.contrib.auth` di `views.py` aplikasi `main`.
    ```python
    def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()  
                if user is not None:
                    login(request, user)
                    response = HttpResponseRedirect(reverse("main:show_main"))
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response
        else:
            form = AuthenticationForm()
        context = {"form": form}
        return render(request, "login.html", context)
    ```

    Saat ini saya melakukan set cookie `last_login` dengan waktu saat ketika `user` berhasil login dengan menggunakan library `datetime`.

    5. Membuat page HTML baru untuk form, yaitu `login.html` di dalam aplikasi `main`.
    ```python
    {% extends 'base.html' %}
    {% block meta %}
    <title>Login</title>
    {% endblock meta %}

    {% block content %}
    <div class="login">
    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Login" /></td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %} Don't have an account yet?
    <a href="{% url 'main:register' %}">Register Now</a>
    </div>

    {% endblock content %}
    ```

    6. Menambahkan `urls.py` untuk `login`
    ```python
    path('login/', login_user, name='login'),   
    ```

    7. Membuat method `logout_user`
    ```python
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        print("Logout successful, redirecting to login page") 
        return response
    ```

    8. Menambahkan pada `urls.py`
    ```python
    path('logout/', logout_user, name='logout_user'),
    ```

    9.'Menambahkan button `logout` pada `main.html`
    ```python
    <a href="{% url 'main:logout_user' %}">
        <button>Logout</button>
    </a>
    ```

    10. Menambahkam baris pada `show_main`
    ```python
    products = Product.objects.filter(user=req.user)
    ```

## Checklist Tugas
- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
- [x] Membuat **dua** akun pengguna dengan masing-masing **tiga** dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun **di lokal**.
- [x] Menghubungkan model `Product` dengan `User`.
- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi.
- [x] Menjawab beberapa pertanyaan berikut pada `README.md` pada root folder (silakan modifikasi `README.md` yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
  - [x] Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
  - [x] Jelaskan cara kerja penghubungan model `Product` dengan `User`!
  - [x] Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
  - [x] Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
  - [x] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [x] Melakukan `add`-`commit`-`push` ke GitHub.

# Tugas 5
## Pertanyaan dan Jawaban
1. **Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**
    
    **Jawab:**
    Pada css terdapat aturan prioritas untuk menentukan selector mana yang dipakai. Urutan dari prioritasnya, yaitu :
    1. Important Rule, seperti contoh `!important` dapat mengesampingkan semua prioritas dan memberikan prioritas tertinggi untuk suatu property.
    2. Inline Styles, seperti contoh `style="color:blue;"` memiliki prioritas tertinggi.
    3. ID Selector, seperti contoh `#para1` memeiliki prioritas lebih tinggi dari elemen atau class.
    4. Class Selector, seperti contoh `.center` memiliki prioritas lebih tinggi dari tag HTML.
    5. Tag Selector, seperti contoh `h1` memiliki prioritas terendah

2. **Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**

    **Jawab:**

    Responsive design merupakan suatu pendekatan dalam desain web yang memungkinkan tampilan dan layout situr web atau aplikasi dapat beradaptasi secara otomatis sesuai dengan ukuran layar dan orientasi perangkat yang digunakan. Tujuan utama dari responsive design adalah memberikan user experience yang konsisten dan optimal, terlepas dari apakah pengguna mengakses situs dari dekstop, laptop, atau smartphone.

    Dengan menggunakan responsive design, suatu web dapat mengoptimalkan tampilannya. Dedngan itu, elemen di halaman web tidak terlihat distorsi atau tidak beraturan saat diakses dari berbagai ukuran perangkat. Selain itu, responsive design dapat memperbaiki aksesibilitas. Pengguna tidak perlu melakukan zoom in atau zoom out untuk membaca teks atau mengklik tombol di perangkat mobile. Serta, responsive design dapat memastikan bahwa elemen, seperti gambar, vide, atau konten lainnya tetap efisien di layar kecil tanpa memperlampat kinerja halaman.

    Contoh aplikasi yang sudah menerapkan responsive design:
    - Google
    - Tokopedia
    - Tiket.com

    Contoh aplikasi yang belum menerapkan responsive design:
    - SiakNG
    - https://nostalgicweb.com/

3. **Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**

    **Jawab:**
    ![Margin, Padding, Border](https://github.com/anthef/eshop-pbp/blob/main/static_file/tugas_5/marginpadborder.png)
    - Margin merupakan ruang di luar elemen, antara elemen dengan elemen lainnya. Penggunaan margin sering digunakan untuk memberikan ruang antar elemen, sehingga tata letak halaman lebih teratur.
    - Border merupakan garis yang membungkus elemen terletak di antara margin dan padding. Border digunakan untuk memberikan definisi atau pemisahan visual antara elemen dan latar belakang.
    - Padding merupakan ruang di dalam elemen, antara content dan border. Padding sering digunakan untuk memberikan ruang di sekitar konten agar lebih mudah dibaca dan terlihat lebih baik.

4. **Jelaskan konsep flex box dan grid layout beserta kegunaannya!**

    **Jawab:**

    Flexbox atau flexible box meruapakan metode layout atau tata letak dalam css yang digunakan untuk mengatur elemen dalam satu dimensi, baik secara horizontal maupun vertikal. Flexbox dapat memudahkan pembuatan layout yang fleksibel dan responsif. Sedangkan grid layout merupakan sistem layout dua dimensi yang memungkinkan developer untuk membuat desain halaman yang lebih kompleks dengan baris dan kolom. Grid layout cocok untuk mengatur elemen dalam struktur grid yang rapi.

    Kegunaan flexbox:
    1. Flexbox memudahkan penataan elemen di dalam container tanpa perlu menggunakan float atau positioning manual. Elemen-elemen dapat disusun secara horizontal (baris) atau vertikal (kolom), dan akan menyesuaikan ukurannya berdasarkan ruang yang tersedia.
    2. Flexbox memungkinkan elemen untuk secara otomatis memperbesar atau memperkecil ukuran mereka agar sesuai dengan ruang yang tersedia. Elemen dapat membagi ruang secara proporsional sesuai kebutuhan, membuat tata letak lebih adaptif terhadap berbagai ukuran layar.
    3. Flexbox menyediakan kontrol yang kuat untuk mengatur alignment (penyelarasan) elemen di dalam container, baik secara horizontal maupun vertikal. Ini sangat memudahkan dalam menyusun konten di tengah-tengah halaman atau div, tanpa kode tambahan yang rumit.
    4. Flexbox secara otomatis menyesuaikan elemen terhadap ukuran layar, menjadikannya alat yang ideal untuk menciptakan tata letak yang responsif. Misalnya, elemen dapat ditata ulang atau diatur ulang ketika ruang tersedia berubah, tanpa perlu menggunakan media queries dalam beberapa kasus.
    5. Flexbox memungkinkan pengaturan jarak antar elemen dengan mudah menggunakan properti seperti `justify-content` dan `align-items`, membuat kontrol terhadap jarak menjadi lebih efisien.
    6. Dengan Flexbox, urutan elemen dapat diatur ulang menggunakan properti `order` tanpa perlu mengubah struktur HTML. Ini sangat membantu ketika membuat layout yang responsif dan adaptif.

    Kegunaan Grid Layout:
    1. Grid layout memungkinkan pengaturan elemen dalam baris dan kolom sekaligus, sehingga cocok untuk membuat layout yang lebih kompleks, seperti tata letak halaman majalah, dashboard, atau galeri gambar.
    2. Grid memungkinkan kontrol penuh atas ukuran kolom dan baris, baik secara proporsional, menggunakan fraksi (`fr`), piksel (`px`), atau satuan lain. Spacing antar elemen dapat dengan mudah dikendalikan menggunakan properti `grid-gap`, `row-gap`, dan `column-gap`.
    3. Dengan grid layout, elemen dapat dengan mudah diposisikan atau direntangkan melintasi beberapa kolom atau baris tanpa harus mengubah urutan HTML. Properti seperti `grid-column` dan `grid-row` memungkinkan penempatan elemen tertentu pada sel tertentu dalam grid.
    4. Grid layout mendukung tata letak yang responsif secara alami. Dengan fitur media queries dan properti auto-fit atau auto-fill, tata letak dapat disesuaikan dengan berbagai ukuran layar. Pengembang dapat membuat berbagai tata letak untuk perangkat yang berbeda hanya dengan mengubah struktur grid.
    5. Grid layout memudahkan pembuatan template halaman yang konsisten. Dengan properti seperti `grid-template-columns` dan `grid-template-rows`, pengembang dapat dengan cepat menentukan struktur layout untuk keseluruhan halaman atau bagian tertentu.
    6. Dalam grid layout, elemen tidak harus mengisi seluruh grid. Elemen dapat dengan mudah ditempatkan di mana saja dalam grid, memungkinkan pengaturan ruang kosong yang efektif untuk desain yang lebih estetis dan minimalis.

5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**

    **Jawab:**
    1. Menambahkan dua function di `views.py`, yaitu `delete_product` dan `edit_product` yang bisa diterapkan pada setiap productnya.
    ```python
    def delete_product(request, id):
        mood = ProductEntry.objects.get(pk = id)
        mood.delete()
        return HttpResponseRedirect(reverse('main:show_main'))

    def edit_product(request, id):
        mood = ProductEntry.objects.get(pk = id)
        form = ProductEntryForm(request.POST or None, instance=mood)
        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        context = {'form': form}
        return render(request, "edit_product.html", context)
    ```

    2. Melakukan routing dari kedua function ini ke `urls.py`
    ```python
        path('delete/<uuid:id>', delete_product, name='delete_product'),
        path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    ```

    3. Pada `base.html` menambahkan beberapa code untuk responsive design web dan juga tailwind css
    ```python
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://cdn.tailwindcss.com"></script>
    ```

    4. Membuat `global.css` untuk mengatur tampilan general dari web
    ```css
    .form-style form input, form textarea, form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc;
    border-radius: 0.375rem;
    }
    .form-style form input:focus, form textarea:focus, form select:focus {
        outline: none;
        border-color: #674ea7;
        box-shadow: 0 0 0 3px #674ea7;
    }
    @keyframes shine {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    .animate-shine {
        background: linear-gradient(120deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.3));
        background-size: 200% 100%;
        animation: shine 3s infinite;
    }
    ```

    5. Membuat dua `navbar.html` berbeda untuk authentication page dan juga main page
    ```html
    <nav class="bg-gradient-to-r from-blue-600 to-purple-700 shadow-lg fixed top-0 left-0 z-40 w-full transition duration-300 ease-in-out">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
            <div class="flex items-center">
                <h1 class="text-4xl font-bold text-center text-white hover:text-yellow-300 transition duration-300 transform hover:scale-105 pulse-animation">Ayo Belanja</h1>
            </div>

            <div class="hidden md:flex items-center space-x-4">
                <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-6 rounded-full transition duration-300 ease-in-out transform hover:scale-105 active:scale-95 shadow-md hover:shadow-lg">
                    Login
                </a>
                <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-6 rounded-full transition duration-300 ease-in-out transform hover:scale-105 active:scale-95 shadow-md hover:shadow-lg">
                    Register
                </a>
            </div>

            <div class="md:hidden flex items-center">
                <button class="mobile-menu-button focus:outline-none">
                    <svg class="w-6 h-6 text-white transition-transform duration-300 transform hover:text-yellow-300" id="menu-icon" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                        <path d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>
        </div>
        </div>

        <div class="mobile-menu hidden md:hidden px-4 w-full md:max-w-full transition-all duration-300 ease-in-out bg-gradient-to-b from-blue-600 to-purple-700">
            <div class="pt-2 pb-3 space-y-2 mx-auto">
                <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out transform hover:scale-105 active:scale-95 shadow-md hover:shadow-lg">
                    Login
                </a>
                <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out transform hover:scale-105 active:scale-95 shadow-md hover:shadow-lg">
                    Register
                </a>
            </div>
        </div>
    </nav>

    <style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .mobile-menu {
        animation: fadeIn 0.3s ease-out;
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }

    .pulse-animation {
        animation: pulse 2s infinite;
    }
    </style>

    <script>
        const btn = document.querySelector("button.mobile-menu-button");
        const menu = document.querySelector(".mobile-menu");
        const menuIcon = document.getElementById('menu-icon');
        const navBar = document.querySelector('nav');

        btn.addEventListener("click", () => {
            menu.classList.toggle("hidden");
            menuIcon.classList.toggle("rotate-90");
        });

        const logo = document.querySelector('h1');
        logo.classList.add('pulse-animation');

        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navBar.classList.add('bg-opacity-90');
            } else {
                navBar.classList.remove('bg-opacity-90');
            }
        });
    </script>
    ```
    Membuat navbar pada authentication page yang hanya berisi login dan juga logout. Sedangkan navbar untuk main page berisi home, products, categories, cart, dan juga profile.
    ```html
    <nav class="bg-gradient-to-r from-blue-500 to-purple-600 shadow-lg fixed top-0 left-0 z-40 w-full transition duration-300 ease-in-out">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
            <div class="flex items-center">
                <h1 class="text-3xl font-bold text-center text-white hover:text-yellow-300 transition duration-300 transform hover:scale-125">Ayo Belanja</h1>
            </div>

            <div class="hidden md:flex items-center space-x-6">
                <a href="{% url 'main:show_main' %}" class="text-white hover:text-yellow-300 transition duration-300 transform hover:scale-110">Home</a>
                <a href="{% url 'main:show_main' %}" class="text-white hover:text-yellow-300 transition duration-300 transform hover:scale-110">Products</a>
                <a href="{% url 'main:show_main' %}" class="text-white hover:text-yellow-300 transition duration-300 transform hover:scale-110">Categories</a>
                <a href="{% url 'main:show_main' %}" class="text-white hover:text-yellow-300 transition duration-300 transform hover:scale-110">Cart</a>

                <div class="flex flex-col items-end group">
                    {% if user.is_authenticated %}
                    <span class="text-white text-sm group-hover:text-yellow-300 transition duration-300">Welcome</span>
                    <span class="text-yellow-300 font-semibold text-sm group-hover:text-white transition duration-300">{{ user.username }}</span>
                    <span class="text-white text-xs group-hover:text-yellow-300 transition duration-300">Last Login: {{ user.last_login|date:"Y-m-d H:i:s" }}</span>
                    {% endif %}
                </div>

                {% if user.is_authenticated %}
                <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300 ease-in-out transform hover:scale-105 active:scale-95 shadow-md hover:shadow-lg">
                    Logout
                </a>
                {% endif %}
            </div>

            <div class="md:hidden flex items-center">
                <button class="mobile-menu-button focus:outline-none">
                    <svg class="w-6 h-6 text-white transition-transform duration-300 transform hover:text-yellow-300" id="menu-icon" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                        <path d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>
            </div>
        </div>

        <div class="mobile-menu hidden md:hidden px-4 w-full md:max-w-full transition-all duration-300 ease-in-out bg-gradient-to-b from-blue-600 to-purple-700">
            <div class="pt-2 pb-3 space-y-1 mx-auto">
                <a href="{% url 'main:show_main' %}" class="block text-white hover:text-yellow-300 transition duration-300 py-2">Home</a>
                <a href="{% url 'main:show_main' %}" class="block text-white hover:text-yellow-300 transition duration-300 py-2">Products</a>
                <a href="{% url 'main:show_main' %}" class="block text-white hover:text-yellow-300 transition duration-300 py-2">Categories</a>
                <a href="{% url 'main:show_main' %}" class="block text-white hover:text-yellow-300 transition duration-300 py-2">Cart</a>
                
                <div class="flex flex-col items-start space-y-1 py-2">
                    {% if user.is_authenticated %}
                    <span class="text-white text-sm">Welcome</span>
                    <span class="text-yellow-300 font-semibold text-sm">{{ user.username }}</span>
                    <span class="text-white text-xs">Last Login: {{ user.last_login|date:"Y-m-d H:i:s" }}</span>
                    {% endif %}
                </div>

                {% if user.is_authenticated %}
                <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300 ease-in-out transform hover:scale-105 active:scale-95 shadow-md hover:shadow-lg">
                    Logout
                </a>
                {% endif %}
            </div>
        </div>
    </nav>

    <style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .mobile-menu {
        animation: fadeIn 0.3s ease-out;
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }

    .pulse-animation {
        animation: pulse 2s infinite;
    }
    </style>

    <script>
        const btn = document.querySelector("button.mobile-menu-button");
        const menu = document.querySelector(".mobile-menu");
        const menuIcon = document.getElementById('menu-icon');
        const navBar = document.querySelector('nav');

        btn.addEventListener("click", () => {
            menu.classList.toggle("hidden");
            menuIcon.classList.toggle("rotate-90");
        });

        const logo = document.querySelector('h1');
        logo.classList.add('pulse-animation');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navBar.classList.add('bg-opacity-90');
            } else {
                navBar.classList.remove('bg-opacity-90');
            }
        });
    </script>
    ```

    6. Menambahkan path untuk ke static folder pada `settings.py`
    ```python
    STATIC_URL = '/static/'
    if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]
    else:
    STATIC_ROOT = BASE_DIR / 'static' 
    ```

    7. Membuat tampilan `login.html` yang meminta username dan juga password serta dapat mengarahkan ke `register.html`
    ```html
    {% extends 'base.html' %}

    {% block meta %}
    <title>Login</title>
    {% endblock meta %}
    {% block content %}
    {% include 'components/auth/navbar.html' %}
        <main class="flex items-center justify-center w-screen h-screen px-5">
            <div class="shadow-xl bg-white p-5 sm:p-10 rounded-3xl flex flex-col gap-10 items-center border-[2px] border-black/5 w-full max-w-md">
                <h2 class="font-bold text-xl sm:text-2xl text-center">Ayo Belanja</h2>
                
                <form class="mt-8 space-y-6 w-full" method="POST" action="">
                    {% csrf_token %}
                    <input type="hidden" name="remember" value="true">
                    
                    <div class="space-y-4">
                        <div>
                            <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
                            <input id="username" name="username" type="text" required aria-label="Username" aria-required="true"
                                class="appearance-none rounded relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Enter your username">
                        </div>

                        <div>
                            <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
                            <input id="password" name="password" type="password" required aria-label="Password" aria-required="true"
                                class="appearance-none rounded relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Enter your password">
                        </div>
                    </div>

                    <div>
                        <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition duration-150 ease-in-out">
                            Sign in
                        </button>
                    </div>
                </form>

                {% if messages %}
                <div class="mt-4 w-full">
                    {% for message in messages %}
                        {% if message.tags == "success" %}
                            <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                                <span class="block sm:inline">{{ message }}</span>
                            </div>
                        {% elif message.tags == "error" %}
                            <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                                <span class="block sm:inline">{{ message }}</span>
                            </div>
                        {% else %}
                            <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                                <span class="block sm:inline">{{ message }}</span>
                            </div>
                        {% endif %}
                    {% endfor %}
                </div>
                {% endif %}

                <div class="text-center mt-4">
                    <p class="text-sm text-black">
                        Don't have an account yet? 
                        <a href="{% url 'main:register' %}" class="font-medium text-indigo-600 hover:text-indigo-800 transition duration-150 ease-in-out">
                            Register Now
                        </a>
                    </p>
                </div>
            </div>
        </main>
    {% endblock content %}
    ```

    8. Membuat `register.html`
    ```html
    {% extends 'base.html' %}
    {% load widget_tweaks %}
    {% block meta %}
    <title>Register</title>
    {% endblock meta %}

    {% block content %}
    {% include 'components/auth/navbar.html' %}
    <div class="flex items-center justify-center min-h-screen px-5 bg-gray-100">
    <div class="shadow-xl bg-white p-5 sm:p-10 rounded-3xl flex flex-col gap-10 items-center border-[2px] border-black/5 w-full max-w-md">
        <h2 class="font-bold text-xl sm:text-2xl text-center text-indigo-700">Ayo Belanja</h2>
        <p class="text-center text-gray-600 text-sm">Create your account to start BELANJA</p>

        <form class="w-full space-y-6" method="POST">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">
        
        <div class="rounded-md shadow-sm space-y-4">
            {% for field in form %}
            <div>
            <label for="{{ field.id_for_label }}" class="block text-sm font-semibold text-gray-700 mb-1">
                {{ field.label }}
            </label>
            <div class="relative">
                {{ field|add_class:"block w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition duration-150 ease-in-out" }}
                {% if field.errors %}
                <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                </svg>
                </div>
                {% endif %}
            </div>
            {% if field.errors %}
            <div class="mt-1 text-sm text-red-600">
                {% for error in field.errors %}
                <p>{{ error }}</p>
                {% endfor %}
            </div>
            {% endif %}
            </div>
            {% endfor %}
        </div>

        <div>
            <button type="submit" class="w-full py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 transition-all duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Register
            </button>
        </div>
        </form>

        {% if messages %}
        <div class="mt-4 w-full">
        {% for message in messages %}
        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
            <span class="block sm:inline">{{ message }}</span>
        </div>
        {% endfor %}
        </div>
        {% endif %}

        <div class="text-center mt-4 w-full">
        <p class="text-sm text-gray-600">
            Already have an account?
            <a href="{% url 'main:login' %}" class="font-medium text-indigo-600 hover:text-indigo-800 transition duration-300">
            Login here
            </a>
        </p>
        </div>
    </div>
    </div>
    {% endblock content %}
    ```

    9. Membuat `card_product.html` yang dapat menampilkan atribut-atribut pada model, menghaous dan mengedit product, serta menambahkannya ke cart.
    ```html
    <div class="max-w-sm rounded overflow-hidden shadow-lg bg-white hover:shadow-xl transition-shadow duration-300 ease-in-out"></div>
    <img class="w-full h-48 object-cover object-center" src="{% if product.image %}{{ product.image.url }}{% else %}https://via.placeholder.com/300x200{% endif %}" alt="{{ product.name }}">
    <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2 text-gray-800">{{ product.name }}</div>
        <p class="text-gray-700 text-base mb-4">{{ product.description|truncatewords:20 }}</p>
        <div class="flex items-center justify-between">
            <span class="text-xl font-bold text-indigo-600">${{ product.price|floatformat:2 }}</span>
            <button class="bg-indigo-500 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-110">
                Add to Cart
            </button>
        </div>
        </div>
        <div class="px-6 pt-4 pb-2">
            <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#category</span>
            <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#tag</span>
        </div>
    </div>
    ```

    10. Memperbaiki tampilan `create_name_entry.html`
    ```python
    {% extends 'base.html' %}
    {% load static %}
    {% load widget_tweaks %}
    {% block meta %}
    <title>Create Product</title>
    {% endblock meta %}

    {% block content %}
    {% include 'components/dashboard/navbar.html' %}

    <div class="flex flex-col min-h-screen bg-gray-100 pt-16">
    <div class="container mx-auto px-4 py-12 max-w-lg"> 
        <h1 class="text-4xl font-extrabold text-center mb-8 text-indigo-700">Create Product</h1>
    
        <div class="bg-white shadow-lg rounded-lg p-8">
        <form method="POST" class="space-y-8">
            {% csrf_token %}
            
            {% for field in form %}
            <div class="flex flex-col space-y-2">
                <label for="{{ field.id_for_label }}" class="text-lg font-semibold text-gray-700">
                {{ field.label }}
                </label>

                <div class="w-full">
                {{ field|add_class:"form-input border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition ease-in-out duration-200" }}
                </div>

                {% if field.help_text %}
                <p class="text-sm text-gray-500">{{ field.help_text }}</p>
                {% endif %}

                {% for error in field.errors %}
                <p class="text-sm text-red-500">{{ error }}</p>
                {% endfor %}
            </div>
            {% endfor %}
            
            <div class="flex justify-center mt-8">
            <button type="submit" class="bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg shadow-lg hover:bg-indigo-700 hover:shadow-xl transition-all duration-300 w-full">
                Create Product
            </button>
            </div>
        </form>
        </div>
    </div>
    </div>

    {% endblock %}

    ```
    11. Memperbaiki tampilan `edit_product.html`
    ```html
    {% extends 'base.html' %}
    {% load static %}
    {% load widget_tweaks %}
    {% block meta %}
    <title>Edit Mood</title>
    {% endblock meta %}

    {% block content %}
    {% include 'components/dashboard/navbar.html' %}

    <div class="flex flex-col min-h-screen bg-gray-100 pt-16">
    <div class="container mx-auto px-4 py-12 max-w-lg">
        <h1 class="text-4xl font-extrabold text-center mb-8 text-indigo-700">Edit Mood Entry</h1>

        <div class="bg-white shadow-md rounded-lg p-8">
        <form method="POST" class="space-y-8">
            {% csrf_token %}
            {% for field in form %}
            <div class="flex flex-col space-y-2">
                <label for="{{ field.id_for_label }}" class="text-lg font-semibold text-gray-700">
                {{ field.label }}
                </label>
                <div class="w-full">
                {{ field|add_class:"form-input border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition ease-in-out duration-200" }}
                </div>

                {% if field.help_text %}
                <p class="text-sm text-gray-500">{{ field.help_text }}</p>
                {% endif %}

                {% for error in field.errors %}
                <p class="text-sm text-red-500">{{ error }}</p>
                {% endfor %}
            </div>
            {% endfor %}

            <div class="flex justify-center mt-8">
            <button type="submit" class="bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg shadow-lg hover:bg-indigo-700 hover:shadow-xl transition-all duration-300 w-full">
                Edit Mood Entry
            </button>
            </div>
        </form>
        </div>
    </div>
    </div>

    {% endblock %}

    ```



## Checklist Tugas
- [x] Implementasikan fungsi untuk menghapus dan mengedit product.
- [x] Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
  - [x] Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
  - [x] Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:
    - [x] Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
    - [x] Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).
  - [x] Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
  - [x] Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.
- [x] Menjawab beberapa pertanyaan berikut pada `README.md` pada root folder (silakan modifikasi `README.md` yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
  - [x] Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
  -  [x] Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
  -  [x] Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
  - [x] Jelaskan konsep flex box dan grid layout beserta kegunaannya!
  - [x] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- [x] Melakukan `add`-`commit`-`push` ke GitHub.


# Tugas 6
## Pertanyaan dan Jawaban
1. **Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!**
    
    **Jawab:**
    - JavaScript memungkinkan pengembang membuat halaman web yang interaktif dan dinamis
    - JavaScript dijalankan di browser pengguna (client-side), yang artinya pemrosesan dan interaksi dapat dilakukan langsung di perangkat pengguna tanpa perlu mengirim data ke server setiap saat.
    - JavaScript memungkinkan pengiriman dan penerimaan data dari server tanpa memuat ulang halaman secara keseluruhan. 
    - JavaScript dapat digunakan untuk menciptakan aplikasi yang lebih responsif dengan mengubah tampilan atau tata letak halaman web sesuai dengan ukuran perangkat. 
    - JavaScript mendukung pembuatan Single Page Applications (SPA), di mana seluruh aplikasi web dimuat dalam satu halaman dan konten diubah secara dinamis tanpa memuat ulang halaman.

2. **Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?**

    **Jawab:**

    Fungsi dari penggunaan `await` ketika kita menggunakan `fetch()` adalah untuk menunggu hingga promise yang dihasilkan oleh `fetch()` selesai diproses (resolved). `fetch()` mengembalikan sebuah promise yang mewakili permintaan asinkron ke server, dan `await` memastikan bahwa kode tidak akan dilanjutkan hingga promise tersebut selesai.

    Jika kita tidak menggunakan `await` atau metode lain untuk menangani promise (seperti `.then()`), JavaScript akan melanjutkan eksekusi kode berikutnya sebelum permintaan selesai. Ini berarti kode yang bergantung pada hasil dari `fetch()` (seperti data yang diambil dari server) bisa jadi dijalankan sebelum data yang diperlukan tersedia.

3. **Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX `POST`?**

    **Jawab:**

    Secara default, Django menyediakan perlindungan CSRF untuk semua permintaan POST agar aplikasi web aman dari serangan CSRF. Namun, dalam beberapa kasus, seperti saat menangani AJAX:
    - Ketika sedang melakukan pengujian atau dalam tahap pengembangan awal, kita mungkin ingin menonaktifkan perlindungan CSRF untuk mempercepat proses pengujian permintaan AJAX. Menggunakan @csrf_exempt akan menonaktifkan sementara validasi token CSRF sehingga kita tidak perlu menambahkan token CSRF pada setiap permintaan POST.
    - Jika kita membuat API yang akan diakses oleh klien yang tidak menggunakan mekanisme CSRF Django, seperti aplikasi mobile atau aplikasi pihak ketiga, kita mungkin perlu menonaktifkan perlindungan CSRF karena aplikasi ini tidak akan mengirimkan token CSRF yang diharapkan Django.
    - Jika permintaan AJAX tidak mengirimkan token CSRF yang sesuai, Django akan menolak permintaan tersebut. Jika kita tidak ingin menangani CSRF dalam permintaan tertentu (misalnya untuk endpoint API yang hanya digunakan di dalam aplikasi kita sendiri), kita dapat menggunakan @csrf_exempt agar Django tidak memeriksa token CSRF pada view tersebut.
    - Ada situasi di mana klien eksternal, seperti layanan pihak ketiga atau aplikasi lain, tidak mendukung atau tidak dapat mengirimkan token CSRF yang diperlukan oleh Django. Dalam kasus ini, menggunakan @csrf_exempt memungkinkan view kita untuk menerima permintaan meskipun tidak ada token CSRF yang valid.


4. **Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?**
    
    **Jawab**

    Validasi dan pembersihan di backend sangat penting karena frontend (client-side) dapat dimanipulasi oleh pengguna. Jika validasi hanya dilakukan di frontend, pengguna yang jahat (malicious user) dapat dengan mudah memodifikasi atau menonaktifkan skrip JavaScript di browser dan mengirim data yang berbahaya langsung ke server

    Validasi di frontend biasanya dilakukan dengan JavaScript atau HTML5, yang meskipun efektif dalam memberikan umpan balik langsung kepada pengguna, memiliki keterbatasan. Beberapa jenis validasi, seperti pemeriksaan unik di database, pemastian referensi antar data (misalnya foreign key), atau validasi kompleks, hanya bisa dilakukan di backend yang memiliki akses penuh ke data di server.

5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**

    **Jawab**
    1. Membuat function add product entry by ajax yang berbeda dari add product yang lainnya.
    ```python
    @login_required(login_url='/login')
    @require_POST
    def add_product_entry_ajax(request):
        try:
            data = json.loads(request.body)
            form = ProductEntryForm(data)
            if form.is_valid():
                product = form.save(commit=False)
                product.user = request.user  
                product.save()
                product_data = {
                    'pk': product.id,
                    'fields': {
                        'name': product.name,
                        'price': product.price,
                        'description': product.description,
                        'time': product.time.strftime('%Y-%m-%d'),
                    }
                }
                return JsonResponse(product_data, status=201)
            else:
                return JsonResponse({'error': form.errors}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    ```
    2. Melakukan routing kembali pada `urls.py` untuk function pada step 1
    ```python
    path('add-product-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
    ```
    3. Menambahkan `strip_tags` untuk pencegahan xss dan clean input setelah seseorang selesai melakukan input pada forms
    ```python
        def clean_name(self):
        name = self.cleaned_data["name"]
        name = strip_tags(name)
        if not name:
            raise ValidationError("Product name cannot be empty.")
        return name

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise ValidationError("Price cannot be negative.")
        return price
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        description = strip_tags(description)
        return description
    ```

    4. Menambahkan script source untuk dompurify
    ```html
    <script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>
    ```

    5. Menambahkan div untuk pembuatan modal/popup yang nantinya terintegrasi dengan function javascript
    ```html
     <div id="product_entry_cards" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6"></div>
    ```

    6. Membuat modal yang nantinya akan ter pop apbila melakukan klik pada suatu button
    ```html
    <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
        <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">

            <div class="flex items-center justify-between p-4 border-b rounded-t">
                <h3 class="text-xl font-semibold text-gray-700">Add New Product</h3>
                <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
                    <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                    </svg>
                    <span class="sr-only">Close modal</span>
                </button>
            </div>
            
            <div class="px-6 py-4 space-y-6">
                <form id="productEntryForm">
                    {% csrf_token %}
                    <div class="mb-4">
                        <label for="name" class="block text-sm font-medium text-gray-700">Product Name</label>
                        <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter product name" required>
                    </div>
                    <div class="mb-4">
                        <label for="price" class="block text-sm font-medium text-gray-700">Price ($)</label>
                        <input type="number" id="price" name="price" min="0" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter product price" required>
                    </div>
                    <div class="mb-4">
                        <label for="description" class="block text-sm font-medium text-gray-700">Description</label>
                        <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-32 resize-none border border-gray-300 rounded-md p-2 hover:border-indigo-700" placeholder="Enter product description" required></textarea>
                    </div>
          
                    <div id="formError" class="text-red-500 text-sm hidden"></div>
                </form>
            </div>
        
       
            <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">
                <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
                <button type="submit" id="submitProductEntry" form="productEntryForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>
            </div>
        </div>
    </div>
    ```

    7. Membuat 2 button untuk memisahkan penggunaan modal dan `create_name_entry.html`
    ```html
    
    <div class="mt-8 space-x-4 text-center">
        <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-3 px-6 rounded-lg shadow-lg hover:shadow-xl transition-all duration-300 ease-in-out transform hover:-translate-y-1" onclick="showModal();">
            Add New Product Entry by AJAX
        </button>
        <a href="{% url 'main:create_name_entry' %}" class="btn inline-block bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-3 px-6 rounded-lg shadow-lg hover:shadow-xl transition-all duration-300 ease-in-out transform hover:-translate-y-1">
            Create Product
        </a>
    </div>
    ```

    8. Membuat getCSRFtoken
    ```python
        function getCSRFToken() {
        const csrfTokenInput = document.querySelector('#productEntryForm input[name="csrfmiddlewaretoken"]');
        if (csrfTokenInput) {
            return csrfTokenInput.value;
        } else {
            console.error("CSRF token not found!");
            return '';
        }
    }
    ```
    9. Membuat inisiasi id dan function untuk edit dan delete product
    ```python
        const editProductBaseURL = "{% url 'main:edit_product' '00000000-0000-0000-0000-000000000000' %}";
    const deleteProductBaseURL = "{% url 'main:delete_product' '00000000-0000-0000-0000-000000000000' %}";

    function getEditProductURL(id) {
        return editProductBaseURL.replace('00000000-0000-0000-0000-000000000000', id);
    }

    function getDeleteProductURL(id) {
        return deleteProductBaseURL.replace('00000000-0000-0000-0000-000000000000', id);
    }
    ```

    10. Membuat get product entries
    ```python
    async function getProductEntries(){
        try {
            const response = await fetch("{% url 'main:show_json' %}", {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'  
                }
            });
            if (!response.ok) throw new Error('Network response was not ok');
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error fetching product entries:', error);
            return [];
        }
    }
    ```

    10. Membuat render product card untuk menampilkan card yang sudah dibuat dari hasil ajax
    ```python
    function renderProductCard(product) {
        const name = DOMPurify.sanitize(product.fields.name);
        const price = parseFloat(DOMPurify.sanitize(product.fields.price));
        const description = DOMPurify.sanitize(product.fields.description);
        const time = new Date(product.fields.time).toLocaleDateString();
        const id = product.pk;
        const imageUrl = 'https://via.placeholder.com/300x200'; 

        return `
        <div class="max-w-sm rounded overflow-hidden shadow-lg bg-white hover:shadow-xl transition-shadow duration-300 ease-in-out flex flex-col">
            <img class="w-full h-48 object-cover object-center" src="${imageUrl}" alt="${name}">
            <div class="px-6 py-4 flex-grow">
                <div class="font-bold text-xl mb-2 text-gray-800">${name}</div>
                <p class="text-gray-600 text-sm mb-2">Added: ${time}</p>
                <p class="text-gray-700 text-base mb-4">${description.length > 100 ? description.substring(0, 100) + '...' : description}</p>
                <div class="flex items-center justify-between mb-4">
                    <span class="text-xl font-bold text-indigo-600">$${price.toFixed(2)}</span>
                </div>
            </div>
            <div class="flex justify-center space-x-4 mb-4">
                <a href="${getEditProductURL(id)}" class="bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
                    Edit
                </a>
                <a href="${getDeleteProductURL(id)}" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
                    Delete
                </a>
            </div>
        </div>
        `;
    }
    ```

    11. Melakukan refresh product secara asynchronus
    ```python
    async function refreshProductEntries() {
        const productContainer = document.getElementById("product_entry_cards");
        productContainer.innerHTML = ""; 

        const productEntries = await getProductEntries();
        
        if (productEntries.length === 0) {
            productContainer.innerHTML = `
            <div class="col-span-full flex flex-col items-center justify-center">
                <img src="{% static 'image/no-product.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada product pada Ayo Belanja.</p>
            </div>
            `;
            return;
        }

        else {
            productEntries.forEach((product) => {
                productContainer.innerHTML += renderProductCard(product);
            });
        }
    }
    ```

    12. Melakukan penambahan/add product entry
    ```python
        async function addProductEntry() {
        const form = document.getElementById("productEntryForm");
        if (!form) {
            console.error("Form with id 'productEntryForm' not found!");
            return;
        }

        const nameInput = form.querySelector('input[name="name"]');
        const priceInput = form.querySelector('input[name="price"]');
        const descriptionInput = form.querySelector('textarea[name="description"]');
        const errorContainer = document.getElementById("formError");

        if (!nameInput || !priceInput || !descriptionInput) {
            console.error("One or more form inputs not found!");
            return;
        }

        const name = DOMPurify.sanitize(nameInput.value.trim());
        const price = parseFloat(DOMPurify.sanitize(priceInput.value.trim()));
        const description = DOMPurify.sanitize(descriptionInput.value.trim());

        errorContainer.classList.add('hidden');
        errorContainer.innerText = '';

        if (!name || isNaN(price) || !description) {
            errorContainer.innerText = "All fields are required and price must be a number!";
            errorContainer.classList.remove('hidden');
            return;
        }

        const data = {
            name: name,
            price: price,
            description: description,
        };

        try {
            const response = await fetch("{% url 'main:add_product_entry_ajax' %}", {
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),
                    'X-Requested-With': 'XMLHttpRequest'  
                },
                body: JSON.stringify(data)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(Object.values(errorData.error).flat().join(', ') || 'Network response was not ok');
            }

            const newProduct = await response.json();

            const productContainer = document.getElementById("product_entry_cards");
            productContainer.innerHTML += renderProductCard(newProduct);

            hideModal();
            form.reset();
        } catch (error) {
            console.error('Error adding product entry:', error);
            errorContainer.innerText = error.message;
            errorContainer.classList.remove('hidden');
        }
    }
    ```

    13. Membuat function untuk menampilkan ataupun menyembunyikan modal
    ```python
       document.addEventListener('DOMContentLoaded', () => {
        refreshProductEntries();
    });

    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    function showModal() {
        modal.classList.remove('hidden'); 
        setTimeout(() => {
            modalContent.classList.remove('opacity-0', 'scale-95');
            modalContent.classList.add('opacity-100', 'scale-100');
        }, 50); 
    }

    function hideModal() {
        modalContent.classList.remove('opacity-100', 'scale-100');
        modalContent.classList.add('opacity-0', 'scale-95');

        setTimeout(() => {
            modal.classList.add('hidden');
        }, 150); 
    }

    document.getElementById("cancelButton").addEventListener("click", hideModal);
    document.getElementById("closeModalBtn").addEventListener("click", hideModal);

    document.getElementById("productEntryForm").addEventListener("submit", (e) => {
        e.preventDefault();
        addProductEntry();
    });
    ```





## Checklist Tugas
- [x] Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.
  - [x] AJAX `GET`
    - [x] Ubahlah kode `cards` data mood agar dapat mendukung AJAX `GET`.
    - [x] Lakukan pengambilan data mood menggunakan AJAX `GET`. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in.
  - [x] AJAX `POST`
    - [x] Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan mood.
    - [x] Buatlah fungsi view baru untuk menambahkan mood baru ke dalam basis data.
    - [x] Buatlah path `/create-ajax/` yang mengarah ke fungsi view yang baru kamu buat.
    - [x] Hubungkan form yang telah kamu buat di dalam modal kamu ke path `/create-ajax/`.
    - [x] Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar mood terbaru tanpa reload halaman utama secara keseluruhan.
- [x] Menjawab beberapa pertanyaan berikut pada `README.md` pada root folder (silakan modifikasi `README.md` yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).
  - [x] Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
  - [x]  Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?
  - [x]  Mengapa kita perlu menggunakan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX `POST`?
  - [x] Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
  - [x] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- [x] Melakukan `add`-`commit`-`push` ke GitHub.
