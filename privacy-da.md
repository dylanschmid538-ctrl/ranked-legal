---
title: Privatlivspolitik · Calisthenics Skills – Ranked
permalink: /privacy/da/
---

> Dette er en oversættelse. Ved uoverensstemmelser er [den engelske version](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/) gældende.

# Privatlivspolitik · Calisthenics Skills – Ranked

**Senest opdateret: 29. september 2026**

Denne politik beskriver, hvilke oplysninger Ranked indsamler, hvor de sendes hen, og hvad du kan gøre ved det. Den er skrevet ud fra appens faktiske kode, ikke en skabelon. Hvis noget her er forkert, er det koden, der skal kontrolleres.

Ranked drives af **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Schweiz**, kontakt **dylan.schmid538@gmail.com**. Hun er dataansvarlig for den behandling, der er beskrevet her.

---

## 1. Kort fortalt

Ranked har **ingen brugerkonti og ingen egen server**. Alt om din træning — hvert registreret sæt, dine fremskridt i hver færdighed, din rang, dit Power Level og dit kropskort — gemmes på din telefon og uploades aldrig nogen steder.

**Din alder, dit køn, din højde og din kropsvægt forlader aldrig din enhed.** Rangformlen bruger dem på telefonen. De sendes hverken til os eller analysetjenesten.

Kun to slags oplysninger forlader din enhed:

1. **Anonym brugsstatistik**, så vi kan se, hvordan appen bruges. Du kan slå den fra i appen når som helst.
2. **Købsoplysninger**, så App Store-abonnementet kan kontrolleres. Apple håndterer betalingen; vi ser aldrig dine betalingsoplysninger.

Ranked sporer dig ikke på tværs af andre apps eller websteder, viser ingen reklamer og læser intet fra Apple Health.

---

## 2. Hvad der bliver på din enhed

Følgende gemmes i appens egen database på din telefon og overføres aldrig:

- Hver træning, hvert sæt, hver gentagelse, hvert hold og hver ekstra vægt, du registrerer
- Dine fremskridt gennem hver færdighed og fase, din ranghistorik og dit Power Level
- Din træningsplan, tidsplan, påmindelser og indstillinger
- De kropsmål, du har indtastet (alder, køn, højde og kropsvægt)
- Dine træningsnoter

Appen udelukker ikke denne database fra sikkerhedskopien af din enhed. Hvis du bruger iCloud Backup eller en sikkerhedskopi på en computer, indgår dine træningsdata i den og vender tilbage ved gendannelse — på Apples vilkår, ikke vores.

Når du sletter appen, slettes alt dette fra enheden. Vi kan ikke genskabe det, fordi vi aldrig har haft det.

---

## 3. Hvad der forlader din enhed

### 3.1 Brugsstatistik (PostHog)

Vi bruger **PostHog**, som hostes i **Den Europæiske Union**, til at forstå, hvordan appen bruges. Appen sender en fast liste af hændelser:

- hvilket trin i opsætningen du nåede, gennemførte eller gik tilbage fra, og hvor lang tid hvert trin tog;
- resultatet af den indledende vurdering: hvor mange færdighedslinjer og faser du angav som opnået, hvilken færdighed du valgte som mål, din startrang og rangen for hver af dine seks kropsregioner;
- hvornår købsskærmen blev vist eller lukket, og hvornår et køb blev startet, gennemført eller gendannet, med det tilhørende produkt og tilbud; hvornår appen senere registrerer en aktiv prøveperiode eller en betalt abonnementsperiode, med produktet og oplysning om, hvorvidt det er et testkøb (dette er ikke en registrering af hver opkrævning, og det sendes ikke, mens appen er lukket);
- hvornår din rang ændrede sig, og hvilken færdighed der udløste det;
- hvornår du klarede en fase: hvilken færdighed og fase, og om det skete via et registreret sæt, en træning tilføjet efterfølgende eller en manuel markering;
- hvilke skærme du åbner, og hvornår en træning slutter. Hændelsen for en afsluttet træning indeholder ingen detaljer: hverken øvelser, sæt eller tal.

PostHog-softwaren i appen føjer også standardtekniske oplysninger til hver hændelse, såsom enhedsmodel, iOS-version, appversion, sprog og tidszone, og registrerer, hvornår appen åbnes og lægges i baggrunden. Som enhver internettjeneste modtager PostHog IP-adressen for anmodningen; den kan bruges til at udlede en omtrentelig placering (land eller by).

**Dette er ikke med:** navn, e-mailadresse (appen spørger aldrig om den), kontoidentifikator (der er ingen konto), alder, køn, højde, kropsvægt eller indholdet af dine træninger.

**Sådan identificeres du:** PostHog danner en tilfældig identifikator, første gang appen kører, og gemmer den på din enhed. Alle hændelser samles under denne identifikator. Appen fortæller aldrig PostHog, hvem du er, og der er hverken konto eller e-mail at fortælle om.

**Sådan slår du det fra:** Indstillinger ▸ Privatliv ▸ *Del anonyme brugsdata*. Når du slår det fra, stopper appen med at sende hændelser fra det tidspunkt. Indstillingen gemmes på din enhed og overlever appopdateringer.

### 3.2 Tilskrivning af Apple Search Ads

Hvis du installerede Ranked efter at have trykket på en Apple Search Ads-annonce, spørger appen Apple én gang ved første start, hvor installationen kom fra. Apple svarer med annoncens kampagne, annoncegruppe, søgeord og sæt af kreativt materiale, landet eller regionen og datoen for klikket samt om det var en ny download eller en gendownload. Appen knytter disse værdier til den anonyme PostHog-identifikator fra §3.1, så senere hændelser kan grupperes efter den annonce, der førte dig til appen.

Dette bruger Apples **AdServices**-framework, som ikke bruger reklameidentifikatoren (IDFA), og som Apple ikke betragter som sporing. Derfor vises ingen dialog om sporingstilladelse. Hvis du ikke kom via en annonce, oplyser Apple det, og intet andet tilføjes. Hvis du slår brugsstatistik fra (§3.1), stopper dette også.

### 3.3 Køb (Apple og RevenueCat)

Abonnementer sælges og faktureres af **Apple** via App Store. Vi ser aldrig dine betalingsoplysninger, din Apple-konto eller dit navn.

For at kontrollere, om dit abonnement er aktivt, bruger appen **RevenueCat**. RevenueCat modtager købsposten fra App Store for dit abonnement — det købte produkt, starttidspunktet og udløbstidspunktet — sammen med standardtekniske oplysninger som iOS-version og appversion. Din installation identificeres med en tilfældig identifikator, som RevenueCat selv danner og gemmer på din enhed. Vi giver ikke RevenueCat dit navn, din e-mailadresse eller nogen anden identitet; fordi Ranked ikke har konti, findes der ingen sådan identitet at give.

Når du trykker på **Gendan køb**, beder appen Apple om de køb, der er foretaget med den Apple-konto, som er logget ind på enheden, og sender resultatet videre til RevenueCat på samme måde.

---

## 4. Hvad Ranked ikke gør

- **Ingen konti.** Du logger aldrig ind. Ingen server har en profil om dig.
- **Intet Apple Health.** Ranked hverken læser fra eller skriver til appen Sundhed.
- **Intet kamera, ingen fotos, mikrofon, placering eller kontakter.** Appen beder ikke om disse tilladelser.
- **Ingen sporing på tværs af apps eller websteder**, ingen reklameidentifikator, ingen reklamer i appen og ingen data, der sælges eller gives til datamæglere.
- **Ingen pushserver.** Påmindelser planlægges lokalt på din telefon; intet om dem forlader enheden. Du bliver spurgt, før den første planlægges, og du kan når som helst slå dem fra i iOS-indstillingerne.

---

## 5. Retsgrundlag (GDPR og schweiziske revDSG)

| Behandling | Grundlag |
|---|---|
| Køb og kontrol af abonnement (§3.3) | Opfyldelse af en kontrakt |
| Brugsstatistik (§3.1) | Legitim interesse i at forstå og forbedre appen; du kan til enhver tid gøre indsigelse ved at slå det fra, se §8 |
| Tilskrivning af Search Ads (§3.2) | Legitim interesse i at vide, hvilke annoncer der virker; indsigelse som ovenfor |

**To love gælder her, ikke kun én.** Ranked drives fra Schweiz, så den reviderede schweiziske føderale databeskyttelseslov (**revDSG**, i kraft siden september 2023) regulerer behandlingen. **GDPR** gælder derudover, hvor appen bruges fra Den Europæiske Union eller Storbritannien. Hvis reglerne er forskellige, følger vi den strengere. Personer bosat i Schweiz har de samme grundlæggende rettigheder som i §8 efter artikel 25 ff. i revDSG.

---

## 6. Hvor oplysningerne behandles

- **PostHog** behandler brugsstatistikken i Den Europæiske Union.
- **RevenueCat, Inc.** har hjemsted i USA og behandler købsoplysningerne fra §3.3 dér.
- **Apple** behandler selve købet og anmodningen om Search Ads-tilskrivning efter sin egen privatlivspolitik, der gælder for din Apple-konto uafhængigt af denne app.

---

## 7. Hvor længe vi opbevarer dem

Brugsstatistik gemmes så længe, som PostHogs opbevaringsperiode for vores abonnement gælder. Vi lover ikke et fast antal måneder, fordi PostHog ikke lader os angive et. En periode, som ingen kan overholde, er værre i en privatlivspolitik end slet ingen.

RevenueCat gemmer købsposter, så længe abonnementet og dets historik findes, hvilket er nødvendigt for at kontrollere et abonnement.

Alt på din enhed bliver der, indtil du sletter appen.

---

## 8. Dine rettigheder

Du kan når som helst:

- **Slå brugsstatistik fra** i Indstillinger ▸ Privatliv. Det er din ret til at gøre indsigelse og, hvor behandlingen bygger på samtykke, til at trække det tilbage. Det virker straks og kræver ingen begrundelse.
- **Slette dine data.** Fordi Ranked ikke har noget om dig på en server, fjerner sletning af appen alt, som appen selv lagrer.
- **Bede os slette din anonyme analyseprofil.** Vi kan ikke finde den ud fra et navn, for den har intet. Hvis du skriver den omtrentlige dato, hvor du første gang brugte appen, og hvilken enhed du brugte, finder vi den manuelt og sletter den.
- **Bede om en kopi** af de data, en tjeneste har under din identifikator, bede os **rette** dem eller **begrænse** behandlingen, mens en anmodning undersøges.
- **Klage til en tilsynsmyndighed** i dit land; i Schweiz er det den føderale data- og offentlighedskommissær (FDPIC).

Skriv til **dylan.schmid538@gmail.com** om noget af dette.

---

## 9. Børn

Ranked er til personer på **16 år og derover**. Appen spørger om din alder under opsætningen, fordi rangformlen afhænger af den, og den er ikke rettet mod yngre personer. Vi indsamler ikke bevidst data fra personer under 16 år.

---

## 10. Ændringer

Den version, der er offentliggjort på denne adresse, er den aktuelle. Datoen øverst viser, hvornår den sidst blev ændret. Tidligere versioner forbliver synlige i den offentlige historik for det arkiv, hvorfra siderne offentliggøres, så du kan se, hvad der blev ændret og hvornår.

---

> **⚠️ Ikke juridisk rådgivning.** Dette dokument er skrevet af en ingeniør ud fra appens kildekode, ikke af en jurist. Det beskriver systemet korrekt pr. ovenstående dato; hvert udsagn er kontrolleret mod, hvad appen faktisk sender. Det er **ikke** blevet gennemgået for overholdelse af GDPR, schweiziske revDSG, CCPA eller andre regler. Offentliggørelse opfylder Apples krav, men gør dig ikke lovmedholdelig. Få en jurist til at gennemgå det, når appen begynder at tjene penge.
