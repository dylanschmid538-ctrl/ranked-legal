---
title: Dasar Privasi · Calisthenics Skills – Ranked
permalink: /privacy/ms/
---

> Ini ialah terjemahan. Jika terdapat percanggahan, [versi bahasa Inggeris](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/) yang terpakai.

# Dasar Privasi · Calisthenics Skills – Ranked

**Kemas kini terakhir: 2026-10-02**

Dasar ini menerangkan data yang dikumpul oleh Ranked, ke mana data itu pergi, dan tindakan yang boleh anda ambil. Ia ditulis berdasarkan kod sebenar aplikasi, bukan templat; jika ada perkara yang salah di sini, kod itulah yang perlu disemak.

Ranked dikendalikan oleh **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Switzerland**, hubungi **dylan.schmid538@gmail.com**. Beliau ialah pengawal data bagi pemprosesan yang diterangkan di sini.

---

## 1. Ringkasan

**Umur, jantina, tinggi dan berat badan anda tidak pernah meninggalkan peranti anda.** Formula kedudukan menggunakan maklumat ini pada telefon anda. Maklumat ini tidak dihantar kepada kami atau perkhidmatan analitik.

Hanya dua jenis data meninggalkan peranti anda:

1. **Statistik penggunaan tanpa nama** supaya kami dapat memahami cara aplikasi digunakan. Anda boleh mematikannya dalam aplikasi pada bila-bila masa.
2. **Data pembelian** supaya langganan App Store dapat disahkan. Apple mengendalikan pembayaran; kami tidak pernah melihat butiran pembayaran anda.

Ranked tidak menjejaki anda merentas aplikasi atau laman web lain, tidak memaparkan iklan, dan tidak membaca apa-apa daripada Apple Health.

---

## 2. Perkara yang kekal pada peranti anda

Perkara berikut disimpan dalam pangkalan data aplikasi pada telefon anda dan tidak pernah dihantar:

- Setiap latihan, set, ulangan, tahanan dan berat tambahan yang anda rekodkan
- Pelan dan jadual latihan, peringatan dan pilihan anda
- Ukuran badan yang anda masukkan (umur, jantina, tinggi, berat badan)
- Nota latihan anda

Aplikasi tidak mengecualikan pangkalan data ini daripada sandaran peranti. Jika anda menggunakan iCloud Backup atau sandaran komputer, data latihan anda termasuk dalam sandaran dan kembali apabila dipulihkan — tertakluk kepada terma Apple, bukan terma kami.

Memadamkan aplikasi akan memadamkan semua data ini daripada peranti. Kami tidak boleh memulihkannya kerana kami tidak pernah memilikinya.

---

## 3. Perkara yang meninggalkan peranti anda

### 3.1 Statistik penggunaan (PostHog)

Kami menggunakan **PostHog**, yang dihoskan di **Kesatuan Eropah**, untuk memahami cara aplikasi digunakan. Aplikasi menghantar senarai peristiwa yang tetap:

- langkah persediaan yang anda capai, selesaikan atau undur daripadanya, serta tempoh setiap langkah;
- hasil penilaian awal: bilangan laluan kemahiran dan tahap yang anda tandakan sebagai dicapai, kemahiran yang dipilih sebagai matlamat, kedudukan permulaan anda dan kedudukan setiap satu daripada enam kawasan badan;
- masa skrin pembelian dipaparkan atau ditutup dan masa pembelian dimulakan, diselesaikan atau dipulihkan, bersama produk dan tawaran yang terlibat; masa aplikasi kemudiannya mengesan tempoh percubaan aktif atau langganan berbayar, bersama produk dan sama ada pembelian itu berlaku dalam persekitaran ujian (ini bukan rekod setiap caj dan tidak dihantar semasa aplikasi ditutup);
- masa kedudukan anda berubah dan kemahiran yang menyebabkannya;
- masa anda menyelesaikan tahap: kemahiran dan tahap tersebut serta sama ada ia berpunca daripada set yang direkodkan, latihan yang dimasukkan kemudian atau pengakuan manual;
- skrin yang anda buka dan masa latihan tamat. Peristiwa tamat latihan tidak mengandungi butiran: bukan senaman, set atau angka.

Perisian PostHog dalam aplikasi turut melampirkan maklumat teknikal lazim pada setiap peristiwa, seperti model peranti, versi iOS, versi aplikasi, bahasa dan zon waktu, serta merekodkan bila aplikasi dibuka atau dipindahkan ke latar belakang. Seperti mana-mana perkhidmatan internet, PostHog menerima alamat IP permintaan tersebut; ia mungkin menganggarkan lokasi kasar (negara atau bandar) daripadanya.

**Perkara yang tidak disertakan:** nama, alamat e-mel (aplikasi tidak pernah memintanya), pengecam akaun (tiada akaun), umur, jantina, tinggi, berat badan atau kandungan latihan anda.

**Cara anda dikenal pasti:** PostHog menjana pengecam rawak apabila aplikasi pertama kali dijalankan dan menyimpannya pada peranti anda. Semua peristiwa dikumpulkan di bawah pengecam tersebut. Aplikasi tidak pernah memberitahu PostHog siapa anda, dan tiada akaun atau e-mel yang boleh diberitahu.

**Cara mematikan:** Tetapan ▸ Privasi ▸ *Kongsi data penggunaan tanpa nama*. Mematikannya menghentikan penghantaran peristiwa oleh aplikasi mulai saat itu. Tetapan disimpan pada peranti anda dan kekal selepas kemas kini aplikasi.

### 3.2 Atribusi Apple Search Ads

Jika anda memasang Ranked selepas mengetik iklan Apple Search Ads, aplikasi bertanya kepada Apple sekali pada pelancaran pertama tentang sumber pemasangan. Apple membalas dengan kempen, kumpulan iklan, kata kunci dan set kreatif iklan tersebut, negara atau wilayah serta tarikh ketikan, dan sama ada ia muat turun baharu atau muat turun semula. Aplikasi melampirkan nilai ini pada pengecam PostHog tanpa nama yang diterangkan dalam §3.1 supaya peristiwa kemudian boleh dikumpulkan mengikut iklan yang membawa anda ke aplikasi.

Ini menggunakan rangka kerja **AdServices** Apple, yang tidak menggunakan pengecam pengiklanan (IDFA) dan tidak dianggap sebagai penjejakan oleh Apple; oleh itu tiada dialog kebenaran penjejakan dipaparkan. Jika anda tidak datang melalui iklan, Apple menyatakannya dan tiada perkara lain dilampirkan. Mematikan statistik penggunaan (§3.1) turut menghentikan perkara ini.

### 3.3 Pembelian (Apple dan RevenueCat)

Langganan dijual dan dibilkan oleh **Apple** melalui App Store. Kami tidak pernah melihat butiran pembayaran, Akaun Apple atau nama anda.

Untuk mengesahkan sama ada langganan anda aktif, aplikasi menggunakan **RevenueCat**. RevenueCat menerima rekod pembelian langganan daripada App Store — produk yang dibeli, masa ia bermula dan tamat — bersama maklumat teknikal lazim seperti versi iOS dan versi aplikasi. Ia mengenal pasti pemasangan anda melalui pengecam rawak yang dijananya sendiri dan disimpan pada peranti anda. Kami tidak memberikan nama, alamat e-mel atau identiti lain kepada RevenueCat; kerana Ranked tiada akaun, identiti seperti itu tidak wujud untuk diberikan.

Apabila anda mengetik **Pulihkan Pembelian**, aplikasi meminta daripada Apple pembelian yang dibuat menggunakan Akaun Apple yang dilog masuk pada peranti, lalu menghantar hasilnya kepada RevenueCat dengan cara yang sama.

---

## 4. Perkara yang Ranked tidak lakukan

- **Tiada akaun.** Anda tidak perlu log masuk. Tiada profil anda pada mana-mana pelayan.
- **Tiada Apple Health.** Ranked tidak membaca atau menulis pada aplikasi Health.
- **Tiada kamera, foto, mikrofon, lokasi atau kenalan.** Aplikasi tidak meminta kebenaran ini.
- **Tiada penjejakan merentas aplikasi atau laman web**, pengecam pengiklanan, iklan dalam aplikasi, atau data yang dijual atau diberikan kepada broker data.
- **Tiada pelayan pemberitahuan tolak.** Peringatan dijadualkan secara setempat pada telefon anda; tiada maklumat mengenainya meninggalkan peranti. Anda ditanya sebelum peringatan pertama dijadualkan dan boleh mematikannya dalam Tetapan iOS pada bila-bila masa.

---

## 5. Asas undang-undang (GDPR dan revDSG Switzerland)

| Pemprosesan | Asas |
|---|---|
| Pembelian dan pengesahan langganan (§3.3) | Pelaksanaan kontrak |
| Statistik penggunaan (§3.1) | Kepentingan sah untuk memahami dan menambah baik aplikasi; anda boleh membantah pada bila-bila masa dengan mematikannya, lihat §8 |
| Atribusi Search Ads (§3.2) | Kepentingan sah untuk mengetahui iklan yang berkesan; bantahan seperti di atas |

**Dua undang-undang terpakai di sini, bukan satu.** Ranked dikendalikan dari Switzerland, maka Akta Perlindungan Data Persekutuan Switzerland yang disemak (**revDSG**, berkuat kuasa sejak September 2023) mengawal pemprosesan ini. **GDPR** turut terpakai apabila aplikasi digunakan dari Kesatuan Eropah atau United Kingdom. Jika kedua-duanya berbeza, kami mengikut peraturan yang lebih ketat. Penduduk Switzerland mempunyai hak asas yang sama seperti yang disenaraikan dalam §8 di bawah Artikel 25 dan seterusnya revDSG.

---

## 6. Tempat data diproses

- **PostHog** memproses statistik penggunaan di Kesatuan Eropah.
- **RevenueCat, Inc.** berpangkalan di Amerika Syarikat dan memproses data pembelian yang diterangkan dalam §3.3 di sana.
- **Apple** memproses pembelian itu sendiri dan permintaan atribusi Search Ads mengikut dasar privasinya sendiri, yang terpakai pada Akaun Apple anda tanpa mengira aplikasi ini.

---

## 7. Tempoh penyimpanan

Statistik penggunaan disimpan selama tempoh pengekalan PostHog yang terpakai pada pelan kami. Kami tidak menjanjikan bilangan bulan yang tetap kerana PostHog tidak membenarkan kami menetapkannya; tempoh yang tidak boleh ditepati lebih buruk dalam dasar privasi daripada tidak menyatakan tempoh.

RevenueCat menyimpan rekod pembelian selagi langganan dan sejarahnya wujud, sebagaimana yang diperlukan untuk mengesahkan langganan.

Segala data pada peranti anda kekal di situ sehingga anda memadamkan aplikasi.

---

## 8. Hak anda

Pada bila-bila masa, anda boleh:

- **Mematikan statistik penggunaan** di Tetapan ▸ Privasi. Ini ialah hak anda untuk membantah dan, apabila pemprosesan berasaskan persetujuan, menarik balik persetujuan itu; ia berkuat kuasa serta-merta tanpa perlu memberikan sebab.
- **Memadamkan data anda.** Oleh sebab Ranked tidak menyimpan apa-apa tentang anda pada pelayan, memadamkan aplikasi menghapuskan semua perkara yang disimpan oleh aplikasi itu sendiri.
- **Meminta kami memadamkan profil analitik tanpa nama anda.** Kami tidak boleh mencarinya melalui nama kerana profil itu tiada nama; jika anda menulis kepada kami dengan anggaran tarikh anda mula-mula menggunakan aplikasi dan peranti yang digunakan, kami akan mencarinya secara manual dan memadamkannya.
- **Meminta salinan** data yang disimpan oleh suatu perkhidmatan di bawah pengecam anda, meminta data itu **dibetulkan**, atau meminta pemprosesannya **dihadkan** semasa permintaan diteliti.
- **Mengadu kepada pihak berkuasa penyeliaan** di negara anda; di Switzerland, Pesuruhjaya Perlindungan Data dan Maklumat Persekutuan (FDPIC).

Tulis kepada **dylan.schmid538@gmail.com** untuk mana-mana perkara ini.

---

## 9. Kanak-kanak

Ranked adalah untuk mereka yang berumur **16 tahun ke atas**. Aplikasi meminta umur anda semasa persediaan kerana formula kedudukan bergantung padanya, dan tidak ditujukan kepada mereka yang lebih muda. Kami tidak dengan sengaja mengumpul data daripada sesiapa di bawah umur 16 tahun.

---

## 10. Perubahan

Versi yang diterbitkan di alamat ini ialah versi semasa; tarikh di atas menunjukkan bila ia kali terakhir berubah. Versi terdahulu kekal kelihatan dalam sejarah awam repositori tempat halaman ini diterbitkan supaya anda boleh melihat apa yang berubah dan bila.

---

> **⚠️ Bukan nasihat undang-undang.** Dokumen ini disediakan oleh seorang jurutera berdasarkan kod sumber aplikasi, bukan oleh peguam. Ia menerangkan sistem dengan tepat pada tarikh di atas; setiap kenyataan telah disemak berbanding data yang benar-benar dihantar oleh aplikasi. Dokumen ini **belum** disemak untuk pematuhan GDPR, revDSG Switzerland, CCPA atau peraturan lain. Penerbitannya memenuhi keperluan Apple, tetapi tidak menjadikan anda patuh undang-undang. Minta peguam menyemaknya apabila aplikasi mula menjana pendapatan.
