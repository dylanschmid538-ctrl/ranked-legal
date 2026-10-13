---
title: Datenschutzerklärung · Calisthenics Skills – Ranked
permalink: /privacy/de/
---

> *Dies ist eine Übersetzung. Im Falle von Abweichungen ist die englische Fassung unter
> https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/ massgebend.*

# Datenschutzerklärung · Calisthenics Skills – Ranked

**Zuletzt aktualisiert: 2026-10-13**

Diese Erklärung beschreibt, was Ranked erhebt, wohin es geht und was Sie dagegen tun können.

Ranked wird betrieben von **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Schweiz**,
Kontakt **dylan.schmid538@gmail.com**. Sie ist die Verantwortliche für die hier beschriebene
Bearbeitung.

---

## 1. Die Kurzfassung

**Ihr Alter, Ihr Geschlecht, Ihre Grösse und Ihr Körpergewicht verlassen Ihr Gerät nie.** Die
Rangformel verwendet sie auf Ihrem Telefon. Sie werden weder an uns noch an den Analysedienst
gesendet.

Drei Arten von Daten können Ihr Gerät verlassen:

1. **Nutzungsstatistiken**, damit wir sehen, wie die App benutzt wird. Sie können das in
   der App jederzeit abschalten.
2. **Kaufdaten**, damit das App-Store-Abonnement überprüft werden kann. Apple wickelt die Zahlung
   ab; wir sehen Ihre Zahlungsdaten nie.
3. **Nachrichten für Feedback und Support**, nur wenn Sie selbst eine senden. Mit Ihrer Einwilligung können Sie eine E-Mail-Adresse oder Telefonnummer für eine Antwort angeben.

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

Die Analyse ist standardmäßig ausgeschaltet. Erst wenn Sie während der Einrichtung oder später in den Einstellungen ausdrücklich zustimmen, sendet Ranked Nutzungsereignisse an PostHog in der EU: Einrichtung und Ersteinstufung, Rang- und Stufenänderungen (mit Skill und Stufe), Kaufbildschirm und Kaufvorgang sowie geöffnete Ansichten. Ereignisse zu Live-Trainings enthalten Start, Abschluss oder Abbruch, verstrichene Sekunden, Anzahl geloggter Sätze, Anzahl unterschiedlicher Skills und ob es das erste abgeschlossene Training war. Sie enthalten keine einzelnen Übungen, Wiederholungen, Gewichte oder Notizen. Alter, Geschlecht, Größe und Körpergewicht werden nicht übermittelt. PostHog erhält übliche Geräte-, iOS-, App- und Sprachangaben sowie die IP-Adresse, aus der ein ungefährer Ort abgeleitet werden kann. Eine zufällige Analysekennung entsteht erst nach Ihrer Zustimmung. Sie können diese unter Einstellungen ▸ Daten & Datenschutz widerrufen; danach werden keine neuen Ereignisse gesendet. Bereits gesendete Daten werden dadurch nicht automatisch gelöscht.

### 3.2 Zuordnung von Apple Search Ads

Nur nach Ihrer Zustimmung zur Analyse fragt Ranked über Apples AdServices einmalig die Zuordnung einer Apple-Search-Ads-Installation ab. Bei einem Anzeigenklick können Kampagne, Anzeigengruppe, Suchbegriff, Werbemotiv, Land oder Region, Klickdatum sowie Neu- oder Wiederdownload mit der zufälligen PostHog-Kennung verbunden werden. Die Werbekennung IDFA wird nicht verwendet. Der Widerruf stoppt weitere Übermittlungen.

### 3.3 Käufe (Apple und RevenueCat)

Erst wenn Sie Analyse aktivieren, teilt Ranked dieselbe zufällige App-Installations-ID mit RevenueCat, die auch PostHog verwendet. So können Aboereignisse mit Nutzungsereignissen der App verknüpft werden. Ein geschützter Server leitet eine begrenzte Auswahl an Aboereignissen und Angaben wie Produkt, Preis, Währung und Store an PostHog weiter. Name, E-Mail-Adresse, Apple-Account und Transaktions-ID werden nicht weitergeleitet. Wenn Sie Analyse ausschalten, entfernt Ranked diese ID aus RevenueCat; sobald RevenueCat die Änderung erhalten hat, werden neue Aboereignisse verworfen. Bereits übermittelte Daten werden nicht automatisch gelöscht.

Abonnements werden von **Apple** über den App Store verkauft und abgerechnet. Wir sehen Ihre
Zahlungsdaten, Ihren Apple-Account und Ihren Namen nie.

Um zu prüfen, ob Ihr Abonnement aktiv ist, verwendet die App **RevenueCat**. RevenueCat erhält den
App-Store-Kaufdatensatz zu Ihrem Abonnement — welches Produkt gekauft wurde, wann es begonnen hat
und wann es abläuft — zusammen mit technischen Standardangaben wie Ihrer iOS-Version und der
App-Version. Ihre Installation wird über eine zufällige Kennung erkannt, die RevenueCat selbst
erzeugt und auf Ihrem Gerät speichert. Wir übermitteln RevenueCat weder Ihren Namen noch Ihre E-Mail-Adresse. Die oben beschriebene zufällige App-ID ist ein Pseudonym und wird nur für Analyse verwendet, wenn Sie diese einschalten; Ranked hat keine Anmeldekonten.

Wenn Sie **Käufe wiederherstellen** antippen, fragt die App bei Apple die Käufe ab, die mit dem auf
dem Gerät angemeldeten Apple-Account getätigt wurden, und gibt das Ergebnis auf demselben Weg an
RevenueCat weiter.

### 3.4 Nachrichten für Feedback und Support (Cloudflare und CloudKit)

Wenn Sie Feedback oder eine Supportanfrage senden, übermittelt Ranked die Nachricht samt Kategorie und Herkunft an einen Cloudflare Worker. Dieser speichert die Angaben mit einem privaten Serverschlüssel in der öffentlichen Datenbank von Apple CloudKit. Für das Senden ist keine iCloud-Anmeldung erforderlich. Der Cloudflare Worker verwendet die Netzwerkadresse für eine technische Begrenzung gegen Missbrauch; weder die ursprüngliche Adresse noch ein Hash davon wird im CloudKit-Feedbackdatensatz gespeichert. Für eine Antwort ausserhalb der App können Sie gesondert in die Übermittlung Ihrer E-Mail-Adresse oder Telefonnummer einwilligen. Nachricht und Kontaktdaten gehen weder an PostHog noch an RevenueCat und sind nicht mit einem App-Konto verknüpft. Wir bearbeiten die Nachricht, um Ihre Anfrage zu beantworten, und die freiwilligen Kontaktdaten mit Ihrer Einwilligung. Für Nachrichten und Kontaktdaten ist derzeit keine feste automatische Löschfrist eingerichtet. Auskunft oder Löschung können Sie unter **dylan.schmid538@gmail.com** verlangen.

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
| Nutzungsstatistiken (§3.1) | Ihre Einwilligung; jederzeit unter Einstellungen ▸ Daten & Datenschutz widerrufbar |
| Search-Ads-Zuordnung (§3.2) | Ihre Einwilligung; jederzeit unter Einstellungen ▸ Daten & Datenschutz widerrufbar |

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

Sie können Ihre Einwilligung zur Analyse unter Einstellungen ▸ Daten & Datenschutz jederzeit ohne Begründung widerrufen. Das stoppt neue Ereignisse sofort, löscht aber nicht automatisch bereits gesendete Daten und beendet kein App-Store-Abonnement.

Ihre lokalen Trainingsdaten können Sie unter Einstellungen ▸ Daten & Datenschutz ▸ *Lokale Trainingsdaten löschen* oder durch Löschen der App entfernen. Das Abonnement verwalten und kündigen Sie getrennt in Ihrem Apple-Account.

Für Daten, die bereits an PostHog gesendet wurden, schreiben Sie an **dylan.schmid538@gmail.com**. Ranked verknüpft die zufällige Analysekennung nicht mit einem Konto. Ein ungefähres Nutzungsdatum oder Gerätemodell allein reicht möglicherweise nicht aus, um Ihr Profil zuverlässig zu finden. Wir erklären, welche Daten wir zuordnen können, und bearbeiten überprüfbare Anträge auf Auskunft, Berichtigung oder Löschung. Bitte senden Sie keine Zugangsdaten Ihres Apple-Accounts.

Sie können eine Einschränkung der Bearbeitung verlangen und sich bei einer Aufsichtsbehörde beschweren; in der Schweiz ist dies der Eidgenössische Datenschutz- und Öffentlichkeitsbeauftragte (EDÖB).

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
