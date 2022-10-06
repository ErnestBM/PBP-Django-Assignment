Tugas 4
Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
Berdasarkan https://owasp.org/www-community/attacks/csrf, Cross-Site Request Forgery adalah serangan yang memaksa pengguna akhir untuk 
melakukan tindakan yang tidak diinginkan pada aplikasi web tempat mereka saat ini diautentikasi. Dengan sedikit bantuan rekayasa sosial 
(seperti mengirim tautan melalui email atau obrolan), penyerang dapat mengelabui pengguna aplikasi web untuk menjalankan tindakan yang 
dipilih penyerang. Jika korbannya adalah pengguna biasa, serangan CSRF yang berhasil dapat memaksa pengguna untuk melakukan permintaan 
perubahan status seperti mentransfer dana, mengubah alamat email, dan sebagainya. Jika korban adalah akun administratif, CSRF dapat membahayakan 
seluruh aplikasi web.
Django memiliki tag {% csrf_token %} yang diimplementasikan untuk menghindari serangan berbahaya. Ini menciptakan token di sisi server saat 
merender halaman dan memastikan untuk memeriksa ulang token ini untuk setiap permintaan yang masuk kembali. Jika permintaan yang masuk tidak 
berisi token, permintaan tersebut tidak dijalankan.


Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? 
Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Secara manual, proses pembuatan form secara manual dapat dilakukan dengan menggunakan tag. Beberapa tag dasar yang umum digunakan adalah tag 
form, input, dan select. Setelah membuat struktur tag, pengembang dapat menentukan atribut method dan action dengan valuenya yang sesuai. 
Selanjutnya, elemen-elemen tersebut perlu dimasukkan ke dalam wrapper dan tipe input juga perlu dipilih. Atribut lain yang mungkin diperlukan 
adalah adalah name. Langkah terakhir adalah pembuatan elemen button yang diperlukan untuk menandakan submisi form yang telah dibuat.
  
  
Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang 
telah disimpan pada template HTML.
Browser memberikan respon dengan mengirm POST ke server setelah user membuat request dengan cara menekan button 
login, register, tambah task. Lalu, akan terjadi perubahan pada server dengan adanya event POST. 
Selanjutnya, fungsi-fungsi pada file views.py akan merespon dengan mengembalikan atau 
mengupdate data dengan melakukan user redirect ke views sebelumnya sehingga tampilan akan mengupdate data baru.
  

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat aplikasi baru bernama todolist dengan menjalankan perintah python manage.py startapp todolist

2. Mendaftarkan aplikasi ke dalam INSTALLED_APPS di file settings.py

3. Membuat model dalam file models.py pada folder todolist dengan variabel user, date, title, dan description

4. Menjalankan perintah makemigrations dan migrate

5. Membuat fungsi-fungsi yang dibutuhkan pada views.py:

    def register(request):
        ......
    def login_user(request):
        ......
    def logout_user(request):
        ......
    @login_required(login_url='/todolist/login/')
    def create(request):
        ......

6. Membuat folder template di dalam folder todolist berisi file-file html yang dibutuhkan menampilkan data

7. Tambahkan path url dengan membuat file urls.py di dalam folder todolist dan isi dengan path untuk melakukan routing ke fungsi-fungsi yang ada fi views.py

    from django.urls import path
    from todolist.views import delete, register, login_user, logout_user, show_todos, create, delete

    app_name = 'todolist'

    urlpatterns = [
        path('', show_todos, name='show_todos'),
        path('create/', create,  name='create'),
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
                  ]
  
8. Daftarkan app todolist ke dalam url pattern pada file urls.py di folder project_django

    urlpatterns = [
    .........,
    path('todolist/', include('todolist.urls')),
    .........,
    ]
  
  
Sekian terima kasih.



Tugas 5
Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Inline CSS menyematkan setting elemen tepat setelah men-declare objek yang dibuat. Styling dengan inline CSS dapat dilakuk dengan menambahkan atribut style ke tag HTML. Tipe ini dapat membantu pemahaman kode karena styling ditempatkan tepat di sebelah deklarasi objek, namun cenderung tidak efisien karena setiap objek perlu di-style satu per satu.
Internal CSS membuat setting styling di file yang sama, namun tidak tepat di sebelah objek yang dibuat. Alhasil, programmer tidak perlu menuliskan styling yang sama setiap kali membuat objek, namun juga meningkatkan running time dari program tersebut. 
Mirip dengan Internal CSS, External CSS juga membuat setting styling dari tiap elemen di luar pembuatan objek. Bedanya, tipe ini menyematkan styling di luar file html. Maka dari itu, file html akan terlihat lebih rapi, namun berpotensi menimbulkan error pada webpage karena styling CSS berada di luar file html.

Jelaskan tag HTML5 yang kamu ketahui!
- <h1> - <h4>     : Font header pada teks
- <a>             : Me-link objek HTML ke sebuat tautan
- <p>             : Membuat format paragraf
- <style>         : Menerapkan CSS styling pada tipe Internal CSS

Jelaskan tipe-tipe CSS selector yang kamu ketahui!
- CSS ID Selector : selector yang mengenakan karakter # dan dilanjutkan dengan nama elemen
- CSS Element Selector : selector yang memilih elemen berdasarkan nama tag HTML yang dideklarasi
- CSS Class Selector : selector yang mengenakan karakter . dan dilanjutkan dengan nama class

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
Pada masing-masing file html, saya membuat styling CSS dengan tipe Internal CSS. Setelah mendeskripsikan setiap class, saya mulai mengimplementasikan styling pada bagian logika utama dari file html yang tertaut pada file views.py. Saya mengulangi langkah-langkah tersebut untuk file login.html, register.html, create_task.html, dan todolist.html.
