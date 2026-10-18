---
title: Privatlivspolitik · Calisthenics Skills – Ranked
permalink: /privacy/da/
---

> Dette er en oversættelse. Ved uoverensstemmelser er [den engelske version](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/) gældende.

# Privatlivspolitik · Calisthenics Skills – Ranked

**Senest opdateret: 2026-10-18**

Denne politik beskriver, hvilke oplysninger Ranked indsamler, hvor de sendes hen, og hvad du kan gøre ved det.

Ranked drives af **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Schweiz**, kontakt **dylan.schmid538@gmail.com**. Hun er dataansvarlig for den behandling, der er beskrevet her.

---

## 1. Kort fortalt

**Din alder, dit køn, din højde og din kropsvægt forlader aldrig din enhed.** Rangformlen bruger dem på telefonen. De sendes hverken til os eller analysetjenesten.

Tre slags oplysninger kan forlade din enhed:

1. **Brugsstatistik**, Ranked deler kun disse statistikker, hvis du tillader Apples standardanmodning om sporing. Du kan slå deling fra i appen eller tilbagekalde tilladelsen i iOS-indstillinger.
2. **Købsoplysninger**, så App Store-abonnementet kan kontrolleres. Apple håndterer betalingen; vi ser aldrig dine betalingsoplysninger.
3. **Feedback- og supportbeskeder**, kun når du selv sender dem. Du kan særskilt give samtykke til at oplyse e-mail eller telefonnummer for et svar.

Ranked bruger ikke annonce-id’et IDFA, viser ikke reklamer i appen og sælger eller videregiver ikke data til datamæglere. Brugsstatistik og tilskrivning fra Apple Search Ads sendes kun, hvis du tillader sporing i ATT-dialogen; overførslen fortsætter, så længe analyse er slået til i appen. Ranked læser heller ikke fra Apple Health.

---

## 2. Hvad der bliver på din enhed

Følgende gemmes i appens egen database på din telefon og overføres aldrig:

- Hver træning, hvert sæt, hver gentagelse, hvert hold og hver ekstra vægt, du registrerer
- Din træningsplan, tidsplan, påmindelser og indstillinger
- De kropsmål, du har indtastet (alder, køn, højde og kropsvægt)
- Dine træningsnoter

Appen udelukker ikke denne database fra sikkerhedskopien af din enhed. Hvis du bruger iCloud Backup eller en sikkerhedskopi på en computer, indgår dine træningsdata i den og vender tilbage ved gendannelse — på Apples vilkår, ikke vores.

Når du sletter appen, slettes alt dette fra enheden. Vi kan ikke genskabe det, fordi vi aldrig har haft det.

---

## 3. Hvad der forlader din enhed

### 3.1 Brugsstatistik (PostHog)

Første gang du åbner appen, viser iOS Apples standarddialog om tilladelse til sporing (App Tracking Transparency, ATT). Ranked sender kun brugsoplysninger til PostHog i EU, hvis du tillader sporing i ATT-dialogen; derefter fortsætter overførslerne, så længe analyse er slået til i appen. Hændelserne omfatter opsætning, første vurdering, ændringer i rang og trin (med færdighed og trin), købsskærm, køb og åbnede skærme. Hændelser fra live træning angiver start, afslutning eller afbrydelse, forløbne sekunder, antal registrerede sæt, antal forskellige færdigheder og om det var den første afsluttede træning. De indeholder ikke enkelte øvelser, gentagelser, vægte eller noter. Alder, køn, højde og kropsvægt sendes ikke. PostHog modtager også almindelige tekniske oplysninger om enhed, iOS, app og sprog samt IP-adressen, hvorfra en omtrentlig placering kan udledes. Når du har tilladt sporing og slået analyse til, opretter PostHog en tilfældig installationsidentifikator og knytter hændelser og kampagneoplysninger til den med henblik på analyse og måling af annoncer. IDFA bruges ikke. Du kan slå analyse fra under Indstillinger ▸ Data og anonymitet eller tilbagekalde sporingstilladelsen i iOS-indstillingerne. Når en af mulighederne slås fra, stopper fremtidige overførsler; allerede sendte data slettes ikke automatisk.

Appen kan også rapportere abonnementsfasen, den aktuelle adgang, fornyelsesstatus og om en opsigelse eller et faktureringsproblem blev registreret. Disse observationer er ikke bevis for en opkrævning og sendes kun, mens analyse er aktiveret.

Med dit samtykke registrerer brugshændelser også, når du vælger en træningsplan, og når du åbner en træningssession. Valg af plan omfatter kun antallet af træningsdage om ugen og øvelser; åbning af en session omfatter kun, om den genoptages, indgangskilden og antallet af foreskrevne øvelser. Planernes fulde indhold, tidsplaner, individuelle øvelser og træningsnoter forbliver på din enhed.

> Valgfrit: Del brug af appen, vurderede færdigheder, rang, træningsaktivitet og kampagnedata fra Apple Search Ads med PostHog for at forbedre Ranked. Vi knytter også denne brug til din prøveperiode og dit abonnement via en tilfældig købsreference. Ingen navne eller træningsnoter. Du kan ændre dette når som helst i Indstillinger.

### 3.2 Tilskrivning af Apple Search Ads

Ranked anmoder kun om tilskrivning fra Apple Search Ads og forespørger kun AdServices, hvis du tillader sporing i ATT-dialogen og har slået analyse til i appen. I så fald kan oplysninger om kampagne, annoncegruppe, søgeord, annonceindhold, land eller region, klikdato og downloadtype knyttes til den tilfældige PostHog-installationsidentifikator med henblik på analyse og måling af annoncer. IDFA bruges ikke. Hvis du slår analyse fra eller tilbagekalder ATT-tilladelsen, stopper tilskrivningen og fremtidige overførsler; tidligere data slettes ikke automatisk.

### 3.3 Køb (Apple og RevenueCat)

Abonnementer sælges og faktureres af **Apple** via App Store. Vi ser aldrig dine betalingsoplysninger, din Apple-konto eller dit navn.

For at kontrollere, om dit abonnement er aktivt, bruger appen **RevenueCat**. RevenueCat modtager købsposten fra App Store for dit abonnement — det købte produkt, starttidspunktet og udløbstidspunktet — sammen med standardtekniske oplysninger som iOS-version og appversion. Din installation identificeres med en tilfældig identifikator, som RevenueCat selv danner og gemmer på din enhed. Vi giver ikke RevenueCat dit navn, din e-mailadresse eller nogen anden identitet; fordi Ranked ikke har konti, findes der ingen sådan identitet at give.

Når du trykker på **Gendan køb**, beder appen Apple om de køb, der er foretaget med den Apple-konto, som er logget ind på enheden, og sender resultatet videre til RevenueCat på samme måde.

### 3.4 Feedback- og supportbeskeder (Cloudflare og CloudKit)

Hvis du sender feedback eller en supportanmodning, sender Ranked beskeden, dens kategori og kilde til en Cloudflare Worker. Den gemmer oplysningerne i Apples offentlige CloudKit-database ved hjælp af en privat servernøgle. Du behøver ikke logge på iCloud for at sende en besked. Cloudflare Worker bruger netværksadressen til en teknisk begrænsning mod misbrug; hverken den oprindelige adresse eller en hash af den gemmes i feedbackposten i CloudKit. Du kan særskilt give samtykke til at oplyse en e-mailadresse eller et telefonnummer, så vi kan svare uden for appen. Beskeder og kontaktoplysninger sendes ikke til PostHog eller RevenueCat og knyttes ikke til en konto i appen. Vi behandler beskeden for at besvare din henvendelse og valgfrie kontaktoplysninger med dit samtykke. Der er i øjeblikket ingen fast frist for automatisk sletning af beskeder eller kontaktoplysninger. Du kan anmode om indsigt eller sletning på **dylan.schmid538@gmail.com**.

---

## 4. Sporing og tilladelser i Ranked

- **Ingen konti.** Du logger aldrig ind. Ingen server har en profil om dig.
- **Intet Apple Health.** Ranked hverken læser fra eller skriver til appen Sundhed.
- **Intet kamera, ingen fotos, mikrofon, placering eller kontakter.** Appen beder ikke om disse tilladelser.
- **Ranked bruger ikke annonce-id’et IDFA, viser ikke reklamer i appen og sælger eller videregiver ikke data til datamæglere. Brugsstatistik og tilskrivning fra Apple Search Ads sendes kun, hvis du tillader sporing i ATT-dialogen; overførslen fortsætter, så længe analyse er slået til i appen.**
- **Ingen pushserver.** Påmindelser planlægges lokalt på din telefon; intet om dem forlader enheden. Du bliver spurgt, før den første planlægges, og du kan når som helst slå dem fra i iOS-indstillingerne.

---

## 5. Retsgrundlag (GDPR og schweiziske revDSG)

| Behandling | Grundlag |
|---|---|
| Køb og kontrol af abonnement (§3.3) | Opfyldelse af en kontrakt |
| Brugsstatistik (§3.1) | Dit samtykke via ATT-tilladelsen og analyseindstillingen i Ranked; du kan slå hver af dem fra når som helst, se §8 |
| Tilskrivning af Search Ads (§3.2) | Dit samtykke via ATT-tilladelsen og analyseindstillingen i Ranked; du kan slå hver af dem fra når som helst, se §8 |

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

Du kan til enhver tid trække dit samtykke til analyse tilbage i Indstillinger ▸ Data og anonymitet uden begrundelse. Det stopper straks nye hændelser, men sletter ikke automatisk allerede sendte data og opsiger ikke dit App Store-abonnement.

Du kan slette lokale træningsdata under Indstillinger ▸ Data og anonymitet ▸ *Slet lokale træningsdata* eller ved at slette appen. Abonnementet administreres og opsiges særskilt i din Apple-konto.

For data, der allerede er sendt til PostHog, kan du skrive til **dylan.schmid538@gmail.com**. Ranked knytter ikke det tilfældige analyse-id til en konto. En omtrentlig dato eller enhedsmodel er muligvis ikke nok til sikkert at finde din profil. Vi forklarer, hvad vi kan identificere, og behandler verificerbare anmodninger om indsigt, rettelse eller sletning. Send ikke oplysningerne til din Apple-konto.

Du kan anmode om begrænsning af behandlingen og klage til tilsynsmyndigheden i dit land; i Schweiz er det den føderale databeskyttelses- og informationskommissær (FDPIC).

---

## 9. Børn

Ranked er til personer på **16 år og derover**. Appen spørger om din alder under opsætningen, fordi rangformlen afhænger af den, og den er ikke rettet mod yngre personer. Vi indsamler ikke bevidst data fra personer under 16 år.

---

## 10. Ændringer

Den version, der er offentliggjort på denne adresse, er den aktuelle. Datoen øverst viser, hvornår den sidst blev ændret. Tidligere versioner forbliver synlige i den offentlige historik for det arkiv, hvorfra siderne offentliggøres, så du kan se, hvad der blev ændret og hvornår.

---
