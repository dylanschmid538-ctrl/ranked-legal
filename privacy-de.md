---
title: Datenschutzerklärung · Calisthenics Skills – Ranked
permalink: /privacy/de/
---

> *Dies ist eine Übersetzung. Im Falle von Abweichungen ist die englische Fassung unter
> https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/ massgebend.*

# Datenschutzerklärung · Calisthenics Skills – Ranked

**Zuletzt aktualisiert: 2026-10-02**

Diese Erklärung beschreibt, was Ranked erhebt, wohin es geht und was Sie dagegen tun können. Sie
wurde anhand des tatsächlichen Codes der App verfasst, nicht nach einer Vorlage — wenn etwas
hierin falsch ist, ist der Code das Massgebliche.

Ranked wird betrieben von **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Schweiz**,
Kontakt **dylan.schmid538@gmail.com**. Sie ist die Verantwortliche für die hier beschriebene
Bearbeitung.

---

## 1. Die Kurzfassung

**Ihr Alter, Ihr Geschlecht, Ihre Grösse und Ihr Körpergewicht verlassen Ihr Gerät nie.** Die
Rangformel verwendet sie auf Ihrem Telefon. Sie werden weder an uns noch an den Analysedienst
gesendet.

Zwei Dinge verlassen Ihr Gerät, und nur diese zwei:

1. **Anonyme Nutzungsstatistiken**, damit wir sehen, wie die App benutzt wird. Sie können das in
   der App jederzeit abschalten.
2. **Kaufdaten**, damit das App-Store-Abonnement überprüft werden kann. Apple wickelt die Zahlung
   ab; wir sehen Ihre Zahlungsdaten nie.

Ranked verfolgt Sie nicht über andere Apps oder Websites hinweg, zeigt keine Werbung und liest
nichts aus Apple Health.

---

## 2. Was auf Ihrem Gerät bleibt

In der eigenen Datenbank der App auf Ihrem Telefon gespeichert und niemals übertragen:

- Jedes Training, jeder Satz, jede Wiederholung, jedes Halten und jedes Zusatzgewicht, das Sie
  loggen
- Ihr Trainingsplan, Ihr Zeitplan, Ihre Erinnerungen und Ihre Einstellungen
- Ihre Körpermasse, so wie Sie sie eingegeben haben (Alter, Geschlecht, Grösse, Körpergewicht)
- Ihre Trainingsnotizen

Die App schliesst diese Datenbank nicht von der Sicherung Ihres Geräts aus. Wenn Sie iCloud-Backup
oder eine Sicherung über einen Computer nutzen, sind Ihre Trainingsdaten Teil dieser Sicherung und
kommen beim Wiederherstellen zurück — zu Apples Bedingungen, nicht zu unseren.

Das Löschen der App löscht all das vom Gerät. Wir können es nicht wiederherstellen, weil wir es nie
hatten.

---

## 3. Was Ihr Gerät verlässt

### 3.1 Nutzungsstatistiken (PostHog)

Wir verwenden **PostHog**, gehostet in der **Europäischen Union**, um zu verstehen, wie die App
benutzt wird. Die App sendet dorthin eine feste Liste von Ereignissen:

- welchen Einrichtungsschritt Sie erreicht, abgeschlossen oder zurückgenommen haben, und wie lange
  jeder gedauert hat;
- was die Ersteinstufung ergeben hat: wie viele Skill-Linien und Stufen Sie angegeben haben,
  welchen Skill Sie sich als Ziel gesetzt haben, Ihren Startrang und den Rang jeder Ihrer sechs
  Körperregionen;
- wann der Kaufbildschirm gezeigt oder geschlossen wurde und wann ein Kauf begonnen, abgeschlossen
  oder wiederhergestellt wurde — mit dem betroffenen Produkt und Angebot; sowie wenn die App später
  einen aktiven Testzeitraum oder einen bezahlten Abonnementzeitraum feststellt — mit dem Produkt
  und der Angabe, ob es sich um einen Sandbox-Kauf handelt. Dies ist kein Protokoll jeder einzelnen
  Abbuchung und wird nicht gesendet, während die App geschlossen ist;
- wann sich Ihr Rang geändert hat und welcher Skill das ausgelöst hat;
- wann Sie eine Stufe geschafft haben — welcher Skill, welche Stufe, und ob es aus einem geloggten
  Satz, einem nachgetragenen Training oder einer manuellen Angabe kam;
- welche Bildschirme Sie öffnen und wann eine Session endet. Das Ereignis zum Session-Ende trägt
  keinerlei Einzelheiten: nicht die Übungen, nicht die Sätze, nicht die Zahlen.

Die PostHog-Software in der App hängt an jedes Ereignis ausserdem technische Standardangaben an —
etwa Ihr Gerätemodell, Ihre iOS-Version, die App-Version, die Sprache und die Zeitzone — und hält
fest, wann die App geöffnet und in den Hintergrund geschickt wird. Wie jeder Internetdienst erhält
PostHog die IP-Adresse der Anfrage; daraus kann ein ungefährer Ort (Land oder Stadt) abgeleitet
werden.

**Was nicht darin steht:** kein Name, keine E-Mail-Adresse (die App fragt nie danach), keine
Kontokennung (es gibt keine), weder Alter noch Geschlecht, Grösse oder Körpergewicht, und keine
Inhalte Ihrer Trainings.

**Wie Sie identifiziert werden:** PostHog erzeugt beim ersten Start der App eine zufällige Kennung
und speichert sie auf Ihrem Gerät. Alle Ereignisse werden unter dieser Kennung gruppiert. Die App
sagt PostHog nie, wer Sie sind, und es gibt auch nichts — kein Konto, keine E-Mail —, was sie sagen
könnte.

**Abschalten:** Einstellungen ▸ Datenschutz ▸ *Anonyme Nutzungsdaten teilen*. Wenn Sie das
ausschalten, sendet die App von diesem Moment an keine Ereignisse mehr. Die Einstellung liegt auf
Ihrem Gerät und übersteht App-Aktualisierungen.

### 3.2 Zuordnung von Apple Search Ads

Wenn Sie Ranked nach dem Tippen auf eine Apple-Search-Ads-Anzeige installiert haben, fragt die App
Apple einmalig beim ersten Start, woher die Installation kam. Apple antwortet mit Kampagne,
Anzeigengruppe, Suchbegriff und Motiv jener Anzeige, dem Land oder der Region des Klicks, dem Datum
des Klicks und der Angabe, ob es ein neuer Download oder ein erneuter war. Die App hängt diese
Werte an die anonyme PostHog-Kennung aus §3.1, damit sich jedes spätere Ereignis der Anzeige
zuordnen lässt, die Sie gebracht hat.

Dafür wird Apples **AdServices**-Framework verwendet, das ohne den Werbe-Identifier (IDFA)
auskommt und das Apple nicht als Tracking wertet — es wird daher kein Tracking-Dialog angezeigt.
Sind Sie nicht über eine Anzeige gekommen, sagt Apple das, und es wird nichts angehängt. Das
Abschalten der Nutzungsstatistiken (§3.1) stoppt auch dies.

### 3.3 Käufe (Apple und RevenueCat)

Abonnements werden von **Apple** über den App Store verkauft und abgerechnet. Wir sehen Ihre
Zahlungsdaten, Ihren Apple-Account und Ihren Namen nie.

Um zu prüfen, ob Ihr Abonnement aktiv ist, verwendet die App **RevenueCat**. RevenueCat erhält den
App-Store-Kaufdatensatz zu Ihrem Abonnement — welches Produkt gekauft wurde, wann es begonnen hat
und wann es abläuft — zusammen mit technischen Standardangaben wie Ihrer iOS-Version und der
App-Version. Ihre Installation wird über eine zufällige Kennung erkannt, die RevenueCat selbst
erzeugt und auf Ihrem Gerät speichert. Wir geben RevenueCat weder Ihren Namen noch Ihre
E-Mail-Adresse noch eine andere Identität, und da Ranked keine Konten hat, gibt es auch keine.

Wenn Sie **Käufe wiederherstellen** antippen, fragt die App bei Apple die Käufe ab, die mit dem auf
dem Gerät angemeldeten Apple-Account getätigt wurden, und gibt das Ergebnis auf demselben Weg an
RevenueCat weiter.

---

## 4. Was Ranked nicht tut

- **Keine Konten.** Sie melden sich nie an. Es gibt kein Profil von Ihnen auf irgendeinem Server.
- **Kein Apple Health.** Ranked liest weder aus der Health-App noch schreibt es dorthin.
- **Keine Kamera, keine Fotos, kein Mikrofon, kein Standort, keine Kontakte.** Die App fordert
  keine dieser Berechtigungen an.
- **Kein Tracking über Apps oder Websites hinweg**, kein Werbe-Identifier, keine Werbung in der
  App, keine Daten, die an Datenhändler verkauft oder weitergegeben werden.
- **Kein Push-Server.** Die Erinnerungen, die Ranked senden kann, werden lokal auf Ihrem Telefon
  geplant; nichts davon verlässt das Gerät. Sie werden vor der ersten gefragt, und Sie können sie
  in den iOS-Einstellungen jederzeit abschalten.

---

## 5. Rechtsgrundlage (DSGVO und Schweizer revDSG)

| Was | Grundlage |
|---|---|
| Käufe und Abo-Überprüfung (§3.3) | Vertragserfüllung |
| Nutzungsstatistiken (§3.1) | Berechtigtes Interesse daran, die App zu verstehen und zu verbessern; Sie können jederzeit widersprechen, indem Sie es abschalten, siehe §8 |
| Search-Ads-Zuordnung (§3.2) | Berechtigtes Interesse daran zu wissen, welche Werbung wirkt; Widerspruch wie oben |

**Hier gelten zwei Rechtsordnungen, nicht eine.** Ranked wird aus der Schweiz betrieben, daher
regelt das revidierte Schweizer Datenschutzgesetz (**revDSG**, in Kraft seit September 2023) diese
Bearbeitung. Die **DSGVO** gilt zusätzlich überall dort, wo die App aus der Europäischen Union oder
dem Vereinigten Königreich genutzt wird. Wo die beiden voneinander abweichen, folgen wir der
strengeren. Personen mit Wohnsitz in der Schweiz haben dieselben Kernrechte aus §8 nach Art. 25 ff.
revDSG.

---

## 6. Wo die Daten bearbeitet werden

- **PostHog** bearbeitet die Nutzungsstatistiken in der Europäischen Union.
- **RevenueCat, Inc.** hat seinen Sitz in den Vereinigten Staaten und bearbeitet die in §3.3
  beschriebenen Kaufdaten dort.
- **Apple** bearbeitet den Kauf selbst und die Search-Ads-Anfrage nach Apples eigener
  Datenschutzerklärung, die unabhängig von dieser App für Ihren Apple-Account gilt.

---

## 7. Wie lange wir die Daten aufbewahren

Nutzungsstatistiken werden so lange aufbewahrt, wie die Aufbewahrungsfrist von PostHog für unseren
Tarif gilt. Wir versprechen keine feste Anzahl Monate, weil PostHog uns keine einstellen lässt —
und eine Zahl, die niemand einhalten kann, ist in einer Datenschutzerklärung schlimmer als keine.

Kaufdatensätze bewahrt RevenueCat so lange auf, wie das Abonnement und seine Historie bestehen;
genau das verlangt die Überprüfung eines Abonnements.

Alles auf Ihrem Gerät bleibt dort, bis Sie die App löschen.

---

## 8. Ihre Rechte

Sie können jederzeit:

- **Nutzungsstatistiken abschalten**, unter Einstellungen ▸ Datenschutz. Das ist Ihr Recht auf
  Widerspruch und, soweit die Bearbeitung auf Einwilligung beruht, auf deren Widerruf — es wirkt
  sofort und braucht keine Begründung.
- **Ihre Daten löschen.** Da Ranked nichts über Sie auf einem Server hält, entfernt das Löschen der
  App alles, was die App selbst speichert.
- **Uns bitten, Ihr anonymes Analyseprofil zu löschen.** Wir können es nicht über einen Namen
  finden — es hat keinen —, aber wenn Sie uns das ungefähre Datum Ihrer ersten Nutzung und das
  verwendete Gerät schreiben, suchen wir es von Hand heraus und löschen es.
- **Eine Kopie** der Daten verlangen, die ein Dienst unter Ihrer Kennung hält, uns um deren
  **Berichtigung** bitten oder um eine **Einschränkung** der Bearbeitung, solange ein Antrag
  geprüft wird.
- **Sich bei einer Aufsichtsbehörde beschweren** in Ihrem Land — in der Schweiz beim
  Eidgenössischen Datenschutz- und Öffentlichkeitsbeauftragten (EDÖB).

Schreiben Sie für all das an **dylan.schmid538@gmail.com**.

---

## 9. Kinder

Ranked ist für Personen ab **16 Jahren**. Die App fragt bei der Einrichtung nach Ihrem Alter, weil
die Rangformel davon abhängt, und sie richtet sich an niemanden, der jünger ist. Wir erheben
wissentlich keine Daten von Personen unter 16 Jahren.

---

## 10. Änderungen

Es gilt die Fassung, die unter dieser Adresse veröffentlicht ist, und das Datum oben sagt Ihnen,
wann sie zuletzt geändert wurde. Frühere Fassungen bleiben in der öffentlichen Historie des
Repositorys sichtbar, aus dem diese Seiten veröffentlicht werden, sodass Sie sehen können, was sich
wann geändert hat.

---

> **⚠️ Keine Rechtsberatung.** Dieses Dokument wurde von einem Entwickler anhand des Quellcodes der
> App verfasst, nicht von einer Juristin oder einem Juristen. Es beschreibt das System zum oben
> genannten Datum zutreffend — jede Aussage darin wurde daran geprüft, was die App tatsächlich
> sendet. Es wurde **nicht** auf die Vereinbarkeit mit der DSGVO, dem Schweizer revDSG, dem CCPA
> oder einer anderen Regelung geprüft. Die Veröffentlichung genügt Apple; sie macht Sie nicht
> rechtskonform. Lassen Sie es von einer Anwältin oder einem Anwalt lesen, sobald die App Geld
> einbringt.
