---
title: Integritetspolicy · Calisthenics Skills – Ranked
permalink: /privacy/sv/
---

> Detta är en översättning. Vid avvikelser gäller [den engelska versionen](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/).

# Integritetspolicy · Calisthenics Skills – Ranked

**Senast uppdaterad: 29 september 2026**

Den här policyn beskriver vilka uppgifter Ranked samlar in, vart de skickas och vad du kan göra åt det. Den är skriven utifrån appens faktiska kod, inte en mall. Om något här är fel är det koden som ska kontrolleras.

Ranked drivs av **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Schweiz**, kontakt **dylan.schmid538@gmail.com**. Hon är personuppgiftsansvarig för den behandling som beskrivs här.

---

## 1. Kortfattat

Ranked har **inga användarkonton och ingen egen server**. Allt om din träning — varje loggat set, dina framsteg i varje färdighet, din rankning, din Power Level och din kroppskarta — lagras på din telefon och laddas aldrig upp någonstans.

**Din ålder, ditt kön, din längd och din kroppsvikt lämnar aldrig enheten.** Rankningsformeln använder dem på telefonen. De skickas varken till oss eller till analystjänsten.

Endast två slags uppgifter lämnar enheten:

1. **Anonym användningsstatistik**, så att vi kan se hur appen används. Du kan stänga av den i appen när som helst.
2. **Köpuppgifter**, så att abonnemanget i App Store kan verifieras. Apple hanterar betalningen; vi ser aldrig dina betalningsuppgifter.

Ranked spårar dig inte mellan andra appar eller webbplatser, visar ingen reklam och läser inget från Apple Health.

---

## 2. Det som stannar på din enhet

Följande lagras i appens egen databas på din telefon och överförs aldrig:

- Varje träningspass, set, repetition, statiskt håll och extra vikt som du loggar
- Dina framsteg inom varje färdighet och nivå, din rankningshistorik och din Power Level
- Din träningsplan, ditt schema, påminnelser och inställningar
- De kroppsmått du angett (ålder, kön, längd och kroppsvikt)
- Dina träningsanteckningar

Appen undantar inte databasen från enhetens säkerhetskopia. Om du använder iCloud Backup eller en säkerhetskopia på datorn ingår träningsuppgifterna där och återkommer när du återställer den, enligt Apples villkor, inte våra.

Om du raderar appen raderas allt detta från enheten. Vi kan inte återskapa det eftersom vi aldrig har haft det.

---

## 3. Det som lämnar din enhet

### 3.1 Användningsstatistik (PostHog)

Vi använder **PostHog**, som finns i **Europeiska unionen**, för att förstå hur appen används. Appen skickar en fast lista med händelser:

- vilket steg i introduktionen du nådde, slutförde eller gick tillbaka från och hur lång tid varje steg tog;
- resultatet av den inledande bedömningen: hur många färdighetslinjer och nivåer du angav som avklarade, vilken färdighet du valde som mål, din startrankning och rankningen för var och en av dina sex kroppsregioner;
- när köpskärmen visades eller stängdes och när ett köp påbörjades, slutfördes eller återställdes, med aktuell produkt och erbjudande; när appen senare ser en aktiv provperiod eller betald abonnemangsperiod, med produkt och om det är ett testköp (detta är inte ett register över varje debitering och skickas inte medan appen är stängd);
- när din rankning ändrades och vilken färdighet som utlöste det;
- när du klarade en nivå: vilken färdighet och nivå samt om det skedde genom ett loggat set, ett träningspass som lades till i efterhand eller en manuell markering;
- vilka skärmar du öppnar och när ett träningspass slutar. Händelsen för avslutat träningspass innehåller inga detaljer: varken övningar, set eller siffror.

PostHog-programvaran i appen lägger också till vanlig teknisk information till varje händelse, till exempel enhetsmodell, iOS-version, appversion, språk och tidszon, och registrerar när appen öppnas och förs till bakgrunden. Som alla internettjänster får PostHog begärans IP-adress; utifrån den kan en ungefärlig plats (land eller stad) härledas.

**Det som inte ingår:** namn, e-postadress (appen frågar aldrig efter någon), kontoidentifierare (det finns inget konto), ålder, kön, längd, kroppsvikt eller innehållet i dina träningspass.

**Så identifieras du:** PostHog skapar en slumpmässig identifierare när appen körs första gången och lagrar den på din enhet. Alla händelser grupperas under den identifieraren. Appen talar aldrig om för PostHog vem du är och det finns inget konto eller någon e-postadress att uppge.

**Stänga av:** Inställningar ▸ Integritet ▸ *Dela anonym användningsdata*. När du stänger av detta slutar appen skicka händelser från den tidpunkten. Inställningen lagras på enheten och finns kvar efter appuppdateringar.

### 3.2 Tillskrivning av Apple Search Ads

Om du installerade Ranked efter att ha tryckt på en Apple Search Ads-annons frågar appen Apple en gång, vid första start, var installationen kom ifrån. Apple svarar med annonsens kampanj, annonsgrupp, sökord och uppsättning annonsmaterial, landet eller regionen och datumet för klicket samt om det var en ny nedladdning eller en omnedladdning. Appen kopplar dessa värden till den anonyma PostHog-identifieraren i §3.1 så att senare händelser kan grupperas efter annonsen som förde dig hit.

Detta använder Apples ramverk **AdServices**, som inte använder reklamidentifieraren (IDFA) och som Apple inte räknar som spårning. Därför visas ingen dialog om spårningstillstånd. Om du inte kom via en annons säger Apple det och inget annat kopplas till identifieraren. Om du stänger av användningsstatistiken (§3.1) stoppas även detta.

### 3.3 Köp (Apple och RevenueCat)

Abonnemang säljs och faktureras av **Apple** via App Store. Vi ser aldrig dina betalningsuppgifter, ditt Apple-konto eller ditt namn.

För att kontrollera om abonnemanget är aktivt använder appen **RevenueCat**. RevenueCat får köpposten från App Store — vilken produkt du köpte, när abonnemanget började och när det löper ut — tillsammans med vanlig teknisk information som iOS-version och appversion. Din installation identifieras med en slumpmässig identifierare som RevenueCat själv skapar och lagrar på enheten. Vi ger inte RevenueCat ditt namn, din e-postadress eller någon annan identitet; eftersom Ranked inte har konton finns det ingen sådan identitet att lämna.

När du trycker på **Återställ köp** begär appen uppgifter från Apple om de köp som gjorts med det Apple-konto som är inloggat på enheten och skickar resultatet till RevenueCat på samma sätt.

---

## 4. Det som Ranked inte gör

- **Inga konton.** Du loggar aldrig in. Ingen server har en profil om dig.
- **Inget Apple Health.** Ranked varken läser från eller skriver till appen Hälsa.
- **Ingen kamera, inga foton, ingen mikrofon, platsdata eller kontakter.** Appen begär inte dessa behörigheter.
- **Ingen spårning mellan appar eller webbplatser**, ingen reklamidentifierare, ingen reklam i appen och inga uppgifter som säljs eller lämnas till datamäklare.
- **Ingen pushserver.** Påminnelser schemaläggs lokalt på din telefon; inget om dem lämnar enheten. Du tillfrågas innan den första schemaläggs och kan när som helst stänga av dem i iOS-inställningarna.

---

## 5. Rättslig grund (GDPR och schweiziska revDSG)

| Behandling | Grund |
|---|---|
| Köp och verifiering av abonnemang (§3.3) | Fullgörande av avtal |
| Användningsstatistik (§3.1) | Berättigat intresse av att förstå och förbättra appen; du kan när som helst invända genom att stänga av den, se §8 |
| Tillskrivning av Search Ads (§3.2) | Berättigat intresse av att veta vilken reklam som fungerar; invändning enligt ovan |

**Två lagar gäller här, inte bara en.** Ranked drivs från Schweiz, så den reviderade schweiziska federala dataskyddslagen (**revDSG**, i kraft sedan september 2023) reglerar behandlingen. **GDPR** gäller dessutom när appen används från Europeiska unionen eller Storbritannien. Om reglerna skiljer sig åt följer vi den striktare. Personer bosatta i Schweiz har samma grundläggande rättigheter som anges i §8 enligt artikel 25 och följande i revDSG.

---

## 6. Var uppgifterna behandlas

- **PostHog** behandlar användningsstatistiken i Europeiska unionen.
- **RevenueCat, Inc.** har sitt säte i USA och behandlar de köpuppgifter som beskrivs i §3.3 där.
- **Apple** behandlar själva köpet och begäran om Search Ads-tillskrivning enligt sin egen integritetspolicy, som gäller ditt Apple-konto oberoende av den här appen.

---

## 7. Hur länge vi sparar uppgifterna

Användningsstatistiken sparas så länge som PostHogs lagringstid för vårt abonnemang gäller. Vi lovar inget fast antal månader, eftersom PostHog inte låter oss ange ett sådant; en tidsgräns som ingen kan hålla är värre i en integritetspolicy än ingen tidsgräns.

RevenueCat sparar köpposter så länge abonnemanget och dess historik finns, vilket behövs för att verifiera abonnemanget.

Allt på din enhet finns kvar där tills du raderar appen.

---

## 8. Dina rättigheter

Du kan när som helst:

- **Stänga av användningsstatistik** i Inställningar ▸ Integritet. Det är din rätt att invända och, när behandlingen bygger på samtycke, att återkalla det. Ändringen gäller omedelbart och kräver ingen motivering.
- **Radera dina uppgifter.** Eftersom Ranked inte har några uppgifter om dig på en server tar en radering av appen bort allt som appen själv lagrar.
- **Be oss radera din anonyma analysprofil.** Vi kan inte hitta den med namn eftersom den inte har något; om du skriver till oss med ungefärligt datum för första användningen och vilken enhet du använde letar vi upp den manuellt och raderar den.
- **Begära en kopia** av uppgifter som en tjänst har under din identifierare, begära **rättelse** eller **begränsning** av behandlingen medan en begäran granskas.
- **Klaga hos en tillsynsmyndighet** i ditt land; i Schweiz är det den federala dataskydds- och offentlighetskommissionären (FDPIC).

Skriv till **dylan.schmid538@gmail.com** för något av detta.

---

## 9. Barn

Ranked är avsedd för personer som är **16 år eller äldre**. Appen frågar om din ålder under introduktionen eftersom rankningsformeln beror på den, och den riktar sig inte till yngre personer. Vi samlar inte medvetet in uppgifter från personer under 16 år.

---

## 10. Ändringar

Den version som publiceras på den här adressen är den aktuella. Datumet överst visar när den senast ändrades. Tidigare versioner finns kvar i den offentliga historiken för det arkiv som publicerar sidorna, så att du kan se vad som ändrades och när.

---

> **⚠️ Ingen juridisk rådgivning.** Detta dokument har skrivits av en ingenjör utifrån appens källkod, inte av en jurist. Det beskriver systemet korrekt per datumet ovan; varje påstående har kontrollerats mot vad appen faktiskt skickar. Det har **inte** granskats för efterlevnad av GDPR, schweiziska revDSG, CCPA eller något annat regelverk. Publiceringen uppfyller Apples krav, men gör dig inte regelefterlevande. Låt en jurist läsa det när appen börjar ge intäkter.
