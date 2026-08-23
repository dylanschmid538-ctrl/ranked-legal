---
title: Privatumo politika
permalink: /privacy/lt/
---

*Tai yra vertimas. Esant neatitikimų, pirmenybė teikiama angliškajai versijai, pateikiamai adresu https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/.*

# Privatumo politika · Calisthenics Skills – Ranked

**Paskutinį kartą atnaujinta: 2026 m. rugpjūčio 23 d.**

Šioje politikoje aprašoma, kokius duomenis renka „Ranked“, kur jie patenka ir ką Jūs galite dėl to
padaryti. Ji parengta pagal faktinį programėlės kodą ir duomenų bazės struktūrą, o ne pagal šabloną
— jeigu kas nors čia neteisinga, tikrinti reikia kodą.

„Ranked“ valdo **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Šveicarija**, kontaktai **dylan.schmid538@gmail.com**.

---

## 1. Trumpoji versija

Beveik viskas, ką „Ranked“ žino apie Jūsų treniruotes, lieka Jūsų telefone. Jūsų treniruočių
istorija, Jūsų pažanga kiekviename įgūdyje, Jūsų reitingas ir Jūsų kūno žemėlapis saugomi vietoje ir
niekada nėra įkeliami.

Iš Jūsų įrenginio išsiunčiami keturi dalykai: Jūsų prisijungimo tapatybė, nedidelis profilis,
naudojamas lyderių lentelėms, įrašai apie tai, kad atlikote patvirtintą bandymą, ir anoniminė
naudojimo analitika. Kiekvienas iš jų paaiškinamas toliau.

**Jūsų patvirtintų bandymų (Verified Attempt) vaizdo įrašai niekada nepalieka Jūsų įrenginio.**
Siunčiamas tik failo skaitmeninis atspaudas.

---

## 2. Kas lieka Jūsų įrenginyje

Vietoje, pačios programėlės duomenų bazėje, saugoma ir niekada neperduodama:

- Kiekviena Jūsų užregistruota treniruotė, serija, pakartojimas, išlaikymas ir papildomas svoris
- Jūsų pažanga kiekviename įgūdyje ir pakopoje bei Jūsų reitingo istorija
- Jūsų treniruočių planas, tvarkaraštis ir nuostatos
- Jūsų kūno matmenys tokie, kokius juos įvedėte (amžius, lytis, ūgis, kūno svoris) — dalies šių
  duomenų kopija taip pat siunčiama lyderių lentelės paslaugai, žr. 3.2 skirsnį
- **Patvirtintų bandymų vaizdo įrašų failai.** Jie įrašomi į privačią programėlės saugyklą. Jie nėra
  įkeliami, nėra atsarginėmis kopijomis kopijuojami į mūsų serverius ir mums neprieinami.

Ištrynus programėlę, visa tai ištrinama. Mes to atkurti negalime.

---

## 3. Kas palieka Jūsų įrenginį

### 3.1 Jūsų paskyra
Kai prisijungiate su Apple arba Google, mes gauname ir saugome naudotojo identifikatorių ir,
priklausomai nuo to, ką leidžiate prisijungdami, el. pašto adresą. Tai tvarko **Supabase**, kuri
priglobia mūsų duomenų bazę ir autentifikavimą.

Kai prisijungiate su Apple, mes taip pat išsaugome atnaujinimo prieigos raktą (refresh token), kurį
tuo metu mums perduoda Apple. Jis turi tik vieną paskirtį: ištrynus Jūsų paskyrą, taip pat
panaikinama „Ranked“ prieiga prie Jūsų Apple ID, kaip to reikalauja Apple. Paskyroms, kurių
paskutinis prisijungimas įvyko dar prieš atsirandant šiam fiksavimui, joks prieigos raktas nėra
saugomas — tuomet ištrinant panaikinimo veiksmas tiesiog praleidžiamas.

### 3.2 Jūsų lyderių lentelės profilis
Kad galėtume Jus įtraukti į lyderių lentelę ir palyginti su panašaus kūno sudėjimo žmonėmis, mūsų
serveryje saugoma:

- atsitiktinai sugeneruotas **draugo kodas**
- Jūsų **amžius**, **lytis** ir **kūno svoris**
- Jūsų profilio sukūrimo data

**Pastaba dėl matomumo:** bet kuris prisijungęs „Ranked“ naudotojas gali rasti profilį pagal jo
draugo kodą. Tokia ir yra draugo kodo paskirtis — jis skirtas kam nors perduoti. Nesidalykite savuoju
su tais, kuriems nenorėtumėte parodyti savo įrašo. Kiti naudotojai mato Jūsų draugo kodą ir Jūsų
vietą lyderių lentelėje — daugiau nieko. Jūsų amžius, lytis ir kūno svoris naudojami palyginimui
serveryje ir niekada nėra rodomi kitiems naudotojams ar jų atsisiunčiami.

Jūsų **ūgis** nesiunčiamas. Jūsų treniruočių istorija nesiunčiama.

### 3.3 Patvirtinti bandymai
Kai įrašote patvirtintą bandymą, mes išsaugome: Jūsų naudotojo id, kurio įgūdžio ir pakopos buvo
bandymas, **kriptografinę vaizdo įrašo failo maišos reikšmę (hash)** ir įrašymo laiką.

Maišos reikšmė yra skaitmeninis atspaudas. Jos negalima paversti atgal į vaizdo įrašą. Ji egzistuoja
tam, kad bandymą būtų galima susieti su konkrečiu įrašu taip, kad tas įrašas niekada nepaliktų Jūsų
telefono.

### 3.4 Draugai
Jeigu ką nors pridedate pagal jo draugo kodą, mes išsaugome ryšį tarp Jūsų ir jo paskyros bei Jūsų
narystę bet kurioje draugų grupėje.

### 3.5 Naudojimo analitika
Mes naudojame **PostHog**, priglobtą **Europos Sąjungoje**, kad suprastume, kaip programėlė
naudojama. Mes registruojame tokius įvykius kaip tai, kurį įvadinio nustatymo žingsnį pasiekėte,
kada buvo užbaigta treniruotė, kada pasikeitė reitingas ir ar buvo parodytas arba uždarytas pirkimo
ekranas.

Šie įvykiai apima Jūsų reitingą ir Jūsų pažangą programėlėje. Jie **neapima** Jūsų vardo, el. pašto,
ūgio ar Jūsų treniruočių turinio.

---

## 4. Pirkiniai

Prenumeratas tvarko **Apple**. Mes niekada nematome Jūsų mokėjimo duomenų. **RevenueCat** mūsų vardu
tvarko Jūsų prenumeratos būseną ir gauna pseudonimizuotą identifikatorių bei Jūsų prenumeratos
būseną. Pats pirkimo ekranas yra programėlės dalis; joks trečiasis asmuo nesprendžia, kuris ekranas
Jums bus parodytas.

---

## 5. Kamera ir mikrofonas

„Ranked“ prašo prieigos prie kameros ir mikrofono dėl vienos funkcijos: patvirtinto bandymo įrašymo.
Įrašas išsaugomas Jūsų įrenginyje. Jis niekada nėra įkeliamas. Jeigu atsisakysite, visos kitos
programėlės dalys veiks toliau.

---

## 6. Sveikatos duomenys

„Ranked“ **neskaito** duomenų iš Apple Health ir į ją nerašo.

Jūsų amžius, lytis ir kūno svoris yra su sveikata susiję duomenys ir pagal BDAR jie gali būti
laikomi duomenimis apie sveikatą. Mes juos renkame vienu tikslu — reitingo formulė normalizuoja
rezultatus pagal kūno sudėjimą, kad 95 kg sveriančio ir 60 kg sveriančio sportininko, išlaikančių tą
pačią svarstyklę, rezultatai nebūtų vertinami taip, tarsi jie padarė tą patį — ir į serverį
siunčiame tik tiek jų, kiek būtina lyderių lentelės palyginimui.

---

## 7. Teisinis pagrindas (BDAR ir Šveicarijos revDSG)

| Kas | Pagrindas |
|---|---|
| Paskyra ir prisijungimas | Sutarties vykdymas — programėlei reikalinga paskyra |
| Amžius, lytis ir kūno svoris | Sutarties vykdymas — pagal juos normalizuojamas reitingas, be jų jo apskaičiuoti neįmanoma |
| Draugo kodas, draugų grupės | Sutarties vykdymas — funkcija yra pati priežastis, dėl kurios šie duomenys egzistuoja |
| Patvirtintų bandymų įrašai ir kiekvieno jų sukuriamas lyderių lentelės įrašas | Sutikimas, duotas sąmoningu bandymo įrašymo veiksmu. Jį atšaukiate pašalindami bandymą atitinkamos pakopos puslapyje, taip ištrindami įrašą — žr. 9 skirsnį |
| Pirkiniai | Sutarties vykdymas |
| Analitika | Teisėtas interesas tobulinti programėlę; bet kada galite nesutikti nustatymuose (Settings), žr. 9 skirsnį |

**Čia taikomi du teisės aktai, ne vienas.** „Ranked“ valdoma iš Šveicarijos, todėl šiam duomenų
tvarkymui taikomas peržiūrėtas Šveicarijos federalinis duomenų apsaugos įstatymas (**revDSG**,
galiojantis nuo 2023 m. rugsėjo mėn.). **BDAR** taikomas papildomai visais atvejais, kai programėle
naudojamasi iš Europos Sąjungos arba Jungtinės Karalystės. Kai šie du teisės aktai skiriasi, mes
laikomės griežtesniojo. Šveicarijos gyventojai turi tas pačias pagrindines teises, išvardytas 9
skirsnyje — teisę susipažinti su duomenimis, teisę reikalauti ištaisyti duomenis, teisę reikalauti
ištrinti duomenis, teisę į duomenų perkeliamumą ir teisę nesutikti — pagal revDSG 25 ir paskesnius
straipsnius.

---

## 8. Kiek laiko saugome duomenis

Paskyros, profilio, draugų ir patvirtintų bandymų įrašai saugomi tol, kol ištrinsite savo paskyrą.
Ištrynus paskyrą, jie pašalinami.

Analitikos įvykiai saugomi tiek laiko, kiek pagal mūsų planą taikoma paties PostHog saugojimo
trukmė. **Jūsų paskyros ištrynimas jų neištrina**, ir mes tai pasakome tiesiai, o ne užsimename apie
priešingai: analitikos profilis nėra susietas su Jūsų paskyra — jame naudojamas atskiras,
programėlės sugeneruotas identifikatorius — todėl nėra jokios sąsajos, pagal kurią galėtume jį rasti
ir pašalinti. Kas jame yra, išvardyta 3.5 skirsnyje: naudojimo įvykiai, Jūsų reitingas ir Jūsų
įvestas amžius, lytis bei kūno svoris. Jame nėra nei vardo, nei el. pašto, nei paskyros id.

Jeigu norite, kad būtų pašalintas ir tas profilis, parašykite mums nurodydami apytikslę datą, kada
pirmą kartą pasinaudojote programėle, ir mes jį surasime bei ištrinsime rankiniu būdu.

---

## 9. Jūsų teisės

Jūs bet kada galite:

- **Ištrinti savo paskyrą** programėlės nustatymuose (Settings). Taip ištrinamas Jūsų serveryje
  esantis profilis, Jūsų draugų ryšiai ir Jūsų patvirtintų bandymų įrašai. Jeigu Jūsų paskyrai yra
  išsaugotas Apple atnaujinimo prieigos raktas (žr. 3.1 skirsnį), taip pat panaikinama „Ranked“
  prieiga prie Jūsų Apple ID. Tik Jūsų įrenginyje saugomi duomenys pašalinami ištrynus programėlę.
- **Atšaukti patvirtintą bandymą** atitinkamos pakopos puslapyje programėlėje. Pašalinus bandymą,
  ištrinamas įrašas ir jo sukurtas lyderių lentelės įrašas, o įrašant duotas sutikimas atšaukiamas.
  Sutikimo atšaukimas neturi įtakos duomenų tvarkymo teisėtumui iki atšaukimo.
- **Prašyti duomenų, kuriuos apie Jus turime, kopijos** arba prašyti mūsų juos ištaisyti.
- **Nesutikti su analitika** naudodami jungiklį nustatymuose (Settings) arba parašydami mums.
- **Pateikti skundą priežiūros institucijai** savo šalyje.

Dėl bet kurio iš šių dalykų rašykite **dylan.schmid538@gmail.com**.

---

## 10. Vaikai

„Ranked“ nėra skirta jaunesniems nei 13 metų vaikams, ir mes sąmoningai nerenkame jų duomenų.

---

## 11. Pakeitimai

Jeigu ši politika bus iš esmės pakeista, programėlė Jums apie tai praneš prieš pakeitimui
įsigaliojant.

---

> **⚠️ Tai nėra teisinė konsultacija.** Šį dokumentą pagal programėlės pirminį kodą ir duomenų bazės
> struktūrą parengė inžinierius, o ne teisininkas. Jame sistema aprašyta tiksliai pagal aukščiau
> nurodytą datą — kiekvienas jame pateiktas teiginys buvo patikrintas pagal tai, ką programėlė iš
> tikrųjų siunčia. Jis **nebuvo** patikrintas dėl atitikties BDAR, Šveicarijos revDSG, CCPA ar bet
> kuriam kitam teisiniam režimui. Tai paskelbus, Apple reikalavimai tenkinami; tai nereiškia, kad
> laikotės teisės aktų reikalavimų. Kai programėlė pradės nešti pajamų, duokite ją perskaityti
> teisininkui.
