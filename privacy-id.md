---
title: Kebijakan Privasi · Calisthenics Skills – Ranked
permalink: /privacy/id/
---

> *Ini adalah terjemahan. Jika terdapat perbedaan, [versi bahasa Inggris](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/) yang berlaku.*

# Kebijakan Privasi · Calisthenics Skills – Ranked

**Terakhir diperbarui: 29 September 2026**

Kebijakan ini menjelaskan data apa yang dikumpulkan Ranked, ke mana data tersebut dikirim, dan apa yang dapat Anda lakukan. Dokumen ini ditulis berdasarkan kode aplikasi yang sebenarnya, bukan templat; jika ada yang keliru, kodenya yang perlu diperiksa.

Ranked dioperasikan oleh **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Swiss**, kontak **dylan.schmid538@gmail.com**. Beliau adalah pengendali pemrosesan yang dijelaskan di sini.

---

## 1. Ringkasan

Ranked **tidak memiliki akun pengguna atau server sendiri**. Semua hal tentang latihan Anda — setiap set yang dicatat, perkembangan setiap keterampilan, peringkat, Power Level, dan peta tubuh — disimpan di ponsel Anda dan tidak pernah diunggah.

**Usia, jenis kelamin, tinggi badan, dan berat badan Anda tidak pernah meninggalkan perangkat.** Rumus peringkat menggunakannya di ponsel Anda. Data itu tidak dikirim kepada kami ataupun layanan analitik.

Hanya dua jenis data yang meninggalkan perangkat:

1. **Statistik penggunaan anonim**, agar kami memahami cara aplikasi digunakan. Anda dapat menonaktifkannya kapan saja di aplikasi.
2. **Data pembelian**, agar langganan App Store dapat diverifikasi. Apple menangani pembayaran; kami tidak pernah melihat rincian pembayaran Anda.

Ranked tidak melacak Anda di aplikasi atau situs web lain, tidak menampilkan iklan, dan tidak membaca apa pun dari Apple Health.

---

## 2. Data yang tetap berada di perangkat

Data berikut disimpan di basis data aplikasi pada ponsel Anda dan tidak pernah dikirim:

- Setiap latihan, set, repetisi, durasi tahan, dan beban tambahan yang Anda catat
- Perkembangan di setiap keterampilan dan tahap, riwayat peringkat, dan Power Level
- Rencana latihan, jadwal, pengingat, dan preferensi
- Ukuran tubuh yang Anda masukkan (usia, jenis kelamin, tinggi badan, berat badan)
- Catatan latihan

Aplikasi tidak mengecualikan basis data ini dari cadangan perangkat. Jika Anda memakai Cadangan iCloud atau cadangan komputer, data latihan menjadi bagian dari cadangan itu dan kembali saat Anda memulihkannya — sesuai ketentuan Apple, bukan ketentuan kami.

Menghapus aplikasi akan menghapus semua data tersebut dari perangkat. Kami tidak dapat memulihkannya karena kami tidak pernah memilikinya.

---

## 3. Data yang meninggalkan perangkat

### 3.1 Statistik penggunaan (PostHog)

Kami menggunakan **PostHog**, yang dihosting di **Uni Eropa**, untuk memahami penggunaan aplikasi. Aplikasi mengirim daftar peristiwa yang tetap:

- langkah penyiapan yang Anda capai, selesaikan, atau mundur darinya, beserta durasi masing-masing;
- hasil penilaian awal: jumlah jalur keterampilan dan tahap yang Anda klaim, keterampilan yang dipilih sebagai tujuan, peringkat awal, dan peringkat masing-masing dari enam wilayah tubuh;
- kapan layar pembelian ditampilkan atau ditutup, dan kapan pembelian dimulai, selesai, atau dipulihkan, beserta produk dan penawaran terkait; ketika aplikasi kemudian mendapati masa percobaan aktif atau periode langganan berbayar, beserta produk dan apakah pembelian dilakukan dalam lingkungan pengujian (ini bukan catatan setiap tagihan dan tidak dikirim saat aplikasi ditutup);
- kapan peringkat Anda berubah dan keterampilan yang memicunya;
- kapan Anda menyelesaikan tahap: keterampilan dan tahapnya, serta apakah berasal dari set yang dicatat, latihan yang dimasukkan belakangan, atau klaim manual;
- layar yang Anda buka dan kapan latihan selesai. Peristiwa penyelesaian latihan tidak membawa rincian: bukan gerakan, set, ataupun angkanya.

Perangkat lunak PostHog di aplikasi juga menambahkan informasi teknis standar pada setiap peristiwa, seperti model perangkat, versi iOS, versi aplikasi, bahasa, dan zona waktu, serta mencatat kapan aplikasi dibuka dan dipindahkan ke latar belakang. Seperti layanan internet lainnya, PostHog menerima alamat IP permintaan dan mungkin menyimpulkan lokasi perkiraan (negara atau kota) darinya.

**Yang tidak disertakan:** nama, alamat email (aplikasi tidak pernah memintanya), pengenal akun (tidak ada), usia, jenis kelamin, tinggi atau berat badan, maupun isi latihan Anda.

**Cara Anda dikenali:** PostHog membuat pengenal acak saat aplikasi pertama kali berjalan dan menyimpannya di perangkat Anda. Semua peristiwa dikelompokkan berdasarkan pengenal tersebut. Aplikasi tidak pernah memberi tahu PostHog siapa Anda; tidak ada akun ataupun email yang dapat disampaikan.

**Cara menonaktifkan:** Pengaturan ▸ Privasi ▸ *Bagikan data penggunaan anonim*. Menonaktifkannya menghentikan pengiriman peristiwa oleh aplikasi sejak saat itu. Pengaturan disimpan di perangkat dan bertahan setelah pembaruan aplikasi.

### 3.2 Atribusi Apple Search Ads

Jika Anda memasang Ranked setelah mengetuk iklan Apple Search Ads, saat pertama kali dibuka aplikasi menanyakan kepada Apple satu kali sumber pemasangannya. Apple memberikan kampanye, grup iklan, kata kunci, dan kumpulan materi iklan, negara atau wilayah serta tanggal klik, dan apakah itu unduhan baru atau unduhan ulang. Aplikasi mengaitkan nilai-nilai ini dengan pengenal PostHog anonim pada §3.1, sehingga peristiwa berikutnya dapat dikelompokkan menurut iklan yang membawa Anda.

Ini menggunakan kerangka kerja **AdServices** Apple, tanpa pengenal iklan (IDFA), dan Apple tidak menganggapnya sebagai pelacakan; karena itu tidak ada dialog izin pelacakan. Jika Anda tidak datang melalui iklan, Apple menyatakannya dan tidak ada informasi lain yang dikaitkan. Menonaktifkan statistik penggunaan (§3.1) juga menghentikan proses ini.

### 3.3 Pembelian (Apple dan RevenueCat)

Langganan dijual dan ditagihkan oleh **Apple** melalui App Store. Kami tidak pernah melihat rincian pembayaran, Akun Apple, atau nama Anda.

Untuk memeriksa apakah langganan aktif, aplikasi menggunakan **RevenueCat**. RevenueCat menerima catatan pembelian App Store untuk langganan Anda — produk yang dibeli, kapan dimulai dan berakhir — bersama informasi teknis standar seperti versi iOS dan aplikasi. RevenueCat mengenali pemasangan aplikasi melalui pengenal acak yang dibuatnya sendiri dan disimpan di perangkat Anda. Kami tidak memberikan nama, email, atau identitas lain kepada RevenueCat; karena Ranked tidak memiliki akun, tidak ada identitas akun untuk diberikan.

Saat Anda mengetuk **Pulihkan Pembelian**, aplikasi meminta Apple memberikan pembelian yang dilakukan dengan Akun Apple yang masuk pada perangkat lalu menyampaikan hasilnya kepada RevenueCat dengan cara yang sama.

---

## 4. Hal yang tidak dilakukan Ranked

- **Tidak ada akun.** Anda tidak perlu masuk. Tidak ada profil tentang Anda di server mana pun.
- **Tidak ada Apple Health.** Ranked tidak membaca dari atau menulis ke aplikasi Kesehatan.
- **Tidak ada kamera, foto, mikrofon, lokasi, atau kontak.** Aplikasi tidak meminta izin tersebut.
- **Tidak ada pelacakan lintas aplikasi atau situs web**, pengenal iklan, iklan dalam aplikasi, atau penjualan maupun pemberian data kepada pialang data.
- **Tidak ada server pemberitahuan push.** Pengingat dijadwalkan secara lokal di ponsel; tidak ada informasinya yang meninggalkan perangkat. Izin diminta sebelum pengingat pertama dijadwalkan, dan Anda dapat menonaktifkannya kapan saja di Pengaturan iOS.

---

## 5. Dasar hukum (GDPR dan UU Perlindungan Data Swiss yang direvisi)

| Pemrosesan | Dasar hukum |
|---|---|
| Pembelian dan verifikasi langganan (§3.3) | Pelaksanaan kontrak |
| Statistik penggunaan (§3.1) | Kepentingan yang sah untuk memahami dan memperbaiki aplikasi; Anda dapat menolak kapan saja dengan menonaktifkannya, lihat §8 |
| Atribusi Search Ads (§3.2) | Kepentingan yang sah untuk mengetahui iklan yang efektif; penolakan seperti di atas |

**Dua hukum berlaku di sini, bukan satu.** Ranked dioperasikan dari Swiss, sehingga Undang-Undang Federal Swiss tentang Perlindungan Data yang direvisi (**revDSG**, berlaku sejak September 2023) mengatur pemrosesan ini. **GDPR** juga berlaku apabila aplikasi digunakan dari Uni Eropa atau Britania Raya. Jika keduanya berbeda, kami mengikuti aturan yang lebih ketat. Penduduk Swiss memiliki hak-hak pokok yang sama sebagaimana tercantum pada §8 berdasarkan Pasal 25 dan seterusnya revDSG.

---

## 6. Lokasi pemrosesan data

- **PostHog** memproses statistik penggunaan di Uni Eropa.
- **RevenueCat, Inc.** berkedudukan di Amerika Serikat dan memproses data pembelian sebagaimana pada §3.3 di sana.
- **Apple** memproses pembelian dan permintaan atribusi Search Ads menurut kebijakan privasinya sendiri, yang berlaku untuk Akun Apple Anda terlepas dari aplikasi ini.

---

## 7. Lama penyimpanan

Statistik penggunaan disimpan selama masa retensi yang berlaku untuk paket PostHog kami. Kami tidak menjanjikan jumlah bulan yang tetap karena PostHog tidak memungkinkan kami menentukannya; angka yang tidak dapat dipenuhi lebih buruk dalam kebijakan privasi daripada tidak menyebutkannya.

Catatan pembelian disimpan oleh RevenueCat selama langganan dan riwayatnya ada, sebagaimana diperlukan untuk memverifikasi langganan.

Semua data pada perangkat tetap tersimpan hingga Anda menghapus aplikasi.

---

## 8. Hak Anda

Anda dapat kapan saja:

- **Menonaktifkan statistik penggunaan** di Pengaturan ▸ Privasi. Ini adalah hak untuk menolak dan, jika pemrosesan didasarkan pada persetujuan, menarik persetujuan tersebut; berlaku segera tanpa perlu alasan.
- **Menghapus data Anda.** Karena Ranked tidak menyimpan apa pun tentang Anda di server, menghapus aplikasi menghilangkan semua yang disimpan aplikasi itu sendiri.
- **Meminta penghapusan profil analitik anonim.** Kami tidak dapat menemukannya berdasarkan nama karena tidak ada nama, tetapi jika Anda menulis kepada kami dengan perkiraan tanggal pertama kali memakai aplikasi dan perangkat yang digunakan, kami akan mencarinya secara manual dan menghapusnya.
- **Meminta salinan** data yang disimpan layanan berdasarkan pengenal Anda, meminta kami **memperbaikinya**, atau **membatasi** pemrosesannya selama permintaan diperiksa.
- **Mengajukan keluhan kepada otoritas pengawas** di negara Anda; di Swiss, Komisaris Federal Perlindungan Data dan Informasi (FDPIC).

Tulislah kepada **dylan.schmid538@gmail.com** untuk hal-hal tersebut.

---

## 9. Anak-anak

Ranked ditujukan bagi orang yang berusia **16 tahun ke atas**. Aplikasi menanyakan usia saat penyiapan karena rumus peringkat bergantung padanya, dan tidak ditujukan kepada siapa pun yang lebih muda. Kami tidak dengan sengaja mengumpulkan data dari anak di bawah 16 tahun.

---

## 10. Perubahan

Versi yang diterbitkan di alamat ini adalah versi yang berlaku, dan tanggal di bagian atas menunjukkan kapan terakhir diperbarui. Versi sebelumnya tetap dapat dilihat dalam riwayat publik repositori tempat halaman ini diterbitkan, sehingga Anda dapat mengetahui apa yang berubah dan kapan.

---

> **⚠️ Bukan nasihat hukum.** Dokumen ini disusun dari kode sumber aplikasi oleh seorang insinyur, bukan pengacara. Dokumen ini menggambarkan sistem secara akurat pada tanggal di atas; setiap pernyataan telah diperiksa terhadap data yang benar-benar dikirim aplikasi. Dokumen ini **belum** ditinjau untuk kepatuhan terhadap GDPR, revDSG Swiss, CCPA, atau aturan lain. Penerbitannya memenuhi persyaratan Apple; penerbitan tidak menjamin kepatuhan hukum. Mintalah pengacara membacanya setelah aplikasi menghasilkan pendapatan.
