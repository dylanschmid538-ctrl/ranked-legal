---
title: Politika zasebnosti · Calisthenics Skills – Ranked
permalink: /privacy/sl/
---

> *To je prevod. V primeru odstopanj velja angleška različica na naslovu
> https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/.*

# Politika zasebnosti · Calisthenics Skills – Ranked

**Zadnja posodobitev: 2026-10-02**

Ta politika opisuje, kaj Ranked zbira, kam to gre in kaj lahko glede tega storite. Nastala je na
podlagi dejanske kode aplikacije, ne po predlogi — če je tukaj kaj napačno, odloča koda.

Ranked upravlja **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Švica**, stik
**dylan.schmid538@gmail.com**. Je upravljavka tukaj opisane obdelave.

---

## 1. Na kratko

**Vaša starost, spol, višina in telesna teža nikoli ne zapustijo vaše naprave.** Formula ranga jih
uporablja v vašem telefonu. Ne pošiljajo se ne nam ne analitični storitvi.

Vašo napravo zapustita dve stvari, in samo ti dve:

1. **Anonimna statistika uporabe**, da vidimo, kako se aplikacija uporablja. V aplikaciji jo lahko
   kadar koli izklopite.
2. **Podatki o nakupu**, da je mogoče preveriti naročnino iz trgovine App Store. Plačilo izvede
   Apple; vaših plačilnih podatkov nikoli ne vidimo.

Ranked vas ne sledi po drugih aplikacijah ali spletnih straneh, ne prikazuje oglasov in ne bere
ničesar iz aplikacije Apple Zdravje.

---

## 2. Kaj ostane v vaši napravi

Shranjeno v lastni podatkovni zbirki aplikacije v vašem telefonu in nikoli preneseno:

- Vsaka vadba, niz, ponovitev, izdrž in dodatna obremenitev, ki jo zabeležite
- Vaš načrt vadbe, urnik, opomniki in nastavitve
- Vaše telesne mere, kot ste jih vnesli (starost, spol, višina, telesna teža)
- Vaše zapiske o vadbi

Aplikacija te podatkovne zbirke ne izloči iz varnostne kopije vaše naprave. Če uporabljate varnostno
kopiranje v iCloud ali varnostno kopijo prek računalnika, so vaši podatki o vadbi njen del in se ob
obnovitvi vrnejo — pod Applovimi pogoji, ne našimi.

Izbris aplikacije izbriše vse to iz naprave. Obnoviti tega ne moremo, ker tega nikoli nismo imeli.

---

## 3. Kaj zapusti vašo napravo

### 3.1 Statistika uporabe (PostHog)

Uporabljamo **PostHog**, gostovan v **Evropski uniji**, da razumemo, kako se aplikacija uporablja.
Aplikacija mu pošilja določen seznam dogodkov:

- do katerega koraka nastavitve ste prišli, katerega ste dokončali ali se z njega vrnili in koliko
  časa je vsak trajal;
- kaj je pokazala začetna ocena: koliko linij veščin in stopenj ste navedli, katero veščino ste
  izbrali za cilj, kakšen je bil vaš začetni rang in rang vsakega od vaših šestih telesnih področij;
- kdaj je bil prikazan ali zaprt nakupni zaslon in kdaj se je nakup začel, zaključil ali obnovil —
  z izdelkom in ponudbo, na katera se je nanašal; ter ko aplikacija pozneje zazna aktivno poskusno
  obdobje ali obdobje plačljive naročnine — z izdelkom in podatkom, ali gre za nakup v preizkusnem
  okolju. To ni evidenca vsake posamezne bremenitve in se ne pošilja, ko je aplikacija zaprta;
- kdaj se je vaš rang spremenil in katera veščina je to sprožila;
- kdaj ste opravili stopnjo — katera veščina, katera stopnja in ali je to izhajalo iz zabeleženega
  niza, naknadno vnesene vadbe ali ročne navedbe;
- katere zaslone odpirate in kdaj se konča seja. Dogodek o koncu seje ne vsebuje nobenih
  podrobnosti: ne vaj, ne nizov, ne številk.

Programska oprema PostHog v aplikaciji vsakemu dogodku poleg tega pripne običajne tehnične podatke —
model naprave, različico sistema iOS, različico aplikacije, jezik in časovni pas — in beleži, kdaj
se aplikacija odpre in premakne v ozadje. Kot vsaka spletna storitev tudi PostHog prejme naslov IP
zahteve; iz njega lahko izpelje približno lokacijo (državo ali mesto).

**Česa v tem ni:** nobenega imena, nobenega e-poštnega naslova (aplikacija zanj nikoli ne vpraša),
nobenega identifikatorja računa (računov ni), ne starosti, spola, višine ali telesne teže, in
nobene vsebine vaših vadb.

**Kako ste identificirani:** PostHog ob prvem zagonu aplikacije ustvari naključni identifikator in
ga shrani v vašo napravo. Vsi dogodki so združeni pod tem identifikatorjem. Aplikacija PostHogu
nikoli ne pove, kdo ste, in tudi povedati ni česa — ni računa, ni e-pošte.

**Izklop:** Nastavitve ▸ Zasebnost ▸ *Deli anonimne podatke o uporabi*. Če to izklopite, aplikacija
od tistega trenutka naprej ne pošilja več dogodkov. Nastavitev je shranjena v vaši napravi in
preživi posodobitve aplikacije.

### 3.2 Pripis Apple Search Ads

Če ste Ranked namestili po dotiku oglasa Apple Search Ads, aplikacija ob prvem zagonu enkrat vpraša
Apple, od kod prihaja namestitev. Apple odgovori s kampanjo, oglasno skupino, ključno besedo in
oglasnim gradivom tistega oglasa, državo ali regijo klika, datumom klika in podatkom, ali je šlo za
nov prenos ali ponoven. Aplikacija te vrednosti pripne anonimnemu identifikatorju PostHog iz §3.1,
da je mogoče vsak poznejši dogodek pripisati oglasu, ki vas je pripeljal.

Za to se uporablja Applovo ogrodje **AdServices**, ki ne uporablja oglaševalskega identifikatorja
(IDFA) in ga Apple ne šteje za sledenje — zato se ne prikaže nobeno dovoljenje za sledenje. Če niste
prišli prek oglasa, Apple to pove in nič se ne pripne. Izklop statistike uporabe (§3.1) ustavi tudi
to.

### 3.3 Nakupi (Apple in RevenueCat)

Naročnine prodaja in zaračunava **Apple** prek trgovine App Store. Vaših plačilnih podatkov, vašega
računa Apple in vašega imena nikoli ne vidimo.

Za preverjanje, ali je vaša naročnina dejavna, aplikacija uporablja **RevenueCat**. RevenueCat
prejme zapis o nakupu iz trgovine App Store za vašo naročnino — kateri izdelek je bil kupljen, kdaj
se je začel in kdaj poteče — skupaj z običajnimi tehničnimi podatki, kot sta različica sistema iOS
in različica aplikacije. Vašo namestitev prepozna po naključnem identifikatorju, ki ga ustvari sam
in shrani v vašo napravo. RevenueCatu ne dajemo vašega imena, e-poštnega naslova ali katere koli
druge identitete, in ker Ranked nima računov, tudi ni česa dati.

Ko se dotaknete **Obnovi nakupe**, aplikacija Apple vpraša po nakupih, opravljenih z računom Apple,
prijavljenim v napravi, in izid na enak način posreduje RevenueCatu.

---

## 4. Česa Ranked ne počne

- **Nobenih računov.** Nikoli se ne prijavljate. Na nobenem strežniku ni vašega profila.
- **Nobenega Apple Zdravja.** Ranked iz aplikacije Zdravje ne bere in vanjo ne piše.
- **Nobene kamere, fotografij, mikrofona, lokacije ali stikov.** Aplikacija za nobeno od teh
  dovoljenj ne prosi.
- **Nobenega sledenja po aplikacijah ali spletnih straneh**, nobenega oglaševalskega
  identifikatorja, nobenega oglaševanja v aplikaciji, nobenih podatkov, prodanih ali izročenih
  posrednikom s podatki.
- **Nobenega strežnika za potisna obvestila.** Opomniki, ki jih Ranked lahko pošlje, se načrtujejo
  lokalno v vašem telefonu; nič o njih ne zapusti naprave. Pred prvim vas aplikacija vpraša, izklopite
  pa jih lahko kadar koli v nastavitvah sistema iOS.

---

## 5. Pravna podlaga (GDPR in švicarski revDSG)

| Kaj | Podlaga |
|---|---|
| Nakupi in preverjanje naročnine (§3.3) | Izvajanje pogodbe |
| Statistika uporabe (§3.1) | Zakoniti interes za razumevanje in izboljševanje aplikacije; kadar koli lahko ugovarjate tako, da jo izklopite, glejte §8 |
| Pripis Search Ads (§3.2) | Zakoniti interes vedeti, katero oglaševanje deluje; ugovor kot zgoraj |

**Tu veljata dva pravna reda, ne eden.** Ranked se upravlja iz Švice, zato to obdelavo ureja
prenovljeni švicarski zvezni zakon o varstvu podatkov (**revDSG**, v veljavi od septembra 2023).
**GDPR** velja dodatno povsod, kjer se aplikacija uporablja iz Evropske unije ali Združenega
kraljestva. Kjer se oba razlikujeta, sledimo strožjemu. Osebe s prebivališčem v Švici imajo iste
temeljne pravice, naštete v §8, na podlagi 25. in naslednjih členov revDSG.

---

## 6. Kje se podatki obdelujejo

- **PostHog** obdeluje statistiko uporabe v Evropski uniji.
- **RevenueCat, Inc.** ima sedež v Združenih državah in tam obdeluje podatke o nakupu, opisane v
  §3.3.
- **Apple** obdeluje sam nakup in zahtevo za pripis Search Ads po lastni politiki zasebnosti, ki za
  vaš račun Apple velja neodvisno od te aplikacije.

---

## 7. Kako dolgo podatke hranimo

Statistika uporabe se hrani toliko časa, kolikor velja PostHogovo obdobje hrambe za naš paket. Ne
obljubljamo določenega števila mesecev, ker nam ga PostHog ne pusti nastaviti — in številka, ki je
nihče ne more držati, je v politiki zasebnosti slabša od nobene.

Zapise o nakupih RevenueCat hrani toliko časa, kolikor obstajata naročnina in njena zgodovina;
prav to zahteva preverjanje naročnine.

Vse, kar je v vaši napravi, tam ostane, dokler aplikacije ne izbrišete.

---

## 8. Vaše pravice

Kadar koli lahko:

- **Izklopite statistiko uporabe** v Nastavitvah ▸ Zasebnost. To je vaša pravica do ugovora in,
  kjer obdelava temelji na privolitvi, do njenega preklica — učinkuje takoj in ne potrebuje
  razloga.
- **Izbrišete svoje podatke.** Ker Ranked o vas na strežniku ne hrani ničesar, izbris aplikacije
  odstrani vse, kar aplikacija sama shranjuje.
- **Nas prosite, da izbrišemo vaš anonimni analitični profil.** Po imenu ga ne moremo najti — nima
  ga —, če pa nam pišete s približnim datumom prve uporabe aplikacije in uporabljeno napravo, ga
  poiščemo ročno in izbrišemo.
- **Zahtevate kopijo** podatkov, ki jih storitev hrani pod vašim identifikatorjem, nas prosite za
  njihov **popravek** ali za **omejitev** obdelave, dokler se zahteva obravnava.
- **Vložite pritožbo pri nadzornem organu** v svoji državi — v Švici pri Zveznem pooblaščencu za
  varstvo podatkov in informacij (EDÖB).

Za vse to pišite na **dylan.schmid538@gmail.com**.

---

## 9. Otroci

Ranked je namenjen osebam, starim **16 let in več**. Aplikacija ob nastavitvi vpraša za vašo
starost, ker je od nje odvisna formula ranga, in ni namenjena nikomur mlajšemu. Zavestno ne zbiramo
podatkov oseb, mlajših od 16 let.

---

## 10. Spremembe

Velja različica, objavljena na tem naslovu, datum na vrhu pa vam pove, kdaj se je nazadnje
spremenila. Prejšnje različice ostajajo vidne v javni zgodovini repozitorija, iz katerega se te
strani objavljajo, tako da lahko vidite, kaj se je spremenilo in kdaj.

---

> **⚠️ Ni pravni nasvet.** To besedilo je iz izvorne kode aplikacije sestavil inženir, ne odvetnik.
> Sistem opisuje na zgoraj navedeni datum točno — vsaka trditev v njem je bila preverjena glede na
> to, kaj aplikacija dejansko pošilja. **Ni** bilo pregledano glede skladnosti z GDPR, švicarskim
> revDSG, CCPA ali katerim koli drugim režimom. Objava zadosti Applu; skladnosti vam ne zagotovi.
> Ko bo aplikacija začela prinašati prihodek, naj jo prebere odvetnik.
