---
title: Polityka prywatności · Calisthenics Skills – Ranked
permalink: /privacy/pl/
---

> *To jest tłumaczenie. W razie rozbieżności rozstrzygająca jest wersja angielska dostępna pod
> adresem https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/.*

# Polityka prywatności · Calisthenics Skills – Ranked

**Ostatnia aktualizacja: 29 września 2026 r.**

Niniejsza polityka opisuje, co Ranked zbiera, dokąd to trafia i co można z tym zrobić. Powstała na
podstawie rzeczywistego kodu aplikacji, a nie z szablonu — jeżeli coś tutaj jest nieprawdziwe,
rozstrzyga kod.

Ranked prowadzi **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Szwajcaria**, kontakt
**dylan.schmid538@gmail.com**. Jest ona administratorem opisanego tu przetwarzania.

---

## 1. W skrócie

Ranked nie ma **kont użytkowników ani własnego serwera.** Wszystko, co dotyczy treningu — każda
zapisana seria, postęp w każdej umiejętności, ranga, Power Level, mapa ciała — jest przechowywane w
telefonie i nigdy nigdzie nie jest przesyłane.

**Wiek, płeć, wzrost i masa ciała nigdy nie opuszczają urządzenia.** Wzór rangi korzysta z nich w
telefonie. Nie są wysyłane ani do nas, ani do usługi analitycznej.

Urządzenie opuszczają dwie rzeczy i tylko te dwie:

1. **Anonimowe statystyki użycia**, żebyśmy widzieli, jak aplikacja jest używana. Można je w
   aplikacji w każdej chwili wyłączyć.
2. **Dane zakupu**, żeby można było zweryfikować subskrypcję App Store. Płatność obsługuje Apple;
   my nigdy nie widzimy danych płatniczych.

Ranked nie śledzi użytkownika w innych aplikacjach ani na stronach internetowych, nie wyświetla
reklam i nie odczytuje niczego z aplikacji Zdrowie firmy Apple.

---

## 2. Co zostaje na urządzeniu

Zapisane we własnej bazie danych aplikacji w telefonie i nigdy nieprzesyłane:

- Każdy trening, seria, powtórzenie, zwis oraz obciążenie dodatkowe, które zapiszesz
- Postęp w każdej umiejętności i na każdym etapie, historia rangi oraz Power Level
- Plan treningowy, harmonogram, przypomnienia i preferencje
- Wymiary ciała w postaci, w jakiej zostały wprowadzone (wiek, płeć, wzrost, masa ciała)
- Notatki treningowe

Aplikacja nie wyklucza tej bazy danych z kopii zapasowej urządzenia. Jeżeli korzystasz z kopii
iCloud lub kopii na komputerze, dane treningowe są jej częścią i wracają przy przywracaniu — na
warunkach Apple, nie naszych.

Usunięcie aplikacji usuwa to wszystko z urządzenia. Nie możemy tego odzyskać, ponieważ nigdy tego
nie mieliśmy.

---

## 3. Co opuszcza urządzenie

### 3.1 Statystyki użycia (PostHog)

Korzystamy z **PostHog**, hostowanego w **Unii Europejskiej**, aby rozumieć, jak używana jest
aplikacja. Aplikacja wysyła tam ustaloną listę zdarzeń:

- do którego kroku konfiguracji dotarłeś, który ukończyłeś lub z którego się wycofałeś i ile czasu
  zajął każdy z nich;
- co dała wstępna ocena: ile linii umiejętności i etapów zadeklarowałeś, którą umiejętność wybrałeś
  jako cel, jaką miałeś rangę początkową oraz rangę każdej z sześciu partii ciała;
- kiedy ekran zakupu został pokazany lub zamknięty i kiedy zakup został rozpoczęty, sfinalizowany
  lub przywrócony — wraz z produktem i ofertą, których dotyczył; oraz gdy aplikacja później stwierdzi
  aktywny okres próbny lub okres płatnej subskrypcji — wraz z produktem i informacją, czy jest to
  zakup w środowisku testowym. Nie jest to zapis każdego obciążenia i dane te nie są wysyłane,
  gdy aplikacja jest zamknięta;
- kiedy zmieniła się ranga i która umiejętność to wywołała;
- kiedy zaliczyłeś etap — która umiejętność, który etap i czy wynikało to z zapisanej serii,
  uzupełnionego treningu czy ręcznej deklaracji;
- które ekrany otwierasz i kiedy kończy się sesja. Zdarzenie zakończenia sesji nie zawiera żadnych
  szczegółów: ani ćwiczeń, ani serii, ani liczb.

Oprogramowanie PostHog w aplikacji dołącza ponadto do każdego zdarzenia standardowe informacje
techniczne — model urządzenia, wersję systemu iOS, wersję aplikacji, język i strefę czasową — oraz
odnotowuje, kiedy aplikacja jest otwierana i przenoszona w tło. Jak każda usługa internetowa,
PostHog otrzymuje adres IP żądania; może z niego wywnioskować przybliżoną lokalizację (kraj lub
miasto).

**Czego tam nie ma:** żadnego imienia i nazwiska, żadnego adresu e-mail (aplikacja nigdy o niego nie
pyta), żadnego identyfikatora konta (nie ma kont), ani wieku, płci, wzrostu czy masy ciała, ani
treści treningów.

**Jak jesteś identyfikowany:** PostHog generuje losowy identyfikator przy pierwszym uruchomieniu
aplikacji i zapisuje go na urządzeniu. Wszystkie zdarzenia są grupowane pod tym identyfikatorem.
Aplikacja nigdy nie mówi PostHogowi, kim jesteś, i nie ma też czego powiedzieć — nie ma konta ani
adresu e-mail.

**Wyłączanie:** Ustawienia ▸ Prywatność ▸ *Udostępniaj anonimowe dane o użyciu*. Wyłączenie tej
opcji sprawia, że od tej chwili aplikacja nie wysyła zdarzeń. Ustawienie jest zapisane na urządzeniu
i przetrwa aktualizacje aplikacji.

### 3.2 Atrybucja Apple Search Ads

Jeżeli zainstalowałeś Ranked po kliknięciu reklamy Apple Search Ads, aplikacja pyta Apple jeden raz,
przy pierwszym uruchomieniu, skąd wzięła się instalacja. Apple odpowiada, podając kampanię, grupę
reklam, słowo kluczowe i kreację tej reklamy, kraj lub region kliknięcia, datę kliknięcia oraz to,
czy było to nowe pobranie, czy ponowne. Aplikacja dołącza te wartości do anonimowego identyfikatora
PostHog opisanego w §3.1, aby każde późniejsze zdarzenie można było przypisać do reklamy, która Cię
przyprowadziła.

Służy do tego framework **AdServices** firmy Apple, który nie wykorzystuje identyfikatora
reklamowego (IDFA) i którego Apple nie uznaje za śledzenie — dlatego nie pojawia się okno zgody na
śledzenie. Jeżeli nie trafiłeś tu z reklamy, Apple tak odpowiada i nic nie zostaje dołączone.
Wyłączenie statystyk użycia (§3.1) zatrzymuje również to.

### 3.3 Zakupy (Apple i RevenueCat)

Subskrypcje sprzedaje i rozlicza **Apple** za pośrednictwem App Store. Nigdy nie widzimy danych
płatniczych, konta Apple ani imienia i nazwiska.

Aby sprawdzić, czy subskrypcja jest aktywna, aplikacja korzysta z **RevenueCat**. RevenueCat
otrzymuje zapis zakupu z App Store dotyczący subskrypcji — jaki produkt kupiono, kiedy się zaczął i
kiedy wygasa — wraz ze standardowymi informacjami technicznymi, takimi jak wersja systemu iOS i
wersja aplikacji. Instalację rozpoznaje po losowym identyfikatorze, który sam generuje i zapisuje na
urządzeniu. Nie przekazujemy RevenueCat imienia i nazwiska, adresu e-mail ani żadnej innej
tożsamości, a ponieważ Ranked nie ma kont, nie ma też czego przekazać.

Po naciśnięciu **Przywróć zakupy** aplikacja pyta Apple o zakupy dokonane z konta Apple zalogowanego
na urządzeniu i przekazuje wynik do RevenueCat w ten sam sposób.

---

## 4. Czego Ranked nie robi

- **Żadnych kont.** Nigdy się nie logujesz. Nie istnieje żaden Twój profil na jakimkolwiek serwerze.
- **Żadnego Apple Zdrowie.** Ranked ani nie czyta z aplikacji Zdrowie, ani do niej nie zapisuje.
- **Żadnego aparatu, zdjęć, mikrofonu, lokalizacji ani kontaktów.** Aplikacja nie prosi o żadne z
  tych uprawnień.
- **Żadnego śledzenia między aplikacjami ani stronami**, żadnego identyfikatora reklamowego, żadnych
  reklam w aplikacji, żadnych danych sprzedawanych ani przekazywanych brokerom danych.
- **Żadnego serwera powiadomień.** Przypomnienia, które Ranked może wysyłać, są planowane lokalnie w
  telefonie; nic na ich temat nie opuszcza urządzenia. Przed pierwszym z nich jesteś pytany o zgodę
  i możesz je w każdej chwili wyłączyć w ustawieniach systemu iOS.

---

## 5. Podstawa prawna (RODO i szwajcarska revDSG)

| Co | Podstawa |
|---|---|
| Zakupy i weryfikacja subskrypcji (§3.3) | Wykonanie umowy |
| Statystyki użycia (§3.1) | Prawnie uzasadniony interes w rozumieniu i ulepszaniu aplikacji; w każdej chwili można wnieść sprzeciw, wyłączając je, zob. §8 |
| Atrybucja Search Ads (§3.2) | Prawnie uzasadniony interes w tym, by wiedzieć, która reklama działa; sprzeciw jak wyżej |

**Obowiązują tu dwa porządki prawne, nie jeden.** Ranked jest prowadzony ze Szwajcarii, więc to
zrewidowana szwajcarska federalna ustawa o ochronie danych (**revDSG**, obowiązująca od września
2023 r.) reguluje to przetwarzanie. **RODO** stosuje się dodatkowo wszędzie tam, gdzie aplikacja
używana jest z Unii Europejskiej lub Zjednoczonego Królestwa. Tam, gdzie oba porządki się różnią,
stosujemy surowszy. Osoby zamieszkałe w Szwajcarii mają te same podstawowe prawa wymienione w §8 na
mocy art. 25 i nast. revDSG.

---

## 6. Gdzie dane są przetwarzane

- **PostHog** przetwarza statystyki użycia w Unii Europejskiej.
- **RevenueCat, Inc.** ma siedzibę w Stanach Zjednoczonych i tam przetwarza dane zakupu opisane w
  §3.3.
- **Apple** przetwarza sam zakup oraz zapytanie o atrybucję Search Ads zgodnie z własną polityką
  prywatności, która dotyczy Twojego konta Apple niezależnie od tej aplikacji.

---

## 7. Jak długo przechowujemy dane

Statystyki użycia są przechowywane tak długo, jak długo obowiązuje okres retencji PostHog dla
naszego planu. Nie obiecujemy stałej liczby miesięcy, ponieważ PostHog nie pozwala nam jej ustawić —
a liczba, której nikt nie jest w stanie dotrzymać, jest w polityce prywatności gorsza niż jej brak.

Zapisy zakupów RevenueCat przechowuje tak długo, jak istnieje subskrypcja i jej historia; właśnie
tego wymaga weryfikacja subskrypcji.

Wszystko, co jest na urządzeniu, pozostaje tam do momentu usunięcia aplikacji.

---

## 8. Twoje prawa

W każdej chwili możesz:

- **Wyłączyć statystyki użycia** w Ustawieniach ▸ Prywatność. To Twoje prawo do sprzeciwu, a tam,
  gdzie przetwarzanie opiera się na zgodzie — do jej wycofania; działa natychmiast i nie wymaga
  uzasadnienia.
- **Usunąć swoje dane.** Ponieważ Ranked nie przechowuje niczego o Tobie na serwerze, usunięcie
  aplikacji usuwa wszystko, co przechowuje sama aplikacja.
- **Poprosić nas o usunięcie anonimowego profilu analitycznego.** Nie możemy go znaleźć po nazwisku —
  nie ma go — ale jeżeli napiszesz do nas, podając przybliżoną datę pierwszego użycia aplikacji i
  używane urządzenie, odszukamy go ręcznie i usuniemy.
- **Zażądać kopii** danych, które usługa przechowuje pod Twoim identyfikatorem, poprosić nas o ich
  **sprostowanie** albo o **ograniczenie** przetwarzania na czas rozpatrywania wniosku.
- **Złożyć skargę do organu nadzorczego** w swoim kraju — w Szwajcarii do Federalnego
  Pełnomocnika ds. Ochrony Danych i Jawności (EDÖB/PFPDT).

W każdej z tych spraw pisz na **dylan.schmid538@gmail.com**.

---

## 9. Dzieci

Ranked jest przeznaczony dla osób w wieku **16 lat i starszych**. Aplikacja pyta o wiek podczas
konfiguracji, ponieważ zależy od niego wzór rangi, i nie jest skierowana do nikogo młodszego. Nie
zbieramy świadomie danych osób poniżej 16 roku życia.

---

## 10. Zmiany

Obowiązuje wersja opublikowana pod tym adresem, a data u góry wskazuje, kiedy zmieniono ją ostatnio.
Wcześniejsze wersje pozostają widoczne w publicznej historii repozytorium, z którego te strony są
publikowane, dzięki czemu widać, co i kiedy się zmieniło.

---

> **⚠️ To nie jest porada prawna.** Dokument sporządził inżynier na podstawie kodu źródłowego
> aplikacji, a nie prawnik. Opisuje system zgodnie ze stanem na powyższą datę — każde stwierdzenie
> zostało sprawdzone z tym, co aplikacja rzeczywiście wysyła. **Nie** został zbadany pod kątem
> zgodności z RODO, szwajcarską revDSG, CCPA ani żadnym innym reżimem. Opublikowanie go spełnia
> wymagania Apple; nie oznacza zgodności z prawem. Gdy aplikacja zacznie zarabiać, należy dać go do
> przeczytania prawnikowi.
