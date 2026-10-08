---
title: Polityka prywatności · Calisthenics Skills – Ranked
permalink: /privacy/pl/
---

> *To jest tłumaczenie. W razie rozbieżności rozstrzygająca jest wersja angielska dostępna pod
> adresem https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/.*

# Polityka prywatności · Calisthenics Skills – Ranked

**Ostatnia aktualizacja: 2026-10-08**

Niniejsza polityka opisuje, co Ranked zbiera, dokąd to trafia i co można z tym zrobić.

Ranked prowadzi **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Szwajcaria**, kontakt
**dylan.schmid538@gmail.com**. Jest ona administratorem opisanego tu przetwarzania.

---

## 1. W skrócie

**Wiek, płeć, wzrost i masa ciała nigdy nie opuszczają urządzenia.** Wzór rangi korzysta z nich w
telefonie. Nie są wysyłane ani do nas, ani do usługi analitycznej.

Urządzenie opuszczają dwie rzeczy i tylko te dwie:

1. **Statystyki użycia**, żebyśmy widzieli, jak aplikacja jest używana. Można je w
   aplikacji w każdej chwili wyłączyć.
2. **Dane zakupu**, żeby można było zweryfikować subskrypcję App Store. Płatność obsługuje Apple;
   my nigdy nie widzimy danych płatniczych.

Ranked nie śledzi użytkownika w innych aplikacjach ani na stronach internetowych, nie wyświetla
reklam i nie odczytuje niczego z aplikacji Zdrowie firmy Apple.

---

## 2. Co zostaje na urządzeniu

Zapisane we własnej bazie danych aplikacji w telefonie i nigdy nieprzesyłane:

- Każdy trening, seria, powtórzenie, zwis oraz obciążenie dodatkowe, które zapiszesz
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

Analityka jest domyślnie wyłączona. Dopiero gdy wyraźnie wyrazisz zgodę podczas konfiguracji lub później w Ustawieniach, Ranked wysyła do PostHog w UE zdarzenia dotyczące konfiguracji, oceny początkowej, zmian rangi i etapu (wraz z umiejętnością i etapem), ekranu zakupu, zakupów i otwieranych ekranów. Zdarzenia treningu na żywo obejmują rozpoczęcie, ukończenie lub przerwanie, liczbę sekund, zapisanych serii, różnych umiejętności oraz informację, czy był to pierwszy ukończony trening. Nie zawierają poszczególnych ćwiczeń, powtórzeń, obciążeń ani notatek. Wiek, płeć, wzrost i masa ciała nie są przesyłane. PostHog otrzymuje też typowe dane techniczne o urządzeniu, iOS, aplikacji i języku oraz adres IP, z którego można wywnioskować przybliżoną lokalizację. Losowy identyfikator analityczny powstaje po wyrażeniu zgody. Zgodę można wycofać w Ustawieniach ▸ Dane i prywatność; nowe zdarzenia przestają być wysyłane, ale wcześniejsze dane nie są automatycznie usuwane.

### 3.2 Atrybucja Apple Search Ads

Dopiero po zgodzie na analitykę Ranked jednorazowo pyta Apple AdServices o przypisanie instalacji do Apple Search Ads. Po kliknięciu reklamy kampania, grupa reklam, słowo kluczowe, materiał reklamowy, kraj lub region, data kliknięcia i typ pobrania mogą zostać powiązane z losowym identyfikatorem PostHog. Identyfikator reklamowy IDFA nie jest używany. Wycofanie zgody zatrzymuje przyszłe przesyłanie.

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
| Statystyki użycia (§3.1) | Twoja zgoda; można ją w każdej chwili wycofać w Ustawieniach ▸ Dane i prywatność |
| Atrybucja Search Ads (§3.2) | Twoja zgoda; można ją w każdej chwili wycofać w Ustawieniach ▸ Dane i prywatność |

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

Możesz w każdej chwili wycofać zgodę na analitykę w Ustawieniach ▸ Dane i prywatność bez podawania przyczyny. Nowe zdarzenia zostają natychmiast zatrzymane, ale już przesłane dane nie są automatycznie usuwane, a subskrypcja App Store nie zostaje anulowana.

Lokalne dane treningowe możesz usunąć w Ustawieniach ▸ Dane i prywatność ▸ *Usuń lokalne dane treningowe* albo usuwając aplikację. Subskrypcją zarządzasz i anulujesz ją oddzielnie na swoim koncie Apple.

W sprawie danych przesłanych już do PostHog napisz na **dylan.schmid538@gmail.com**. Ranked nie łączy losowego identyfikatora analitycznego z kontem. Przybliżona data lub model urządzenia mogą nie wystarczyć, by wiarygodnie odnaleźć profil. Wyjaśnimy, co możemy zidentyfikować, i rozpatrzymy możliwe do zweryfikowania żądania dostępu, sprostowania lub usunięcia. Nie przesyłaj danych logowania do konta Apple.

Możesz zażądać ograniczenia przetwarzania i złożyć skargę do organu nadzorczego w swoim kraju; w Szwajcarii jest nim federalny komisarz ds. ochrony danych i informacji (FDPIC).

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
