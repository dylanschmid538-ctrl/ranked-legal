---
title: Politica de confidențialitate · Calisthenics Skills – Ranked
permalink: /privacy/ro/
---

> Aceasta este o traducere. În caz de diferențe, prevalează [versiunea în limba engleză](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/).

# Politica de confidențialitate · Calisthenics Skills – Ranked

**Ultima actualizare: 29 septembrie 2026**

Această politică descrie ce date colectează Ranked, unde ajung și ce puteți face în privința lor. A fost redactată pe baza codului efectiv al aplicației, nu a unui șablon; dacă ceva de aici este greșit, codul trebuie verificat.

Ranked este operată de **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Elveția**, contact **dylan.schmid538@gmail.com**. Ea este operatorul prelucrărilor descrise aici.

---

## 1. Pe scurt

Ranked **nu are conturi de utilizator și nici server propriu**. Tot ce ține de antrenamentul dvs. — fiecare serie înregistrată, progresul la fiecare abilitate, rangul, Power Level și harta corpului — este stocat pe telefon și nu este încărcat nicăieri.

**Vârsta, sexul, înălțimea și greutatea dvs. nu părăsesc niciodată dispozitivul.** Formula de calcul al rangului le folosește pe telefon. Nu sunt trimise nici nouă, nici serviciului de analiză.

Doar două categorii de date părăsesc dispozitivul:

1. **Statistici anonime de utilizare**, pentru a înțelege cum este folosită aplicația. Le puteți dezactiva oricând în aplicație.
2. **Date despre cumpărături**, pentru verificarea abonamentului App Store. Apple procesează plata; noi nu vedem niciodată detaliile dvs. de plată.

Ranked nu vă urmărește între alte aplicații sau site-uri, nu afișează reclame și nu citește date din Apple Health.

---

## 2. Ce rămâne pe dispozitiv

Următoarele sunt stocate în baza de date a aplicației, pe telefon, și nu sunt transmise:

- Fiecare antrenament, serie, repetare, menținere și greutate suplimentară înregistrată
- Progresul la fiecare abilitate și etapă, istoricul rangurilor și Power Level
- Planul și programul de antrenament, mementourile și preferințele
- Măsurile corporale introduse de dvs. (vârsta, sexul, înălțimea, greutatea)
- Notele de antrenament

Aplicația nu exclude această bază de date din copia de rezervă a dispozitivului. Dacă folosiți iCloud Backup sau o copie de rezervă pe computer, datele de antrenament sunt incluse și revin la restaurare, în condițiile Apple, nu ale noastre.

Ștergerea aplicației șterge toate acestea de pe dispozitiv. Nu le putem recupera, deoarece nu le-am avut niciodată.

---

## 3. Ce părăsește dispozitivul

### 3.1 Statistici de utilizare (PostHog)

Folosim **PostHog**, găzduit în **Uniunea Europeană**, pentru a înțelege utilizarea aplicației. Aplicația trimite o listă fixă de evenimente:

- ce pas de configurare ați atins, finalizat sau din care v-ați întors și durata fiecărui pas;
- rezultatul evaluării inițiale: câte linii de abilități și etape ați revendicat, abilitatea aleasă drept obiectiv, rangul inițial și rangul fiecăreia dintre cele șase regiuni ale corpului;
- când a fost afișat sau închis ecranul de cumpărare și când o cumpărare a fost inițiată, finalizată sau restaurată, cu produsul și oferta aferente; când aplicația observă ulterior o perioadă activă de probă sau de abonament plătit, cu produsul și informația dacă este o cumpărare în mediul de testare (aceasta nu este o evidență a fiecărei plăți și nu se transmite cât timp aplicația este închisă);
- când vi s-a schimbat rangul și ce abilitate a declanșat schimbarea;
- când ați finalizat o etapă: abilitatea, etapa și dacă a rezultat dintr-o serie înregistrată, un antrenament adăugat ulterior sau o revendicare manuală;
- ce ecrane deschideți și când se încheie un antrenament. Evenimentul de încheiere nu conține detalii: nici exerciții, nici serii, nici cifre.

Software-ul PostHog din aplicație adaugă fiecărui eveniment informații tehnice standard, precum modelul dispozitivului, versiunea iOS, versiunea aplicației, limba și fusul orar, și înregistrează când aplicația este deschisă sau trecută în fundal. Ca orice serviciu de internet, PostHog primește adresa IP a cererii; din aceasta poate deduce o locație aproximativă (țară sau oraș).

**Ce nu este inclus:** numele, adresa de e-mail (aplicația nu o cere), un identificator de cont (nu există), vârsta, sexul, înălțimea, greutatea sau conținutul antrenamentelor.

**Cum sunteți identificat:** PostHog generează la prima pornire un identificator aleatoriu, stocat pe dispozitiv. Toate evenimentele sunt grupate sub acest identificator. Aplicația nu îi spune niciodată PostHog cine sunteți și nu există niciun cont sau e-mail pe care l-ar putea comunica.

**Dezactivare:** Setări ▸ Confidențialitate ▸ *Partajează date anonime de utilizare*. Dezactivarea oprește trimiterea evenimentelor din acel moment. Setarea este stocată pe dispozitiv și rămâne valabilă după actualizările aplicației.

### 3.2 Atribuirea Apple Search Ads

Dacă ați instalat Ranked după ce ați apăsat pe o reclamă Apple Search Ads, la prima lansare aplicația întreabă o singură dată Apple de unde a provenit instalarea. Apple răspunde cu campania, grupul de anunțuri, cuvântul-cheie și setul de materiale creative ale reclamei, țara sau regiunea clicului, data clicului și dacă a fost o descărcare nouă sau repetată. Aplicația atașează aceste valori identificatorului anonim PostHog din §3.1, pentru ca evenimentele ulterioare să poată fi grupate după reclama care v-a adus.

Este folosit framework-ul **AdServices** de la Apple, fără identificatorul publicitar (IDFA); Apple nu consideră acest lucru urmărire, deci nu apare un dialog de permisiune pentru urmărire. Dacă nu ați venit printr-o reclamă, Apple indică acest lucru și nu se atașează nimic altceva. Dezactivarea statisticilor de utilizare (§3.1) oprește și această atribuire.

### 3.3 Cumpărături (Apple și RevenueCat)

Abonamentele sunt vândute și facturate de **Apple** prin App Store. Nu vedem niciodată detaliile dvs. de plată, contul Apple sau numele dvs.

Pentru a verifica dacă abonamentul este activ, aplicația folosește **RevenueCat**. RevenueCat primește înregistrarea cumpărării din App Store — produsul cumpărat, data începerii și data expirării — împreună cu informații tehnice standard, precum versiunea iOS și a aplicației. Identifică instalarea printr-un identificator aleatoriu generat de RevenueCat și stocat pe dispozitiv. Nu îi transmitem numele, adresa de e-mail sau altă identitate; Ranked nu are conturi, deci nu există o asemenea identitate de transmis.

Când apăsați **Restaurare cumpărături**, aplicația cere de la Apple cumpărăturile făcute cu contul Apple conectat pe dispozitiv și transmite rezultatul către RevenueCat în același mod.

---

## 4. Ce nu face Ranked

- **Fără conturi.** Nu vă conectați niciodată. Nu există un profil despre dvs. pe vreun server.
- **Fără Apple Health.** Ranked nu citește și nu scrie în aplicația Health.
- **Fără cameră, fotografii, microfon, locație sau contacte.** Aplicația nu cere aceste permisiuni.
- **Fără urmărire între aplicații sau site-uri**, identificator publicitar, reclame în aplicație ori date vândute sau transmise brokerilor de date.
- **Fără server de notificări push.** Mementourile sunt programate local pe telefon; nimic despre ele nu părăsește dispozitivul. Vi se cere permisiunea înainte de primul memento și le puteți dezactiva oricând în configurările iOS.

---

## 5. Temeiul juridic (GDPR și legea elvețiană revDSG)

| Prelucrare | Temei |
|---|---|
| Cumpărături și verificarea abonamentului (§3.3) | Executarea unui contract |
| Statistici de utilizare (§3.1) | Interesul legitim de a înțelege și îmbunătăți aplicația; vă puteți opune oricând prin dezactivare, vezi §8 |
| Atribuirea Search Ads (§3.2) | Interesul legitim de a ști ce publicitate funcționează; opoziție ca mai sus |

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

Puteți oricând:

- **Dezactiva statisticile de utilizare** în Setări ▸ Confidențialitate. Acesta este dreptul de opoziție și, când prelucrarea se bazează pe consimțământ, de retragere a lui; efectul este imediat și nu trebuie motivat.
- **Șterge datele dvs.** Deoarece Ranked nu deține nimic despre dvs. pe un server, ștergerea aplicației elimină tot ce stochează aplicația însăși.
- **Solicita ștergerea profilului anonim de analiză.** Nu îl putem găsi după nume, fiindcă nu are unul; dacă ne scrieți data aproximativă când ați folosit prima dată aplicația și dispozitivul utilizat, îl vom găsi manual și îl vom șterge.
- **Solicita o copie** a datelor deținute de un serviciu sub identificatorul dvs., **corectarea** lor sau **restricționarea** prelucrării pe durata examinării unei cereri.
- **Depune o plângere la autoritatea de supraveghere** din țara dvs.; în Elveția, Comisarul federal pentru protecția datelor și transparență (FDPIC).

Pentru oricare dintre acestea, scrieți la **dylan.schmid538@gmail.com**.

---

## 9. Copiii

Ranked este destinată persoanelor de **16 ani și peste**. Aplicația vă cere vârsta în timpul configurării deoarece formula rangului depinde de ea și nu se adresează celor mai tineri. Nu colectăm cu bună știință date de la persoane sub 16 ani.

---

## 10. Modificări

Versiunea publicată la această adresă este cea actuală, iar data de sus arată când a fost modificată ultima dată. Versiunile anterioare rămân vizibile în istoricul public al depozitului din care sunt publicate aceste pagini, astfel încât puteți vedea ce s-a schimbat și când.

---

> **⚠️ Nu reprezintă consultanță juridică.** Acest document a fost redactat de un inginer pe baza codului sursă al aplicației, nu de un avocat. Descrie sistemul corect la data de mai sus; fiecare afirmație a fost verificată în raport cu ceea ce transmite efectiv aplicația. **Nu** a fost verificat pentru conformitatea cu GDPR, revDSG elvețian, CCPA sau alte reglementări. Publicarea lui satisface cerința Apple, dar nu vă face conform cu legea. Solicitați revizuirea lui de către un avocat când aplicația începe să genereze venituri.
