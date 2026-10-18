---
title: Integritetspolicy · Calisthenics Skills – Ranked
permalink: /privacy/sv/
---

> Detta är en översättning. Vid avvikelser gäller [den engelska versionen](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/).

# Integritetspolicy · Calisthenics Skills – Ranked

**Senast uppdaterad: 2026-10-18**

Den här policyn beskriver vilka uppgifter Ranked samlar in, vart de skickas och vad du kan göra åt det.

Ranked drivs av **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Schweiz**, kontakt **dylan.schmid538@gmail.com**. Hon är personuppgiftsansvarig för den behandling som beskrivs här.

---

## 1. Kortfattat

**Din ålder, ditt kön, din längd och din kroppsvikt lämnar aldrig enheten.** Rankningsformeln använder dem på telefonen. De skickas varken till oss eller till analystjänsten.

Tre typer uppgifter kan lämna enheten:

1. **Användningsstatistik**, Ranked delar bara den här statistiken om du tillåter Apples standardfråga om spårning. Du kan stänga av delning i appen eller återkalla tillståndet i iOS-inställningarna.
2. **Köpuppgifter**, så att abonnemanget i App Store kan verifieras. Apple hanterar betalningen; vi ser aldrig dina betalningsuppgifter.
3. **Feedback- och supportmeddelanden**, bara när du själv skickar dem. Med separat samtycke kan du ange e-post eller telefonnummer för svar.

Ranked spårar dig inte mellan andra appar eller webbplatser. Användningsstatistik och annonskampanjers tillskrivning enligt beskrivningen nedan skickas bara när ATT har godkänts och inställningen ”Share usage data” är på. Appen visar ingen reklam och läser inget från Apple Health.

---

## 2. Det som stannar på din enhet

Följande lagras i appens egen databas på din telefon och överförs aldrig:

- Varje träningspass, set, repetition, statiskt håll och extra vikt som du loggar
- Din träningsplan, ditt schema, påminnelser och inställningar
- De kroppsmått du angett (ålder, kön, längd och kroppsvikt)
- Dina träningsanteckningar

Appen undantar inte databasen från enhetens säkerhetskopia. Om du använder iCloud Backup eller en säkerhetskopia på datorn ingår träningsuppgifterna där och återkommer när du återställer den, enligt Apples villkor, inte våra.

Om du raderar appen raderas allt detta från enheten. Vi kan inte återskapa det eftersom vi aldrig har haft det.

---

## 3. Det som lämnar din enhet

### 3.1 Användningsstatistik (PostHog)

När appen öppnas första gången visar iOS Apples vanliga systemdialog för App Tracking Transparency (ATT). När du godkänner ATT aktiveras analys automatiskt och fortsätter så länge inställningen ”Share usage data” är på i Ranked. Händelser skickas till PostHog i EU endast medan ATT är godkänt och inställningen är på; vid avslag eller avstängning skickas inga nya uppgifter. Ranked skickar händelser till PostHog i EU om introduktion, första bedömning, ändringar av rang och steg (med färdighet och steg), betalningsvy, köp och öppnade vyer. Händelser från träningspass i realtid omfattar start, slutförande eller avbrott, antal sekunder, registrerade set, olika färdigheter och om det var det första slutförda passet. De innehåller inte enskilda övningar, repetitioner, vikter eller anteckningar. Ålder, kön, längd och kroppsvikt skickas inte. PostHog får också vanliga tekniska uppgifter om enhet, iOS, app och språk samt IP-adressen, som kan ge en ungefärlig plats. Ett slumpmässigt installations-id för PostHog skapas när ATT har godkänts. Händelser och kampanjuppgifter kopplas till detta id för analys och mätning av annonser. Du kan återkalla ATT i iOS-inställningarna eller stänga av ”Share usage data” i Ranked under Inställningar ▸ Data och integritet; nya händelser stoppas men redan skickade uppgifter raderas inte automatiskt.

Appen kan även rapportera prenumerationsfasen, aktuell åtkomst, förnyelsestatus och om en uppsägning eller ett faktureringsproblem upptäcktes. Dessa observationer är inte bevis på en debitering och skickas endast medan analys är aktiverad.

Med ditt samtycke registrerar användningshändelser även när du väljer en träningsplan och öppnar ett träningspass. Val av plan omfattar endast antalet träningsdagar per vecka och övningar; öppning av ett pass omfattar endast om det återupptas, ingångskällan och antalet föreskrivna övningar. Planernas fullständiga innehåll, scheman, enskilda övningar och träningsanteckningar stannar på din enhet.

> Valfritt: Dela appanvändning, bedömda färdigheter, rang, träningsaktivitet och kampanjdata från Apple Search Ads med PostHog för att förbättra Ranked. Vi kopplar också denna användning till din provperiod och prenumeration med en slumpmässig köpreferens. Inga namn eller träningsanteckningar. Ändra detta när som helst i Inställningar.

### 3.2 Tillskrivning av Apple Search Ads

Endast medan ATT är godkänt och ”Share usage data” är på frågar Ranked en gång Apples AdServices om koppling av en installation från Apple Search Ads. Efter ett annonsklick kan kampanj, annonsgrupp, sökord, annonsmaterial, land eller region, klickdatum och typ av nedladdning kopplas till det slumpmässiga PostHog-id:t. Annonsidentifieraren IDFA används inte. Framtida överföringar stoppas om du återkallar ATT i iOS-inställningarna eller stänger av ”Share usage data” i Ranked.

### 3.3 Köp (Apple och RevenueCat)

Abonnemang säljs och faktureras av **Apple** via App Store. Vi ser aldrig dina betalningsuppgifter, ditt Apple-konto eller ditt namn.

För att kontrollera om abonnemanget är aktivt använder appen **RevenueCat**. RevenueCat får köpposten från App Store — vilken produkt du köpte, när abonnemanget började och när det löper ut — tillsammans med vanlig teknisk information som iOS-version och appversion. Din installation identifieras med en slumpmässig identifierare som RevenueCat själv skapar och lagrar på enheten. Vi ger inte RevenueCat ditt namn, din e-postadress eller någon annan identitet; eftersom Ranked inte har konton finns det ingen sådan identitet att lämna.

När du trycker på **Återställ köp** begär appen uppgifter från Apple om de köp som gjorts med det Apple-konto som är inloggat på enheten och skickar resultatet till RevenueCat på samma sätt.

### 3.4 Feedback- och supportmeddelanden (Cloudflare och CloudKit)

Om du skickar feedback eller en supportfråga skickar Ranked meddelandet, dess kategori och källa till en Cloudflare Worker. Den lagrar uppgifterna i Apples offentliga CloudKit-databas med en privat servernyckel. Du behöver inte logga in på iCloud för att skicka ett meddelande. Cloudflare Worker använder förfrågans nätverksadress för en teknisk begränsning mot missbruk; varken den ursprungliga adressen eller en hash av den lagras i CloudKit-posten för feedbacken. Du kan separat samtycka till att lämna en e-postadress eller ett telefonnummer för svar utanför appen. Meddelanden och kontaktuppgifter skickas inte till PostHog eller RevenueCat och kopplas inte till ett konto i appen. Vi behandlar meddelandet för att svara på din förfrågan och frivilliga kontaktuppgifter med ditt samtycke. Det finns för närvarande ingen fast tidsfrist för automatisk radering av meddelanden eller kontaktuppgifter. Du kan begära tillgång eller radering på **dylan.schmid538@gmail.com**.

---

## 4. Det som Ranked inte gör

- **Inga konton.** Du loggar aldrig in. Ingen server har en profil om dig.
- **Inget Apple Health.** Ranked varken läser från eller skriver till appen Hälsa.
- **Ingen kamera, inga foton, ingen mikrofon, platsdata eller kontakter.** Appen begär inte dessa behörigheter.
- **Ranked spårar dig inte mellan andra appar eller webbplatser.** Användningsstatistik och kampanjmätning enligt §3 används endast när ATT är godkänt och ”Share usage data” är på; IDFA används inte. Appen visar ingen reklam och uppgifter säljs inte eller lämnas till datamäklare.
- **Ingen pushserver.** Påminnelser schemaläggs lokalt på din telefon; inget om dem lämnar enheten. Du tillfrågas innan den första schemaläggs och kan när som helst stänga av dem i iOS-inställningarna.

---

## 5. Rättslig grund (GDPR och schweiziska revDSG)

| Behandling | Grund |
|---|---|
| Köp och verifiering av abonnemang (§3.3) | Fullgörande av avtal |
| Användningsstatistik (§3.1) | Ditt samtycke; kan återkallas när som helst i Inställningar ▸ Data och integritet |
| Tillskrivning av Search Ads (§3.2) | Ditt samtycke; kan återkallas när som helst i Inställningar ▸ Data och integritet |

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

Du kan när som helst stoppa framtida analysdata genom att återkalla ATT i iOS-inställningarna eller stänga av ”Share usage data” i Ranked: Inställningar ▸ Data och integritet. Uppgifter som redan skickats raderas inte automatiskt och ditt App Store-abonnemang avslutas inte.

Du kan radera lokala träningsuppgifter i Inställningar ▸ Data och integritet ▸ *Radera lokal träningsdata* eller genom att radera appen. Abonnemanget hanteras och avslutas separat i ditt Apple-konto.

För uppgifter som redan skickats till PostHog, skriv till **dylan.schmid538@gmail.com**. Ranked kopplar inte det slumpmässiga analys-id:t till ett konto. Ungefärligt datum eller enhetsmodell kanske inte räcker för att hitta din profil säkert. Vi förklarar vad vi kan identifiera och hanterar verifierbara begäranden om tillgång, rättelse eller radering. Skicka inte inloggningsuppgifter till ditt Apple-konto.

Du kan begära begränsning av behandlingen och klaga hos tillsynsmyndigheten i ditt land; i Schweiz är det den federala dataskydds- och informationskommissionären (FDPIC).

---

## 9. Barn

Ranked är avsedd för personer som är **16 år eller äldre**. Appen frågar om din ålder under introduktionen eftersom rankningsformeln beror på den, och den riktar sig inte till yngre personer. Vi samlar inte medvetet in uppgifter från personer under 16 år.

---

## 10. Ändringar

Den version som publiceras på den här adressen är den aktuella. Datumet överst visar när den senast ändrades. Tidigare versioner finns kvar i den offentliga historiken för det arkiv som publicerar sidorna, så att du kan se vad som ändrades och när.

---
