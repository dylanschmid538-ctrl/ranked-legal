---
title: Datenschutzerklärung · Calisthenics Skills – Ranked
permalink: /privacy/de/
---

> *Dies ist eine Übersetzung. Im Falle von Abweichungen ist die englische Fassung unter
> https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/ massgebend.*

# Datenschutzerklärung · Calisthenics Skills – Ranked

**Zuletzt aktualisiert: 23. August 2026**

Diese Erklärung beschreibt, was Ranked erhebt, wohin diese Daten gelangen und was Sie dagegen tun
können. Sie wurde anhand des tatsächlichen Codes und des Datenbankschemas der App verfasst, nicht
anhand einer Vorlage — wenn hier etwas falsch ist, ist der Code massgebend.

Ranked wird betrieben von **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Schweiz**, Kontakt **dylan.schmid538@gmail.com**.

---

## 1. Die Kurzfassung

Fast alles, was Ranked über Ihr Training weiss, bleibt auf Ihrem Telefon. Ihr Trainingsverlauf, Ihr
Fortschritt in jedem Skill, Ihr Rang und Ihre Körperkarte werden lokal gespeichert und niemals
hochgeladen.

Vier Dinge verlassen Ihr Gerät: Ihre Anmelde-Identität, ein kleines Profil für die Bestenlisten,
Aufzeichnungen darüber, dass Sie einen verifizierten Versuch absolviert haben, und anonyme
Nutzungsanalysen. Jedes davon wird unten erläutert.

**Ihre Videos von verifizierten Versuchen verlassen Ihr Gerät nie.** Es wird nur ein Fingerabdruck
der Datei übermittelt.

---

## 2. Was auf Ihrem Gerät bleibt

Lokal in der app-eigenen Datenbank gespeichert und niemals übertragen:

- Jedes Workout, jeder Satz, jede Wiederholung, jeder Halt und jedes Zusatzgewicht, das Sie erfassen
- Ihr Fortschritt in jedem Skill und jeder Stufe sowie Ihr Rangverlauf
- Ihr Trainingsplan, Ihr Zeitplan und Ihre Einstellungen
- Ihre Körpermasse, wie Sie sie eingegeben haben (Alter, Geschlecht, Grösse, Körpergewicht) — eine
  Kopie einiger dieser Angaben wird zusätzlich an den Bestenlisten-Dienst gesendet, siehe §3.2
- **Die Videodateien aus verifizierten Versuchen.** Diese werden in den privaten Speicher der App
  geschrieben. Sie werden nicht hochgeladen, nicht auf unseren Servern gesichert und sind für uns
  nicht zugänglich.

Wenn Sie die App löschen, wird all dies gelöscht. Wir können es nicht wiederherstellen.

---

## 3. Was Ihr Gerät verlässt

### 3.1 Ihr Konto
Wenn Sie sich mit Apple oder Google anmelden, erhalten und speichern wir eine Nutzerkennung und, je
nachdem, was Sie bei der Anmeldung erlauben, eine E-Mail-Adresse. Dies wird von **Supabase**
abgewickelt, wo unsere Datenbank und die Authentifizierung gehostet werden.

Wenn Sie sich mit Apple anmelden, speichern wir zusätzlich das Refresh-Token, das Apple uns in
diesem Moment übergibt. Es hat nur einen einzigen Zweck: Beim Löschen Ihres Kontos wird dadurch
auch der Zugriff von Ranked auf Ihre Apple-ID widerrufen, wie Apple es verlangt. Für Konten, deren
letzte Anmeldung vor Einführung dieser Erfassung stattfand, ist kein Token gespeichert — die
Löschung überspringt den Widerruf dann einfach.

### 3.2 Ihr Bestenlisten-Profil
Um Sie auf einer Bestenliste zu platzieren und Sie mit Personen ähnlichen Körperbaus zu
vergleichen, wird Folgendes auf unserem Server gespeichert:

- ein zufällig erzeugter **Freundescode**
- Ihr **Alter**, Ihr **Geschlecht** und Ihr **Körpergewicht**
- das Datum, an dem Ihr Profil erstellt wurde

**Hinweis zur Sichtbarkeit:** Jede angemeldete Ranked-Nutzerin und jeder angemeldete Ranked-Nutzer
kann ein Profil über dessen Freundescode aufrufen. Genau das ist der Zweck eines Freundescodes — er
ist dazu da, weitergegeben zu werden. Geben Sie Ihren nicht an Personen weiter, die Ihren Eintrag
nicht sehen sollen. Was andere Nutzerinnen und Nutzer sehen können, ist Ihr Freundescode und Ihre
Position auf einer Bestenliste — sonst nichts. Ihr Alter, Ihr Geschlecht und Ihr Körpergewicht
werden für den Vergleich auf dem Server verwendet und anderen Nutzerinnen und Nutzern niemals
angezeigt oder zum Download bereitgestellt.

Ihre **Grösse** wird nicht übermittelt. Ihr Trainingsverlauf wird nicht übermittelt.

### 3.3 Verifizierte Versuche
Wenn Sie einen verifizierten Versuch aufzeichnen, speichern wir: Ihre Nutzer-ID, für welchen Skill
und welche Stufe der Versuch war, einen **kryptografischen Hash der Videodatei** und den Zeitpunkt
der Aufnahme.

Der Hash ist ein Fingerabdruck. Er lässt sich nicht in das Video zurückverwandeln. Er existiert,
damit ein Versuch einer bestimmten Aufnahme zugeordnet werden kann, ohne dass diese Aufnahme jemals
Ihr Telefon verlässt.

### 3.4 Freunde
Wenn Sie jemanden über dessen Freundescode hinzufügen, speichern wir die Verbindung zwischen Ihrem
Konto und dem anderen Konto sowie Ihre Mitgliedschaft in allfälligen Freundesgruppen.

### 3.5 Nutzungsanalyse
Wir verwenden **PostHog**, gehostet in der **Europäischen Union**, um zu verstehen, wie die App
genutzt wird. Wir erfassen Ereignisse wie zum Beispiel, welchen Onboarding-Schritt Sie erreicht
haben, wann ein Workout abgeschlossen wurde, wann sich ein Rang geändert hat und ob ein
Kaufbildschirm angezeigt oder weggeklickt wurde.

Diese Ereignisse enthalten Ihren Rang und Ihren Fortschritt in der App. Sie enthalten **nicht**
Ihren Namen, Ihre E-Mail-Adresse, Ihre Grösse oder die Inhalte Ihrer Workouts.

---

## 4. Käufe

Abonnements werden von **Apple** abgewickelt. Wir sehen Ihre Zahlungsdaten nie. **RevenueCat**
verwaltet Ihren Abonnementstatus in unserem Auftrag und erhält eine pseudonyme Kennung sowie Ihren
Abonnementstatus. Der Kaufbildschirm selbst ist Teil der App; kein Dritter entscheidet, welcher
Ihnen angezeigt wird.

---

## 5. Kamera und Mikrofon

Ranked fragt für eine einzige Funktion nach Zugriff auf Kamera und Mikrofon: die Aufzeichnung eines
verifizierten Versuchs. Die Aufnahme wird auf Ihrem Gerät gespeichert. Sie wird niemals hochgeladen.
Wenn Sie den Zugriff ablehnen, funktioniert jeder andere Teil der App weiterhin.

---

## 6. Gesundheitsdaten

Ranked liest **keine** Daten aus Apple Health und schreibt **keine** Daten dorthin.

Ihr Alter, Ihr Geschlecht und Ihr Körpergewicht sind gesundheitsnahe Daten und können nach der
DSGVO als Gesundheitsdaten gelten. Wir erheben sie zu einem einzigen Zweck — die Rangformel
normalisiert die Leistung nach Körperbau, damit ein 95-kg-Athlet und ein 60-kg-Athlet, die denselben
Hebel halten, nicht so bewertet werden, als hätten sie dasselbe geleistet — und wir senden davon
nur das Minimum an den Server, das der Vergleich auf der Bestenliste benötigt.

---

## 7. Rechtsgrundlage (DSGVO und Schweizer revDSG)

| Was | Grundlage |
|---|---|
| Konto und Anmeldung | Vertragserfüllung — die App setzt ein Konto voraus |
| Alter, Geschlecht und Körpergewicht | Vertragserfüllung — der Rang wird anhand dieser Angaben normalisiert und kann ohne sie nicht berechnet werden |
| Freundescode, Freundesgruppen | Vertragserfüllung — die Funktion ist der Grund, weshalb die Daten überhaupt bestehen |
| Aufzeichnungen verifizierter Versuche und der Bestenlisten-Eintrag, den jede von ihnen erzeugt | Einwilligung, erteilt durch die bewusste Handlung der Aufzeichnung eines Versuchs. Sie widerrufen sie, indem Sie den Versuch auf der Seite der Stufe entfernen, wodurch der Eintrag gelöscht wird — siehe §9 |
| Käufe | Vertragserfüllung |
| Analyse | Berechtigtes Interesse an der Verbesserung der App; Sie können jederzeit in den Einstellungen Widerspruch einlegen, siehe §9 |

**Hier gelten zwei Gesetze, nicht eines.** Ranked wird aus der Schweiz betrieben, daher gilt für
diese Verarbeitung das revidierte Schweizer Bundesgesetz über den Datenschutz (**revDSG**, in Kraft
seit September 2023). Die **DSGVO** gilt zusätzlich überall dort, wo die App aus der Europäischen
Union oder dem Vereinigten Königreich genutzt wird. Wo die beiden voneinander abweichen, folgen wir
dem strengeren. Personen mit Wohnsitz in der Schweiz haben dieselben Kernrechte, die in §9
aufgeführt sind — Auskunft, Berichtigung, Löschung, Datenübertragbarkeit und Widerspruch — nach
Artikel 25 ff. revDSG.

---

## 8. Wie lange wir die Daten aufbewahren

Konto, Profil, Freunde und Aufzeichnungen verifizierter Versuche werden aufbewahrt, bis Sie Ihr
Konto löschen. Das Löschen des Kontos entfernt sie.

Analyse-Ereignisse werden so lange aufbewahrt, wie die Aufbewahrungsfrist von PostHog für unseren
Tarif gilt. **Das Löschen Ihres Kontos löscht sie nicht**, und wir sagen das ausdrücklich, statt
etwas anderes anzudeuten: Das Analyse-Profil ist nicht mit Ihrem Konto verknüpft — es verwendet
eine separate, von der App erzeugte Kennung — deshalb gibt es keine Verbindung, über die wir es
finden und entfernen könnten. Was es enthält, ist in §3.5 aufgeführt: Nutzungsereignisse, Ihren
Rang sowie das Alter, das Geschlecht und das Körpergewicht, die Sie eingegeben haben. Es enthält
keinen Namen, keine E-Mail-Adresse und keine Konto-ID.

Wenn Sie möchten, dass auch dieses Profil entfernt wird, schreiben Sie uns mit dem ungefähren Datum,
an dem Sie die App erstmals genutzt haben, und wir werden es von Hand suchen und löschen.

---

## 9. Ihre Rechte

Sie können jederzeit:

- **Ihr Konto löschen**, in den Einstellungen der App. Damit werden Ihr serverseitiges Profil, Ihre
  Freundesverbindungen und Ihre Aufzeichnungen verifizierter Versuche gelöscht. Sofern für Ihr
  Konto ein Apple-Refresh-Token gespeichert ist (siehe §3.1), wird dadurch auch der Zugriff von
  Ranked auf Ihre Apple-ID widerrufen. Daten, die nur auf Ihrem Gerät gespeichert sind, werden
  durch das Löschen der App entfernt.
- **Einen verifizierten Versuch zurückziehen**, auf der Seite der Stufe in der App. Das Entfernen
  des Versuchs löscht die Aufzeichnung und den dadurch erzeugten Bestenlisten-Eintrag und nimmt
  die durch die Aufzeichnung erteilte Einwilligung zurück. Durch den Widerruf wird die
  Rechtmässigkeit der aufgrund der Einwilligung bis zum Widerruf erfolgten Verarbeitung nicht
  berührt.
- **Eine Kopie anfordern** der Daten, die wir über Sie gespeichert haben (Recht auf Auskunft), oder
  uns bitten, diese zu berichtigen.
- **Der Analyse widersprechen**, mit dem Schalter in den Einstellungen oder schriftlich an uns.
- **Bei einer Aufsichtsbehörde** in Ihrem Land **Beschwerde einreichen**.

Schreiben Sie für all dies an **dylan.schmid538@gmail.com**.

---

## 10. Kinder

Ranked richtet sich nicht an Kinder unter 13 Jahren, und wir erheben deren Daten nicht wissentlich.

---

## 11. Änderungen

Wenn sich diese Erklärung wesentlich ändert, wird die App Sie informieren, bevor die Änderung wirksam
wird.

---

> **⚠️ Keine Rechtsberatung.** Dieses Dokument wurde von einem Entwickler anhand des Quellcodes und
> des Datenbankschemas der App verfasst, nicht von einer Juristin oder einem Juristen. Es
> beschreibt das System zum oben genannten Datum zutreffend — jede Aussage darin wurde daran
> geprüft, was die App tatsächlich sendet. Es wurde **nicht** auf die Vereinbarkeit mit der DSGVO,
> dem Schweizer revDSG, dem CCPA oder einer anderen Regelung geprüft. Die Veröffentlichung genügt
> Apple; sie macht Sie nicht rechtskonform. Lassen Sie es von einer Anwältin oder einem Anwalt
> lesen, sobald die App Geld einbringt.
