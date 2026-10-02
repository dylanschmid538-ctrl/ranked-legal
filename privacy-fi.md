---
title: Tietosuojaseloste · Calisthenics Skills – Ranked
permalink: /privacy/fi/
---

> *Tämä on käännös. Jos versiot eroavat toisistaan, [englanninkielinen versio](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/) on määräävä.*

# Tietosuojaseloste · Calisthenics Skills – Ranked

**Päivitetty viimeksi: 2026-10-02**

Tässä selosteessa kerrotaan, mitä tietoja Ranked kerää, minne ne siirtyvät ja mitä voit tehdä asialle. Seloste on laadittu sovelluksen todellisen koodin pohjalta, ei mallista; jos jokin tässä on väärin, koodi on tarkistettava.

Ranked-sovellusta ylläpitää **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Sveitsi**, yhteys **dylan.schmid538@gmail.com**. Hän on tässä kuvatun käsittelyn rekisterinpitäjä.

---

## 1. Lyhyesti

**Ikäsi, sukupuolesi, pituutesi ja painosi eivät koskaan poistu laitteeltasi.** Tasolaskenta käyttää niitä puhelimessasi. Niitä ei lähetetä meille eikä analytiikkapalveluun.

Vain kahdenlaiset tiedot poistuvat laitteeltasi:

1. **Nimettömät käyttötilastot**, joiden avulla näemme, miten sovellusta käytetään. Voit poistaa ne käytöstä sovelluksessa milloin tahansa.
2. **Ostotiedot**, jotta App Store -tilaus voidaan vahvistaa. Apple käsittelee maksun; me emme koskaan näe maksutietojasi.

Ranked ei seuraa sinua muissa sovelluksissa tai verkkosivustoilla, ei näytä mainoksia eikä lue tietoja Apple Healthista.

---

## 2. Laitteellesi jäävät tiedot

Seuraavat tiedot tallennetaan sovelluksen omaan tietokantaan puhelimessasi eikä niitä koskaan siirretä:

- Jokainen kirjaamasi harjoitus, sarja, toisto, pito ja lisäpaino
- Harjoitussuunnitelmasi, aikataulusi, muistutuksesi ja asetuksesi
- Ilmoittamasi kehon mitat (ikä, sukupuoli, pituus ja paino)
- Harjoitusmuistiinpanosi

Sovellus ei jätä tätä tietokantaa pois laitteen varmuuskopiosta. Jos käytät iCloud-varmuuskopiointia tai tietokoneen varmuuskopiota, harjoitustietosi sisältyvät siihen ja palautuvat varmuuskopiota palautettaessa — Applen, eivät meidän, ehtojen mukaisesti.

Sovelluksen poistaminen poistaa nämä tiedot laitteelta. Emme voi palauttaa niitä, koska ne eivät koskaan olleet meillä.

---

## 3. Laitteelta siirtyvät tiedot

### 3.1 Käyttötilastot (PostHog)

Käytämme **PostHogia**, jota isännöidään **Euroopan unionissa**, ymmärtääksemme sovelluksen käyttöä. Sovellus lähettää sille kiinteän luettelon tapahtumia:

- mihin käyttöönoton vaiheeseen pääsit, minkä suoritit tai mistä palasit takaisin sekä kunkin vaiheen kesto;
- aloitusarvioinnin tulos: kuinka monta taitolinjaa ja vaihetta ilmoitit hallitsevasi, minkä taidon valitsit tavoitteeksi, aloitustasosi ja kunkin kuuden kehonalueesi taso;
- milloin ostonäkymä näytettiin tai suljettiin ja milloin osto aloitettiin, saatiin päätökseen tai palautettiin, kyseisine tuotteineen ja tarjouksineen; kun sovellus myöhemmin havaitsee aktiivisen kokeilujakson tai maksetun tilausjakson, tuotteen ja tiedon siitä, onko kyse testiyhteisön ostosta (tämä ei ole luettelo jokaisesta veloituksesta eikä sitä lähetetä sovelluksen ollessa suljettuna);
- milloin tasosi muuttui ja mikä taito muutoksen aiheutti;
- milloin suoritit vaiheen: mikä taito ja vaihe oli kyseessä ja perustuiko se kirjattuun sarjaan, jälkikäteen lisättyyn harjoitukseen vai manuaaliseen ilmoitukseen;
- mitkä näkymät avaat ja milloin harjoitus päättyy. Harjoituksen päättymistapahtumassa ei ole yksityiskohtia: ei liikkeitä, sarjoja eikä lukumääriä.

Sovelluksen PostHog-ohjelmisto liittää tapahtumiin myös tavanomaisia teknisiä tietoja, kuten laitteen mallin, iOS-version, sovellusversion, kielen ja aikavyöhykkeen, ja kirjaa sovelluksen avaamisen ja siirtymisen taustalle. Kuten mikä tahansa verkkopalvelu, PostHog saa pyynnön IP-osoitteen ja saattaa päätellä siitä likimääräisen sijainnin (maan tai kaupungin).

**Mukana ei ole:** nimeä, sähköpostiosoitetta (sovellus ei kysy sitä), tilitunnistetta (sellaista ei ole), ikää, sukupuolta, pituutta, painoa eikä harjoitustesi sisältöä.

**Tunnistaminen:** PostHog luo satunnaisen tunnisteen, kun sovellus käynnistetään ensimmäisen kerran, ja tallentaa sen laitteellesi. Kaikki tapahtumat ryhmitellään tämän tunnisteen alle. Sovellus ei koskaan kerro PostHogille, kuka olet, eikä sillä ole tiliä tai sähköpostia, jonka se voisi kertoa.

**Poistaminen käytöstä:** Asetukset ▸ Tietosuoja ▸ *Jaa nimettömiä käyttötietoja*. Kun poistat asetuksen käytöstä, sovellus lakkaa lähettämästä tapahtumia siitä hetkestä alkaen. Asetus tallennetaan laitteellesi ja säilyy sovelluspäivitysten jälkeen.

### 3.2 Apple Search Ads -mainonnan kohdistaminen

Jos asensit Rankedin napautettuasi Apple Search Ads -mainosta, sovellus kysyy Applelta kerran ensimmäisellä käynnistyskerralla, mistä asennus tuli. Apple vastaa mainoksen kampanjan, mainosryhmän, hakusanan ja mainosaineiston, klikkauksen maan tai alueen ja päivämäärän sekä tiedon siitä, oliko kyse uudesta latauksesta vai uudelleenlatauksesta. Sovellus liittää nämä tiedot §3.1:ssä kuvattuun nimettömään PostHog-tunnisteeseen, jotta myöhemmät tapahtumat voidaan ryhmitellä sinut tuoneen mainoksen mukaan.

Tämä käyttää Applen **AdServices**-kehystä, joka ei käytä mainostunnistetta (IDFA) ja jota Apple ei pidä seurannana; siksi seurantaluvan kyselyä ei näytetä. Jos et tullut mainoksen kautta, Apple ilmoittaa sen eikä muuta liitetä. Käyttötilastojen poistaminen käytöstä (§3.1) lopettaa myös tämän.

### 3.3 Ostot (Apple ja RevenueCat)

**Apple** myy ja laskuttaa tilaukset App Storessa. Emme koskaan näe maksutietojasi, Apple-tiliäsi tai nimeäsi.

Sovellus käyttää **RevenueCatia** tarkistaakseen tilauksesi voimassaolon. RevenueCat saa tilauksesi App Store -ostotiedon — ostetun tuotteen sekä tilauksen alku- ja päättymisajan — ja tavanomaisia teknisiä tietoja, kuten iOS- ja sovellusversion. Se tunnistaa sovelluksen asennuksen itse luomallaan satunnaisella tunnisteella, joka tallennetaan laitteellesi. Emme anna RevenueCatille nimeäsi, sähköpostiosoitettasi tai muuta henkilöllisyyttä; koska Rankedissa ei ole tilejä, sellaista ei ole annettavaksi.

Kun napautat **Palauta ostot**, sovellus pyytää Applelta laitteelle kirjautuneella Apple-tilillä tehdyt ostot ja välittää tuloksen RevenueCatille samalla tavalla.

---

## 4. Mitä Ranked ei tee

- **Ei tilejä.** Et koskaan kirjaudu sisään. Sinusta ei ole profiilia millään palvelimella.
- **Ei Apple Healthia.** Ranked ei lue Terveys-sovelluksen tietoja eikä kirjoita sinne.
- **Ei kameraa, kuvia, mikrofonia, sijaintia eikä yhteystietoja.** Sovellus ei pyydä näitä käyttöoikeuksia.
- **Ei seurantaa sovellusten tai verkkosivustojen välillä**, ei mainostunnistetta, sovelluksen sisäisiä mainoksia eikä tietojen myyntiä tai antamista tietovälittäjille.
- **Ei push-palvelinta.** Muistutukset ajastetaan paikallisesti puhelimellasi; niihin liittyviä tietoja ei siirretä laitteelta. Sinulta kysytään lupaa ennen ensimmäisen muistutuksen ajastamista, ja voit poistaa ne käytöstä iOS-asetuksissa milloin tahansa.

---

## 5. Oikeusperuste (GDPR ja Sveitsin uudistettu tietosuojalaki)

| Käsittely | Oikeusperuste |
|---|---|
| Ostot ja tilauksen vahvistaminen (§3.3) | Sopimuksen täytäntöönpano |
| Käyttötilastot (§3.1) | Oikeutettu etu ymmärtää ja parantaa sovellusta; voit vastustaa milloin tahansa poistamalla tilastot käytöstä, ks. §8 |
| Search Ads -kohdistaminen (§3.2) | Oikeutettu etu selvittää, mikä mainonta toimii; vastustaminen kuten edellä |

**Tässä sovelletaan kahta lakia, ei vain yhtä.** Rankedia ylläpidetään Sveitsistä, joten käsittelyä säätelee Sveitsin uudistettu liittovaltion tietosuojalaki (**revDSG**, voimassa syyskuusta 2023). **GDPR** soveltuu lisäksi, kun sovellusta käytetään Euroopan unionista tai Yhdistyneestä kuningaskunnasta. Jos säännöt eroavat, noudatamme tiukempaa. Sveitsissä asuvilla on samat §8:ssa luetellut keskeiset oikeudet revDSG:n 25 artiklasta eteenpäin.

---

## 6. Missä tietoja käsitellään

- **PostHog** käsittelee käyttötilastot Euroopan unionissa.
- **RevenueCat, Inc.** sijaitsee Yhdysvalloissa ja käsittelee siellä §3.3:ssa kuvatut ostotiedot.
- **Apple** käsittelee oston ja Search Ads -kohdistamista koskevan pyynnön oman tietosuojakäytäntönsä mukaisesti. Käytäntö koskee Apple-tiliäsi tästä sovelluksesta riippumatta.

---

## 7. Säilytysaika

Käyttötilastoja säilytetään niin kauan kuin PostHog-sopimuksemme säilytysaika edellyttää. Emme lupaa kiinteää kuukausimäärää, koska PostHog ei anna meidän asettaa sitä; mahdoton lupaus olisi tietosuojaselosteessa huonompi kuin luvun puuttuminen.

RevenueCat säilyttää ostotiedot niin kauan kuin tilaus ja sen historia ovat olemassa, koska tilausten vahvistaminen edellyttää sitä.

Laitteesi tiedot pysyvät siellä, kunnes poistat sovelluksen.

---

## 8. Oikeutesi

Voit milloin tahansa:

- **Poistaa käyttötilastot käytöstä** kohdassa Asetukset ▸ Tietosuoja. Tämä on oikeutesi vastustaa käsittelyä ja, jos käsittely perustuu suostumukseen, peruuttaa suostumus. Muutos tulee voimaan heti eikä vaadi perustelua.
- **Poistaa tietosi.** Koska Ranked ei säilytä sinua koskevia tietoja palvelimella, sovelluksen poistaminen poistaa kaiken, mitä sovellus itse tallentaa.
- **Pyytää nimettömän analytiikkaprofiilisi poistamista.** Emme löydä sitä nimellä, koska sillä ei ole nimeä. Jos kirjoitat meille likimääräisen ensimmäisen käyttöpäivän ja käyttämäsi laitteen, etsimme sen käsin ja poistamme sen.
- **Pyytää kopiota** tiedoista, joita palvelu säilyttää tunnisteellasi, pyytää meitä **oikaisemaan** niitä tai **rajoittamaan** käsittelyä pyyntöä käsiteltäessä.
- **Tehdä valituksen valvontaviranomaiselle** omassa maassasi; Sveitsissä se on liittovaltion tietosuoja- ja tietojulkisuusvaltuutettu (FDPIC).

Kirjoita näissä asioissa osoitteeseen **dylan.schmid538@gmail.com**.

---

## 9. Lapset

Ranked on tarkoitettu **vähintään 16-vuotiaille**. Sovellus kysyy ikää käyttöönotossa, koska tasolaskenta riippuu siitä, eikä sovellus ole tarkoitettu nuoremmille. Emme tietoisesti kerää tietoja alle 16-vuotiailta.

---

## 10. Muutokset

Tässä osoitteessa julkaistu versio on ajantasainen, ja yläreunan päivämäärä kertoo viimeisimmän muutoksen. Aiemmat versiot näkyvät edelleen näiden sivujen julkaisurepositorion julkisessa historiassa, joten voit nähdä, mitä muuttui ja milloin.

---

> **⚠️ Ei oikeudellista neuvontaa.** Tämän asiakirjan on laatinut insinööri sovelluksen lähdekoodin perusteella, ei juristi. Se kuvaa järjestelmän täsmällisesti yllä mainittuna päivänä; jokainen väite on tarkistettu suhteessa siihen, mitä sovellus todella lähettää. Sitä **ei ole** tarkistettu GDPR:n, Sveitsin revDSG:n, CCPA:n tai muun sääntelyn noudattamisen osalta. Julkaiseminen täyttää Applen vaatimuksen; se ei yksin tarkoita lainmukaisuutta. Anna juristin lukea se, kun sovellus alkaa tuottaa rahaa.
