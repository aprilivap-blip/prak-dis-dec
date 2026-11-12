# Laporan Praktikum 07

## Identitas

- **Nama:** Apriliva Putri P
- **NIM:** 255410035
- **Kelas:** Informatika-1
- **Mata kuliah:** Praktikum Sistem Terdistribusi dan Terdesentralisasi

# LAPORAN PRAKTIKUM SISTEM TERDISTRIBUSI DAN TERDESENTRALISASI
## MODUL 7 – CLOUD COMPUTING

# 1. TUJUAN PEMBELAJARAN

Setelah melaksanakan praktikum Modul 7 tentang Cloud Computing, mahasiswa diharapkan mampu:

1. Memahami konsep dasar Cloud Computing dan penerapan layanan XaaS (Everything as a Service).
2. Mengetahui perbedaan layanan SaaS (Software as a Service), PaaS (Platform as a Service), dan IaaS (Infrastructure as a Service).
3. Memahami konsep Containerized Application sebagai aplikasi yang dijalankan menggunakan teknologi container.
4. Membuat dan menjalankan aplikasi berbasis Flask menggunakan bahasa pemrograman Python.
5. Membuat image aplikasi menggunakan Dockerfile dengan bantuan Docker dan Podman.
6. Menjalankan aplikasi dalam container serta melakukan pemetaan port agar aplikasi dapat diakses melalui browser.

# 2. DASAR TEORI

## 2.1 Cloud Computing

Cloud Computing merupakan teknologi yang memungkinkan pengguna memanfaatkan sumber daya komputasi melalui jaringan internet tanpa harus menyediakan dan mengelola seluruh infrastruktur secara mandiri. Sumber daya tersebut dapat berupa perangkat lunak, platform pengembangan, maupun infrastruktur server. Dalam penerapannya, penyedia layanan cloud menyediakan berbagai kebutuhan komputasi dalam bentuk layanan yang dapat digunakan sesuai kebutuhan pengguna.

## 2.2 Everything as a Service (XaaS)

Everything as a Service atau XaaS merupakan pendekatan dalam Cloud Computing yang menyediakan berbagai sumber daya komputasi dalam bentuk layanan. Melalui pendekatan ini, pengguna dapat memanfaatkan layanan yang disediakan oleh penyedia cloud tanpa harus membangun seluruh sistem sendiri. Secara umum, XaaS dibagi menjadi tiga kategori, yaitu SaaS, PaaS, dan IaaS.

### a. Software as a Service (SaaS)

Software as a Service merupakan layanan yang menyediakan perangkat lunak melalui jaringan internet. Pengguna dapat menggunakan aplikasi secara langsung tanpa perlu melakukan instalasi dan pemeliharaan sistem secara menyeluruh. Contohnya adalah Google Workspace yang menyediakan layanan seperti Google Docs, Google Sheets, dan Google Drive.

### b. Platform as a Service (PaaS)

Platform as a Service merupakan layanan yang menyediakan lingkungan untuk mengembangkan, menjalankan, dan mengelola aplikasi. Pengembang dapat menggunakan platform yang tersedia tanpa harus mengatur infrastruktur server secara langsung. Salah satu contohnya adalah Heroku yang menyediakan platform untuk melakukan deployment aplikasi.

### c. Infrastructure as a Service (IaaS)

Infrastructure as a Service merupakan layanan yang menyediakan sumber daya komputasi berupa server virtual, penyimpanan, dan jaringan melalui internet. Pengguna dapat mengatur sistem operasi dan aplikasi sesuai kebutuhan. Salah satu contohnya adalah Amazon Web Services (AWS) melalui layanan Amazon EC2.

## 2.3 Containerized Application

Containerized Application merupakan aplikasi yang dikemas dalam sebuah container agar dapat dijalankan pada lingkungan komputasi yang mendukung teknologi container. Container berisi aplikasi beserta kebutuhan pendukungnya sehingga proses pemindahan dan pengoperasian aplikasi menjadi lebih mudah. Teknologi ini dapat membantu menjaga konsistensi lingkungan aplikasi ketika dijalankan pada perangkat yang berbeda.

## 2.4 Flask

Flask merupakan framework berbasis Python yang digunakan untuk membangun aplikasi web. Flask memiliki struktur yang sederhana dan fleksibel sehingga dapat digunakan untuk membuat aplikasi web dengan kebutuhan yang berbeda. Dalam praktikum ini, Flask digunakan untuk menjalankan aplikasi blog yang kemudian dikemas menjadi container.

## 2.5 Docker

Docker merupakan platform yang digunakan untuk membangun, mengemas, dan menjalankan aplikasi dalam container. Docker menggunakan Dockerfile sebagai instruksi untuk membangun image yang berisi aplikasi dan seluruh kebutuhan pendukungnya. Image tersebut kemudian dapat dijalankan menjadi container sehingga aplikasi dapat digunakan dalam lingkungan yang terisolasi.

## 2.6 Podman

Podman merupakan perangkat pengelola container yang dapat digunakan untuk membangun dan menjalankan container. Podman dapat menggunakan Dockerfile sehingga proses pembuatan image dapat dilakukan dengan instruksi yang sama seperti pada Docker. Salah satu karakteristik Podman adalah kemampuannya menjalankan container tanpa harus menggunakan daemon Docker secara khusus.

## 2.7 Dockerfile dan Container Image

Dockerfile merupakan file yang berisi serangkaian instruksi untuk membangun sebuah container image. Instruksi di dalamnya dapat digunakan untuk menentukan image dasar, membuat direktori kerja, menyalin file aplikasi, memasang paket yang dibutuhkan, serta menentukan perintah yang dijalankan ketika container dimulai.

Container image merupakan hasil dari proses build yang digunakan sebagai dasar untuk membuat dan menjalankan container.

# 3. ALAT DAN BAHAN

Alat dan bahan yang digunakan dalam praktikum ini meliputi:

1. Laptop atau komputer dengan sistem operasi Windows.
2. Visual Studio Code sebagai editor kode dan terminal.
3. Ubuntu WSL2 sebagai lingkungan Linux.
4. Python versi 3.14.4.
5. uv sebagai pengelola environment dan paket Python.
6. Git untuk mengambil source code dari repository.
7. Docker untuk membangun dan menjalankan container.
8. Podman untuk membangun dan menjalankan container.
9. Browser untuk mengakses aplikasi Flask.

# 4. LANGKAH KERJA DAN PEMBAHASAN

## 4.1 Pemeriksaan Instalasi Perangkat Lunak

Sebelum memulai praktikum, dilakukan pemeriksaan terhadap perangkat lunak yang dibutuhkan. Pemeriksaan dilakukan melalui terminal Ubuntu WSL2 yang tersedia pada Visual Studio Code.

**Langkah 1. Pemeriksaan versi Python**

Perintah:

<img src="Images/01.png" width="700">

Berdasarkan perintah tersebut, terminal menampilkan versi Python yang terpasang pada sistem. Pemeriksaan ini dilakukan untuk memastikan Python telah tersedia dan dapat digunakan sebagai bahasa pemrograman dalam menjalankan aplikasi Flask.

**Langkah 2. Pemeriksaan versi uv**

Perintah:

<img src="Images/02.png" width="700">

Perintah tersebut digunakan untuk mengetahui versi uv yang terpasang. uv digunakan dalam praktikum ini untuk membuat environment Python dan memasang paket yang dibutuhkan oleh aplikasi.

**Langkah 3. Pemeriksaan versi Git**

Perintah:

<img src="Images/03.png" width="700">

Pemeriksaan Git dilakukan untuk memastikan perangkat lunak pengelola repository telah tersedia. Git nantinya digunakan untuk mengambil source code Flask dari GitHub.

**Langkah 4. Pemeriksaan versi Docker**

Perintah:

<img src="Images/04.png" width="700">

Perintah tersebut digunakan untuk mengetahui versi Docker yang telah terpasang. Docker akan digunakan untuk membangun image dan menjalankan aplikasi Flask dalam container.

**Langkah 5. Pemeriksaan versi Podman**

Perintah:

<img src="Images/05.png" width="700">

Pemeriksaan dilakukan untuk mengetahui versi Podman yang digunakan. Podman menjadi alternatif dalam proses pembuatan dan pengoperasian container pada praktikum ini.

## 4.2 Mengambil Source Code Flask

Pada tahap ini dilakukan pengambilan source code Flask dari repository GitHub. Source code tersebut digunakan sebagai dasar pembuatan aplikasi blog yang nantinya akan dijalankan menggunakan container.

**Langkah 1. Membuat direktori penyimpanan repository**

Perintah:

<img src="Images/06.png" width="700">

Perintah tersebut digunakan untuk membuat direktori bernama `src` pada direktori utama pengguna. Direktori ini berfungsi sebagai tempat penyimpanan repository yang akan diunduh. Opsi `-p` digunakan agar direktori tidak menimbulkan kesalahan apabila sebelumnya sudah tersedia.

**Langkah 2. Masuk ke direktori src**

Perintah:

<img src="Images/07.png" width="700">

Perintah `cd` digunakan untuk berpindah ke direktori `src` yang telah dibuat sebelumnya. Proses pengunduhan repository dilakukan dari direktori tersebut agar susunan file lebih terorganisasi.

**Langkah 3. Mengunduh repository Flask**

Perintah:

<img src="Images/08.png" width="700">

Perintah tersebut digunakan untuk mengunduh seluruh source code Flask dari GitHub ke dalam komputer. Repository yang diunduh akan tersimpan dalam direktori bernama `flask`. Source code ini nantinya digunakan untuk mengambil contoh aplikasi tutorial yang telah disediakan oleh pengembang Flask. Tapi diterminal terlihat tulisan fatal karena folder repository Flask sudah tersedia di ~/src/flask jadi tidak perlu clone ulang.

**Langkah 4. Menyalin folder tutorial Flask**

Perintah:

<img src="Images/09.png" width="700">

Perintah tersebut digunakan untuk menyalin direktori `tutorial` yang berada di dalam repository Flask ke direktori praktikum dengan nama `flask-app`. Opsi `-R` digunakan agar seluruh isi direktori beserta subdirektorinya ikut disalin. Folder tersebut berisi source code aplikasi blog yang akan digunakan pada tahap berikutnya.

**Langkah 5. Masuk ke direktori aplikasi**

Perintah:

<img src="Images/10.png" width="700">

Perintah tersebut digunakan untuk masuk ke direktori `flask-app`. Seluruh proses konfigurasi, instalasi paket, dan pembuatan container selanjutnya dilakukan dari direktori ini.

**Langkah 6. Memeriksa isi direktori aplikasi**

Perintah:

<img src="Images/11.png" width="700">

Perintah `ls -la` digunakan untuk menampilkan seluruh file dan folder yang terdapat pada direktori aplikasi, termasuk file tersembunyi. Pemeriksaan ini dilakukan untuk memastikan source code Flask telah berhasil disalin dan file konfigurasi yang diperlukan tersedia.

## 4.3 Membuat Environment Python

Setelah source code tersedia, tahap selanjutnya adalah membuat environment Python sesuai ketentuan modul, yaitu menggunakan Python versi 3.14.4. Environment digunakan agar kebutuhan paket aplikasi dapat dikelola secara terpisah.

**Langkah 1. Memastikan Python 3.14.4 tersedia**

Perintah:

<img src="Images/12.png" width="700">

Perintah tersebut digunakan untuk menyediakan Python versi 3.14.4 melalui uv. Apabila versi tersebut sudah tersedia, uv akan menggunakan instalasi yang ada sehingga tidak perlu mengunduhnya kembali.

**Langkah 2. Membuat virtual environment**

Perintah:

<img src="Images/13.png" width="700">

Perintah tersebut digunakan untuk membuat virtual environment menggunakan Python versi 3.14.4. Secara default, environment akan dibuat dalam direktori `.venv`. Environment ini berfungsi untuk memisahkan paket yang digunakan oleh aplikasi Flask dari instalasi Python utama.

**Langkah 3. Mengaktifkan virtual environment**

Perintah:

<img src="Images/14.png" width="700">

Perintah tersebut digunakan untuk mengaktifkan virtual environment yang telah dibuat. Apabila berhasil, biasanya nama environment akan muncul pada bagian awal prompt terminal. Dengan demikian, perintah Python dan instalasi paket selanjutnya menggunakan environment tersebut.

## 4.4 Menginstal Paket yang Diperlukan

Setelah environment aktif, dilakukan pemasangan paket yang dibutuhkan oleh aplikasi Flask.

Perintah:

<img src="Images/15.png" width="700">

Perintah tersebut digunakan untuk memasang paket aplikasi berdasarkan konfigurasi yang terdapat pada file `pyproject.toml`. Opsi `-e` menunjukkan bahwa instalasi dilakukan dalam mode editable sehingga perubahan pada source code lokal dapat digunakan tanpa harus memasang ulang paket setiap kali terjadi perubahan.

## 4.5 Menjalankan Aplikasi Flask

Setelah proses instalasi selesai, aplikasi perlu diinisialisasi sebelum dijalankan. Tahap ini bertujuan untuk mempersiapkan database yang digunakan oleh aplikasi blog.

**Langkah 1. Inisialisasi database**

Perintah:

<img src="Images/16.png" width="700">

Perintah tersebut digunakan untuk menjalankan perintah inisialisasi database pada aplikasi Flask. Proses ini mempersiapkan database yang dibutuhkan agar aplikasi dapat menyimpan dan mengelola data.

**Langkah 2. Menjalankan aplikasi Flask**

Perintah:

<img src="Images/17.png" width="700">

Perintah tersebut digunakan untuk menjalankan aplikasi Flask menggunakan development server bawaan. Secara default, aplikasi dapat diakses melalui alamat lokal `http://127.0.0.1:5000`.

**Langkah 3. Mengakses aplikasi melalui browser**

Buka browser dan masukkan alamat:

<img src="Images/18.png" width="700">

Berdasarkan tampilan browser, aplikasi blog Flask dapat diperiksa melalui halaman utama yang menampilkan bagian Posts serta menu Register dan Log In. Pada tahap ini, menu Register dapat digunakan untuk mencoba membuat akun, kemudian dilanjutkan dengan menu Log In untuk menguji proses masuk ke aplikasi.

Untuk menghentikan server Flask, tekan `CTRL + C` pada terminal.

## 4.6 Membuat Containerized Application Menggunakan Docker

Pada tahap ini aplikasi Flask yang sebelumnya dijalankan secara langsung akan dikemas menjadi container image menggunakan Docker. Proses pembuatan image dilakukan dengan menggunakan file Dockerfile.

**Langkah 1. Membuat file Dockerfile**

Buat file baru dengan nama `Dockerfile` pada direktori utama `flask-app`.

Isi file:

<img src="Images/19.png" width="700">

Dockerfile tersebut berisi instruksi yang digunakan untuk membangun image aplikasi Flask. Instruksi `FROM` menentukan image Python sebagai dasar pembuatan container. `RUN mkdir /app` digunakan untuk membuat direktori aplikasi, sedangkan `WORKDIR /app` menentukan direktori kerja di dalam container. Instruksi `ADD` digunakan untuk menyalin file aplikasi ke dalam container.

Selanjutnya, `RUN pip install -e .` digunakan untuk memasang paket aplikasi, sedangkan `RUN flask --app flaskr init-db` digunakan untuk menginisialisasi database. Instruksi `EXPOSE 5000` menunjukkan port yang digunakan aplikasi, dan `CMD` menentukan perintah yang dijalankan ketika container dimulai.

**Langkah 2. Memastikan Docker dapat digunakan**

Pada Windows, Docker Desktop harus dalam keadaan berjalan dan integrasi WSL2 harus aktif.

Perintah pemeriksaan:

<img src="Images/20.png" width="700">

Perintah tersebut digunakan untuk memeriksa informasi Docker, termasuk konfigurasi client dan server. Pemeriksaan ini memastikan Docker dapat berkomunikasi dengan engine yang digunakan untuk membangun dan menjalankan container.

**Langkah 3. Membangun Docker image**

Pastikan terminal berada pada direktori `flask-app`, kemudian jalankan:

<img src="Images/21.png" width="700">
<img src="Images/22.png" width="700">

Perintah tersebut digunakan untuk membangun image aplikasi berdasarkan instruksi yang terdapat dalam Dockerfile. Opsi `-f Dockerfile` menentukan file yang digunakan, sedangkan `-t flaskr:1.0.0` memberikan nama dan tag pada image. Tanda titik di akhir perintah menunjukkan bahwa direktori saat ini digunakan sebagai build context.

**Langkah 4. Memeriksa Docker image**

Perintah:

<img src="Images/23.png" width="700">

Perintah tersebut digunakan untuk menampilkan daftar image yang tersedia pada Docker. Pemeriksaan dilakukan untuk memastikan image `flaskr` dengan tag `1.0.0` telah berhasil dibuat.

**Langkah 5. Menjalankan Docker container**

Perintah:

<img src="Images/24.png" width="700">

Perintah tersebut digunakan untuk menjalankan image Flask sebagai container. Opsi `-p 5001:5000` digunakan untuk menghubungkan port 5000 pada container dengan port 5001 pada komputer lokal. Dengan demikian, aplikasi dapat diakses melalui port 5001 dari browser.

**Langkah 6. Mengakses aplikasi Docker melalui browser**

Buka browser dan masukkan alamat:

<img src="Images/25.png" width="700">

Apabila halaman aplikasi Flask berhasil ditampilkan, berarti proses pembuatan image dan menjalankan container menggunakan Docker telah berhasil dilakukan. Aplikasi dapat diakses melalui port lokal 5001 meskipun aplikasi di dalam container menggunakan port 5000.

Untuk menghentikan container yang sedang berjalan, tekan `CTRL + C` pada terminal.

## 4.7 Membuat Containerized Application Menggunakan Podman

Selain Docker, praktikum ini juga menggunakan Podman untuk membangun dan menjalankan aplikasi dalam container. Podman dapat menggunakan Dockerfile yang sama sehingga tidak diperlukan pembuatan file konfigurasi baru.

**Langkah 1. Memeriksa kondisi Podman**

Perintah:

<img src="Images/26.png" width="700">
<img src="Images/27.png" width="700">

Perintah tersebut digunakan untuk menampilkan informasi konfigurasi Podman, termasuk lingkungan container dan penyimpanan image. Pemeriksaan ini dilakukan untuk memastikan Podman dapat digunakan sebelum proses pembangunan image dimulai.

Pada lingkungan Windows dengan WSL2, pengelolaan Podman mengikuti konfigurasi Podman yang telah dipasang. Tidak perlu menjalankan perintah `systemctl stop docker` dari modul apabila Docker dikelola melalui Docker Desktop dan tidak terdapat service Docker yang berjalan langsung di distribusi WSL2.

**Langkah 2. Membangun image menggunakan Podman**

Pastikan kembali berada pada direktori `flask-app`, kemudian jalankan:

<img src="Images/28.png" width="700">
<img src="Images/29.png" width="700">

Perintah tersebut digunakan untuk membangun image aplikasi Flask menggunakan Podman. File Dockerfile yang telah dibuat sebelumnya tetap digunakan sebagai dasar proses build. Podman akan membaca setiap instruksi dalam Dockerfile, mengambil image Python yang diperlukan, memasang paket aplikasi, serta menginisialisasi database.

**Langkah 3. Memeriksa image Podman**

Perintah:

<img src="Images/30.png" width="700">

Perintah tersebut digunakan untuk menampilkan daftar image yang telah tersedia pada Podman. Hasil pemeriksaan digunakan untuk mengetahui apakah image Flask dengan tag `1.0.0` telah berhasil dibuat.

**Langkah 4. Menjalankan container menggunakan Podman**

Perintah:

<img src="Images/31.png" width="700">

Perintah tersebut digunakan untuk menjalankan image Flask menggunakan Podman. Pemetaan port dilakukan dengan menghubungkan port 5000 pada container ke port 5001 pada komputer lokal. Dengan pengaturan tersebut, aplikasi dapat diakses melalui browser menggunakan alamat localhost.

**Langkah 5. Mengakses aplikasi melalui browser**

Buka browser dan masukkan alamat:

<img src="Images/32.png" width="700">

Apabila halaman aplikasi Flask berhasil ditampilkan, berarti image telah berhasil dijalankan menggunakan Podman. Hasil ini menunjukkan bahwa aplikasi yang sama dapat dijalankan melalui dua teknologi container, yaitu Docker dan Podman.

Untuk menghentikan container, tekan `CTRL + C` pada terminal.

# 5. PEMBAHASAN TUGAS 0

## 5.1 Contoh Vendor SaaS, PaaS, dan IaaS

Berdasarkan pembagian layanan XaaS dalam modul, berikut merupakan contoh penyedia layanan dari setiap kategori.

**a. Software as a Service (SaaS)**

Contoh vendor: Google Workspace.

<img src="Images/33.png" width="700">

Google Workspace merupakan layanan perangkat lunak berbasis cloud yang menyediakan berbagai aplikasi produktivitas, seperti Google Docs, Google Sheets, Google Slides, dan Google Drive. Pengguna dapat mengakses layanan tersebut melalui browser tanpa harus memasang aplikasi server sendiri. Service yang diberikan berupa penyediaan perangkat lunak siap pakai untuk membantu pekerjaan, pengolahan dokumen, penyimpanan file, dan kolaborasi secara daring.

**b. Platform as a Service (PaaS)**

Contoh vendor: Heroku.

<img src="Images/34.png" width="700">

Heroku merupakan platform cloud yang digunakan untuk mengembangkan, menjalankan, dan melakukan deployment aplikasi. Service yang diberikan berupa lingkungan pengembangan dan pengoperasian aplikasi tanpa mengharuskan pengguna mengelola seluruh infrastruktur server secara langsung. Pengembang dapat berfokus pada pembuatan aplikasi, sedangkan platform menyediakan lingkungan untuk menjalankannya.

**c. Infrastructure as a Service (IaaS)**

Contoh vendor: Amazon Web Services (AWS).

<img src="Images/35.png" width="700">

AWS menyediakan layanan infrastruktur cloud, salah satunya Amazon EC2 yang memungkinkan pengguna menggunakan server virtual. Service yang diberikan berupa sumber daya komputasi, penyimpanan, dan jaringan yang dapat dikonfigurasi sesuai kebutuhan. Pengguna memiliki kendali lebih besar terhadap sistem operasi dan aplikasi yang dijalankan pada server virtual tersebut.

## 5.2 Perbedaan Service SaaS, PaaS, dan IaaS

| Kategori | Service yang diberikan | Contoh |
|---|---|---|
| SaaS | Perangkat lunak siap digunakan | Google Workspace |
| PaaS | Platform untuk mengembangkan dan menjalankan aplikasi | Heroku |
| IaaS | Infrastruktur komputasi virtual | AWS EC2 |

## 5.3 Arsitektur XaaS

Secara umum, ketiga kategori XaaS memiliki pembagian tanggung jawab yang berbeda antara penyedia layanan dan pengguna.

**a. Arsitektur SaaS**

Pengguna mengakses aplikasi yang telah disediakan oleh penyedia layanan melalui internet. Penyedia bertanggung jawab terhadap pengelolaan aplikasi, platform, sistem operasi, server, dan infrastruktur pendukung.

**b. Arsitektur PaaS**

Pengguna bertanggung jawab terhadap aplikasi dan data yang dikembangkan, sedangkan penyedia layanan mengelola platform, runtime, sistem operasi, server, dan infrastruktur.

**c. Arsitektur IaaS**

Penyedia menyediakan infrastruktur virtual berupa server, penyimpanan, dan jaringan. Pengguna memiliki tanggung jawab untuk mengelola sistem operasi, middleware, runtime, aplikasi, serta data yang digunakan.

Visualisasi arsitektur secara sederhana:

<img src="Images/Infografik Arsitektur XaaS Pastel.png" width="700">

# 6. PEMBAHASAN HASIL PRAKTIKUM

Praktikum Modul 7 membahas penerapan Cloud Computing melalui pembuatan aplikasi berbasis Flask yang dikemas menjadi Containerized Application. Tahap awal dilakukan dengan mengambil source code Flask dari repository GitHub, kemudian menyiapkan environment Python dan memasang paket yang diperlukan.

Setelah aplikasi berhasil disiapkan, dilakukan inisialisasi database dan pengujian aplikasi melalui browser. Tahap berikutnya adalah membuat Dockerfile yang berisi instruksi untuk membangun image aplikasi. Image tersebut kemudian dijalankan menggunakan Docker dengan pemetaan port agar aplikasi dapat diakses melalui browser.

Proses yang sama juga dilakukan menggunakan Podman dengan memanfaatkan Dockerfile yang telah dibuat sebelumnya. Penggunaan kedua teknologi tersebut memberikan gambaran mengenai proses pembuatan dan pengoperasian container menggunakan alat yang berbeda. Hasil akhir praktikum akan dinilai berdasarkan keberhasilan proses build image, menjalankan container, dan mengakses aplikasi melalui browser.

# 7. KESIMPULAN

Berdasarkan praktikum Modul 7 tentang Cloud Computing, dapat dipahami bahwa Cloud Computing menyediakan sumber daya komputasi dalam bentuk layanan yang terdiri atas SaaS, PaaS, dan IaaS. Selain itu, teknologi container memungkinkan aplikasi dikemas bersama kebutuhan pendukungnya sehingga dapat dijalankan dalam lingkungan yang lebih terisolasi.

Melalui praktikum ini, aplikasi blog berbasis Flask digunakan sebagai contoh penerapan Containerized Application. Proses pengemasan aplikasi dilakukan menggunakan Dockerfile, kemudian image dibangun dan dijalankan menggunakan Docker serta Podman. Kedua teknologi tersebut dapat memanfaatkan Dockerfile yang sama untuk membangun aplikasi dalam container.

Dengan demikian, praktikum ini memberikan pemahaman mengenai konsep layanan Cloud Computing sekaligus penerapan teknologi container dalam proses pengembangan dan pengoperasian aplikasi.
