---
title: Politika zasebnosti
permalink: /privacy/sl/
---

*To je prevod. V primeru odstopanj velja angleška različica, dostopna na naslovu https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/.*

# Politika zasebnosti · Calisthenics Skills – Ranked

**Zadnja posodobitev: 23. avgust 2026**

Ta politika opisuje, kaj aplikacija Ranked zbira, kam ti podatki gredo in kaj lahko glede tega
storite. Sestavljena je bila ob dejanski programski kodi in podatkovni shemi aplikacije, ne po
predlogi — če je karkoli v njej napačno, je treba preveriti kodo.

Aplikacijo Ranked upravlja **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Švica**, kontakt **dylan.schmid538@gmail.com**.

---

## 1. Na kratko

Skoraj vse, kar Ranked ve o vaši vadbi, ostane v vašem telefonu. Zgodovina vadbe, vaš napredek pri
vsaki veščini, vaš rang in vaš telesni zemljevid so shranjeni lokalno in se nikoli ne prenesejo v
oblak.

Štiri stvari zapustijo vašo napravo: vaša prijavna identiteta, majhen profil za lestvice, zapisi o
tem, da ste opravili preverjeni poskus, in anonimna analitika uporabe. Vsaka je pojasnjena spodaj.

**Videoposnetki vaših preverjenih poskusov nikoli ne zapustijo vaše naprave.** Poslan je le
prstni odtis datoteke.

---

## 2. Kaj ostane v vaši napravi

Shranjeno lokalno v lastni podatkovni bazi aplikacije in nikoli poslano:

- Vsaka vadba, serija, ponovitev, izdržaj in dodana teža, ki jo zabeležite
- Vaš napredek pri vsaki veščini in stopnji ter zgodovina vašega ranga
- Vaš načrt vadbe, urnik in nastavitve
- Vaše telesne mere, kot ste jih vnesli (starost, spol, višina, telesna teža) — kopija nekaterih
  od teh se pošlje tudi storitvi za lestvice, glejte §3.2
- **Videodatoteke preverjenih poskusov.** Te se zapišejo v zasebno shrambo aplikacije. Ne
  prenesejo se v oblak, ne varnostno kopirajo se na naše strežnike in za nas niso dostopne.

Z izbrisom aplikacije se izbriše vse to. Tega ne moremo obnoviti.

---

## 3. Kaj zapusti vašo napravo

### 3.1 Vaš račun
Ko se prijavite z računom Apple ali Google, prejmemo in shranimo identifikator uporabnika in,
odvisno od tega, kaj ob prijavi dovolite, e-poštni naslov. To izvaja **Supabase**, ki gosti našo
podatkovno bazo in avtentikacijo.

Ko se prijavite z računom Apple, shranimo tudi žeton za osvežitev, ki nam ga Apple izroči v tistem
trenutku. Njegov edini namen je: z izbrisom vašega računa se prekliče tudi dostop aplikacije
Ranked do vašega računa Apple ID, kot to zahteva Apple. Pri računih, pri katerih se je zadnja
prijava zgodila, preden je bilo to zajemanje uvedeno, žeton ni shranjen — izbris takrat korak
preklica preprosto preskoči.

### 3.2 Vaš profil za lestvice
Da vas lahko uvrstimo na lestvico in primerjamo z ljudmi podobne postave, se na našem strežniku
shrani naslednje:

- naključno ustvarjena **koda prijatelja**
- vaša **starost**, **spol** in **telesna teža**
- datum, ko je bil vaš profil ustvarjen

**Opomba o vidnosti:** vsak prijavljen uporabnik aplikacije Ranked lahko poišče profil po njegovi
kodi prijatelja. V tem je namen kode prijatelja — obstaja zato, da jo nekomu izročite. Svoje ne
delite z nikomer, za katerega ne želite, da vidi vaš vnos. Drugi uporabniki vidijo vašo kodo
prijatelja in vaše mesto na lestvici — nič drugega. Vaša starost, spol in telesna teža se na
strežniku uporabljajo za primerjavo in se drugim uporabnikom nikoli ne prikažejo niti jih ti ne
morejo prenesti.

Vaša **višina** se ne pošlje. Vaša zgodovina vadbe se ne pošlje.

### 3.3 Preverjeni poskusi
Ko posnamete preverjeni poskus, shranimo: vaš uporabniški id, za katero veščino in stopnjo je šlo
pri poskusu, **kriptografsko zgoščeno vrednost videodatoteke** in čas snemanja.

Zgoščena vrednost je prstni odtis. Ni je mogoče pretvoriti nazaj v videoposnetek. Obstaja zato, da
je poskus mogoče povezati z določenim posnetkom, ne da bi ta posnetek kdaj zapustil vaš telefon.

### 3.4 Prijatelji
Če nekoga dodate prek njegove kode prijatelja, shranimo povezavo med vašim in njegovim računom ter
vaše članstvo v morebitnih skupinah prijateljev.

### 3.5 Analitika uporabe
Uporabljamo **PostHog**, gostovan v **Evropski uniji**, da razumemo, kako se aplikacija uporablja.
Beležimo dogodke, kot so, do katerega koraka uvajanja ste prišli, kdaj je bila vadba zaključena,
kdaj se je rang spremenil in ali je bil zaslon za nakup prikazan ali zavrnjen.

Ti dogodki vsebujejo vaš rang in vaš napredek v aplikaciji. **Ne** vsebujejo vašega imena,
e-poštnega naslova, višine ali vsebine vaših vadb.

---

## 4. Nakupi

Naročnine obdeluje **Apple**. Vaših plačilnih podatkov nikoli ne vidimo. **RevenueCat** v našem
imenu upravlja stanje vaše naročnine ter prejme psevdonimni identifikator in stanje vaše
naročnine. Zaslon za nakup je sam del aplikacije; noben tretji ponudnik ne odloča o tem, kateri
vam bo prikazan.

---

## 5. Kamera in mikrofon

Ranked prosi za dostop do kamere in mikrofona zaradi ene same funkcije: snemanja preverjenega
poskusa. Posnetek se shrani v vašo napravo. Nikoli se ne prenese v oblak. Če dostop zavrnete,
vsi drugi deli aplikacije še naprej delujejo.

---

## 6. Zdravstveni podatki

Ranked **ne** bere iz aplikacije Apple Health in vanjo **ne** zapisuje.

Vaša starost, spol in telesna teža so zdravju sorodni podatki in se po GDPR lahko štejejo za
podatke o zdravstvenem stanju. Zbiramo jih za en sam namen — formula za rang normalizira zmogljivost
glede na postavo, tako da 95-kilogramski in 60-kilogramski športnik, ki držita isti lever, nista
ocenjena, kot da bi naredila isto — na strežnik pa pošljemo najmanjši del teh podatkov, ki ga
primerjava na lestvici potrebuje.

---

## 7. Zakonita podlaga (GDPR in švicarski revDSG)

| Kaj | Podlaga |
|---|---|
| Račun in prijava | Izvajanje pogodbe — aplikacija zahteva račun |
| Starost, spol in telesna teža | Izvajanje pogodbe — rang je normaliziran glede nanje in ga brez njih ni mogoče izračunati |
| Koda prijatelja, skupine prijateljev | Izvajanje pogodbe — funkcija je razlog, zaradi katerega ti podatki obstajajo |
| Zapisi o preverjenih poskusih in vnos na lestvico, ki ga vsak od njih ustvari | Privolitev, dana z zavestnim dejanjem snemanja poskusa. Prekličete jo tako, da poskus odstranite na strani stopnje, s čimer se vnos izbriše — glejte §9 |
| Nakupi | Izvajanje pogodbe |
| Analitika | Zakoniti interes za izboljševanje aplikacije; kadar koli lahko ugovarjate v nastavitvah, glejte §9 |

**Tu se uporabljata dva zakona, ne eden.** Ranked se upravlja iz Švice, zato to obdelavo ureja
revidirani švicarski zvezni zakon o varstvu podatkov (**revDSG**, v veljavi od septembra 2023).
**GDPR** se uporablja poleg tega povsod, kjer se aplikacija uporablja iz Evropske unije ali
Združenega kraljestva. Kjer se oba razlikujeta, upoštevamo strožjega. Prebivalci Švice imajo iste
temeljne pravice, naštete v §9 — dostop, popravek, izbris, prenosljivost podatkov in ugovor —,
in sicer po členu 25 in naslednjih revDSG.

---

## 8. Kako dolgo jih hranimo

Račun, profil, prijatelje in zapise o preverjenih poskusih hranimo, dokler ne izbrišete svojega
računa. Z izbrisom računa se odstranijo.

Analitične dogodke hranimo toliko časa, kolikor za naš paket velja PostHogovo lastno obdobje
hrambe. **Z izbrisom vašega računa se ti ne izbrišejo**, in to izrecno povemo, namesto da bi
nakazovali nasprotno: analitični profil ni povezan z vašim računom — uporablja ločen
identifikator, ki ga ustvari aplikacija —, zato ne obstaja povezava, po kateri bi ga lahko našli
in odstranili. Kaj vsebuje, je našteto v §3.5: dogodke uporabe, vaš rang ter starost, spol in
telesno težo, ki ste jih vnesli. Ne vsebuje imena, e-poštnega naslova in id-ja računa.

Če želite, da se odstrani tudi ta profil, nam pišite in navedite približen datum, ko ste
aplikacijo prvič uporabili, mi pa ga bomo poiskali in ročno izbrisali.

---

## 9. Vaše pravice

Kadar koli lahko:

- **Izbrišete svoj račun** v nastavitvah v aplikaciji. S tem se izbrišejo vaš profil na strežniku,
  vaše povezave s prijatelji in vaši zapisi o preverjenih poskusih. Kadar je za vaš račun shranjen
  Applov žeton za osvežitev (glejte §3.1), se s tem prekliče tudi dostop aplikacije Ranked do
  vašega računa Apple ID. Podatki, shranjeni samo v vaši napravi, se odstranijo z izbrisom
  aplikacije.
- **Umaknete preverjeni poskus** na strani stopnje v aplikaciji. Z odstranitvijo poskusa se
  izbrišeta zapis in vnos na lestvici, ki ga je ustvaril, ter se prekliče privolitev, dana s
  snemanjem poskusa. Preklic ne vpliva na zakonitost obdelave pred preklicem.
- **Zahtevate kopijo** podatkov, ki jih hranimo o vas, ali zahtevate njihov popravek.
- **Ugovarjate analitiki** s stikalom v nastavitvah ali tako, da nam pišete.
- **Vložite pritožbo pri nadzornem organu** v svoji državi.

Za katero koli od tega pišite na **dylan.schmid538@gmail.com**.

---

## 10. Otroci

Ranked ni namenjen otrokom, mlajšim od 13 let, in njihovih podatkov ne zbiramo zavestno.

---

## 11. Spremembe

Če se ta politika bistveno spremeni, vas bo aplikacija o tem obvestila, preden sprememba začne
veljati.

---

> **⚠️ Ni pravni nasvet.** Ta dokument je na podlagi izvorne kode in podatkovne sheme aplikacije
> sestavil inženir, ne odvetnik. Sistem opisuje točno na dan, naveden zgoraj — vsaka trditev v njem
> je bila preverjena glede na to, kar aplikacija dejansko pošilja. **Ni** bil pregledan glede
> skladnosti z GDPR, švicarskim revDSG, CCPA ali katero koli drugo ureditvijo. Objava tega besedila
> zadosti Applu; skladnosti vam ne zagotovi. Ko bo aplikacija začela prinašati prihodek, naj jo
> prebere odvetnik.
