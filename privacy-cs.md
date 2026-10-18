---
title: Zásady ochrany osobních údajů
permalink: /privacy/cs/
---

> *Toto je překlad. V případě rozdílů je rozhodující [anglická verze](../).*

# Zásady ochrany osobních údajů · Calisthenics Skills – Ranked

**Poslední aktualizace: 2026-10-18**

Tyto zásady popisují, jaké údaje Ranked shromažďuje, kam putují a jaké možnosti v souvislosti s nimi máte.

Ranked provozuje **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Švýcarsko**, kontakt **dylan.schmid538@gmail.com**. Je správcem osobních údajů popsaných v těchto zásadách.

---

## 1. Stručně

**Váš věk, pohlaví, výška a tělesná hmotnost nikdy neopouštějí zařízení.** Výpočet hodnosti je používá přímo v telefonu. Neodesílají se nám ani analytické službě.

Zařízení mohou opustit tři druhy údajů:

1. **Statistiky používání**, abychom věděli, jak se aplikace používá. V aplikaci je můžete kdykoli vypnout.
2. **Údaje o nákupech**, aby bylo možné ověřit předplatné v App Storu. Platbu zpracovává Apple; vaše platební údaje nikdy nevidíme.
3. **Zprávy se zpětnou vazbou a žádosti o podporu**, pouze pokud je sami odešlete. Se samostatným souhlasem můžete uvést e-mail či telefon pro odpověď.

Ranked nepoužívá reklamní identifikátor IDFA, nezobrazuje reklamy v aplikaci a neprodává údaje ani je neposkytuje datovým zprostředkovatelům. Statistiky používání a přiřazení Apple Search Ads odesílá pouze po povolení sledování v dialogu ATT; přenos pokračuje, dokud máte v aplikaci zapnutou analytiku. Ranked také nečte data z aplikace Apple Zdraví.

---

## 2. Co zůstává v zařízení

Následující údaje jsou uloženy ve vlastní databázi aplikace v telefonu a nikdy se nepřenášejí:

- Každý zaznamenaný trénink, sérii, opakování, výdrž a přidanou zátěž
- Tréninkový plán, rozvrh, připomínky a nastavení
- Vámi zadané tělesné údaje (věk, pohlaví, výška, tělesná hmotnost)
- Tréninkové poznámky

Aplikace tuto databázi nevylučuje ze zálohování zařízení. Pokud používáte zálohu na iCloudu nebo v počítači, tréninkové údaje jsou její součástí a po obnovení zálohy se vrátí — za podmínek Applu, nikoli našich.

Odstranění aplikace tyto údaje ze zařízení smaže. Nemůžeme je obnovit, protože jsme je nikdy neměli.

---

## 3. Co opouští zařízení

### 3.1 Statistiky používání (PostHog)

Při prvním spuštění aplikace zobrazí iOS standardní dialog Apple pro povolení sledování (App Tracking Transparency, ATT). Ranked odesílá údaje o používání službě PostHog v EU pouze po povolení sledování v dialogu ATT; poté přenos pokračuje, dokud máte v aplikaci zapnutou analytiku. Události zahrnují úvodní nastavení, počáteční hodnocení, změny hodnosti a úrovní (včetně dovednosti a úrovně), nákupní obrazovku, nákupy a otevřené obrazovky. Události živého tréninku zahrnují začátek, dokončení nebo opuštění, uplynulé sekundy, počet zaznamenaných sérií, počet různých dovedností a údaj, zda šlo o první dokončený trénink. Neobsahují jednotlivá cvičení, opakování, zátěž ani poznámky. Věk, pohlaví, výška a hmotnost se neodesílají. PostHog také získává běžné technické údaje o zařízení, iOS, aplikaci a jazyce a IP adresu, z níž lze odvodit přibližnou polohu. Po povolení sledování a zapnutí analytiky vytvoří PostHog náhodný identifikátor instalace a spojí s ním události i údaje o reklamní kampani pro analytiku a měření reklamy. Reklamní identifikátor IDFA se nepoužívá. Analytiku můžete vypnout v Nastavení ▸ Data a soukromí nebo odvolat oprávnění ke sledování v nastavení iOS. Vypnutím kterékoli možnosti se zastaví budoucí přenosy; dříve odeslané údaje se automaticky nesmažou.

### 3.2 Přiřazení Apple Search Ads

Ranked žádá o přiřazení Apple Search Ads a dotazuje se služby AdServices pouze tehdy, když povolíte sledování v dialogu ATT a máte zapnutou analytiku v aplikaci. Údaje o kampani, reklamní skupině, klíčovém slovu, kreativní sadě, zemi či oblasti, datu klepnutí a typu stažení se pak mohou spojit s náhodným identifikátorem instalace PostHog pro analytiku a měření reklamy. IDFA se nepoužívá. Vypnutím analytiky nebo odvoláním oprávnění ATT se zastaví další přiřazování a přenosy; dříve odeslané údaje se automaticky nesmažou.

### 3.3 Nákupy (Apple a RevenueCat)

Předplatné prodává a účtuje **Apple** prostřednictvím App Storu. Nikdy nevidíme vaše platební údaje, účet Apple ani vaše jméno.

K ověření aktivního předplatného aplikace využívá **RevenueCat**. RevenueCat obdrží záznam o nákupu předplatného z App Storu — zakoupený produkt, datum začátku a konce — spolu s běžnými technickými údaji, jako je verze iOS a aplikace. Vaši instalaci rozpoznává pomocí náhodného identifikátoru, který sám vytvoří a uloží do zařízení. RevenueCatu nepředáváme vaše jméno, e-mailovou adresu ani jinou totožnost a protože Ranked nemá účty, žádná taková totožnost ani neexistuje.

Když klepnete na **Obnovit nákupy**, aplikace požádá Apple o nákupy provedené účtem Apple přihlášeným v zařízení a stejným způsobem předá výsledek RevenueCatu.

### 3.4 Zprávy se zpětnou vazbou a žádosti o podporu (Cloudflare a CloudKit)

Pokud odešlete zpětnou vazbu nebo žádost o podporu, Ranked předá zprávu, její kategorii a zdroj službě Cloudflare Worker. Ta je pomocí soukromého serverového klíče uloží do veřejné databáze Apple CloudKit. K odeslání zprávy se nemusíte přihlašovat k iCloudu. Cloudflare Worker používá síťovou adresu k technickému omezení zneužívání; původní adresu ani její otisk neukládá do záznamu zpětné vazby v CloudKitu. Samostatně můžete souhlasit s poskytnutím e-mailové adresy nebo telefonního čísla pro odpověď mimo aplikaci. Zprávy ani kontaktní údaje neposíláme společnostem PostHog či RevenueCat a nespojujeme je s účtem v aplikaci. Zprávu zpracováváme kvůli odpovědi na váš požadavek; nepovinné kontaktní údaje na základě vašeho souhlasu. Pro automatické odstranění zpráv a kontaktních údajů nyní není stanovena pevná lhůta. O přístup k údajům nebo jejich odstranění můžete požádat na **dylan.schmid538@gmail.com**.

---

## 4. Sledování a oprávnění v Ranked

- **Žádné účty.** Nikdy se nepřihlašujete. Na žádném serveru o vás není profil.
- **Žádné Apple Zdraví.** Ranked nečte data z aplikace Zdraví ani do ní nezapisuje.
- **Žádný fotoaparát, fotky, mikrofon, poloha ani kontakty.** Aplikace o tato oprávnění nežádá.
- **Ranked nepoužívá reklamní identifikátor IDFA, nezobrazuje reklamy v aplikaci a neprodává údaje ani je neposkytuje datovým zprostředkovatelům. Statistiky používání a přiřazení Apple Search Ads se odesílají pouze po povolení sledování v dialogu ATT; přenos pokračuje, dokud máte v aplikaci zapnutou analytiku.**
- **Žádný server pro push oznámení.** Připomínky Ranked se plánují místně v telefonu; nic o nich neopouští zařízení. Před naplánováním první vás aplikace požádá o svolení a kdykoli je můžete vypnout v nastavení iOS.

---

## 5. Právní základ (GDPR a švýcarský revDSG)

| Zpracování | Právní základ |
|---|---|
| Nákupy a ověřování předplatného (§3.3) | Plnění smlouvy |
| Statistiky používání (§3.1) | Váš souhlas prostřednictvím oprávnění ATT a analytického nastavení v Ranked; kteroukoli možnost můžete kdykoli vypnout, viz §8 |
| Přiřazení Search Ads (§3.2) | Váš souhlas prostřednictvím oprávnění ATT a analytického nastavení v Ranked; kteroukoli možnost můžete kdykoli vypnout, viz §8 |

**Uplatňují se zde dva právní předpisy, nikoli jen jeden.** Ranked se provozuje ze Švýcarska, takže se toto zpracování řídí revidovaným švýcarským federálním zákonem o ochraně osobních údajů (**revDSG**, účinným od září 2023). **GDPR** se navíc uplatní při používání aplikace z Evropské unie nebo Spojeného království. Pokud se pravidla liší, řídíme se přísnějším z nich. Obyvatelé Švýcarska mají podle článku 25 a následujících revDSG stejná základní práva uvedená v §8.

---

## 6. Kde se údaje zpracovávají

- **PostHog** zpracovává statistiky používání v Evropské unii.
- **RevenueCat, Inc.** sídlí ve Spojených státech a tam zpracovává údaje o nákupech popsané v §3.3.
- **Apple** zpracovává samotný nákup a žádost o přiřazení Search Ads podle vlastní zásady ochrany soukromí, která se vztahuje na váš účet Apple nezávisle na této aplikaci.

---

## 7. Jak dlouho údaje uchováváme

Statistiky používání se uchovávají po dobu platnou pro náš tarif PostHogu. Neslibujeme pevný počet měsíců, protože PostHog nám jej neumožňuje nastavit — uvést v zásadách lhůtu, kterou nelze dodržet, by bylo horší než žádnou neuvést.

Záznamy o nákupech uchovává RevenueCat po dobu existence předplatného a jeho historie, což je nezbytné k ověřování předplatného.

Údaje v zařízení v něm zůstávají, dokud aplikaci neodstraníte.

---

## 8. Vaše práva

Souhlas s analytikou můžete kdykoli bez udání důvodu odvolat v Nastavení ▸ Data a soukromí. Nové události se ihned přestanou odesílat, ale dříve odeslané údaje se automaticky nesmažou a předplatné App Store se nezruší.

Místní tréninkové údaje můžete smazat v Nastavení ▸ Data a soukromí ▸ *Smazat místní tréninková data* nebo odstraněním aplikace. Předplatné spravujete a rušíte samostatně ve svém účtu Apple.

Ohledně údajů již odeslaných službě PostHog napište na **dylan.schmid538@gmail.com**. Ranked nespojuje náhodný analytický identifikátor s účtem. Přibližné datum nebo model zařízení nemusí stačit ke spolehlivému nalezení profilu. Vysvětlíme, co lze identifikovat, a vyřídíme ověřitelné žádosti o přístup, opravu či výmaz. Neposílejte přihlašovací údaje k účtu Apple.

Můžete požádat o omezení zpracování a podat stížnost dozorovému úřadu ve své zemi; ve Švýcarsku je jím federální komisař pro ochranu údajů a informace (FDPIC).

---

## 9. Děti

Ranked je určena osobám ve věku **16 let a více**. Aplikace se během nastavení ptá na věk, protože na něm závisí výpočet hodnosti, a není určena mladším osobám. Vědomě neshromažďujeme údaje o osobách mladších 16 let.

---

## 10. Změny

Verze zveřejněná na této adrese je aktuální a datum nahoře ukazuje, kdy se naposledy změnila. Starší verze zůstávají dostupné ve veřejné historii repozitáře, z něhož se tyto stránky zveřejňují, abyste mohli zjistit, co a kdy se změnilo.

---
