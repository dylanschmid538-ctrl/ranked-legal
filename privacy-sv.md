---
title: Integritetspolicy · Calisthenics Skills – Ranked
permalink: /privacy/sv/
---

> Detta är en översättning. Vid avvikelser gäller [den engelska versionen](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/).

# Integritetspolicy · Calisthenics Skills – Ranked

**Senast uppdaterad: 2026-10-08**

Den här policyn beskriver vilka uppgifter Ranked samlar in, vart de skickas och vad du kan göra åt det.

Ranked drivs av **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Schweiz**, kontakt **dylan.schmid538@gmail.com**. Hon är personuppgiftsansvarig för den behandling som beskrivs här.

---

## 1. Kortfattat

**Din ålder, ditt kön, din längd och din kroppsvikt lämnar aldrig enheten.** Rankningsformeln använder dem på telefonen. De skickas varken till oss eller till analystjänsten.

Endast två slags uppgifter lämnar enheten:

1. **Användningsstatistik**, så att vi kan se hur appen används. Du kan stänga av den i appen när som helst.
2. **Köpuppgifter**, så att abonnemanget i App Store kan verifieras. Apple hanterar betalningen; vi ser aldrig dina betalningsuppgifter.

Ranked spårar dig inte mellan andra appar eller webbplatser, visar ingen reklam och läser inget från Apple Health.

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

Analys är avstängd som standard. Först när du uttryckligen samtycker under introduktionen eller senare i Inställningar skickar Ranked händelser till PostHog i EU om introduktion, första bedömning, ändringar av rang och steg (med färdighet och steg), betalningsvy, köp och öppnade vyer. Händelser från träningspass i realtid omfattar start, slutförande eller avbrott, antal sekunder, registrerade set, olika färdigheter och om det var det första slutförda passet. De innehåller inte enskilda övningar, repetitioner, vikter eller anteckningar. Ålder, kön, längd och kroppsvikt skickas inte. PostHog får också vanliga tekniska uppgifter om enhet, iOS, app och språk samt IP-adressen, som kan ge en ungefärlig plats. Ett slumpmässigt analys-id skapas först efter ditt samtycke. Du kan återkalla det i Inställningar ▸ Integritet; nya händelser stoppas men redan skickade uppgifter raderas inte automatiskt.

### 3.2 Tillskrivning av Apple Search Ads

Först efter samtycke till analys frågar Ranked en gång Apples AdServices om koppling av en installation från Apple Search Ads. Efter ett annonsklick kan kampanj, annonsgrupp, sökord, annonsmaterial, land eller region, klickdatum och typ av nedladdning kopplas till det slumpmässiga PostHog-id:t. Annonsidentifieraren IDFA används inte. Återkallelse stoppar framtida överföringar.

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
| Användningsstatistik (§3.1) | Ditt samtycke; kan återkallas när som helst i Inställningar ▸ Integritet |
| Tillskrivning av Search Ads (§3.2) | Ditt samtycke; kan återkallas när som helst i Inställningar ▸ Integritet |

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

Du kan när som helst återkalla ditt samtycke till analys i Inställningar ▸ Integritet utan att ange skäl. Nya händelser stoppas direkt, men redan skickade uppgifter raderas inte automatiskt och ditt App Store-abonnemang avslutas inte.

Du kan radera lokala träningsuppgifter i Inställningar ▸ Data ▸ *Radera lokala träningsuppgifter* eller genom att radera appen. Abonnemanget hanteras och avslutas separat i ditt Apple-konto.

För uppgifter som redan skickats till PostHog, skriv till **dylan.schmid538@gmail.com**. Ranked kopplar inte det slumpmässiga analys-id:t till ett konto. Ungefärligt datum eller enhetsmodell kanske inte räcker för att hitta din profil säkert. Vi förklarar vad vi kan identifiera och hanterar verifierbara begäranden om tillgång, rättelse eller radering. Skicka inte inloggningsuppgifter till ditt Apple-konto.

Du kan begära begränsning av behandlingen och klaga hos tillsynsmyndigheten i ditt land; i Schweiz är det den federala dataskydds- och informationskommissionären (FDPIC).

---

## 9. Barn

Ranked är avsedd för personer som är **16 år eller äldre**. Appen frågar om din ålder under introduktionen eftersom rankningsformeln beror på den, och den riktar sig inte till yngre personer. Vi samlar inte medvetet in uppgifter från personer under 16 år.

---

## 10. Ändringar

Den version som publiceras på den här adressen är den aktuella. Datumet överst visar när den senast ändrades. Tidigare versioner finns kvar i den offentliga historiken för det arkiv som publicerar sidorna, så att du kan se vad som ändrades och när.

---
