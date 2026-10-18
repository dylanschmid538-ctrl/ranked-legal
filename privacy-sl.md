---
title: Politika zasebnosti · Calisthenics Skills – Ranked
permalink: /privacy/sl/
---

> *To je prevod. V primeru odstopanj velja angleška različica na naslovu
> https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/.*

# Politika zasebnosti · Calisthenics Skills – Ranked

**Zadnja posodobitev: 2026-10-18**

Ta politika opisuje, kaj Ranked zbira, kam to gre in kaj lahko glede tega storite.

Ranked upravlja **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Švica**, stik
**dylan.schmid538@gmail.com**. Je upravljavka tukaj opisane obdelave.

---

## 1. Na kratko

**Vaša starost, spol, višina in telesna teža nikoli ne zapustijo vaše naprave.** Formula ranga jih
uporablja v vašem telefonu. Ne pošiljajo se ne nam ne analitični storitvi.

Vašo napravo lahko zapustijo tri vrste podatkov:

1. **Statistika uporabe**, Ranked deli to statistiko samo, če dovolite standardno Applovo zahtevo za sledenje. Deljenje lahko izklopite v aplikaciji ali prekličete dovoljenje v nastavitvah sistema iOS.
2. **Podatki o nakupu**, da je mogoče preveriti naročnino iz trgovine App Store. Plačilo izvede
   Apple; vaših plačilnih podatkov nikoli ne vidimo.
3. **Sporočila s povratnimi informacijami in prošnjami za podporo**, samo če jih pošljete. Z ločenim soglasjem lahko za odgovor navedete e-pošto ali telefon.

Ranked vam ne sledi med drugimi aplikacijami ali spletnimi mesti. Spodaj opisani statistika uporabe in pripisovanje oglaševalskih kampanj se pošiljata samo po odobritvi ATT in dokler je vklopljena možnost »Share usage data«. Aplikacija ne prikazuje oglasov in ne bere podatkov iz Apple Zdravja.

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

Ob prvem zagonu iOS prikaže standardno sistemsko okno za dovoljenje App Tracking Transparency (ATT). Ko dovoljenje ATT odobrite, se analitika samodejno vklopi in deluje, dokler je v Ranked vklopljena možnost »Share usage data«. Dogodki se v PostHog v EU pošiljajo samo, dokler je ATT odobren in je ta možnost vklopljena; ob zavrnitvi ali izklopu se novi podatki ne pošiljajo. Ranked pošilja storitvi PostHog v EU dogodke o uvajanju, začetni oceni, spremembah ranga in stopnje (s spretnostjo in stopnjo), plačilnem zaslonu, nakupih in odprtih zaslonih. Dogodki vadbe v živo vsebujejo začetek, zaključek ali prekinitev, pretečene sekunde, število zabeleženih serij, število različnih spretnosti in podatek o prvi zaključeni vadbi. Ne vsebujejo posameznih vaj, ponovitev, uteži ali zapiskov. Starost, spol, višina in telesna teža se ne pošiljajo. PostHog prejme tudi običajne tehnične podatke o napravi, iOS, aplikaciji in jeziku ter naslov IP, iz katerega je mogoče sklepati o približni lokaciji. Naključni identifikator namestitve PostHog se ustvari po odobritvi ATT. Dogodki in podatki o pripisu kampanje se povežejo s tem identifikatorjem za analitiko in merjenje učinkovitosti oglasov. Dovoljenje ATT lahko prekličete v nastavitvah iOS ali izklopite možnost »Share usage data« v Ranked v Nastavitvah ▸ Podatki in zasebnost; novi dogodki prenehajo, že poslani podatki pa se ne izbrišejo samodejno.

Aplikacija lahko sporoča tudi fazo naročnine, trenutni dostop, stanje obnove in ali je bila zaznana odpoved ali težava z obračunavanjem. Ta opažanja niso dokaz bremenitve in se pošiljajo samo, ko je analitika vklopljena.

Z vašim soglasjem dogodki uporabe beležijo tudi, kdaj izberete načrt vadbe in kdaj odprete vadbeno sejo. Izbira načrta vključuje le število vadbenih dni na teden in vaj; odprtje seje vključuje le, ali se nadaljuje, vir vstopa in število predpisanih vaj. Celotna vsebina načrtov, urniki, posamezne vaje in zapiski vadbe ostanejo v vaši napravi.

### 3.2 Pripis Apple Search Ads

Samo dokler je ATT odobren in je možnost »Share usage data« vklopljena, Ranked enkrat vpraša Apple AdServices o pripisu namestitve iz Apple Search Ads. Po kliku na oglas se lahko z naključnim identifikatorjem PostHog povežejo kampanja, oglasna skupina, ključna beseda, ustvarjalna vsebina, država ali regija, datum klika in vrsta prenosa. Oglaševalski identifikator IDFA se ne uporablja. Preklic dovoljenja ATT v nastavitvah iOS ali izklop možnosti »Share usage data« v Ranked ustavi prihodnje prenose.

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

### 3.4 Sporočila s povratnimi informacijami in prošnjami za podporo (Cloudflare in CloudKit)

Če pošljete povratne informacije ali prošnjo za podporo, Ranked pošlje sporočilo, njegovo kategorijo in vir storitvi Cloudflare Worker. Ta jih s zasebnim strežniškim ključem shrani v javno podatkovno zbirko Apple CloudKit. Za pošiljanje sporočila se vam ni treba prijaviti v iCloud. Cloudflare Worker uporablja omrežni naslov zahteve za tehnično omejevanje zlorab; niti izvirni naslov niti njegova zgoščena vrednost se ne shranita v zapis povratnih informacij v CloudKitu. Ločeno lahko privolite v posredovanje e-poštnega naslova ali telefonske številke, da vam odgovorimo zunaj aplikacije. Sporočila in kontaktni podatki se ne pošiljajo družbama PostHog ali RevenueCat in niso povezani z računom v aplikaciji. Sporočilo obdelujemo, da odgovorimo na vašo prošnjo, neobvezne kontaktne podatke pa z vašim soglasjem. Trenutno ni določenega roka za samodejni izbris sporočil ali kontaktnih podatkov. Dostop do podatkov ali izbris lahko zahtevate na **dylan.schmid538@gmail.com**.

---

## 4. Česa Ranked ne počne

- **Nobenih računov.** Nikoli se ne prijavljate. Na nobenem strežniku ni vašega profila.
- **Nobenega Apple Zdravja.** Ranked iz aplikacije Zdravje ne bere in vanjo ne piše.
- **Nobene kamere, fotografij, mikrofona, lokacije ali stikov.** Aplikacija za nobeno od teh
  dovoljenj ne prosi.
- **Ranked vam ne sledi med drugimi aplikacijami ali spletnimi mesti.** Statistika uporabe in merjenje kampanj iz §3 se uporabljata samo ob dovoljenju ATT in vklopljeni možnosti »Share usage data«; IDFA se ne uporablja. Aplikacija ne prikazuje oglasov, podatki pa se ne prodajajo ali posredujejo podatkovnim posrednikom.
- **Nobenega strežnika za potisna obvestila.** Opomniki, ki jih Ranked lahko pošlje, se načrtujejo
  lokalno v vašem telefonu; nič o njih ne zapusti naprave. Pred prvim vas aplikacija vpraša, izklopite
  pa jih lahko kadar koli v nastavitvah sistema iOS.

---

## 5. Pravna podlaga (GDPR in švicarski revDSG)

| Kaj | Podlaga |
|---|---|
| Nakupi in preverjanje naročnine (§3.3) | Izvajanje pogodbe |
| Statistika uporabe (§3.1) | Vaša privolitev; kadar koli jo lahko umaknete v Nastavitvah ▸ Podatki in zasebnost |
| Pripis Search Ads (§3.2) | Vaša privolitev; kadar koli jo lahko umaknete v Nastavitvah ▸ Podatki in zasebnost |

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

Prihodnje pošiljanje analitičnih podatkov lahko kadar koli ustavite tako, da prekličete dovoljenje ATT v nastavitvah iOS ali izklopite možnost »Share usage data« v Ranked: Nastavitve ▸ Podatki in zasebnost. Že poslani podatki se ne izbrišejo samodejno, naročnina v App Store pa ostane veljavna.

Lokalne podatke o vadbi lahko izbrišete v Nastavitvah ▸ Podatki in zasebnost ▸ *Izbriši lokalne podatke o vadbi* ali z izbrisom aplikacije. Naročnino upravljate in prekličete posebej v računu Apple.

Za podatke, že poslane storitvi PostHog, pišite na **dylan.schmid538@gmail.com**. Ranked naključnega analitičnega identifikatorja ne povezuje z računom. Približen datum ali model naprave morda ne zadostuje za zanesljivo iskanje profila. Pojasnili bomo, kaj lahko identificiramo, in obravnavali preverljive zahteve za dostop, popravek ali izbris. Ne pošiljajte prijavnih podatkov za račun Apple.

Lahko zahtevate omejitev obdelave in vložite pritožbo pri nadzornem organu v svoji državi; v Švici je to zvezni pooblaščenec za varstvo podatkov in informacije (FDPIC).

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
