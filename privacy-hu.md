---
title: Adatvédelmi tájékoztató
permalink: /privacy/hu/
---

> *Ez fordítás. Eltérés esetén az [angol változat](../) az irányadó.*

# Adatvédelmi tájékoztató · Calisthenics Skills – Ranked

**Utolsó frissítés: 2026. szeptember 29.**

Ez a tájékoztató ismerteti, milyen adatokat gyűjt a Ranked, hová kerülnek, és milyen lehetőségei vannak velük kapcsolatban. A tényleges alkalmazáskód alapján készült, nem sablonból; ha valamely állítás pontatlan, a kódot kell ellenőrizni.

A Ranked üzemeltetője és az itt leírt adatkezelés adatkezelője **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Svájc**. Kapcsolat: **dylan.schmid538@gmail.com**.

---

## 1. Röviden

A Rankednek **nincsenek felhasználói fiókjai és saját szervere.** Az edzéseivel kapcsolatos minden adat — minden rögzített sorozat, az egyes készségekben elért fejlődés, a rangja, a Power Level és a testtérkép — a telefonján tárolódik, és soha nem kerül feltöltésre.

**Életkora, neme, magassága és testsúlya soha nem hagyja el az eszközét.** A rangot számító képlet a telefonon használja ezeket. Sem nekünk, sem az elemzőszolgáltatásnak nem küldi el őket.

Csak kétféle adat hagyja el az eszközét:

1. **Névtelen használati statisztikák**, amelyek alapján láthatjuk, hogyan használják az alkalmazást. Ezt az alkalmazásban bármikor kikapcsolhatja.
2. **Vásárlási adatok**, hogy ellenőrizni lehessen az App Store-előfizetést. A fizetést az Apple kezeli; fizetési adatait mi soha nem látjuk.

A Ranked nem követi Önt más alkalmazásokban vagy webhelyeken, nem jelenít meg hirdetéseket, és nem olvas adatot az Apple Egészség alkalmazásból.

---

## 2. Mi marad az eszközén

Az alábbi adatok a telefonon, az alkalmazás saját adatbázisában tárolódnak, és soha nem kerülnek továbbításra:

- Minden rögzített edzés, sorozat, ismétlés, kitartás és hozzáadott súly
- Az egyes készségekben és szinteken elért fejlődés, a rang előzményei és a Power Level
- Edzésterv, ütemezés, emlékeztetők és beállítások
- A megadott testadatok (életkor, nem, magasság, testsúly)
- Edzésjegyzetek

Az alkalmazás nem zárja ki ezt az adatbázist az eszköz biztonsági mentéséből. Ha iCloud biztonsági mentést vagy számítógépes mentést használ, edzésadatai annak részét képezik, és a visszaállítással visszakerülnek — az Apple feltételei szerint, nem a mieink alapján.

Az alkalmazás törlése ezeket az adatokat is törli az eszközről. Nem tudjuk visszaállítani őket, mert soha nem rendelkeztünk velük.

---

## 3. Mi hagyja el az eszközét

### 3.1 Használati statisztikák (PostHog)

Az alkalmazás használatának megértéséhez az **Európai Unióban** üzemeltetett **PostHog** szolgáltatást használjuk. Az alkalmazás a következő rögzített eseménylistát küldi el neki:

- melyik beállítási lépéshez jutott el, melyiket fejezte be, illetve melyikről lépett vissza, és mennyi ideig tartott mindegyik;
- a kezdeti felmérés eredménye: hány készségvonalat és szintet jelölt meg, melyik készséget választotta célul, a kezdő rangja és a hat testrégiója rangja;
- mikor jelent meg vagy zárult be a vásárlási képernyő, és mikor indult, fejeződött be vagy állt helyre egy vásárlás, az érintett termékkel és ajánlattal; amikor az alkalmazás később aktív próbaidőszakot vagy fizetős előfizetési időszakot észlel, a termékkel és annak jelzésével, hogy tesztkörnyezetbeli vásárlásról van-e szó (ez nem minden terhelés nyilvántartása, és az alkalmazás bezárt állapotában nem kerül elküldésre);
- mikor változott a rangja, és melyik készség váltotta ezt ki;
- mikor teljesített egy szintet: melyik készséget és szintet, valamint hogy ez rögzített sorozatból, utólag felvitt edzésből vagy kézi megjelölésből származott-e;
- mely képernyőket nyitja meg, és mikor ér véget egy edzés. Az edzés végét jelző esemény nem tartalmaz részleteket: sem gyakorlatokat, sem sorozatokat, sem számokat.

Az alkalmazásba épített PostHog szoftver minden eseményhez szokásos műszaki adatokat is csatol, például az eszköz modelljét, az iOS és az alkalmazás verzióját, a nyelvet és az időzónát. Rögzíti az alkalmazás megnyitását és háttérbe helyezését is. Mint minden internetes szolgáltatás, a PostHog megkapja a kérés IP-címét, amelyből hozzávetőleges helyet (országot vagy várost) állapíthat meg.

**Amit nem tartalmaz:** nevet, e-mail-címet (az alkalmazás nem kér ilyet), fiókazonosítót (nincs fiók), életkort, nemet, magasságot, testsúlyt vagy az edzések tartalmát.

**Azonosítás módja:** A PostHog az alkalmazás első indításakor véletlenszerű azonosítót hoz létre, és az eszközön tárolja. Az események ezen azonosító alatt csoportosulnak. Az alkalmazás soha nem közli a PostHoggal, hogy Ön kicsoda; nincs fiók vagy e-mail-cím, amelyet közölhetne.

**Kikapcsolás:** Beállítások ▸ Adatvédelem ▸ *Névtelen használati adatok megosztása*. A kikapcsolás attól a pillanattól megakadályozza az események küldését. A beállítás az eszközön tárolódik, és az alkalmazás frissítése után is megmarad.

### 3.2 Apple Search Ads-hozzárendelés

Ha a Ranked alkalmazást egy Apple Search Ads-hirdetésre koppintva telepítette, az alkalmazás az első indításkor egyszer megkérdezi az Apple-től a telepítés forrását. Az Apple megadja a hirdetés kampányát, hirdetéscsoportját, kulcsszavát és kreatív anyagát, a kattintás országát vagy régióját és dátumát, valamint azt, hogy új vagy ismételt letöltés történt-e. Az alkalmazás ezeket az értékeket a §3.1-ben leírt névtelen PostHog-azonosítóhoz kapcsolja, hogy a későbbi események a megfelelő hirdetéshez rendelhetők legyenek.

Ehhez az Apple **AdServices** keretrendszerét használja, amely nem alkalmaz hirdetési azonosítót (IDFA), és amelyet az Apple nem tekint követésnek, ezért nem jelenik meg követési engedélykérés. Ha nem hirdetésen keresztül érkezett, az Apple ezt jelzi, és semmi nem kapcsolódik az azonosítóhoz. A használati statisztikák kikapcsolása (§3.1) ezt is leállítja.

### 3.3 Vásárlások (Apple és RevenueCat)

Az előfizetéseket az **Apple** értékesíti és számlázza az App Store-on keresztül. Fizetési adatait, Apple-fiókját és nevét soha nem látjuk.

Az aktív előfizetés ellenőrzésére az alkalmazás a **RevenueCat** szolgáltatást használja. A RevenueCat megkapja az előfizetés App Store-beli vásárlási rekordját — a megvásárolt terméket, a kezdés és a lejárat időpontját —, valamint szokásos műszaki adatokat, például az iOS és az alkalmazás verzióját. A telepítést saját maga által létrehozott, az eszközön tárolt véletlenszerű azonosítóval ismeri fel. Nem adjuk át a RevenueCatnek az Ön nevét, e-mail-címét vagy más személyazonossági adatát, és mivel a Rankednek nincsenek fiókjai, nincs is ilyen adat, amelyet átadhatnánk.

Ha a **Vásárlások visszaállítása** lehetőségre koppint, az alkalmazás lekéri az Apple-től az eszközön bejelentkezett Apple-fiókkal végzett vásárlásokat, és az eredményt ugyanígy továbbítja a RevenueCatnek.

---

## 4. Amit a Ranked nem tesz

- **Nincsenek fiókok.** Nem kell bejelentkeznie. Semmilyen szerveren nincs Önről profil.
- **Nincs Apple Egészség-hozzáférés.** A Ranked nem olvas és nem ír adatot az Egészség alkalmazásban.
- **Nincs kamera-, fénykép-, mikrofon-, helyadat- vagy névjegyhozzáférés.** Az alkalmazás nem kér ilyen engedélyeket.
- **Nincs alkalmazások vagy webhelyek közötti követés**, hirdetési azonosító, alkalmazáson belüli reklám, valamint adatértékesítés vagy adatközvetítőknek történő adattovábbítás.
- **Nincs pushértesítési szerver.** A Ranked emlékeztetőit a telefon helyben ütemezi; semmilyen kapcsolódó adat nem hagyja el az eszközt. Az első ütemezése előtt engedélyt kérünk, és az iOS beállításaiban bármikor kikapcsolhatja őket.

---

## 5. Jogalap (GDPR és svájci revDSG)

| Adatkezelés | Jogalap |
|---|---|
| Vásárlások és előfizetés-ellenőrzés (§3.3) | Szerződés teljesítése |
| Használati statisztikák (§3.1) | Az alkalmazás megértéséhez és fejlesztéséhez fűződő jogos érdek; a kikapcsolással bármikor tiltakozhat, lásd §8 |
| Search Ads-hozzárendelés (§3.2) | Annak megismeréséhez fűződő jogos érdek, hogy mely hirdetés működik; tiltakozás a fentiek szerint |

**Itt két jogszabályrendszer alkalmazandó, nem csak egy.** A Rankedet Svájcból üzemeltetik, ezért az adatkezelést a felülvizsgált svájci szövetségi adatvédelmi törvény (**revDSG**, 2023 szeptembere óta hatályos) szabályozza. A **GDPR** emellett akkor is alkalmazandó, ha az alkalmazást az Európai Unióból vagy az Egyesült Királyságból használják. Eltérés esetén a szigorúbb szabályt követjük. A svájci lakosokat a revDSG 25. és következő cikke alapján ugyanazok a §8-ban felsorolt alapvető jogok illetik meg.

---

## 6. Hol történik az adatkezelés

- A **PostHog** az Európai Unióban kezeli a használati statisztikákat.
- A **RevenueCat, Inc.** székhelye az Egyesült Államokban van, és ott kezeli a §3.3-ban leírt vásárlási adatokat.
- Az **Apple** magát a vásárlást és a Search Ads-hozzárendelési kérelmet saját adatvédelmi szabályzata szerint kezeli, amely az Ön Apple-fiókjára ettől az alkalmazástól függetlenül vonatkozik.

---

## 7. Az adatok megőrzési ideje

A használati statisztikákat a PostHog-csomagunkra érvényes megőrzési időig tárolják. Nem ígérünk meghatározott számú hónapot, mert a PostHog nem engedi ezt beállítani; egy betarthatatlan szám feltüntetése rosszabb volna annál, mint ha nem szerepelne ilyen szám.

A RevenueCat addig őrzi meg a vásárlási rekordokat, amíg az előfizetés és annak előzményei léteznek, mert ez szükséges az előfizetés ellenőrzéséhez.

Az eszközén tárolt adatok az alkalmazás törléséig maradnak ott.

---

## 8. Az Ön jogai

Bármikor jogosult:

- **Kikapcsolni a használati statisztikákat** a Beállítások ▸ Adatvédelem menüben. Ez tiltakozási joga, és ahol az adatkezelés hozzájáruláson alapul, a hozzájárulás visszavonása; azonnal hatályos, indokolás nélkül.
- **Törölni adatait.** Mivel a Ranked nem tárol Önről adatot szerveren, az alkalmazás törlése minden általa tárolt adatot eltávolít.
- **Kérni névtelen elemzési profilja törlését.** Név alapján nem tudjuk megtalálni, mert nincs neve, de ha megírja az első használat hozzávetőleges dátumát és a használt eszközt, kézzel megkeressük és töröljük.
- **Másolatot kérni** a szolgáltató által az azonosítója alatt tárolt adatokról, kérni azok **helyesbítését**, vagy kérni az adatkezelés **korlátozását** a kérelem vizsgálata alatt.
- **Panaszt tenni az országa felügyeleti hatóságánál**; Svájcban ez a szövetségi adatvédelmi és információs biztos (FDPIC).

E jogokkal kapcsolatban írjon a **dylan.schmid538@gmail.com** címre.

---

## 9. Gyermekek

A Ranked **16 éves vagy idősebb** személyeknek szól. A beállítás során az alkalmazás azért kérdezi meg az életkorát, mert a rangképlet attól függ, és az alkalmazás nem fiatalabbaknak készült. Tudatosan nem gyűjtünk adatot 16 év alatti személyektől.

---

## 10. Módosítások

Az ezen a címen közzétett változat az aktuális; a fenti dátum mutatja az utolsó módosítást. A korábbi változatok megtekinthetők az oldalak közzétételére használt adattár nyilvános előzményeiben, így láthatja, mi és mikor változott.

---

> **⚠️ Ez nem jogi tanácsadás.** Ezt a dokumentumot mérnök készítette az alkalmazás forráskódja alapján, nem ügyvéd. A fenti dátum szerinti rendszert írja le; minden állítását ellenőriztük az alkalmazás által ténylegesen küldött adatokhoz képest. A dokumentumot **nem vizsgálták felül** a GDPR, a svájci revDSG, a CCPA vagy más szabályozás szerinti megfelelés szempontjából. A közzététel teljesíti az Apple követelményeit, de önmagában nem tesz jogszabályoknak megfelelővé. Amikor az alkalmazás bevételt termel, vizsgáltassa felül ügyvéddel.
