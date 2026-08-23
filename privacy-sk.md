---
title: Zásady ochrany osobných údajov
permalink: /privacy/sk/
---

*Toto je preklad. V prípade rozporu je rozhodujúca anglická verzia na adrese https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/.*

# Zásady ochrany osobných údajov · Calisthenics Skills – Ranked

**Posledná aktualizácia: 23. augusta 2026**

Tieto zásady opisujú, čo Ranked zhromažďuje, kam sa to dostáva a čo s tým môžete urobiť. Boli
napísané podľa skutočného kódu aplikácie a schémy databázy, nie podľa šablóny — ak je tu niečo
nesprávne, overiť treba kód.

Aplikáciu Ranked prevádzkuje **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Švajčiarsko**, kontakt **dylan.schmid538@gmail.com**.

---

## 1. Krátka verzia

Takmer všetko, čo Ranked o vašom tréningu vie, zostáva vo vašom telefóne. História vašich tréningov,
váš pokrok v každej zručnosti, vaša hodnosť a vaša mapa tela sú uložené lokálne a nikdy sa
neodosielajú.

Zo zariadenia odchádzajú štyri veci: vaša prihlasovacia identita, malý profil používaný pre
rebríčky, záznamy o tom, že ste absolvovali overený pokus, a anonymná analytika používania. Každá
z nich je vysvetlená nižšie.

**Vaše videá z Overených pokusov nikdy neopustia vaše zariadenie.** Odosiela sa iba odtlačok súboru.

---

## 2. Čo zostáva vo vašom zariadení

Uložené lokálne vo vlastnej databáze aplikácie a nikdy neprenášané:

- Každý tréning, séria, opakovanie, výdrž a pridaná záťaž, ktoré si zaznamenáte
- Váš pokrok v každej zručnosti a v každom stupni a história vašej hodnosti
- Váš tréningový plán, rozvrh a preferencie
- Vaše telesné miery tak, ako ste ich zadali (vek, pohlavie, výška, telesná hmotnosť) — kópia
  niektorých z nich sa odosiela aj službe rebríčkov, pozri § 3.2
- **Videosúbory z Overených pokusov.** Zapisujú sa do súkromného úložiska aplikácie. Neodosielajú
  sa, nezálohujú sa na naše servery a nemáme k nim prístup.

Odstránením aplikácie sa toto všetko vymaže. Nemôžeme to obnoviť.

---

## 3. Čo opúšťa vaše zariadenie

### 3.1 Váš účet
Keď sa prihlásite cez Apple alebo Google, dostávame a ukladáme identifikátor používateľa a, podľa
toho, čo pri prihlásení povolíte, e-mailovú adresu. Zabezpečuje to **Supabase**, ktorý hostí našu
databázu a autentifikáciu.

Keď sa prihlásite cez Apple, ukladáme aj obnovovací token (refresh token), ktorý nám Apple v tej
chvíli odovzdá. Má jediný účel: vymazaním vášho účtu sa zároveň odvolá prístup aplikácie Ranked
k vášmu Apple ID, ako to Apple vyžaduje. Pri účtoch, ktorých posledné prihlásenie prebehlo skôr,
než toto zachytávanie existovalo, nie je uložený žiadny token — vymazanie potom krok odvolania
jednoducho preskočí.

### 3.2 Váš profil v rebríčku
Aby sme vás mohli zaradiť do rebríčka a porovnať s ľuďmi podobnej stavby tela, na našom serveri sa
ukladá:

- náhodne vygenerovaný **kód priateľa**
- váš **vek**, **pohlavie** a **telesná hmotnosť**
- dátum vytvorenia vášho profilu

**Poznámka k viditeľnosti:** ktorýkoľvek prihlásený používateľ aplikácie Ranked si môže profil
vyhľadať podľa jeho kódu priateľa. To je účelom kódu priateľa — existuje na to, aby ste ho niekomu
dali. Nezdieľajte svoj kód s nikým, komu by ste nechceli ukázať svoj záznam. Ostatní používatelia
vidia váš kód priateľa a vaše umiestnenie v rebríčku — nič iné. Váš vek, pohlavie a telesná
hmotnosť sa používajú na porovnanie na serveri a nikdy sa iným používateľom nezobrazujú ani ich
nemôžu stiahnuť.

Vaša **výška** sa neodosiela. História vašich tréningov sa neodosiela.

### 3.3 Overené pokusy
Keď zaznamenáte Overený pokus, ukladáme: vaše používateľské ID, o ktorú zručnosť a ktorý stupeň
pokus išlo, **kryptografický hash videosúboru** a čas jeho zaznamenania.

Hash je odtlačok. Nemožno ho spätne premeniť na video. Existuje preto, aby sa pokus dal priradiť ku
konkrétnej nahrávke bez toho, aby táto nahrávka kedykoľvek opustila váš telefón.

### 3.4 Priatelia
Ak si niekoho pridáte podľa jeho kódu priateľa, ukladáme prepojenie medzi vaším a jeho účtom a vaše
členstvo v prípadných skupinách priateľov.

### 3.5 Analytika používania
Používame **PostHog**, hostovaný v **Európskej únii**, aby sme rozumeli tomu, ako sa aplikácia
používa. Zaznamenávame udalosti, ako je to, ku ktorému kroku úvodného nastavenia ste sa dostali,
kedy bol tréning dokončený, kedy sa zmenila hodnosť a či sa zobrazila alebo zavrela obrazovka
nákupu.

Tieto udalosti nesú vašu hodnosť a váš pokrok v aplikácii. **Nenesú** vaše meno, e-mail, výšku ani
obsah vašich tréningov.

---

## 4. Nákupy

Predplatné spracúva **Apple**. Vaše platobné údaje nikdy nevidíme. **RevenueCat** spravuje v našom
mene stav vášho predplatného a dostáva pseudonymný identifikátor a stav vášho predplatného. Samotná
obrazovka nákupu je súčasťou aplikácie; o tom, ktorá sa vám zobrazí, nerozhoduje žiadna tretia
strana.

---

## 5. Kamera a mikrofón

Ranked žiada o prístup ku kamere a mikrofónu kvôli jedinej funkcii: zaznamenaniu Overeného pokusu.
Nahrávka sa uloží do vášho zariadenia. Nikdy sa neodosiela. Ak prístup odmietnete, každá ďalšia
časť aplikácie funguje ďalej.

---

## 6. Zdravotné údaje

Ranked z Apple Health **nečíta** ani doň **nezapisuje**.

Váš vek, pohlavie a telesná hmotnosť sú údaje blízke zdraviu a podľa GDPR sa môžu kvalifikovať ako
údaje týkajúce sa zdravia. Zhromažďujeme ich na jediný účel — vzorec hodnosti normalizuje výkon
podľa stavby tela, aby 95-kilogramový a 60-kilogramový športovec držiaci ten istý lever neboli
hodnotení, akoby urobili to isté — a na server odosielame z nich len to minimum, ktoré porovnanie
v rebríčku potrebuje.

---

## 7. Právny základ (GDPR a švajčiarsky revDSG)

| Čo | Právny základ |
|---|---|
| Účet a prihlásenie | Plnenie zmluvy — aplikácia si vyžaduje účet |
| Vek, pohlavie a telesná hmotnosť | Plnenie zmluvy — hodnosť je nimi normalizovaná a bez nich ju nemožno vypočítať |
| Kód priateľa, skupiny priateľov | Plnenie zmluvy — táto funkcia je dôvodom, prečo tieto údaje existujú |
| Záznamy o Overených pokusoch a záznam v rebríčku, ktorý každý z nich vytvorí | Súhlas, udelený zámerným úkonom zaznamenania pokusu. Odvoláte ho odstránením pokusu na stránke príslušného stupňa, čím sa záznam vymaže — pozri § 9 |
| Nákupy | Plnenie zmluvy |
| Analytika | Oprávnený záujem na zlepšovaní aplikácie; kedykoľvek môžete namietať v Nastaveniach, pozri § 9 |

**Uplatňujú sa tu dva právne predpisy, nie jeden.** Ranked je prevádzkovaná zo Švajčiarska, takže
toto spracúvanie sa riadi revidovaným švajčiarskym spolkovým zákonom o ochrane údajov (**revDSG**,
účinný od septembra 2023). **GDPR** sa uplatňuje popri ňom všade tam, kde sa aplikácia používa
z Európskej únie alebo zo Spojeného kráľovstva. Ak sa oba líšia, riadime sa prísnejším z nich.
Osoby s pobytom vo Švajčiarsku majú rovnaké základné práva uvedené v § 9 — na prístup, opravu,
vymazanie, prenosnosť a namietanie — podľa článku 25 a nasl. revDSG.

---

## 8. Ako dlho ich uchovávame

Účet, profil, priateľov a záznamy o overených pokusoch uchovávame, kým svoj účet nevymažete.
Vymazaním účtu sa odstránia.

Analytické udalosti sa uchovávajú tak dlho, ako to pre náš plán vyplýva z vlastných zásad
uchovávania služby PostHog. **Vymazanie vášho účtu ich nevymaže**, a hovoríme to výslovne, namiesto
toho, aby sme naznačovali opak: analytický profil nie je prepojený s vaším účtom — používa
samostatný identifikátor generovaný aplikáciou — takže neexistuje väzba, pomocou ktorej by sme ho
mohli nájsť a odstrániť. Čo obsahuje, je uvedené v § 3.5: udalosti používania, vaša hodnosť a vek,
pohlavie a telesná hmotnosť, ktoré ste zadali. Nenesie žiadne meno, žiadny e-mail a žiadne ID účtu.

Ak chcete, aby bol odstránený aj tento profil, napíšte nám približný dátum, kedy ste aplikáciu
použili prvýkrát, a my ho ručne nájdeme a vymažeme.

---

## 9. Vaše práva

Kedykoľvek môžete:

- **Vymazať svoj účet** v Nastaveniach v aplikácii. Tým sa vymaže váš profil na serveri, vaše
  prepojenia s priateľmi a vaše záznamy o overených pokusoch. Ak je pre váš účet uložený obnovovací
  token Apple (pozri § 3.1), odvolá sa tým aj prístup aplikácie Ranked k vášmu Apple ID. Údaje
  uložené iba vo vašom zariadení odstránite odstránením aplikácie.
- **Odvolať Overený pokus** na stránke príslušného stupňa v aplikácii. Odstránením pokusu sa vymaže
  záznam aj záznam v rebríčku, ktorý vytvoril, a odvolá sa tým súhlas udelený jeho zaznamenaním.
  Odvolanie nemá vplyv na to, čo bolo zákonné pred jeho odvolaním.
- **Požiadať o kópiu** údajov, ktoré o vás uchovávame, alebo nás požiadať o ich opravu.
- **Namietať proti analytike** prepínačom v Nastaveniach alebo tým, že nám napíšete.
- **Podať sťažnosť dozornému orgánu** vo svojej krajine.

Vo všetkých týchto veciach píšte na **dylan.schmid538@gmail.com**.

---

## 10. Deti

Ranked nie je určená deťom mladším ako 13 rokov a vedome nezhromažďujeme ich údaje.

---

## 11. Zmeny

Ak sa tieto zásady podstatne zmenia, aplikácia vám to oznámi predtým, než zmena nadobudne účinnosť.

---

> **⚠️ Nejde o právne poradenstvo.** Tento dokument vypracoval inžinier na základe zdrojového kódu
> aplikácie a schémy databázy, nie právnik. Systém opisuje presne k dátumu uvedenému vyššie — každé
> tvrdenie v ňom bolo overené oproti tomu, čo aplikácia skutočne odosiela. **Nebol** preskúmaný
> z hľadiska súladu s GDPR, švajčiarskym revDSG, CCPA ani s akýmkoľvek iným režimom. Zverejnenie
> tohto dokumentu uspokojí Apple; súlad s predpismi vám tým nevzniká. Keď bude aplikácia zarábať,
> dajte to prečítať právnikovi.
