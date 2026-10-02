---
title: Pravila o privatnosti · Calisthenics Skills – Ranked
permalink: /privacy/hr/
---

> Ovo je prijevod. U slučaju odstupanja mjerodavna je [engleska verzija](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/).

# Pravila o privatnosti · Calisthenics Skills – Ranked

**Posljednje ažuriranje: 2026-10-02**

Ova pravila opisuju koje podatke Ranked prikuplja, kamo odlaze i što možete učiniti u vezi s njima. Sastavljena su prema stvarnom kodu aplikacije, a ne prema predlošku. Ako je nešto ovdje netočno, treba provjeriti kod.

Ranked vodi **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Švicarska**, kontakt **dylan.schmid538@gmail.com**. Ona je voditeljica obrade opisane ovdje.

---

## 1. Ukratko

**Vaša dob, spol, visina i tjelesna težina nikad ne napuštaju uređaj.** Formula za rang koristi ih na telefonu. Ne šalju se nama ni analitičkoj usluzi.

Uređaj napuštaju samo dvije vrste podataka:

1. **Anonimna statistika korištenja**, kako bismo razumjeli kako se aplikacija koristi. Možete je bilo kada isključiti u aplikaciji.
2. **Podaci o kupnji**, radi provjere pretplate u App Storeu. Apple obrađuje plaćanje; mi nikad ne vidimo vaše podatke o plaćanju.

Ranked vas ne prati kroz druge aplikacije ili web-mjesta, ne prikazuje oglase i ne čita ništa iz Apple Healtha.

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

Koristimo **PostHog**, smješten u **Europskoj uniji**, kako bismo razumjeli uporabu aplikacije. Aplikacija mu šalje fiksni popis događaja:

- do kojeg ste koraka početnog postavljanja došli, koji ste dovršili ili s kojeg ste se vratili te koliko je svaki trajao;
- rezultat početne procjene: koliko ste linija vještina i razina označili kao ostvarene, koju ste vještinu odabrali za cilj, početni rang i rang svake od šest tjelesnih regija;
- kada je zaslon za kupnju prikazan ili zatvoren te kada je kupnja započeta, dovršena ili obnovljena, uz odgovarajući proizvod i ponudu; kada aplikacija kasnije utvrdi aktivno probno ili plaćeno razdoblje pretplate, uz proizvod i podatak radi li se o testnoj kupnji (to nije zapis svake naplate i ne šalje se dok je aplikacija zatvorena);
- kada se vaš rang promijeni i koja je vještina to uzrokovala;
- kada dovršite razinu: koja vještina i razina te je li ostvarena zabilježenom serijom, naknadno unesenim treningom ili ručnom potvrdom;
- koje zaslone otvarate i kada trening završi. Događaj završetka treninga ne sadrži pojedinosti: ni vježbe, ni serije, ni brojke.

Softver PostHoga u aplikaciji svakom događaju dodaje standardne tehničke podatke, poput modela uređaja, verzije iOS-a i aplikacije, jezika i vremenske zone, te bilježi kada se aplikacija otvori ili ode u pozadinu. Kao i svaka internetska usluga, PostHog prima IP adresu zahtjeva; iz nje može izvesti približnu lokaciju (državu ili grad).

**Što nije uključeno:** ime, adresa e-pošte (aplikacija je ne traži), oznaka računa (račun ne postoji), dob, spol, visina, težina ili sadržaj vaših treninga.

**Kako vas se prepoznaje:** PostHog pri prvom pokretanju stvara nasumičnu oznaku i pohranjuje je na uređaju. Svi se događaji grupiraju pod tom oznakom. Aplikacija nikad ne govori PostHogu tko ste i nema računa ni e-pošte koju bi mu mogla dati.

**Isključivanje:** Postavke ▸ Privatnost ▸ *Dijeli anonimne podatke o korištenju*. Isključivanje odmah zaustavlja slanje novih događaja. Postavka je pohranjena na uređaju i ostaje nakon ažuriranja aplikacije.

### 3.2 Pripisivanje Apple Search Ads oglasa

Ako ste Ranked instalirali nakon dodira oglasa Apple Search Ads, aplikacija pri prvom pokretanju jednom pita Apple odakle je instalacija došla. Apple odgovara kampanjom, grupom oglasa, ključnom riječi i skupom kreativnih materijala tog oglasa, državom ili regijom klika, datumom klika i podatkom je li riječ o novom ili ponovnom preuzimanju. Aplikacija te vrijednosti pridružuje anonimnoj oznaci PostHoga iz §3.1 kako bi kasniji događaji bili grupirani prema oglasu koji vas je doveo.

Za to se koristi Appleov okvir **AdServices**, bez oglašivačke oznake (IDFA), a Apple to ne smatra praćenjem; zato se ne prikazuje upit za dopuštenje praćenja. Ako niste došli putem oglasa, Apple to navodi i ništa se drugo ne pridružuje. Isključivanje statistike korištenja (§3.1) zaustavlja i ovo.

### 3.3 Kupnje (Apple i RevenueCat)

Pretplate prodaje i naplaćuje **Apple** putem App Storea. Nikad ne vidimo vaše podatke o plaćanju, Apple račun ni ime.

Za provjeru aktivne pretplate aplikacija koristi **RevenueCat**. RevenueCat prima zapis kupnje iz App Storea — kupljeni proizvod, početak i istek pretplate — zajedno sa standardnim tehničkim podacima kao što su verzije iOS-a i aplikacije. Instalaciju prepoznaje po nasumičnoj oznaci koju sam stvara i pohranjuje na uređaju. Ne dajemo RevenueCatu vaše ime, e-poštu ni drugi identitet; Ranked nema račune, pa takvog identiteta nema.

Kad dodirnete **Vrati kupnje**, aplikacija traži od Applea kupnje povezane s Apple računom prijavljenim na uređaju i rezultat prosljeđuje RevenueCatu na isti način.

---

## 4. Što Ranked ne radi

- **Nema računa.** Nikad se ne prijavljujete. Na poslužitelju ne postoji vaš profil.
- **Nema Apple Healtha.** Ranked ne čita iz aplikacije Health niti piše u nju.
- **Nema kamere, fotografija, mikrofona, lokacije ni kontakata.** Aplikacija ne traži ta dopuštenja.
- **Nema praćenja između aplikacija ili web-mjesta**, oglašivačke oznake, oglasa u aplikaciji ni prodaje ili predaje podataka posrednicima u trgovini podacima.
- **Nema poslužitelja za push obavijesti.** Podsjetnici se zakazuju lokalno na telefonu; ništa o njima ne napušta uređaj. Pitanje dopuštenja postavlja se prije prvog, a možete ih bilo kada isključiti u postavkama iOS-a.

---

## 5. Pravna osnova (GDPR i švicarski revDSG)

| Obrada | Osnova |
|---|---|
| Kupnje i provjera pretplate (§3.3) | Izvršavanje ugovora |
| Statistika korištenja (§3.1) | Legitimni interes za razumijevanje i poboljšanje aplikacije; možete se usprotiviti bilo kada isključivanjem, vidi §8 |
| Pripisivanje Search Ads oglasa (§3.2) | Legitimni interes za saznanje koji oglasi djeluju; prigovor kao gore |

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

U bilo kojem trenutku možete:

- **Isključiti statistiku korištenja** u Postavke ▸ Privatnost. To je vaše pravo na prigovor i, kada se obrada temelji na privoli, njezino povlačenje; vrijedi odmah i ne traži razlog.
- **Izbrisati svoje podatke.** Budući da Ranked na poslužitelju nema ništa o vama, brisanjem aplikacije uklanja se sve što sama pohranjuje.
- **Zatražiti brisanje anonimnog analitičkog profila.** Ne možemo ga pronaći po imenu jer ga nema; ako nam javite približan datum prvog korištenja i uređaj koji ste koristili, ručno ćemo ga pronaći i izbrisati.
- **Zatražiti kopiju** podataka koje usluga čuva pod vašom oznakom, njihovo **ispravljanje** ili **ograničenje** obrade dok se zahtjev razmatra.
- **Podnijeti pritužbu nadzornom tijelu** u svojoj državi; u Švicarskoj je to Savezni povjerenik za zaštitu podataka i transparentnost (FDPIC).

Za bilo što od toga pišite na **dylan.schmid538@gmail.com**.

---

## 9. Djeca

Ranked je namijenjen osobama od **16 godina naviše**. Aplikacija pri postavljanju traži dob jer o njoj ovisi formula za rang i nije namijenjena mlađima. Ne prikupljamo svjesno podatke osoba mlađih od 16 godina.

---

## 10. Promjene

Verzija objavljena na ovoj adresi trenutačna je; datum na vrhu pokazuje kada je posljednji put promijenjena. Ranije verzije ostaju vidljive u javnoj povijesti repozitorija iz kojeg se ove stranice objavljuju, tako da možete vidjeti što se i kada promijenilo.

---

> **⚠️ Nije pravni savjet.** Ovaj je dokument sastavio inženjer prema izvornom kodu aplikacije, a ne odvjetnik. Točno opisuje sustav na navedeni datum; svaka je tvrdnja provjerena prema onome što aplikacija stvarno šalje. **Nije** pregledan radi usklađenosti s GDPR-om, švicarskim revDSG-om, CCPA-om ni drugim propisima. Objavljivanje zadovoljava Appleov zahtjev, ali ne znači pravnu usklađenost. Dajte ga odvjetniku na pregled kada aplikacija počne donositi prihod.
