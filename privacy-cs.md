---
title: Zásady ochrany osobních údajů
permalink: /privacy/cs/
---

> *Toto je překlad. V případě rozdílů je rozhodující [anglická verze](../).*

# Zásady ochrany osobních údajů · Calisthenics Skills – Ranked

**Poslední aktualizace: 2026-10-02**

Tyto zásady popisují, jaké údaje Ranked shromažďuje, kam putují a jaké možnosti v souvislosti s nimi máte. Vycházejí ze skutečného kódu aplikace, nikoli ze šablony; pokud je zde něco nepřesné, je třeba ověřit kód.

Ranked provozuje **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Švýcarsko**, kontakt **dylan.schmid538@gmail.com**. Je správcem osobních údajů popsaných v těchto zásadách.

---

## 1. Stručně

**Váš věk, pohlaví, výška a tělesná hmotnost nikdy neopouštějí zařízení.** Výpočet hodnosti je používá přímo v telefonu. Neodesílají se nám ani analytické službě.

Zařízení opouštějí pouze dva druhy údajů:

1. **Statistiky používání**, abychom věděli, jak se aplikace používá. V aplikaci je můžete kdykoli vypnout.
2. **Údaje o nákupech**, aby bylo možné ověřit předplatné v App Storu. Platbu zpracovává Apple; vaše platební údaje nikdy nevidíme.

Ranked vás nesleduje v jiných aplikacích ani na webových stránkách, nezobrazuje reklamy a nečte nic z aplikace Apple Zdraví.

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

Pro pochopení způsobu používání aplikace využíváme **PostHog** hostovaný v **Evropské unii**. Aplikace mu odesílá pevně stanovený seznam událostí:

- ke kterému kroku nastavení jste došli, který jste dokončili nebo ze kterého jste se vrátili, a jak dlouho každý krok trval;
- výsledek úvodního hodnocení: kolik linií dovedností a úrovní jste uvedli, kterou dovednost jste si zvolili jako cíl, vaši počáteční hodnost a hodnost každé ze šesti oblastí těla;
- kdy se zobrazila nebo zavřela obrazovka nákupu a kdy byl nákup zahájen, dokončen nebo obnoven, včetně příslušného produktu a nabídky; když aplikace později zjistí aktivní zkušební období nebo období placeného předplatného, včetně produktu a údaje o tom, zda jde o nákup v testovacím prostředí (nejde o záznam každé jednotlivé platby a tyto údaje se neodesílají, když je aplikace zavřená);
- kdy se změnila vaše hodnost a která dovednost změnu vyvolala;
- kdy jste splnili úroveň: o kterou dovednost a úroveň šlo a zda to vycházelo ze zaznamenané série, dodatečně zadaného tréninku nebo ručního označení;
- které obrazovky otevíráte a kdy končí trénink. Událost konce tréninku neobsahuje žádné podrobnosti: ani cviky, ani série, ani čísla.

Software PostHog v aplikaci také ke každé události připojuje běžné technické údaje, například model zařízení, verzi iOS a aplikace, jazyk a časové pásmo, a zaznamenává otevření aplikace a její přesun na pozadí. Jako každá internetová služba dostává PostHog IP adresu požadavku a může z ní odvodit přibližnou polohu (zemi nebo město).

**Co údaje neobsahují:** jméno, e-mailovou adresu (aplikace ji nikdy nevyžaduje), identifikátor účtu (žádný účet neexistuje), věk, pohlaví, výšku, tělesnou hmotnost ani obsah tréninků.

**Jak jste rozpoznáni:** PostHog při prvním spuštění aplikace vytvoří náhodný identifikátor a uloží jej v zařízení. Všechny události se sdružují pod tímto identifikátorem. Aplikace PostHogu nikdy nesděluje, kdo jste, a nemá žádný účet ani e-mailovou adresu, které by mohla sdělit.

**Jak statistiky vypnout:** Nastavení ▸ Soukromí ▸ *Sdílet anonymní údaje o používání*. Vypnutí od dané chvíle zastaví odesílání událostí. Nastavení zůstává uložené v zařízení i po aktualizacích aplikace.

### 3.2 Přiřazení Apple Search Ads

Pokud jste Ranked nainstalovali po klepnutí na reklamu Apple Search Ads, aplikace se při prvním spuštění jednou zeptá Applu na zdroj instalace. Apple odpoví údajem o kampani, reklamní skupině, klíčovém slově a podobě reklamy, zemi nebo oblasti a datu kliknutí a o tom, zda šlo o nové nebo opakované stažení. Aplikace tyto údaje připojí k anonymnímu identifikátoru PostHog popsanému v §3.1, aby bylo možné další události sdružit podle reklamy, která vás přivedla.

Používá se framework **AdServices** od Applu, který nevyužívá reklamní identifikátor (IDFA) a který Apple nepovažuje za sledování; proto se nezobrazuje žádost o povolení sledování. Pokud jste nepřišli přes reklamu, Apple to sdělí a nic dalšího se nepřipojí. Vypnutí statistik používání (§3.1) zastaví i toto přiřazování.

### 3.3 Nákupy (Apple a RevenueCat)

Předplatné prodává a účtuje **Apple** prostřednictvím App Storu. Nikdy nevidíme vaše platební údaje, účet Apple ani vaše jméno.

K ověření aktivního předplatného aplikace využívá **RevenueCat**. RevenueCat obdrží záznam o nákupu předplatného z App Storu — zakoupený produkt, datum začátku a konce — spolu s běžnými technickými údaji, jako je verze iOS a aplikace. Vaši instalaci rozpoznává pomocí náhodného identifikátoru, který sám vytvoří a uloží do zařízení. RevenueCatu nepředáváme vaše jméno, e-mailovou adresu ani jinou totožnost a protože Ranked nemá účty, žádná taková totožnost ani neexistuje.

Když klepnete na **Obnovit nákupy**, aplikace požádá Apple o nákupy provedené účtem Apple přihlášeným v zařízení a stejným způsobem předá výsledek RevenueCatu.

---

## 4. Co Ranked nedělá

- **Žádné účty.** Nikdy se nepřihlašujete. Na žádném serveru o vás není profil.
- **Žádné Apple Zdraví.** Ranked nečte data z aplikace Zdraví ani do ní nezapisuje.
- **Žádný fotoaparát, fotky, mikrofon, poloha ani kontakty.** Aplikace o tato oprávnění nežádá.
- **Žádné sledování napříč aplikacemi nebo weby**, reklamní identifikátor ani reklama v aplikaci; žádný prodej údajů ani jejich předávání datovým zprostředkovatelům.
- **Žádný server pro push oznámení.** Připomínky Ranked se plánují místně v telefonu; nic o nich neopouští zařízení. Před naplánováním první vás aplikace požádá o svolení a kdykoli je můžete vypnout v nastavení iOS.

---

## 5. Právní základ (GDPR a švýcarský revDSG)

| Zpracování | Právní základ |
|---|---|
| Nákupy a ověřování předplatného (§3.3) | Plnění smlouvy |
| Statistiky používání (§3.1) | Oprávněný zájem porozumět aplikaci a zlepšovat ji; kdykoli můžete vznést námitku jejich vypnutím, viz §8 |
| Přiřazení Search Ads (§3.2) | Oprávněný zájem zjistit účinnost reklamy; námitka jako výše |

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

Kdykoli můžete:

- **Vypnout statistiky používání** v Nastavení ▸ Soukromí. Jde o právo vznést námitku a tam, kde se zpracování opírá o souhlas, jej odvolat. Účinek je okamžitý a nemusíte uvádět důvod.
- **Smazat své údaje.** Protože Ranked o vás nic neuchovává na serveru, odstranění aplikace smaže vše, co sama ukládá.
- **Požádat o smazání svého anonymního analytického profilu.** Podle jména jej najít nemůžeme, protože žádné neobsahuje. Pokud nám napíšete přibližné datum prvního použití aplikace a používané zařízení, ručně jej vyhledáme a smažeme.
- **Požádat o kopii** údajů, které služba uchovává pod vaším identifikátorem, požádat o jejich **opravu** nebo o **omezení** zpracování během posuzování žádosti.
- **Podat stížnost u dozorového úřadu** ve své zemi; ve Švýcarsku jde o federálního komisaře pro ochranu údajů a informace (FDPIC).

S žádostmi o uplatnění těchto práv pište na **dylan.schmid538@gmail.com**.

---

## 9. Děti

Ranked je určena osobám ve věku **16 let a více**. Aplikace se během nastavení ptá na věk, protože na něm závisí výpočet hodnosti, a není určena mladším osobám. Vědomě neshromažďujeme údaje o osobách mladších 16 let.

---

## 10. Změny

Verze zveřejněná na této adrese je aktuální a datum nahoře ukazuje, kdy se naposledy změnila. Starší verze zůstávají dostupné ve veřejné historii repozitáře, z něhož se tyto stránky zveřejňují, abyste mohli zjistit, co a kdy se změnilo.

---

> **⚠️ Nejde o právní poradenství.** Tento dokument sepsal na základě zdrojového kódu aplikace inženýr, nikoli právník. Popisuje systém ke dni uvedenému výše; každé tvrzení bylo porovnáno s tím, co aplikace skutečně odesílá. Dokument **neprošel** právním posouzením souladu s GDPR, švýcarským revDSG, CCPA ani jinými předpisy. Jeho zveřejnění splňuje požadavky Applu, samo o sobě však neznamená právní soulad. Jakmile aplikace začne vydělávat, nechte jej zkontrolovat právníkem.
