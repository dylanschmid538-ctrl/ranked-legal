---
title: Kebijakan Privasi · Calisthenics Skills – Ranked
permalink: /privacy/id/
---

> *Ini adalah terjemahan. Jika terdapat perbedaan, [versi bahasa Inggris](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/) yang berlaku.*

# Kebijakan Privasi · Calisthenics Skills – Ranked

**Terakhir diperbarui: 2026-10-18**

Kebijakan ini menjelaskan data apa yang dikumpulkan Ranked, ke mana data tersebut dikirim, dan apa yang dapat Anda lakukan.

Ranked dioperasikan oleh **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Swiss**, kontak **dylan.schmid538@gmail.com**. Beliau adalah pengendali pemrosesan yang dijelaskan di sini.

---

## 1. Ringkasan

**Usia, jenis kelamin, tinggi badan, dan berat badan Anda tidak pernah meninggalkan perangkat.** Rumus peringkat menggunakannya di ponsel Anda. Data itu tidak dikirim kepada kami ataupun layanan analitik.

Tiga jenis data dapat meninggalkan perangkat Anda:

1. **Statistik penggunaan**, agar kami memahami cara aplikasi digunakan. Anda dapat menonaktifkannya kapan saja di aplikasi.
2. **Data pembelian**, agar langganan App Store dapat diverifikasi. Apple menangani pembayaran; kami tidak pernah melihat rincian pembayaran Anda.
3. **Pesan masukan dan dukungan**, hanya jika Anda memilih untuk mengirimnya. Anda dapat memberi persetujuan terpisah untuk menyertakan email atau nomor telepon agar kami dapat membalas.

Ranked tidak menampilkan iklan dan tidak membaca data dari Apple Health. Setelah ATT diizinkan, Ranked otomatis mengaktifkan berbagi data penggunaan; pengiriman berlanjut selama tombol berbagi di Pengaturan Ranked tetap aktif. Data penggunaan dan atribusi instalasi Apple Search Ads dapat ditautkan untuk pengukuran; lihat §3.1–3.2.

Setelah Anda mengizinkan ATT pada peluncuran pertama, Ranked otomatis mengaktifkan berbagi data penggunaan. Data dikirim selama ATT diizinkan dan tombol berbagi tetap aktif di Pengaturan Ranked. Anda dapat mematikan berbagi kapan saja di Pengaturan Ranked. Pengumpulan dan pengiriman berikutnya juga berhenti jika Anda mencabut ATT di Pengaturan iOS; data yang sudah dikirim tidak dihapus.

---

## 2. Data yang tetap berada di perangkat

Data berikut disimpan di basis data aplikasi pada ponsel Anda dan tidak pernah dikirim:

- Setiap latihan, set, repetisi, durasi tahan, dan beban tambahan yang Anda catat
- Rencana latihan, jadwal, pengingat, dan preferensi
- Ukuran tubuh yang Anda masukkan (usia, jenis kelamin, tinggi badan, berat badan)
- Catatan latihan

Aplikasi tidak mengecualikan basis data ini dari cadangan perangkat. Jika Anda memakai Cadangan iCloud atau cadangan komputer, data latihan menjadi bagian dari cadangan itu dan kembali saat Anda memulihkannya — sesuai ketentuan Apple, bukan ketentuan kami.

Menghapus aplikasi akan menghapus semua data tersebut dari perangkat. Kami tidak dapat memulihkannya karena kami tidak pernah memilikinya.

---

## 3. Data yang meninggalkan perangkat

### 3.1 Statistik penggunaan (PostHog)

Saat pertama kali aplikasi dibuka, iOS menampilkan dialog standar Apple untuk izin pelacakan (App Tracking Transparency, ATT). Setelah Anda mengizinkan ATT, Ranked otomatis mengaktifkan berbagi data penggunaan. Ranked hanya mengirim peristiwa ke PostHog di UE selama ATT diizinkan dan tombol berbagi di Pengaturan Ranked tetap aktif. Peristiwa mencakup langkah penyiapan dan hasil penilaian awal, perubahan peringkat dan tahap (beserta keahlian dan tahap), layar pembelian dan pembelian, layar yang dibuka, serta mulai, selesai atau ditinggalkannya latihan langsung; peristiwa ini juga mencakup detik yang berlalu, jumlah set yang dicatat, jumlah keahlian berbeda, dan apakah itu latihan pertama yang selesai. Peristiwa tidak mencakup latihan individual, repetisi, beban, atau catatan. Usia, jenis kelamin, tinggi dan berat badan tidak dikirim. PostHog juga menerima informasi teknis umum tentang perangkat, iOS, aplikasi, bahasa dan alamat IP yang dapat menunjukkan lokasi perkiraan. Peristiwa ditautkan di bawah ID instalasi PostHog yang acak untuk analitik dan pengukuran iklan; IDFA tidak digunakan. Menonaktifkan tombol berbagi di Pengaturan Ranked atau mencabut izin ATT di Pengaturan iOS menghentikan pengumpulan dan pengiriman berikutnya. Peristiwa yang sudah dikirim tidak otomatis dihapus.

### 3.2 Atribusi Apple Search Ads

Ranked meminta atribusi instalasi dari Apple AdServices hanya selama ATT diizinkan dan tombol berbagi di Pengaturan Ranked tetap aktif. Jika Anda mengetuk iklan, kampanye, grup iklan, kata kunci, materi iklan, negara atau wilayah, tanggal ketukan dan jenis unduhan dapat ditautkan ke ID instalasi PostHog yang sama untuk pengukuran iklan. ID iklan IDFA tidak digunakan. Mencabut izin atau menonaktifkan berbagi menghentikan permintaan dan pengiriman berikutnya; data yang sudah dikirim tidak dihapus.

### 3.3 Pembelian (Apple dan RevenueCat)

Langganan dijual dan ditagihkan oleh **Apple** melalui App Store. Kami tidak pernah melihat rincian pembayaran, Akun Apple, atau nama Anda.

Untuk memeriksa apakah langganan aktif, aplikasi menggunakan **RevenueCat**. RevenueCat menerima catatan pembelian App Store untuk langganan Anda — produk yang dibeli, kapan dimulai dan berakhir — bersama informasi teknis standar seperti versi iOS dan aplikasi. RevenueCat mengenali pemasangan aplikasi melalui pengenal acak yang dibuatnya sendiri dan disimpan di perangkat Anda. Kami tidak memberikan nama, email, atau identitas lain kepada RevenueCat; karena Ranked tidak memiliki akun, tidak ada identitas akun untuk diberikan.

Saat Anda mengetuk **Pulihkan Pembelian**, aplikasi meminta Apple memberikan pembelian yang dilakukan dengan Akun Apple yang masuk pada perangkat lalu menyampaikan hasilnya kepada RevenueCat dengan cara yang sama.

### 3.4 Pesan masukan dan dukungan (Cloudflare dan CloudKit)

Jika Anda mengirim masukan atau permintaan dukungan, Ranked mengirim pesan, kategori, dan sumber ke Cloudflare Worker. Layanan tersebut menyimpannya di basis data publik Apple CloudKit menggunakan kunci server pribadi. Anda tidak perlu masuk ke iCloud untuk mengirim pesan. Cloudflare Worker menggunakan alamat jaringan permintaan untuk pembatasan teknis terhadap penyalahgunaan; alamat asli maupun hash-nya tidak disimpan dalam catatan masukan CloudKit. Anda dapat memberikan persetujuan terpisah untuk menyertakan alamat email atau nomor telepon agar kami dapat membalas di luar aplikasi. Pesan dan informasi kontak tidak dikirim ke PostHog atau RevenueCat dan tidak dihubungkan dengan akun aplikasi. Kami memproses pesan untuk menanggapi permintaan Anda dan informasi kontak opsional berdasarkan persetujuan Anda. Saat ini tidak ada batas waktu tetap untuk penghapusan otomatis pesan atau informasi kontak. Anda dapat meminta akses atau penghapusan melalui **dylan.schmid538@gmail.com**.

---

## 4. Hal yang tidak dilakukan Ranked

- **Tidak ada akun.** Anda tidak perlu masuk. Tidak ada profil tentang Anda di server mana pun.
- **Tidak ada Apple Health.** Ranked tidak membaca dari atau menulis ke aplikasi Kesehatan.
- **Tidak ada kamera, foto, mikrofon, lokasi, atau kontak.** Aplikasi tidak meminta izin tersebut.
- **Pelacakan dan atribusi:** Ranked tidak menggunakan IDFA. Data penggunaan dan atribusi instalasi Apple Search Ads dapat ditautkan untuk pengukuran iklan hanya jika ATT diizinkan dan berbagi data penggunaan diaktifkan. Tidak ada iklan di dalam aplikasi, dan data tidak dijual atau diberikan kepada broker data.
- **Tidak ada server pemberitahuan push.** Pengingat dijadwalkan secara lokal di ponsel; tidak ada informasinya yang meninggalkan perangkat. Izin diminta sebelum pengingat pertama dijadwalkan, dan Anda dapat menonaktifkannya kapan saja di Pengaturan iOS.

---
## 5. Dasar hukum (GDPR dan UU Perlindungan Data Swiss yang direvisi)

| Pemrosesan | Dasar hukum |
|---|---|
| Pembelian dan verifikasi langganan (§3.3) | Pelaksanaan kontrak |
| Statistik penggunaan (§3.1) | Persetujuan Anda untuk berbagi data penggunaan dan izin ATT dari Apple; masing-masing dapat dicabut kapan saja. Menonaktifkan berbagi data di Pengaturan Ranked atau mencabut ATT di Pengaturan iOS menghentikan pengumpulan berikutnya; data yang sudah dikirim tidak dihapus. |
| Atribusi Search Ads (§3.2) | Persetujuan Anda untuk berbagi data penggunaan dan izin ATT dari Apple; masing-masing dapat dicabut kapan saja. Menonaktifkan berbagi data di Pengaturan Ranked atau mencabut ATT di Pengaturan iOS menghentikan pengumpulan berikutnya; data yang sudah dikirim tidak dihapus. |

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

Anda dapat menonaktifkan berbagi data penggunaan kapan saja di Pengaturan Ranked ▸ Data & privasi dan mencabut izin ATT di Pengaturan iOS. Masing-masing tindakan menghentikan pengumpulan dan pengiriman berikutnya. Data yang sudah dikirim tidak otomatis dihapus dan langganan App Store tidak dibatalkan.

Anda dapat menghapus data latihan lokal di Pengaturan ▸ Data & privasi ▸ *Hapus data latihan lokal* atau dengan menghapus aplikasi. Langganan dikelola dan dibatalkan secara terpisah di Akun Apple Anda.

Untuk data yang sudah dikirim ke PostHog, tulis ke **dylan.schmid538@gmail.com**. Ranked tidak menghubungkan ID analitik acak dengan akun. Tanggal perkiraan atau model perangkat mungkin tidak cukup untuk menemukan profil secara andal. Kami akan menjelaskan data yang dapat diidentifikasi dan memproses permintaan akses, koreksi atau penghapusan yang dapat diverifikasi. Jangan kirim kredensial Akun Apple.

Anda dapat meminta pembatasan pemrosesan dan mengajukan keluhan kepada otoritas pengawas di negara Anda; di Swiss kepada Komisaris Federal Perlindungan Data dan Informasi (FDPIC).

---

## 9. Anak-anak

Ranked ditujukan bagi orang yang berusia **16 tahun ke atas**. Aplikasi menanyakan usia saat penyiapan karena rumus peringkat bergantung padanya, dan tidak ditujukan kepada siapa pun yang lebih muda. Kami tidak dengan sengaja mengumpulkan data dari anak di bawah 16 tahun.

---

## 10. Perubahan

Versi yang diterbitkan di alamat ini adalah versi yang berlaku, dan tanggal di bagian atas menunjukkan kapan terakhir diperbarui. Versi sebelumnya tetap dapat dilihat dalam riwayat publik repositori tempat halaman ini diterbitkan, sehingga Anda dapat mengetahui apa yang berubah dan kapan.

---
