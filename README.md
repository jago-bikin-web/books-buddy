![Deploy](https://github.com/jago-bikin-web/books-buddy/actions/workflows/pbp-deploy.yml/badge.svg)
<hr/>
# TUGAS KELOMPOK PROYEK TENGAH SEMESTER PEMROGRAMAN BERBASIS PLATFORM :computer:

### Kelompok E06:
  1. **Restu Ahmad Ar Ridho - 2206028951**
  2. **Nadhira Widyaniswari - 2206811884**
  3. **Gamma Farrel - 2206025035**
  4. **Daffa Mohamad Fathoni - 2206824161**


## Books Buddy (BB) :books:

**Books Buddy** merupakan sebuah aplikasi yang dirancang untuk mendukung gerakan Indonesia membaca dengan menyediakan fitur yang dapat memudahkan pengguna untuk mencari, mengelola dan berbagi informasi mengenai buku sesama pengguna aplikasi. Books Buddy juga memfasilitasi pengguna dengan memberi informasi mengenai kegiatan-kegiatan yang ingin diadakan untuk dipublikasikan di dalam aplikasi sehingga pengguna dapat menemukan kegiatan yang menarik sesuai dengan minatnya.

Pada awal **Landing Page**, pengguna akan diarahkan untuk Sign Up akun baru. Saat proses pembuatan akun tersebut, pengguna akan diminta untuk memilih Role untuk akun tersebut. Perincian masing-masing Role adalah sebagai berikut:


## Role :point_up:

|Reguler User |Member User |
| --- | --- |
| Pengguna reguler hanya memiliki akses pada fitur MyBuddy, FindBuddy, dan melakukan RSVP pada EventBuddy. Reguler User tidak dapat mengakses ReachBuddy (membuat forum) dan menambah event pada EventBuddy.| Member User merupakan versi lebih lengkap dari Reguler User yang hanya dapat mengakses beberapa modul. Member User dapat bergabung dengan komunitas ReachBuddy, dimana Member User dapat berdiskusi antar sesama Member User. Member User juga dapat menambahkan informasi mengenai kegiatan dan membuka RSVP bagi Reguler User maupun Member User jika ingin mengikuti suatu kegiatan.|

## Features

Adapun fitur utama dalam aplikasi ini adalah sebagai berikut:

**Landing Page**:
1. Welcoming
2. Description
3. Login & Sign Up

**Home Page**:
1. Welcoming
2. Description
4. Moduls (MyBuddy, FindBuddy, ReachBuddy, EventBuddy)
5. FAQ

## Moduls

### 1. MyBuddy :school_satchel: (Koleksi Buku):
Pada modul “MyBuddy” pengguna dengan mudah melacak dan mengelola koleksi buku pribadinya. Pengguna dapat memfilter koleksi bukunya sesuai keinginan seperti buku yang dimiliki, yang ingin dibaca, dan sedang dibaca. Pada setiap buku terdapat informasi mengenai judul buku dan ulasan yang diberikan oleh pengguna serta track page.

#### Reguler User dan Member User 
Pengguna yang telah masuk ke dalam aplikasi dapat menyimpan koleksi bukunya secara pribadi untuk dibaca pada lain kesempatan.


### 2. FindBuddy :mag_right: (Jelajahi Dunia Buku):
Dengan menggunakan API, "FindBuddy" akan menampilkan buku buku yang terdapat pada API yang digunakan sehingga memungkinkan pengguna menjelajahi banyak buku dengan mudah. Pengguna dapat mencari buku berdasarkan berbagai kriteria seperti judul, penulis, atau genre. Informasi seperti deskripsi buku dan sampulnya akan membantu pengguna memilih buku yang tepat dan dapat menambahkan kedalam modul “MyBuddy”.

#### Reguler User dan Member User
Pengguna yang telah masuk ke dalam aplikasi dapat mencari buku sesuai dengan minat pengguna.


### 3. ReachBuddy :incoming_envelope: (Berkomunikasi dalam Komunitas Pembaca): 
Pada modul “ReachBuddy", pengguna dapat mengeksplorasi dan bertemu dengan komunitas pembaca yang ada. Setiap pengguna akan bertukar wawasan terkait bukunya yang ingin dibahas. Pada postingan tersebut akan ditampilkan detail buku yang diulas, dan pengguna yang melihat postingan tersebut dapat melihat buku tersebut sehingga memunculkan informasi buku tersebut.

#### Member User
Pengguna yang menjadi bagian dari komunitas dapat mengakses dan membuat postingan berisi ulasan, komentar, ataupun kritik terhadap buku yang dipilih pada modul “ReachBuddy” ini.


### 4. EventBuddy :date: (Jadwalkan dan Daftar Acara Buku):
Dengan “EventBuddy”, pengguna berkesempatan mengikuti kegiatan dengan tema literasi dan buku yang mengagumkan. Pengguna dapat mencari acara buku menarik di berbagai tempat dan mendaftar untuk menghadirinya. Informasi lengkap tentang deskripsi acara, tanggal, lokasi, tema, dan buku yang akan dibahas atau ditampilkan akan membuat pengguna selalu siap untuk acara berikutnya.

|Reguler User|Member User|
| --- | --- |
|Pengguna yang telah masuk ke dalam aplikasi dapat mendaftarkan diri mengikuti kegiatan yang akan dilaksanakan.| Pengguna yang merupakan bagian dari komunitas dapat menambahkan acara kegiatan yang berkaitan dengan buku dan dapat melihat daftar peserta yang terdaftar pada acara tertentu.|

<hr>

Aplikasi ini dirancang untuk memberdayakan pembaca untuk lebih mendalam dalam eksplorasi buku, terhubung dengan komunitas pembaca, dan berpartisipasi dalam banyak acara yang akan menginspirasi pengguna. Dengan apikasi ini, kami berharap pengguna dapat terpicu untuk ikut serta dalam gerakan membaca buku di Indonesia. Selamat datang di aplikasi kami!

#### **Pembagian peran** dalam mengerjakan modul masing-masing adalah sebagai berikut:
1. **My Buddy** - Restu Ahmad Ar Ridho
2. **Find Buddy** - Gamma Farrel
3. **Reach Buddy** - Daffa Mohamad Fathoni
4. **Event Buddy** - Nadhira Widyaniswari

Sumber Data Set Buku: **Google Books API**

Adapun **Flow Chart** untuk aplikasi ini sebagai berikut:
![flowchart](./static/img/flowchart.jpg)
