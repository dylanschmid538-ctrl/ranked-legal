---
title: Privātuma politika
permalink: /privacy/lv/
---

*Šis ir tulkojums. Neatbilstības gadījumā noteicošā ir angļu valodas versija, kas pieejama vietnē https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/.*

# Privātuma politika · Calisthenics Skills – Ranked

**Pēdējoreiz atjaunināts: 2026. gada 23. augusts**

Šī politika apraksta, ko Ranked vāc, kurp šie dati nonāk un ko Jūs varat par to darīt. Tā ir
sagatavota, balstoties uz lietotnes faktisko kodu un datubāzes shēmu, nevis pēc veidnes — ja kaut kas
šeit ir nepareizi, jāpārbauda ir kods.

Lietotni Ranked nodrošina **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Šveice**, kontaktinformācija **dylan.schmid538@gmail.com**.

---

## 1. Īsā versija

Gandrīz viss, ko Ranked zina par Jūsu treniņiem, paliek Jūsu tālrunī. Jūsu treniņu vēsture, Jūsu
progress katrā prasmē, Jūsu rangs un Jūsu ķermeņa karte tiek glabāti lokāli un nekad netiek augšupielādēti.

Četras lietas Jūsu ierīci pamet: Jūsu pieteikšanās identitāte, neliels profils, ko izmanto līderu
saraksti, ieraksti par to, ka esat izpildījis apstiprinātu mēģinājumu, un anonīma lietojuma
analītika. Katra no tām ir izskaidrota turpmāk.

**Jūsu apstiprināto mēģinājumu video nekad nepamet Jūsu ierīci.** Tiek nosūtīts tikai faila nospiedums.

---

## 2. Kas paliek Jūsu ierīcē

Lokāli glabājas lietotnes pašas datubāzē un nekad netiek pārraidīts:

- Katrs treniņš, piegājiens, atkārtojums, izturēšana un pievienotais svars, ko Jūs reģistrējat
- Jūsu progress katrā prasmē un posmā, kā arī Jūsu rangu vēsture
- Jūsu treniņu plāns, grafiks un iestatījumi
- Jūsu ķermeņa mērījumi tādā veidā, kā Jūs tos ievadījāt (vecums, dzimums, augums, ķermeņa svars) — daļas
  no tiem kopija tiek nosūtīta arī līderu sarakstu pakalpojumam, skatīt 3.2. punktu
- **Apstiprināto mēģinājumu video faili.** Tie tiek ierakstīti lietotnes privātajā krātuvē. Tie
  netiek augšupielādēti, netiek dublēti mūsu serveros un nav mums pieejami.

Lietotnes dzēšana izdzēš visu šo. Mēs to nevaram atjaunot.

---

## 3. Kas pamet Jūsu ierīci

### 3.1. Jūsu konts
Kad Jūs piesakāties ar Apple vai Google, mēs saņemam un glabājam lietotāja identifikatoru un —
atkarībā no tā, ko Jūs pieteikšanās brīdī atļaujat — e-pasta adresi. To apstrādā **Supabase**, kas
mitina mūsu datubāzi un autentifikāciju.

Kad Jūs piesakāties ar Apple, mēs glabājam arī atsvaidzināšanas pilnvaru (refresh token), ko Apple
mums tajā brīdī izsniedz. Tai ir tikai viens mērķis: Jūsu konta dzēšana pēc tam atsauc arī Ranked
piekļuvi Jūsu Apple ID, kā to prasa Apple. Kontiem, kuru pēdējā pieteikšanās notikusi pirms šīs
pilnvaras saglabāšanas ieviešanas, pilnvara netiek glabāta — dzēšana tad vienkārši izlaiž atsaukšanas
soli.

### 3.2. Jūsu līderu saraksta profils
Lai ierindotu Jūs līderu sarakstā un salīdzinātu Jūs ar līdzīgas uzbūves cilvēkiem, mūsu serverī
tiek glabāts:

- nejauši ģenerēts **drauga kods**
- Jūsu **vecums**, **dzimums** un **ķermeņa svars**
- Jūsu profila izveides datums

**Piezīme par redzamību:** jebkurš Ranked lietotājs, kurš ir pieteicies, var atrast profilu pēc tā
drauga koda. Tāds ir drauga koda mērķis — tas pastāv, lai to kādam nodotu. Nedaliet savu kodu ne ar
vienu, kam Jūs nevēlaties ļaut redzēt savu ierakstu. Tas, ko citi lietotāji var redzēt, ir Jūsu
drauga kods un Jūsu pozīcija līderu sarakstā — nekas cits. Jūsu vecums, dzimums un ķermeņa svars
tiek izmantoti salīdzinājumam serverī, un tie nekad netiek rādīti citiem lietotājiem un nav viņiem
lejupielādējami.

Jūsu **augums** netiek nosūtīts. Jūsu treniņu vēsture netiek nosūtīta.

### 3.3. Apstiprinātie mēģinājumi
Kad Jūs ierakstāt apstiprinātu mēģinājumu, mēs glabājam: Jūsu lietotāja id, to, kurai prasmei un
posmam mēģinājums bija paredzēts, **video faila kriptogrāfisko jaucējvērtību (hash)** un ieraksta
veikšanas laiku.

Jaucējvērtība ir nospiedums. To nav iespējams pārvērst atpakaļ par video. Tā pastāv, lai mēģinājumu
varētu sasaistīt ar konkrētu ierakstu, šim ierakstam nekad nepametot Jūsu tālruni.

### 3.4. Draugi
Ja Jūs pievienojat kādu pēc viņa drauga koda, mēs glabājam saikni starp Jūsu un viņa kontu, kā arī
Jūsu dalību jebkurā draugu grupā.

### 3.5. Lietojuma analītika
Mēs izmantojam **PostHog**, kas mitināts **Eiropas Savienībā**, lai saprastu, kā lietotne tiek
lietota. Mēs reģistrējam tādus notikumus kā to, līdz kuram ievadīšanas solim Jūs nonācāt, kad
treniņš tika pabeigts, kad mainījās rangs un vai pirkuma ekrāns tika parādīts vai aizvērts.

Šie notikumi ietver Jūsu rangu un Jūsu progresu lietotnē. Tie **neietver** Jūsu vārdu, e-pasta
adresi, augumu vai Jūsu treniņu saturu.

---

## 4. Pirkumi

Abonementus apstrādā **Apple**. Mēs nekad neredzam Jūsu maksājumu datus. **RevenueCat** mūsu vārdā
pārvalda Jūsu abonementa statusu un saņem pseidonimizētu identifikatoru un Jūsu abonementa stāvokli.
Pats pirkuma ekrāns ir lietotnes daļa; neviena trešā persona neizlemj, kurš no tiem Jums tiek
parādīts.

---

## 5. Kamera un mikrofons

Ranked pieprasa piekļuvi kamerai un mikrofonam vienai funkcijai: apstiprināta mēģinājuma ierakstīšanai.
Ieraksts tiek saglabāts Jūsu ierīcē. Tas nekad netiek augšupielādēts. Ja Jūs piekļuvi atsakāt, visas
pārējās lietotnes daļas turpina darboties.

---

## 6. Veselības dati

Ranked **nelasa** datus no Apple Health un tos tur **neieraksta**.

Jūsu vecums, dzimums un ķermeņa svars ir ar veselību saistīti dati, un saskaņā ar VDAR tie var
kvalificēties kā veselības dati. Mēs tos vācam vienam mērķim — ranga formula normalizē sniegumu pēc
ķermeņa uzbūves, tāpēc 95 kg smags sportists un 60 kg smags sportists, kas notur vienu un to pašu
sviru, netiek vērtēti tā, it kā viņi būtu paveikuši vienu un to pašu — un mēs uz serveri nosūtām
mazāko no tiem apjomu, kāds līderu saraksta salīdzinājumam ir nepieciešams.

---

## 7. Tiesiskais pamats (VDAR un Šveices revDSG)

| Kas | Pamats |
|---|---|
| Konts un pieteikšanās | Līguma izpilde — lietotnei ir nepieciešams konts |
| Vecums, dzimums un ķermeņa svars | Līguma izpilde — rangs tiek pēc tiem normalizēts, un bez tiem to nav iespējams aprēķināt |
| Drauga kods, draugu grupas | Līguma izpilde — funkcija ir iemesls, kāpēc šie dati pastāv |
| Apstiprinātu mēģinājumu ieraksti un līderu saraksta ieraksts, ko katrs no tiem rada | Piekrišana, kas dota ar apzinātu darbību — mēģinājuma ierakstīšanu. Atsauciet to, dzēšot mēģinājumu attiecīgā posma lapā, kas izdzēš ierakstu — skatīt 9. punktu |
| Pirkumi | Līguma izpilde |
| Analītika | Leģitīmās intereses uzlabot lietotni; Jūs jebkurā laikā varat iebilst iestatījumos, skatīt 9. punktu |

**Šeit piemēro divus tiesību aktus, ne vienu.** Ranked tiek nodrošināta no Šveices, tāpēc uz šo
apstrādi attiecas pārskatītais Šveices Federālais datu aizsardzības likums (**revDSG**, spēkā kopš
2023. gada septembra). **VDAR** piemēro papildus visur, kur lietotne tiek lietota no Eiropas
Savienības vai Apvienotās Karalistes. Ja abi atšķiras, mēs ievērojam stingrāko. Šveices iedzīvotājiem
ir tās pašas pamattiesības, kas uzskaitītas 9. punktā — piekļuve, labošana, dzēšana, pārnesamība un
iebilšana —, saskaņā ar revDSG 25. un turpmākajiem pantiem.

---

## 8. Cik ilgi mēs to glabājam

Konta, profila, draugu un apstiprināto mēģinājumu ieraksti tiek glabāti, līdz Jūs dzēšat savu kontu.
Konta dzēšana tos noņem.

Analītikas notikumi tiek glabāti tik ilgi, cik uz mūsu plānu attiecas paša PostHog glabāšanas
termiņš. **Jūsu konta dzēšana tos neizdzēš**, un mēs to sakām skaidri, nevis liekam saprast pretējo:
analītikas profils nav saistīts ar Jūsu kontu — tas izmanto atsevišķu, lietotnes ģenerētu
identifikatoru —, tāpēc nav saiknes, pēc kuras mēs to varētu atrast un noņemt. Kas tajā ir ietverts,
ir uzskaitīts 3.5. punktā: lietojuma notikumi, Jūsu rangs un Jūsu ievadītais vecums, dzimums un
ķermeņa svars. Tajā nav ne vārda, ne e-pasta adreses, ne konta id.

Ja Jūs vēlaties, lai arī šis profils tiktu noņemts, rakstiet mums, norādot aptuveno datumu, kad
pirmoreiz lietojāt lietotni, un mēs to atradīsim un izdzēsīsim manuāli.

---

## 9. Jūsu tiesības

Jūs jebkurā laikā varat:

- **Dzēst savu kontu** lietotnes iestatījumos. Tas izdzēš Jūsu servera puses profilu, Jūsu draugu
  saiknes un Jūsu apstiprināto mēģinājumu ierakstus. Ja Jūsu kontam ir saglabāta Apple
  atsvaidzināšanas pilnvara (skatīt 3.1. punktu), tas atsauc arī Ranked piekļuvi Jūsu Apple ID. Dati,
  kas glabājas tikai Jūsu ierīcē, tiek noņemti, dzēšot lietotni.
- **Atsaukt apstiprinātu mēģinājumu** lietotnē attiecīgā posma lapā. Mēģinājuma dzēšana izdzēš
  ierakstu un līderu saraksta ierakstu, ko tas radīja, un atsauc piekrišanu, kas dota ar tā
  ierakstīšanu. Atsaukšana neietekmē to, kas bija tiesisks pirms atsaukuma.
- **Pieprasīt kopiju** no datiem, kas mums par Jums ir, vai lūgt mums tos labot.
- **Iebilst pret analītiku** ar slēdzi iestatījumos vai rakstot mums.
- **Iesniegt sūdzību uzraudzības iestādē** savā valstī.

Jebkurā no šiem gadījumiem rakstiet uz **dylan.schmid538@gmail.com**.

---

## 10. Bērni

Ranked nav paredzēta bērniem, kas jaunāki par 13 gadiem, un mēs apzināti nevācam viņu datus.

---

## 11. Izmaiņas

Ja šī politika būtiski mainīsies, lietotne Jums par to paziņos pirms izmaiņu stāšanās spēkā.

---

> **⚠️ Nav juridiska konsultācija.** Šo dokumentu, balstoties uz lietotnes pirmkodu un datubāzes
> shēmu, sagatavojis inženieris, nevis jurists. Tas precīzi apraksta sistēmu uz iepriekš norādīto
> datumu — katrs tajā ietvertais apgalvojums tika pārbaudīts pret to, ko lietotne faktiski nosūta.
> Tas **nav** pārbaudīts attiecībā uz atbilstību VDAR, Šveices revDSG, CCPA vai jebkuram citam
> regulējumam. Tā publicēšana apmierina Apple prasības; tā nepadara Jūs atbilstīgu tiesību aktiem.
> Ļaujiet juristam to izlasīt, tiklīdz lietotne sāk pelnīt naudu.
