---
title: Politica de confidențialitate · Calisthenics Skills – Ranked
permalink: /privacy/ro/
---

> Aceasta este o traducere. În caz de diferențe, prevalează [versiunea în limba engleză](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/).

# Politica de confidențialitate · Calisthenics Skills – Ranked

**Ultima actualizare: 2026-10-18**

Această politică descrie ce date colectează Ranked, unde ajung și ce puteți face în privința lor.

Ranked este operată de **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Elveția**, contact **dylan.schmid538@gmail.com**. Ea este operatorul prelucrărilor descrise aici.

---

## 1. Pe scurt

**Vârsta, sexul, înălțimea și greutatea dvs. nu părăsesc niciodată dispozitivul.** Formula de calcul al rangului le folosește pe telefon. Nu sunt trimise nici nouă, nici serviciului de analiză.

Trei tipuri de date pot părăsi dispozitivul:

1. **Statistici de utilizare**, pentru a înțelege cum este folosită aplicația. Le puteți dezactiva oricând în aplicație.
2. **Date despre cumpărături**, pentru verificarea abonamentului App Store. Apple procesează plata; noi nu vedem niciodată detaliile dvs. de plată.
3. **Mesaje de feedback și asistență**, doar dacă alegeți să le trimiteți. Cu acord separat puteți oferi e-mailul sau telefonul pentru răspuns.

Ranked nu vă urmărește între alte aplicații sau site-uri. Statisticile de utilizare și atribuirea campaniilor publicitare descrise mai jos sunt trimise numai dacă ați autorizat ATT și ați activat partajarea datelor de utilizare. Aplicația nu afișează reclame și nu citește date din Apple Health.

---

## 2. Ce rămâne pe dispozitiv

Următoarele sunt stocate în baza de date a aplicației, pe telefon, și nu sunt transmise:

- Fiecare antrenament, serie, repetare, menținere și greutate suplimentară înregistrată
- Planul și programul de antrenament, mementourile și preferințele
- Măsurile corporale introduse de dvs. (vârsta, sexul, înălțimea, greutatea)
- Notele de antrenament

Aplicația nu exclude această bază de date din copia de rezervă a dispozitivului. Dacă folosiți iCloud Backup sau o copie de rezervă pe computer, datele de antrenament sunt incluse și revin la restaurare, în condițiile Apple, nu ale noastre.

Ștergerea aplicației șterge toate acestea de pe dispozitiv. Nu le putem recupera, deoarece nu le-am avut niciodată.

---

## 3. Ce părăsește dispozitivul

### 3.1 Statistici de utilizare (PostHog)

La prima deschidere a aplicației, iOS afișează dialogul standard de autorizare „App Tracking Transparency” (ATT). Ranked trimite evenimente către PostHog în UE numai dacă ați autorizat ATT și ați activat partajarea datelor de utilizare în Setări. Dacă autorizarea nu este acordată sau partajarea este dezactivată, aceste date nu sunt trimise. Ranked trimite către PostHog evenimente privind configurarea, evaluarea inițială, schimbările de rang și etapă (cu abilitatea și etapa), ecranul de cumpărare, achizițiile și ecranele deschise. Evenimentele antrenamentelor în timp real includ începutul, finalizarea sau abandonarea, secundele scurse, numărul de seturi înregistrate, numărul de abilități diferite și dacă a fost primul antrenament finalizat. Nu includ exerciții individuale, repetări, greutăți sau note. Vârsta, sexul, înălțimea și greutatea corporală nu sunt transmise. PostHog primește și informații tehnice obișnuite despre dispozitiv, iOS, aplicație și limbă, precum și adresa IP, din care se poate deduce o locație aproximativă. Un identificator aleatoriu de instalare PostHog este creat după autorizarea ATT și activarea partajării datelor de utilizare. Evenimentele și datele de atribuire a campaniilor sunt asociate acestui identificator pentru analiză și măsurarea eficienței publicitare. Puteți revoca autorizarea ATT în configurările iOS și puteți dezactiva partajarea datelor de utilizare în Ranked, Setări ▸ Date și confidențialitate; noile evenimente se opresc, dar datele deja trimise nu sunt șterse automat.

### 3.2 Atribuirea Apple Search Ads

Numai dacă ați autorizat ATT și ați activat partajarea datelor de utilizare, Ranked întreabă o singură dată Apple AdServices dacă instalarea provine din Apple Search Ads. După un clic pe reclamă, campania, grupul, cuvântul-cheie, materialul publicitar, țara sau regiunea, data clicului și tipul descărcării pot fi asociate identificatorului aleatoriu PostHog. IDFA nu este folosit. Transmiterea viitoare se oprește dacă revocați autorizarea ATT în configurările iOS sau dezactivați partajarea datelor de utilizare în Setările Ranked.

### 3.3 Cumpărături (Apple și RevenueCat)

Abonamentele sunt vândute și facturate de **Apple** prin App Store. Nu vedem niciodată detaliile dvs. de plată, contul Apple sau numele dvs.

Pentru a verifica dacă abonamentul este activ, aplicația folosește **RevenueCat**. RevenueCat primește înregistrarea cumpărării din App Store — produsul cumpărat, data începerii și data expirării — împreună cu informații tehnice standard, precum versiunea iOS și a aplicației. Identifică instalarea printr-un identificator aleatoriu generat de RevenueCat și stocat pe dispozitiv. Nu îi transmitem numele, adresa de e-mail sau altă identitate; Ranked nu are conturi, deci nu există o asemenea identitate de transmis.

Când apăsați **Restaurare cumpărături**, aplicația cere de la Apple cumpărăturile făcute cu contul Apple conectat pe dispozitiv și transmite rezultatul către RevenueCat în același mod.

### 3.4 Mesaje de feedback și asistență (Cloudflare și CloudKit)

Dacă trimiteți feedback sau o cerere de asistență, Ranked transmite mesajul, categoria și sursa către un Cloudflare Worker. Acesta le stochează în baza de date publică Apple CloudKit folosind o cheie privată de server. Nu trebuie să vă conectați la iCloud pentru a trimite un mesaj. Cloudflare Worker folosește adresa de rețea a cererii pentru o limită tehnică împotriva abuzurilor; nici adresa inițială, nici o amprentă a ei nu sunt stocate în înregistrarea de feedback din CloudKit. Puteți consimți separat să furnizați o adresă de e-mail sau un număr de telefon pentru a primi un răspuns în afara aplicației. Mesajele și datele de contact nu sunt trimise către PostHog sau RevenueCat și nu sunt asociate unui cont din aplicație. Prelucrăm mesajul pentru a răspunde cererii dumneavoastră și datele de contact opționale pe baza consimțământului dumneavoastră. În prezent nu este aplicată o perioadă fixă de ștergere automată pentru mesaje sau datele de contact. Puteți solicita accesul sau ștergerea la **dylan.schmid538@gmail.com**.

---

## 4. Ce nu face Ranked

- **Fără conturi.** Nu vă conectați niciodată. Nu există un profil despre dvs. pe vreun server.
- **Fără Apple Health.** Ranked nu citește și nu scrie în aplicația Health.
- **Fără cameră, fotografii, microfon, locație sau contacte.** Aplicația nu cere aceste permisiuni.
- **Ranked nu vă urmărește între alte aplicații sau site-uri.** Statisticile de utilizare și măsurarea campaniilor descrise la §3 sunt folosite numai după autorizarea ATT și activarea partajării datelor de utilizare; IDFA nu este utilizat. Aplicația nu afișează reclame, iar datele nu sunt vândute sau transmise brokerilor de date.
- **Fără server de notificări push.** Mementourile sunt programate local pe telefon; nimic despre ele nu părăsește dispozitivul. Vi se cere permisiunea înainte de primul memento și le puteți dezactiva oricând în configurările iOS.

---

## 5. Temeiul juridic (GDPR și legea elvețiană revDSG)

| Prelucrare | Temei |
|---|---|
| Cumpărături și verificarea abonamentului (§3.3) | Executarea unui contract |
| Statistici de utilizare (§3.1) | Consimțământul dvs.; poate fi retras oricând în Setări ▸ Date și confidențialitate |
| Atribuirea Search Ads (§3.2) | Consimțământul dvs.; poate fi retras oricând în Setări ▸ Date și confidențialitate |

**Se aplică două legi, nu una.** Ranked este operată din Elveția, deci prelucrarea este guvernată de Legea federală elvețiană revizuită privind protecția datelor (**revDSG**, în vigoare din septembrie 2023). **GDPR** se aplică suplimentar oriunde aplicația este utilizată din Uniunea Europeană sau Regatul Unit. Dacă diferă, urmăm regula mai strictă. Rezidenții elvețieni au aceleași drepturi de bază enumerate la §8 potrivit art. 25 și următoarele din revDSG.

---

## 6. Unde sunt prelucrate datele

- **PostHog** prelucrează statisticile de utilizare în Uniunea Europeană.
- **RevenueCat, Inc.** are sediul în Statele Unite și prelucrează acolo datele despre cumpărături descrise la §3.3.
- **Apple** prelucrează cumpărarea și cererea de atribuire Search Ads potrivit propriei politici de confidențialitate, aplicabilă contului dvs. Apple independent de această aplicație.

---

## 7. Cât timp păstrăm datele

Statisticile de utilizare sunt păstrate cât timp se aplică perioada de retenție PostHog pentru planul nostru. Nu promitem un număr fix de luni, deoarece PostHog nu ne permite să îl stabilim, iar o durată pe care nimeni nu o poate respecta este mai rea într-o politică de confidențialitate decât lipsa uneia.

RevenueCat păstrează înregistrările cumpărăturilor cât timp există abonamentul și istoricul său, așa cum este necesar pentru verificarea abonamentului.

Tot ce este pe dispozitiv rămâne acolo până ștergeți aplicația.

---

## 8. Drepturile dvs.

Puteți opri oricând transmiterea viitoare a datelor analitice revocând autorizarea ATT în configurările iOS sau dezactivând partajarea datelor de utilizare în Ranked: Setări ▸ Date și confidențialitate. Datele deja trimise nu sunt șterse automat, iar abonamentul App Store nu este anulat.

Puteți șterge datele locale de antrenament în Setări ▸ Date și confidențialitate ▸ *Șterge datele locale de antrenament* sau prin ștergerea aplicației. Abonamentul se gestionează și se anulează separat în Contul Apple.

Pentru datele deja trimise către PostHog, scrieți la **dylan.schmid538@gmail.com**. Ranked nu leagă identificatorul aleatoriu de un cont. O dată aproximativă sau modelul dispozitivului pot să nu fie suficiente pentru identificarea sigură a profilului. Vom explica ce putem identifica și vom procesa cererile verificabile de acces, rectificare sau ștergere. Nu trimiteți datele de acces ale Contului Apple.

Puteți solicita restricționarea prelucrării și depune plângere la autoritatea de supraveghere din țara dvs.; în Elveția este Comisarul federal pentru protecția datelor și transparență (FDPIC).

---

## 9. Copiii

Ranked este destinată persoanelor de **16 ani și peste**. Aplicația vă cere vârsta în timpul configurării deoarece formula rangului depinde de ea și nu se adresează celor mai tineri. Nu colectăm cu bună știință date de la persoane sub 16 ani.

---

## 10. Modificări

Versiunea publicată la această adresă este cea actuală, iar data de sus arată când a fost modificată ultima dată. Versiunile anterioare rămân vizibile în istoricul public al depozitului din care sunt publicate aceste pagini, astfel încât puteți vedea ce s-a schimbat și când.

---
