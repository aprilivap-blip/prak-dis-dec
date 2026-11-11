# Laporan Praktikum 06

## Identitas

- **Nama:** Apriliva Putri P
- **NIM:** 255410035
- **Kelas:** Informatika-1
- **Mata kuliah:** Praktikum Sistem Terdistribusi dan Terdesentralisasi

# LAPORAN PRAKTIKUM MODUL 6

# DISTRIBUTED FILE SYSTEM – HADOOP DISTRIBUTED FILE SYSTEM (HDFS)

## BAB I. PENDAHULUAN

### 1.1 Tujuan Praktikum

Praktikum Modul 6 tentang Distributed File System – Hadoop Distributed File System (HDFS) bertujuan untuk:

1. Memahami konsep dasar Distributed File System sebagai sistem penyimpanan data secara terdistribusi.
2. Mengetahui fungsi dan cara kerja Apache Hadoop dalam pengelolaan data berukuran besar.
3. Memahami proses instalasi dan konfigurasi Apache Hadoop menggunakan lingkungan Linux melalui WSL2 pada Windows.
4. Mengetahui fungsi NameNode dan DataNode dalam sistem HDFS.
5. Mempelajari penggunaan perintah HDFS untuk membuat direktori dan mengelola file.
6. Mampu mengunggah tiga file CSV ke dalam direktori HDFS.
7. Memahami cara memeriksa hasil penyimpanan file pada HDFS.

### 1.2 Dasar Teori

**1. Distributed File System (DFS)**

Distributed File System merupakan sistem penyimpanan file yang memungkinkan data disimpan dan dikelola pada beberapa komputer atau node yang saling terhubung melalui jaringan. Sistem ini memungkinkan pengguna mengakses data seolah-olah berada dalam satu sistem penyimpanan. DFS digunakan untuk membantu pengelolaan data dalam jumlah besar.

**2. Apache Hadoop**

Apache Hadoop merupakan framework yang digunakan untuk menyimpan dan memproses data dalam jumlah besar secara terdistribusi. Hadoop memiliki beberapa komponen utama, yaitu Hadoop Distributed File System (HDFS) sebagai sistem penyimpanan, MapReduce sebagai model pemrosesan data, dan YARN sebagai pengelola sumber daya.

**3. Hadoop Distributed File System (HDFS)**

HDFS merupakan sistem file terdistribusi yang menjadi bagian dari Apache Hadoop. HDFS dirancang untuk menyimpan file berukuran besar dengan membagi data menjadi beberapa blok. Blok tersebut dapat disimpan pada beberapa node sehingga penyimpanan data dapat dilakukan secara terdistribusi.

**4. NameNode dan DataNode**

NameNode merupakan komponen utama HDFS yang bertugas mengelola metadata, seperti nama file, struktur direktori, dan lokasi blok data. Sementara itu, DataNode bertugas menyimpan blok data yang dikelola oleh NameNode. Kedua komponen tersebut bekerja sama dalam proses penyimpanan dan pengaksesan data.

**5. Java Development Kit (JDK)**

Java Development Kit (JDK) merupakan perangkat pengembangan yang menyediakan berbagai alat untuk menjalankan dan mengembangkan aplikasi berbasis Java. Apache Hadoop membutuhkan Java untuk menjalankan berbagai komponennya. Pada praktikum ini digunakan JDK versi 17 sesuai ketentuan modul.

**6. Secure Shell (SSH)**

SSH merupakan protokol jaringan yang digunakan untuk melakukan komunikasi dan akses jarak jauh secara aman. Dalam Hadoop, SSH digunakan untuk membantu menjalankan proses pada node tanpa harus memasukkan password setiap kali melakukan koneksi.

**7. PDSH (Parallel Distributed Shell)**

PDSH merupakan perangkat yang digunakan untuk menjalankan perintah pada beberapa komputer atau node secara bersamaan. Dalam lingkungan Hadoop, PDSH membantu proses administrasi pada node yang terhubung.

**8. YARN dan MapReduce**

YARN (Yet Another Resource Negotiator) merupakan komponen Hadoop yang bertugas mengelola sumber daya dan penjadwalan aplikasi. Sementara itu, MapReduce merupakan model pemrosesan data yang digunakan untuk membagi pekerjaan menjadi beberapa bagian agar dapat diproses secara terdistribusi.

**9. Windows Subsystem for Linux (WSL2)**

WSL2 merupakan fitur Windows yang memungkinkan pengguna menjalankan lingkungan Linux secara langsung tanpa harus menggunakan mesin virtual tradisional. Pada praktikum ini, WSL2 digunakan untuk menjalankan Ubuntu melalui terminal Visual Studio Code sehingga perintah Linux yang dibutuhkan Hadoop dapat dijalankan pada perangkat Windows.

---

## BAB II. LANGKAH-LANGKAH PENGERJAAN PRAKTIKUM

### 2.1 Pemeriksaan Lingkungan Praktikum

**Langkah 1. Memeriksa status WSL**

Jalankan perintah berikut pada terminal bawaan Visual Studio Code dengan lingkungan PowerShell:

<img src="images/01.png" width="700">

**Penjelasan:**

Perintah `wsl --status` digunakan untuk mengetahui informasi konfigurasi Windows Subsystem for Linux (WSL) pada perangkat Windows. Pemeriksaan ini dilakukan untuk mengetahui apakah WSL sudah tersedia dan dapat digunakan sebagai lingkungan Linux dalam menjalankan Apache Hadoop.

**Langkah 2. Memeriksa distribusi Linux**

Jalankan perintah berikut:

<img src="images/02.png" width="700">

**Penjelasan:**

Perintah tersebut digunakan untuk menampilkan daftar distribusi Linux yang sudah terpasang pada Windows. Informasi yang ditampilkan meliputi nama distribusi, status penggunaan, dan versi WSL.

### 2.2 Instalasi Java Development Kit (JDK)

**Langkah 3. Memeriksa versi Java**

Pada terminal Ubuntu di Visual Studio Code, dan periksa compiler Java:

<img src="images/03.png" width="700">

**Penjelasan:**

Perintah `java -version` digunakan untuk mengetahui versi Java yang terpasang pada sistem, sedangkan `javac -version` digunakan untuk memeriksa versi compiler Java. Pada praktikum ini digunakan JDK versi 17 karena sesuai dengan persyaratan server Hadoop dalam modul.

Apabila JDK belum terpasang, lakukan instalasi menggunakan perintah:

<img src="images/04.png" width="700">

**Langkah 4. Mengatur JAVA_HOME**

Periksa lokasi instalasi Java dengan perintah:
Kemudian atur variabel JAVA_HOME sesuai lokasi JDK yang terpasang. Contoh:
Agar konfigurasi tetap tersimpan, jalankan:

<img src="images/05.png" width="700">

**Penjelasan:**

JAVA_HOME merupakan variabel lingkungan yang digunakan untuk menunjukkan lokasi instalasi Java. Pengaturan ini diperlukan agar Apache Hadoop dapat menemukan dan menggunakan Java ketika menjalankan komponennya. Lokasi yang digunakan harus disesuaikan dengan hasil pemeriksaan pada perangkat.

### 2.3 Instalasi Apache Hadoop

**Langkah 5. Mengunduh Apache Hadoop**

<img src="images/06.png" width="700">

**Penjelasan:**

Pada tahap ini dilakukan pengunduhan Apache Hadoop versi 3.5.0 yang akan digunakan sebagai perangkat utama dalam praktikum. File yang diunduh memiliki format `.tar.gz`, yaitu file arsip terkompresi yang perlu diekstrak sebelum digunakan.

**Langkah 6. Mengekstrak file Hadoop**

<img src="images/07.png" width="700">

**Penjelasan:**

Perintah `tar -xvf` digunakan untuk mengekstrak file Hadoop yang telah diunduh. Setelah proses ekstraksi selesai, dibuat symbolic link bernama `hadoop` yang mengarah ke direktori `hadoop-3.5.0`. Hal ini bertujuan untuk mempermudah pemanggilan direktori instalasi Hadoop.

**Langkah 7. Mengatur variabel lingkungan Hadoop**

<img src="images/08.png" width="700">

**Penjelasan:**

Konfigurasi variabel lingkungan dilakukan agar sistem dapat mengenali lokasi instalasi Hadoop dan Java. Variabel `HADOOP_HOME` menunjukkan direktori utama Hadoop, sedangkan `PATH` memungkinkan perintah Hadoop dijalankan dari berbagai direktori terminal.

Perintah `hadoop version` digunakan untuk memastikan bahwa instalasi Hadoop telah dikenali oleh sistem.

### 2.4 Instalasi dan Konfigurasi SSH serta PDSH

**Langkah 8. Menginstal SSH dan PDSH**

Jalankan perintah, Kemudian aktifkan layanan SSH:

<img src="images/09.png" width="700">

<img src="images/10.png" width="700">

**Penjelasan:**

SSH digunakan sebagai sarana komunikasi antar-node, sedangkan PDSH digunakan untuk menjalankan perintah pada node yang ditentukan. Kedua perangkat tersebut diperlukan untuk mendukung proses administrasi Hadoop.

**Langkah 9. Mengatur konfigurasi PDSH**

Jalankan perintah, Tambahkan konfigurasi ke `.bashrc`:

<img src="images/11.png" width="700">

**Penjelasan:**

Variabel `PDSH_RCMD_TYPE` digunakan untuk menentukan jenis komunikasi jarak jauh yang digunakan oleh PDSH. Pada praktikum ini, jenis komunikasi yang digunakan adalah SSH.

**Langkah 10. Membuat SSH tanpa password**

<img src="images/12.png" width="700">

<img src="images/13.png" width="700">

**Penjelasan:**

Pada tahap ini dibuat pasangan SSH key yang terdiri dari private key dan public key. Public key ditambahkan ke file `authorized_keys` agar pengguna dapat melakukan koneksi SSH ke localhost tanpa memasukkan password setiap kali melakukan koneksi.

### 2.5 Konfigurasi Apache Hadoop

File konfigurasi Hadoop berada pada direktori:

<img src="images/14.png" width="700">

**Langkah 11. Mengatur file hdfs-site.xml**

<img src="images/15.png" width="700">

**Penjelasan:**

File `hdfs-site.xml` digunakan untuk mengatur konfigurasi khusus HDFS. Pada konfigurasi tersebut, nilai `dfs.replication` diatur menjadi 1. Artinya, setiap blok data memiliki satu salinan. Pengaturan ini disesuaikan dengan praktikum yang menggunakan satu node lokal.

**Langkah 12. Mengatur file core-site.xml**
Masukkan konfigurasi berikut:

<img src="images/16.png" width="700">

**Penjelasan:**

File `core-site.xml` digunakan untuk mengatur konfigurasi utama Hadoop. Properti `fs.defaultFS` menunjukkan alamat sistem file default yang digunakan, yaitu HDFS pada localhost dengan port 9000. Konfigurasi proxyuser digunakan untuk mengatur izin pengguna yang menjalankan layanan proxy Hadoop.

**Langkah 13. Mengatur file mapred-site.xml**

<img src="images/17.png" width="700">

**Penjelasan:**

File `mapred-site.xml` digunakan untuk mengatur konfigurasi MapReduce. Properti `mapreduce.framework.name` diatur menjadi `yarn`, yang menunjukkan bahwa pemrosesan MapReduce menggunakan YARN sebagai pengelola sumber daya.

**Langkah 14. Mengatur file yarn-site.xml**
Masukkan konfigurasi:

<img src="images/18.png" width="700">

**Penjelasan:**

File `yarn-site.xml` digunakan untuk mengatur konfigurasi YARN. Pengaturan tersebut meliputi layanan tambahan NodeManager, daftar variabel lingkungan yang diizinkan, serta kapasitas memori yang digunakan dalam pengelolaan sumber daya. Nilai memori perlu disesuaikan dengan kapasitas RAM perangkat.

### 2.6 Format NameNode

**Langkah 15. Melakukan format NameNode**

Jalankan perintah:

<img src="images/19.png" width="700">

**Penjelasan:**

Format NameNode dilakukan untuk menginisialisasi metadata sistem file HDFS sebelum digunakan. Proses ini merupakan tahap awal agar NameNode memiliki struktur penyimpanan metadata yang diperlukan.

Format NameNode hanya dilakukan satu kali pada saat inisialisasi. Sesuai petunjuk modul, format ulang dapat menghapus informasi sistem file HDFS yang telah tersimpan sehingga perintah ini tidak boleh dijalankan sembarangan.

### 2.7 Konfigurasi JAVA_HOME pada Hadoop

**Langkah 16. Mengatur JAVA_HOME pada file hadoop-env.sh**
Sesuaikan bagian JAVA_HOME menjadi:

<img src="images/20.png" width="700">

**Penjelasan:**

Konfigurasi ini bertujuan agar Apache Hadoop dapat menemukan lokasi instalasi Java secara langsung. Pengaturan JAVA_HOME pada file `hadoop-env.sh` memastikan bahwa layanan Hadoop menggunakan versi Java yang sesuai dengan kebutuhan praktikum.

### 2.8 Menjalankan Daemon HDFS

**Langkah 17. Menjalankan layanan HDFS**

<img src="images/21.png" width="700">

**Penjelasan:**

Perintah `start-dfs.sh` digunakan untuk menjalankan layanan HDFS. Pada konfigurasi satu node, proses ini akan menjalankan NameNode, DataNode, dan SecondaryNameNode pada localhost.

NameNode bertugas mengelola metadata, DataNode menyimpan blok data, sedangkan SecondaryNameNode membantu proses pengelolaan metadata melalui mekanisme checkpoint.

**Langkah 18. Memeriksa proses Hadoop**

Jalankan perintah:

<img src="images/22.png" width="700">

**Penjelasan:**

Perintah `jps` digunakan untuk menampilkan proses Java yang sedang berjalan. Melalui perintah ini, pengguna dapat memeriksa apakah proses NameNode, DataNode, dan SecondaryNameNode telah aktif.

### 2.9 Memeriksa HDFS melalui Web Browser

**Langkah 19. Membuka halaman monitoring Hadoop**

Buka browser Windows dan akses alamat:

<img src="images/23.png" width="700">

**Penjelasan:**

Halaman tersebut merupakan antarmuka web NameNode yang digunakan untuk memantau kondisi HDFS. Informasi yang dapat dilihat meliputi status sistem, kapasitas penyimpanan, jumlah DataNode, dan informasi penggunaan ruang penyimpanan.

Apabila halaman dapat diakses dan menunjukkan layanan aktif, hal tersebut menjadi salah satu indikator bahwa NameNode berhasil dijalankan.

### 2.10 Pengerjaan Tugas Praktikum

**Langkah 20. Membuat direktori datasets pada HDFS**

Jalankan perintah:

<img src="images/24.png" width="700">

**Penjelasan:**

Perintah `hdfs dfs -mkdir -p` digunakan untuk membuat direktori baru pada HDFS. Direktori tersebut dibuat dengan struktur `/user/nama_user/datasets`. Penggunaan variabel `$USER` bertujuan agar nama direktori mengikuti username Ubuntu yang sedang digunakan.

Opsi `-p` memungkinkan pembuatan direktori induk apabila sebelumnya belum tersedia.

**Langkah 21. Memeriksa direktori yang telah dibuat**

Jalankan perintah:

<img src="images/25.png" width="700">

**Penjelasan:**

Perintah `hdfs dfs -ls` digunakan untuk menampilkan daftar file dan direktori yang terdapat pada HDFS. Pemeriksaan ini dilakukan untuk memastikan bahwa direktori datasets telah berhasil dibuat sesuai dengan lokasi yang ditentukan dalam tugas praktikum.

**Langkah 22. Mencari dan mengunduh tiga file CSV**

Jalankan perintah :

<img src="images/26.png" width="700">

**Penjelasan:**

Pada tahap ini dilakukan pengumpulan tiga dataset dengan format CSV yang akan digunakan sebagai data uji dalam praktikum HDFS. File disimpan terlebih dahulu pada direktori lokal Ubuntu agar dapat diperiksa sebelum dipindahkan ke sistem penyimpanan Hadoop.

**Langkah 23. Mengunggah tiga file CSV ke HDFS**

Setelah ketiga file tersedia pada direktori lokal, jalankan perintah:

<img src="images/27.png" width="700">

**Penjelasan:**

Perintah `hdfs dfs -put` digunakan untuk menyalin file dari penyimpanan lokal ke dalam HDFS. Tanda `*.csv` digunakan untuk memilih seluruh file yang memiliki ekstensi CSV pada direktori datasets. Dengan demikian, ketiga file yang telah dikumpulkan dapat dimasukkan ke dalam direktori tujuan secara bersamaan.

**Langkah 24. Memeriksa hasil penyimpanan file CSV**

Jalankan perintah, untuk melihat ukuran file, gunakan:

<img src="images/28.png" width="700">

**Penjelasan:**

Pada tahap ini dilakukan pemeriksaan terhadap file yang telah dipindahkan ke HDFS. Perintah `hdfs dfs -ls` digunakan untuk menampilkan nama file yang tersimpan, sedangkan `hdfs dfs -du -h` digunakan untuk melihat ukuran penyimpanan masing-masing file.

Apabila ketiga file CSV muncul pada direktori datasets, berarti proses pemindahan data ke HDFS telah berhasil dilakukan.

### 2.11 Menghentikan Layanan HDFS

**Langkah 25. Menghentikan daemon HDFS**

Setelah seluruh proses praktikum selesai, jalankan perintah:

<img src="images/29.png" width="700">

**Penjelasan:**

Perintah `stop-dfs.sh` digunakan untuk menghentikan seluruh layanan HDFS yang sebelumnya dijalankan. Penghentian layanan dilakukan setelah proses praktikum selesai agar penggunaan sumber daya komputer tidak terus berlangsung ketika Hadoop sudah tidak digunakan.

---

## BAB III. KESIMPULAN

Berdasarkan praktikum Modul 6 mengenai Distributed File System – Hadoop Distributed File System (HDFS), dapat disimpulkan bahwa Apache Hadoop merupakan framework yang dapat digunakan untuk mengelola penyimpanan data dalam jumlah besar melalui sistem file terdistribusi. HDFS memiliki komponen utama, yaitu NameNode yang bertugas mengelola metadata dan DataNode yang berfungsi menyimpan blok data.

Melalui praktikum ini, mahasiswa mempelajari proses persiapan lingkungan Linux menggunakan WSL2, instalasi JDK, instalasi Apache Hadoop, konfigurasi SSH, serta pengaturan berbagai file konfigurasi Hadoop. Selain itu, praktikum juga memberikan pemahaman mengenai penggunaan perintah HDFS untuk membuat direktori, memindahkan file, dan memeriksa data yang tersimpan.

Tugas pembuatan direktori datasets dan pemindahan tiga file CSV menjadi penerapan langsung dari penggunaan HDFS sebagai sistem penyimpanan terdistribusi. Dengan demikian, praktikum ini memberikan pemahaman mengenai dasar pengelolaan file menggunakan Apache Hadoop serta cara menjalankan HDFS melalui lingkungan Windows dengan bantuan WSL2 dan Visual Studio Code.
