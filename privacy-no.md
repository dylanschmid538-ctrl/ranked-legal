---
title: Personvernerklæring
permalink: /privacy/no/
---

> *Dette er en oversettelse. Ved avvik gjelder den [engelske versjonen](../).*

# Personvernerklæring · Calisthenics Skills – Ranked

**Sist oppdatert: 29. september 2026**

Denne erklæringen beskriver hvilke opplysninger Ranked samler inn, hvor de sendes, og hva du kan gjøre med dem. Den er skrevet ut fra appens faktiske kode, ikke en mal. Hvis noe her er feil, må koden kontrolleres.

Ranked drives av **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Sveits**, kontakt **dylan.schmid538@gmail.com**. Hun er behandlingsansvarlig for behandlingen som beskrives her.

---

## 1. Kort fortalt

Ranked har **ingen brukerkontoer og ingen egen server.** Alt som gjelder treningen din — hvert sett du logger, fremgangen i hver ferdighet, rangeringen din, Power Level og kroppskartet — lagres på telefonen din og lastes aldri opp noe sted.

**Alder, kjønn, høyde og kroppsvekt forlater aldri enheten din.** Rangformelen bruker dem på telefonen. De sendes verken til oss eller analysetjenesten.

Bare to typer opplysninger forlater enheten:

1. **Anonym bruksstatistikk**, slik at vi kan se hvordan appen brukes. Du kan når som helst slå dette av i appen.
2. **Kjøpsopplysninger**, slik at abonnementet fra App Store kan bekreftes. Apple håndterer betalingen; vi ser aldri betalingsopplysningene dine.

Ranked sporer deg ikke på tvers av andre apper eller nettsteder, viser ingen annonser og leser ingenting fra Apple Helse.

---

## 2. Hva som blir på enheten

Følgende lagres i appens egen database på telefonen og overføres aldri:

- Alle treningsøkter, sett, repetisjoner, statiske hold og ekstra vekter du logger
- Fremgang gjennom hver ferdighet og hvert trinn, rangeringshistorikken og Power Level
- Treningsplan, tidsplan, påminnelser og innstillinger
- Kroppsmålene du oppga (alder, kjønn, høyde, kroppsvekt)
- Treningsnotatene dine

Appen utelukker ikke denne databasen fra sikkerhetskopiering av enheten. Hvis du bruker iCloud-sikkerhetskopi eller en sikkerhetskopi på datamaskinen, inngår treningsdataene dine i den og kommer tilbake når den gjenopprettes — etter Apples vilkår, ikke våre.

Når du sletter appen, slettes alt dette fra enheten. Vi kan ikke gjenopprette det, fordi vi aldri har hatt det.

---

## 3. Hva som forlater enheten

### 3.1 Bruksstatistikk (PostHog)

Vi bruker **PostHog**, som driftes i **Den europeiske union**, for å forstå hvordan appen brukes. Appen sender en fast liste med hendelser:

- hvilket oppsettstrinn du kom til, fullførte eller gikk tilbake fra, og hvor lang tid hvert trinn tok;
- resultatet av den innledende vurderingen: hvor mange ferdighetslinjer og trinn du oppga, hvilken ferdighet du valgte som mål, startrangeringen din og rangeringen for hver av de seks kroppsregionene;
- når kjøpsskjermen ble vist eller lukket, og når et kjøp ble startet, fullført eller gjenopprettet, med tilhørende produkt og tilbud; når appen senere registrerer en aktiv prøveperiode eller en betalt abonnementsperiode, med produktet og om det er et kjøp i testmiljøet (dette er ikke en oversikt over hver belastning og sendes ikke mens appen er lukket);
- når rangeringen din endres, og hvilken ferdighet som utløste endringen;
- når du fullfører et trinn: hvilken ferdighet, hvilket trinn, og om det kom fra et loggført sett, en treningsøkt registrert i ettertid eller en manuell angivelse;
- hvilke skjermer du åpner, og når en treningsøkt avsluttes. Hendelsen for avsluttet økt inneholder ingen detaljer: verken øvelser, sett eller tall.

PostHog-programvaren i appen legger også ved vanlige tekniske opplysninger til hver hendelse, som enhetsmodell, iOS-versjon, appversjon, språk og tidssone, og registrerer når appen åpnes og legges i bakgrunnen. Som alle internetttjenester mottar PostHog forespørselens IP-adresse og kan utlede en omtrentlig plassering (land eller by).

**Dette er ikke med:** navn, e-postadresse (appen ber aldri om den), kontoidentifikator (det finnes ingen), alder, kjønn, høyde, kroppsvekt eller innholdet i treningsøktene dine.

**Hvordan du identifiseres:** PostHog oppretter en tilfeldig identifikator første gang appen kjører og lagrer den på enheten. Alle hendelser grupperes under denne identifikatoren. Appen forteller aldri PostHog hvem du er, og har verken konto eller e-postadresse den kunne oppgitt.

**Slik slår du det av:** Innstillinger ▸ Personvern ▸ *Del anonyme bruksdata*. Når du slår dette av, slutter appen å sende hendelser fra det tidspunktet. Innstillingen lagres på enheten og beholdes gjennom appoppdateringer.

### 3.2 Tilordning fra Apple Search Ads

Hvis du installerte Ranked etter å ha trykket på en Apple Search Ads-annonse, spør appen Apple én gang ved første oppstart hvor installasjonen kom fra. Apple oppgir annonsekampanje, annonsegruppe, søkeord og annonsemateriell, landet eller regionen og datoen for klikket, samt om det var en ny nedlasting eller en nedlasting på nytt. Appen knytter disse verdiene til den anonyme PostHog-identifikatoren i §3.1, slik at senere hendelser kan grupperes etter annonsen som førte deg hit.

Dette bruker Apples **AdServices**-rammeverk, som ikke bruker annonseidentifikatoren (IDFA), og som Apple ikke regner som sporing. Derfor vises ingen forespørsel om sporingstillatelse. Hvis du ikke kom via en annonse, oppgir Apple dette og ingenting knyttes til. Hvis du slår av bruksstatistikk (§3.1), stopper også dette.

### 3.3 Kjøp (Apple og RevenueCat)

Abonnementer selges og faktureres av **Apple** gjennom App Store. Vi ser aldri betalingsopplysningene dine, Apple-kontoen din eller navnet ditt.

For å kontrollere om abonnementet ditt er aktivt bruker appen **RevenueCat**. RevenueCat mottar kjøpsoppføringen fra App Store for abonnementet ditt — hvilket produkt som ble kjøpt, når det startet og når det utløper — sammen med vanlige tekniske opplysninger, som iOS-versjon og appversjon. Tjenesten kjenner igjen installasjonen din ved hjelp av en tilfeldig identifikator som den selv oppretter og lagrer på enheten. Vi gir ikke RevenueCat navn, e-postadresse eller annen identitet, og siden Ranked ikke har kontoer, finnes det heller ingen slik identitet å gi.

Når du trykker på **Gjenopprett kjøp**, ber appen Apple om kjøp gjort med Apple-kontoen som er logget inn på enheten og sender resultatet til RevenueCat på samme måte.

---

## 4. Hva Ranked ikke gjør

- **Ingen kontoer.** Du logger aldri inn. Det finnes ingen profil av deg på en server.
- **Ingen Apple Helse.** Ranked verken leser fra eller skriver til Helse-appen.
- **Ingen kamera, bilder, mikrofon, posisjon eller kontakter.** Appen ber ikke om disse tillatelsene.
- **Ingen sporing på tvers av apper eller nettsteder**, ingen annonseidentifikator, ingen annonser i appen og ingen salg eller overføring av data til datameglere.
- **Ingen server for pushvarsler.** Påminnelsene fra Ranked planlegges lokalt på telefonen; ingen opplysninger om dem forlater enheten. Du blir spurt før den første planlegges, og du kan når som helst slå dem av i iOS-innstillingene.

---

## 5. Rettslig grunnlag (GDPR og sveitsisk revDSG)

| Behandling | Grunnlag |
|---|---|
| Kjøp og bekreftelse av abonnement (§3.3) | Oppfyllelse av en avtale |
| Bruksstatistikk (§3.1) | Berettiget interesse i å forstå og forbedre appen; du kan når som helst protestere ved å slå den av, se §8 |
| Tilordning fra Search Ads (§3.2) | Berettiget interesse i å vite hvilken annonsering som virker; protest som ovenfor |

**To lovverk gjelder her, ikke bare ett.** Ranked drives fra Sveits, og behandlingen reguleres derfor av den reviderte sveitsiske føderale personvernloven (**revDSG**, i kraft siden september 2023). **GDPR** gjelder i tillegg når appen brukes fra Den europeiske union eller Storbritannia. Der regelverkene er forskjellige, følger vi det strengeste. Bosatte i Sveits har de samme grunnleggende rettighetene som er beskrevet i §8 etter artikkel 25 flg. i revDSG.

---

## 6. Hvor opplysningene behandles

- **PostHog** behandler bruksstatistikk i Den europeiske union.
- **RevenueCat, Inc.** er basert i USA og behandler kjøpsopplysningene i §3.3 der.
- **Apple** behandler selve kjøpet og forespørselen om tilordning fra Search Ads etter sin egen personvernerklæring, som gjelder Apple-kontoen din uavhengig av denne appen.

---

## 7. Hvor lenge vi oppbevarer opplysningene

Bruksstatistikk oppbevares så lenge oppbevaringsperioden for vår PostHog-plan gjelder. Vi lover ikke et fast antall måneder, fordi PostHog ikke lar oss bestemme det — et tall ingen kan overholde, er verre i en personvernerklæring enn ingen tall.

RevenueCat oppbevarer kjøpsoppføringer så lenge abonnementet og historikken finnes, noe som er nødvendig for å bekrefte abonnementet.

Alt på enheten blir der til du sletter appen.

---

## 8. Rettighetene dine

Du kan når som helst:

- **Slå av bruksstatistikk** under Innstillinger ▸ Personvern. Dette er retten din til å protestere og, der behandlingen bygger på samtykke, til å trekke det tilbake. Det virker umiddelbart og krever ingen begrunnelse.
- **Slette dataene dine.** Fordi Ranked ikke lagrer noe om deg på en server, fjerner sletting av appen alt den selv lagrer.
- **Be oss slette den anonyme analyseprofilen din.** Vi kan ikke finne den via navn — den har ikke noe navn — men hvis du skriver til oss med omtrentlig dato for første gangs bruk og hvilken enhet du brukte, vil vi finne den manuelt og slette den.
- **Be om en kopi** av data en tjeneste har under identifikatoren din, be oss **rette** dem eller **begrense** behandlingen mens forespørselen undersøkes.
- **Klage til en tilsynsmyndighet** i landet ditt; i Sveits er dette den føderale datatilsynsmyndigheten (FDPIC).

Skriv til **dylan.schmid538@gmail.com** for å benytte deg av disse rettighetene.

---

## 9. Barn

Ranked er beregnet på personer som er **16 år eller eldre**. Appen spør om alderen din under oppsettet fordi rangformelen avhenger av den, og er ikke rettet mot yngre personer. Vi samler ikke bevisst inn data fra noen under 16 år.

---

## 10. Endringer

Versjonen som er publisert på denne adressen, er den gjeldende. Datoen øverst viser når den sist ble endret. Tidligere versjoner finnes i den offentlige historikken til repositoriet disse sidene publiseres fra, slik at du kan se hva som endret seg og når.

---

> **⚠️ Ikke juridisk rådgivning.** Dette dokumentet ble skrevet ut fra appens kildekode av en ingeniør, ikke en advokat. Det beskriver systemet slik det er på datoen ovenfor; hver påstand er kontrollert mot det appen faktisk sender. Det er **ikke** vurdert for samsvar med GDPR, sveitsisk revDSG, CCPA eller annet regelverk. Publisering oppfyller Apples krav, men betyr ikke at du er i samsvar med loven. Be en advokat gjennomgå det når appen begynner å tjene penger.
