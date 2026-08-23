---
title: Polityka prywatności · Calisthenics Skills – Ranked
permalink: /privacy/pl/
---

*To jest tłumaczenie. W razie rozbieżności rozstrzygające znaczenie ma wersja angielska dostępna pod adresem https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/.*

# Polityka prywatności · Calisthenics Skills – Ranked

**Ostatnia aktualizacja: 18 sierpnia 2026 r.**

Niniejsza polityka opisuje, jakie dane zbiera Ranked, dokąd one trafiają i co użytkownik może w tej
sprawie zrobić. Została sporządzona na podstawie rzeczywistego kodu aplikacji i schematu bazy
danych, a nie na podstawie wzorca — jeżeli coś jest tu niezgodne z prawdą, należy sprawdzić kod.

Aplikację Ranked prowadzi **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Szwajcaria**, kontakt **dylan.schmid538@gmail.com**.

---

## 1. Wersja skrócona

Niemal wszystko, co Ranked wie o treningu użytkownika, pozostaje na jego telefonie. Historia
treningów, postępy w każdej umiejętności, ranga oraz mapa ciała są przechowywane lokalnie i nigdy
nie są przesyłane.

Cztery rodzaje danych opuszczają urządzenie: tożsamość używana do logowania, niewielki profil
wykorzystywany w tabelach wyników, zapisy o wykonaniu zweryfikowanej próby oraz anonimowe dane
analityczne o korzystaniu z aplikacji. Każdy z nich został opisany poniżej.

**Nagrania wideo ze Zweryfikowanych prób nigdy nie opuszczają urządzenia.** Przesyłany jest
wyłącznie odcisk pliku.

---

## 2. Co pozostaje na urządzeniu

Przechowywane lokalnie we własnej bazie danych aplikacji i nigdy nieprzesyłane:

- Każdy trening, seria, powtórzenie, utrzymanie pozycji (hold) oraz dodatkowe obciążenie, które
  użytkownik zapisze
- Postępy w każdej umiejętności i na każdym etapie oraz historia rangi
- Plan treningowy, harmonogram i preferencje
- Pomiary ciała w postaci wprowadzonej przez użytkownika (wiek, płeć, wzrost, masa ciała) — kopia
  części z nich jest dodatkowo przesyłana do usługi tabel wyników, zob. §3.2
- **Pliki wideo ze Zweryfikowanych prób.** Są zapisywane w prywatnej pamięci aplikacji. Nie są
  przesyłane, nie są kopiowane na nasze serwery i nie mamy do nich dostępu.

Usunięcie aplikacji usuwa wszystkie te dane. Nie możemy ich odzyskać.

---

## 3. Co opuszcza urządzenie

### 3.1 Konto użytkownika
Przy logowaniu za pomocą Apple lub Google otrzymujemy i przechowujemy identyfikator użytkownika
oraz — w zależności od tego, na co użytkownik zezwoli podczas logowania — adres e-mail. Obsługuje
to **Supabase**, który hostuje naszą bazę danych i uwierzytelnianie.

Przy logowaniu za pomocą Apple przechowujemy również token odświeżający, który Apple przekazuje nam
w tym momencie. Ma on tylko jedno przeznaczenie: usunięcie konta powoduje wówczas także cofnięcie
dostępu aplikacji Ranked do Apple ID użytkownika, zgodnie z wymogiem Apple. W przypadku kont,
których ostatnie logowanie nastąpiło przed wprowadzeniem tego rozwiązania, żaden token nie jest
przechowywany — usunięcie konta po prostu pomija wtedy etap cofnięcia dostępu.

### 3.2 Profil w tabeli wyników
Aby umieścić użytkownika w tabeli wyników i porównać go z osobami o podobnej budowie ciała, na
naszym serwerze przechowywane są następujące dane:

- losowo wygenerowany **kod znajomego**
- **wiek**, **płeć** i **masa ciała**
- data utworzenia profilu

**Uwaga dotycząca widoczności:** każdy zalogowany użytkownik Ranked może wyszukać profil po jego
kodzie znajomego. Taki jest cel kodu znajomego — istnieje po to, by przekazać go innej osobie. Nie
należy udostępniać swojego kodu nikomu, kto nie powinien widzieć danego wpisu. Inni użytkownicy
widzą kod znajomego oraz pozycję w tabeli wyników — i nic poza tym. Wiek, płeć i masa ciała służą
do porównania po stronie serwera i nigdy nie są pokazywane innym użytkownikom ani możliwe do
pobrania przez nich.

**Wzrost** nie jest przesyłany. Historia treningów nie jest przesyłana.

### 3.3 Zweryfikowane próby
Gdy użytkownik nagrywa Zweryfikowaną próbę, przechowujemy: jego identyfikator użytkownika,
informację o tym, której umiejętności i którego etapu próba dotyczyła, **kryptograficzny skrót
(hash) pliku wideo** oraz czas nagrania.

Skrót jest odciskiem. Nie da się go z powrotem przekształcić w nagranie. Istnieje po to, aby próbę
można było powiązać z konkretnym nagraniem bez tego, by nagranie kiedykolwiek opuściło telefon.

### 3.4 Znajomi
Jeżeli użytkownik doda kogoś przy użyciu kodu znajomego, przechowujemy powiązanie między jego
kontem a kontem tej osoby oraz przynależność do dowolnej grupy znajomych.

### 3.5 Dane analityczne o korzystaniu z aplikacji
Korzystamy z **PostHog**, hostowanego w **Unii Europejskiej**, aby zrozumieć, w jaki sposób
aplikacja jest używana. Rejestrujemy zdarzenia takie jak to, do którego kroku wprowadzenia dotarł
użytkownik, kiedy trening został ukończony, kiedy zmieniła się ranga oraz czy ekran zakupu został
wyświetlony lub zamknięty.

Zdarzenia te zawierają rangę użytkownika i jego postępy w aplikacji. **Nie** zawierają imienia i
nazwiska, adresu e-mail, wzrostu ani treści treningów.

---

## 4. Zakupy

Subskrypcje są obsługiwane przez **Apple**. Nigdy nie widzimy danych płatniczych użytkownika.
**RevenueCat** zarządza w naszym imieniu statusem subskrypcji i otrzymuje pseudonimowy
identyfikator oraz stan subskrypcji. Sam ekran zakupu jest częścią aplikacji; żaden podmiot trzeci
nie decyduje o tym, który ekran zostanie wyświetlony.

---

## 5. Aparat i mikrofon

Ranked prosi o dostęp do aparatu i mikrofonu w jednym celu: nagrania Zweryfikowanej próby. Nagranie
jest zapisywane na urządzeniu. Nigdy nie jest przesyłane. W razie odmowy każda pozostała część
aplikacji działa nadal.

---

## 6. Dane dotyczące zdrowia

Ranked **nie** odczytuje danych z Apple Health ani ich tam nie zapisuje.

Wiek, płeć i masa ciała to dane zbliżone do danych o zdrowiu i w świetle RODO mogą stanowić dane
dotyczące zdrowia. Zbieramy je w jednym celu — wzór na rangę normalizuje wynik względem budowy
ciała, tak aby atleta o masie 95 kg i atleta o masie 60 kg utrzymujący tę samą dźwignię nie byli
oceniani tak, jakby zrobili to samo — i przesyłamy na serwer tylko taki ich zakres, jaki jest
niezbędny do porównania w tabeli wyników.

---

## 7. Podstawa prawna (RODO i szwajcarski revDSG)

| Czego dotyczy | Podstawa |
|---|---|
| Konto i logowanie | Wykonanie umowy — aplikacja wymaga konta |
| Profil w tabeli wyników | Zgoda, wyrażona przez skorzystanie z funkcji tabeli wyników |
| Zapisy zweryfikowanych prób | Zgoda, wyrażona przez nagranie próby |
| Zakupy | Wykonanie umowy |
| Dane analityczne | Prawnie uzasadniony interes polegający na ulepszaniu aplikacji; można wnieść sprzeciw, zob. §9 |

**Zastosowanie mają dwie ustawy, nie jedna.** Ranked jest prowadzony ze Szwajcarii, dlatego
przetwarzanie to podlega zrewidowanej szwajcarskiej ustawie federalnej o ochronie danych
(**revDSG**, obowiązującej od września 2023 r.). **RODO** stosuje się dodatkowo wszędzie tam, gdzie
aplikacja jest używana na terenie Unii Europejskiej lub Zjednoczonego Królestwa. W razie różnic
między nimi stosujemy przepis surowszy. Osobom zamieszkałym w Szwajcarii przysługują te same
podstawowe prawa wymienione w §9 — dostęp, sprostowanie, usunięcie, przenoszenie danych i sprzeciw
— na podstawie art. 25 i nast. revDSG.

---

## 8. Jak długo przechowujemy dane

Konto, profil, znajomi i zapisy zweryfikowanych prób są przechowywane do momentu usunięcia konta
przez użytkownika. Usunięcie konta powoduje ich usunięcie.

Zdarzenia analityczne są przechowywane tak długo, jak długo obowiązuje wobec naszego planu własna
polityka retencji PostHog. **Usunięcie konta nie powoduje ich usunięcia** — mówimy o tym wprost,
zamiast sugerować co innego: profil analityczny nie jest powiązany z kontem użytkownika, ponieważ
korzysta z odrębnego identyfikatora generowanego przez aplikację, więc nie istnieje powiązanie,
dzięki któremu moglibyśmy go odnaleźć i usunąć. Jego zawartość wymieniono w §3.5: zdarzenia
dotyczące korzystania z aplikacji, ranga oraz wprowadzone przez użytkownika wiek, płeć i masa
ciała. Nie zawiera on imienia i nazwiska, adresu e-mail ani identyfikatora konta.

Jeżeli użytkownik chce, aby również ten profil został usunięty, prosimy o wiadomość z przybliżoną
datą pierwszego skorzystania z aplikacji — odnajdziemy go i usuniemy ręcznie.

---

## 9. Prawa użytkownika

W każdej chwili można:

- **Usunąć konto** w Ustawieniach w aplikacji. Powoduje to usunięcie profilu po stronie serwera,
  powiązań ze znajomymi oraz zapisów zweryfikowanych prób. Jeżeli dla danego konta przechowywany
  jest token odświeżający Apple (zob. §3.1), cofa to również dostęp aplikacji Ranked do Apple ID
  użytkownika. Dane przechowywane wyłącznie na urządzeniu usuwa się przez usunięcie aplikacji.
- **Zażądać kopii** danych, które o użytkowniku przechowujemy, lub poprosić o ich sprostowanie.
- **Wnieść sprzeciw wobec danych analitycznych.**
- **Wnieść skargę do organu nadzorczego** w swoim kraju.

W każdej z tych spraw prosimy pisać na adres **dylan.schmid538@gmail.com**.

---

## 10. Dzieci

Ranked nie jest skierowany do dzieci poniżej 13. roku życia i nie zbieramy świadomie ich danych.

---

## 11. Zmiany

Jeżeli niniejsza polityka ulegnie istotnej zmianie, aplikacja poinformuje o tym użytkownika, zanim
zmiana wejdzie w życie.

---

> **⚠️ To nie jest porada prawna.** Niniejszy dokument został sporządzony na podstawie kodu
> źródłowego aplikacji i schematu bazy danych przez inżyniera, a nie przez prawnika. Opisuje on
> system zgodnie ze stanem na dzień podany powyżej — każde zawarte w nim twierdzenie zostało
> sprawdzone pod kątem tego, co aplikacja rzeczywiście przesyła. **Nie** został poddany ocenie pod
> kątem zgodności z RODO, szwajcarskim revDSG, CCPA ani jakimkolwiek innym reżimem prawnym. Jego
> opublikowanie spełnia wymagania Apple; nie oznacza jednak zgodności z prawem. Gdy aplikacja
> zacznie zarabiać, należy dać go do przeczytania prawnikowi.
