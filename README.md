# Ayo Belanja
E-commerce terbaik untuk segala kalangan umur

- [Profile](#profile)
- [Deployment](#deployment)
- [Tugas 2](#tugas-2)
- [Tugas 3](#tugas-3)
- [Tugas 4](#tugas-4)

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
| JSON       | ![JSON](https://github.com/anthef/eshop-pbp/blob/main/screenshot_post/json.png) |
| XML        | ![XML](https://github.com/anthef/eshop-pbp/blob/main/screenshot_post/xml.png) |
| JSON_ID    | ![JSON_ID](https://github.com/anthef/eshop-pbp/blob/main/screenshot_post/json_id.png) |
| XML_ID     | ![XML_ID](https://github.com/anthef/eshop-pbp/blob/main/screenshot_post/xml_id.png) |


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
    Authentication di Django ditangani melalui sistem otentikasi bawaan (`django.contrib.auth`). Built-in sistem tersebut akan memverifikasi kredensial pengguna menggunakan metode seperti `authenticate()` dan ``login()`.

    Authorization dikelola melalui izin dan grup. Setelah otentikasi, Django memeriksa izin pengguna (misalnya, menggunakan `user.has_perm()`) untuk menentukan apakah mereka berwenang untuk melakukan tindakan tertentu.

4. **Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**

    **Jawab:**

5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

    **Jawab:**




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

