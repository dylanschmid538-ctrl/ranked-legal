---
title: Pravila o privatnosti · Calisthenics Skills – Ranked
permalink: /privacy/hr/
---

> Ovo je prijevod. U slučaju odstupanja mjerodavna je [engleska verzija](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/).

# Pravila o privatnosti · Calisthenics Skills – Ranked

**Posljednje ažuriranje: 2026-10-18**

Ova pravila opisuju koje podatke Ranked prikuplja, kamo odlaze i što možete učiniti u vezi s njima.

Ranked vodi **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Švicarska**, kontakt **dylan.schmid538@gmail.com**. Ona je voditeljica obrade opisane ovdje.

---

## 1. Ukratko

**Vaša dob, spol, visina i tjelesna težina nikad ne napuštaju uređaj.** Formula za rang koristi ih na telefonu. Ne šalju se nama ni analitičkoj usluzi.

Tri vrste podataka mogu napustiti vaš uređaj:

1. **Statistika korištenja**, kako bismo razumjeli kako se aplikacija koristi. Možete je bilo kada isključiti u aplikaciji.
2. **Podaci o kupnji**, radi provjere pretplate u App Storeu. Apple obrađuje plaćanje; mi nikad ne vidimo vaše podatke o plaćanju.
3. **Poruke s povratnim informacijama i upiti podršci**, samo ako ih sami pošaljete. Uz zaseban pristanak možete dati e-adresu ili telefon za odgovor.

Ranked ne prikazuje oglase i ne čita podatke iz Apple Healtha. Nakon dopuštenja ATT-a dijeljenje podataka o korištenju automatski se uključuje i ostaje uključeno dok ga ne isključite u Rankedovim Postavkama. Podaci o korištenju i atribuciji instalacija putem Apple Search Ads mogu se povezati radi mjerenja; vidi §3.1–3.2.

Kad dopustite ATT pri prvom pokretanju, Ranked automatski uključuje dijeljenje podataka o korištenju. Podaci se šalju dok je ATT dopušten i dok je prekidač dijeljenja uključen u Rankedovim Postavkama. Dijeljenje možete isključiti u Rankedovim Postavkama. Opoziv dopuštenja ATT-a u postavkama iOS-a također zaustavlja buduće prikupljanje i slanje; već poslani podaci ne brišu se.

---

## 2. Što ostaje na vašem uređaju

U bazi podataka aplikacije na telefonu pohranjuje se i nikad se ne prenosi:

- Svaki zabilježeni trening, serija, ponavljanje, izdržaj i dodatna težina
- Plan i raspored treninga, podsjetnici i postavke
- Tjelesne mjere koje ste unijeli (dob, spol, visina, težina)
- Bilješke o treninzima

Aplikacija ne isključuje ovu bazu iz sigurnosne kopije uređaja. Ako koristite iCloud Backup ili sigurnosnu kopiju na računalu, podaci o treningu uključeni su u nju i vraćaju se pri obnovi, prema Appleovim uvjetima, a ne našima.

Brisanjem aplikacije sve se to briše s uređaja. Ne možemo to vratiti jer nikad nismo imali te podatke.

---

## 3. Što napušta vaš uređaj

### 3.1 Statistika korištenja (PostHog)

Pri prvom pokretanju iOS prikazuje Appleov standardni dijalog za dopuštenje praćenja (App Tracking Transparency, ATT). Nakon što dopustite ATT, Ranked automatski uključuje dijeljenje podataka o korištenju. Ranked šalje događaje PostHogu u EU samo dok je ATT dopušten i dok je prekidač dijeljenja uključen u Rankedovim Postavkama. Događaji obuhvaćaju korake postavljanja i početnu procjenu, promjene ranga i stupnja (uključujući vještinu i stupanj), zaslon za kupnju i kupnje, otvorene zaslone te početak, završetak ili prekid treninga uživo, protekle sekunde, broj zabilježenih serija, broj različitih vještina i podatak je li to bio prvi završeni trening. Ne uključuju pojedinačne vježbe, ponavljanja, utege ni bilješke. Dob, spol, visina i tjelesna težina ne šalju se. PostHog prima i uobičajene tehničke podatke o uređaju, iOS-u, aplikaciji i jeziku te IP adresu iz koje se može izvesti približna lokacija. Događaji se povezuju pod nasumičnim identifikatorom instalacije u PostHogu radi analitike i mjerenja oglašavanja; IDFA se ne koristi. Isključivanje dijeljenja u Rankedovim Postavkama ili opoziv dopuštenja ATT-a u postavkama iOS-a zaustavlja buduće prikupljanje i slanje. Već poslani događaji ne brišu se automatski.

### 3.2 Pripisivanje Apple Search Ads oglasa

Ranked traži atribuciju instalacije od Apple AdServices samo dok je ATT dopušten i dok je dijeljenje podataka o korištenju uključeno u Rankedovim Postavkama. Nakon klika na oglas, kampanja, oglasna grupa, ključna riječ, oglasni sadržaj, država ili regija, datum klika i vrsta preuzimanja mogu se povezati s istim nasumičnim identifikatorom instalacije u PostHogu radi mjerenja oglašavanja. Oglašivački identifikator IDFA ne koristi se. Opoziv dopuštenja ili isključivanje dijeljenja zaustavlja buduće upite i slanje; već poslani podaci ne brišu se.

### 3.3 Kupnje (Apple i RevenueCat)

Pretplate prodaje i naplaćuje **Apple** putem App Storea. Nikad ne vidimo vaše podatke o plaćanju, Apple račun ni ime.

Za provjeru aktivne pretplate aplikacija koristi **RevenueCat**. RevenueCat prima zapis kupnje iz App Storea — kupljeni proizvod, početak i istek pretplate — zajedno sa standardnim tehničkim podacima kao što su verzije iOS-a i aplikacije. Instalaciju prepoznaje po nasumičnoj oznaci koju sam stvara i pohranjuje na uređaju. Ne dajemo RevenueCatu vaše ime, e-poštu ni drugi identitet; Ranked nema račune, pa takvog identiteta nema.

Kad dodirnete **Vrati kupnje**, aplikacija traži od Applea kupnje povezane s Apple računom prijavljenim na uređaju i rezultat prosljeđuje RevenueCatu na isti način.

### 3.4 Poruke s povratnim informacijama i upiti podršci (Cloudflare i CloudKit)

Ako pošaljete povratne informacije ili upit podršci, Ranked šalje poruku, njezinu kategoriju i izvor usluzi Cloudflare Worker. Ona ih pohranjuje u javnu bazu podataka Apple CloudKit pomoću privatnog poslužiteljskog ključa. Za slanje poruke nije potrebna prijava na iCloud. Cloudflare Worker koristi mrežnu adresu zahtjeva za tehničko ograničavanje zloupotrebe; ni izvorna adresa ni njezin hash ne pohranjuju se u zapis povratnih informacija u CloudKitu. Zasebno možete pristati dati adresu e-pošte ili telefonski broj kako bismo vam odgovorili izvan aplikacije. Poruke i podaci za kontakt ne šalju se PostHogu ili RevenueCatu niti se povezuju s računom u aplikaciji. Poruku obrađujemo kako bismo odgovorili na vaš zahtjev, a neobavezne podatke za kontakt uz vaš pristanak. Trenutačno nije određen stalan rok za automatsko brisanje poruka ili podataka za kontakt. Pristup ili brisanje možete zatražiti na **dylan.schmid538@gmail.com**.

---

## 4. Što Ranked ne radi

- **Nema računa.** Nikad se ne prijavljujete. Na poslužitelju ne postoji vaš profil.
- **Nema Apple Healtha.** Ranked ne čita iz aplikacije Health niti piše u nju.
- **Nema kamere, fotografija, mikrofona, lokacije ni kontakata.** Aplikacija ne traži ta dopuštenja.
- **Praćenje i atribucija:** Ranked ne koristi IDFA. Podaci o korištenju i atribuciji instalacija putem Apple Search Ads mogu se povezati radi mjerenja oglašavanja samo uz dopuštenje ATT-a i uključeno dijeljenje podataka o korištenju. U aplikaciji nema oglasa, a podaci se ne prodaju ni ne predaju posrednicima za podatke.
- **Nema poslužitelja za push obavijesti.** Podsjetnici se zakazuju lokalno na telefonu; ništa o njima ne napušta uređaj. Pitanje dopuštenja postavlja se prije prvog, a možete ih bilo kada isključiti u postavkama iOS-a.

---
## 5. Pravna osnova (GDPR i švicarski revDSG)

| Obrada | Osnova |
|---|---|
| Kupnje i provjera pretplate (§3.3) | Izvršavanje ugovora |
| Statistika korištenja (§3.1) | Vaš pristanak na dijeljenje podataka o korištenju i dopuštenje ATT-a koje daje Apple; svako od njih možete povući u bilo kojem trenutku. Isključivanje dijeljenja u Rankedovim Postavkama ili opoziv dopuštenja ATT-a u postavkama iOS-a zaustavlja buduće prikupljanje; već poslani podaci ne brišu se. |
| Pripisivanje Search Ads oglasa (§3.2) | Vaš pristanak na dijeljenje podataka o korištenju i dopuštenje ATT-a koje daje Apple; svako od njih možete povući u bilo kojem trenutku. Isključivanje dijeljenja u Rankedovim Postavkama ili opoziv dopuštenja ATT-a u postavkama iOS-a zaustavlja buduće prikupljanje; već poslani podaci ne brišu se. |

**Ovdje se primjenjuju dva zakona, ne jedan.** Ranked se vodi iz Švicarske, pa ovu obradu uređuje revidirani švicarski Savezni zakon o zaštiti podataka (**revDSG**, na snazi od rujna 2023.). **GDPR** se dodatno primjenjuje gdje god se aplikacija koristi iz Europske unije ili Ujedinjene Kraljevine. Ako se zakoni razlikuju, slijedimo stroži. Stanovnici Švicarske imaju ista temeljna prava iz §8 prema članku 25. i sljedećima revDSG-a.

---
## 6. Gdje se podaci obrađuju

- **PostHog** obrađuje statistiku korištenja u Europskoj uniji.
- **RevenueCat, Inc.** ima sjedište u Sjedinjenim Američkim Državama i ondje obrađuje podatke o kupnji iz §3.3.
- **Apple** obrađuje samu kupnju i zahtjev za pripisivanje Search Ads oglasa prema vlastitim pravilima o privatnosti, koja se odnose na vaš Apple račun neovisno o ovoj aplikaciji.

---

## 7. Koliko dugo ih čuvamo

Statistika korištenja čuva se onoliko dugo koliko vrijedi razdoblje čuvanja PostHoga za naš paket. Ne obećavamo fiksni broj mjeseci jer ga PostHog ne dopušta postaviti; broj koji nitko ne može poštovati gori je u pravilima o privatnosti nego nikakav broj.

RevenueCat čuva zapise kupnji dok postoje pretplata i njezina povijest, što je potrebno za provjeru pretplate.

Sve na vašem uređaju ostaje ondje dok ne izbrišete aplikaciju.

---

## 8. Vaša prava

Dijeljenje podataka o korištenju možete isključiti u Rankedovim Postavkama ▸ Podaci i privatnost, a dopuštenje ATT-a možete opozvati u postavkama iOS-a. Obje radnje zaustavljaju buduće prikupljanje i slanje. Već poslani podaci ne brišu se automatski, a pretplata na App Store ne otkazuje se.

Lokalne podatke o treningu možete izbrisati u Postavkama ▸ Podaci i privatnost ▸ *Izbriši lokalne podatke treninga* ili brisanjem aplikacije. Pretplatom zasebno upravljate i otkazujete je na svom Apple računu.

Za podatke već poslane PostHogu pišite na **dylan.schmid538@gmail.com**. Ranked ne povezuje nasumični analitički identifikator s računom. Približan datum ili model uređaja možda nisu dovoljni za pouzdano pronalaženje profila. Objasnit ćemo što možemo identificirati i obraditi provjerljive zahtjeve za pristup, ispravak ili brisanje. Ne šaljite podatke za prijavu na Apple račun.

Možete zatražiti ograničenje obrade i podnijeti pritužbu nadzornom tijelu svoje zemlje; u Švicarskoj je to savezni povjerenik za zaštitu podataka i informiranje (FDPIC).

---

## 9. Djeca

Ranked je namijenjen osobama od **16 godina naviše**. Aplikacija pri postavljanju traži dob jer o njoj ovisi formula za rang i nije namijenjena mlađima. Ne prikupljamo svjesno podatke osoba mlađih od 16 godina.

---

## 10. Promjene

Verzija objavljena na ovoj adresi trenutačna je; datum na vrhu pokazuje kada je posljednji put promijenjena. Ranije verzije ostaju vidljive u javnoj povijesti repozitorija iz kojeg se ove stranice objavljuju, tako da možete vidjeti što se i kada promijenilo.

---
