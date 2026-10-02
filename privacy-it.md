---
title: Informativa sulla privacy
permalink: /privacy/it/
---

> *Questa è una traduzione. In caso di divergenze, prevale la [versione inglese](../).*

# Informativa sulla privacy · Calisthenics Skills – Ranked

**Ultimo aggiornamento: 2026-10-02**

Questa informativa descrive quali dati Ranked raccoglie, dove vanno e quali scelte puoi fare. È stata redatta sulla base del codice effettivo dell'app, senza usare un modello: se qualcosa qui non è corretto, occorre verificare il codice.

Ranked è gestita da **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Svizzera**, contatto **dylan.schmid538@gmail.com**. È la titolare del trattamento descritto qui.

---

## 1. In breve

**Età, sesso, altezza e peso corporeo non lasciano mai il dispositivo.** La formula del rango li usa sul telefono. Non sono inviati né a noi né al servizio di analisi.

Solo due categorie di dati lasciano il dispositivo:

1. **Statistiche d'uso anonime**, per capire come viene utilizzata l'app. Puoi disattivarle nell'app in qualsiasi momento.
2. **Dati relativi agli acquisti**, per verificare l'abbonamento all'App Store. Apple gestisce il pagamento; noi non vediamo mai i tuoi dati di pagamento.

Ranked non ti traccia su altre app o siti web, non mostra pubblicità e non legge dati da Apple Salute.

---

## 2. Cosa rimane sul dispositivo

I seguenti dati sono conservati nel database dell'app sul telefono e non vengono mai trasmessi:

- Ogni allenamento, serie, ripetizione, tenuta e peso aggiuntivo che registri
- Il piano di allenamento, il calendario, i promemoria e le preferenze
- Le misure corporee inserite (età, sesso, altezza, peso corporeo)
- Le note sugli allenamenti

L'app non esclude questo database dal backup del dispositivo. Se usi Backup iCloud o un backup sul computer, i dati degli allenamenti ne fanno parte e vengono ripristinati insieme al backup, secondo le condizioni di Apple, non le nostre.

Eliminando l'app, elimini tutti questi dati dal dispositivo. Non possiamo recuperarli, perché non li abbiamo mai ricevuti.

---

## 3. Cosa lascia il dispositivo

### 3.1 Statistiche d'uso (PostHog)

Usiamo **PostHog**, ospitato nell'**Unione europea**, per capire come viene utilizzata l'app. L'app gli invia un elenco definito di eventi:

- quale passaggio della configurazione hai raggiunto, completato o dal quale sei tornato indietro, e quanto tempo ha richiesto ciascuno;
- il risultato della valutazione iniziale: quante linee di abilità e fasi hai dichiarato, quale abilità hai scelto come obiettivo, il rango iniziale e il rango di ciascuna delle sei regioni corporee;
- quando la schermata di acquisto è stata mostrata o chiusa e quando un acquisto è stato avviato, completato o ripristinato, con il prodotto e l'offerta interessati; quando l'app rileva successivamente un periodo di prova attivo o un periodo di abbonamento a pagamento, con il prodotto e l'indicazione se si tratta di un acquisto nell'ambiente di test (non è il registro di ogni addebito e non viene inviato mentre l'app è chiusa);
- quando il tuo rango cambia e quale abilità provoca il cambiamento;
- quando completi una fase: quale abilità, quale fase e se ciò deriva da una serie registrata, un allenamento inserito in seguito o una dichiarazione manuale;
- quali schermate apri e quando termina un allenamento. L'evento di fine allenamento non contiene dettagli: né esercizi, né serie, né numeri.

Il software PostHog integrato nell'app aggiunge a ogni evento informazioni tecniche standard, come modello del dispositivo, versione di iOS e dell'app, lingua e fuso orario, e registra quando l'app viene aperta o mandata in background. Come ogni servizio Internet, PostHog riceve l'indirizzo IP della richiesta e può ricavarne una posizione approssimativa (Paese o città).

**Cosa non contiene:** nome, indirizzo email (l'app non lo chiede), identificativo di account (non esiste), età, sesso, altezza, peso corporeo o contenuti degli allenamenti.

**Come vieni identificato:** PostHog genera un identificativo casuale al primo avvio dell'app e lo memorizza sul dispositivo. Gli eventi vengono raggruppati sotto tale identificativo. L'app non comunica mai a PostHog chi sei e non dispone di account o email da comunicare.

**Come disattivarle:** Impostazioni ▸ Privacy ▸ *Condividi dati d'uso anonimi*. La disattivazione impedisce all'app di inviare eventi da quel momento. L'impostazione rimane sul dispositivo anche dopo gli aggiornamenti dell'app.

### 3.2 Attribuzione Apple Search Ads

Se hai installato Ranked dopo aver toccato un annuncio Apple Search Ads, al primo avvio l'app chiede una sola volta ad Apple da dove proviene l'installazione. Apple risponde con campagna, gruppo di annunci, parola chiave e contenuto creativo dell'annuncio, Paese o regione e data del clic, e indica se si tratta di un primo download o di un nuovo download. L'app associa questi valori all'identificativo anonimo di PostHog descritto al §3.1, per raggruppare gli eventi successivi in base all'annuncio che ti ha portato qui.

Viene usato il framework **AdServices** di Apple, che non utilizza l'identificativo pubblicitario (IDFA) e che Apple non considera tracciamento: pertanto non compare una richiesta di autorizzazione al tracciamento. Se non provieni da un annuncio, Apple lo segnala e non viene associato nulla. Disattivare le statistiche d'uso (§3.1) interrompe anche questa attribuzione.

### 3.3 Acquisti (Apple e RevenueCat)

Gli abbonamenti sono venduti e fatturati da **Apple** tramite l'App Store. Non vediamo mai i tuoi dati di pagamento, il tuo Apple Account o il tuo nome.

Per verificare se l'abbonamento è attivo, l'app usa **RevenueCat**. RevenueCat riceve la registrazione dell'acquisto dell'App Store relativa all'abbonamento — prodotto acquistato, data di inizio e di scadenza — insieme a informazioni tecniche standard, come la versione di iOS e dell'app. Riconosce l'installazione tramite un identificativo casuale che genera e memorizza sul dispositivo. Non forniamo a RevenueCat nome, indirizzo email o altra identità e, poiché Ranked non ha account, non ne esiste una da fornire.

Quando tocchi **Ripristina acquisti**, l'app chiede ad Apple gli acquisti effettuati con l'Apple Account connesso al dispositivo e ne trasmette l'esito a RevenueCat allo stesso modo.

---

## 4. Cosa Ranked non fa

- **Nessun account.** Non devi effettuare l'accesso. Non esiste un tuo profilo su un server.
- **Nessun accesso ad Apple Salute.** Ranked non legge né scrive dati nell'app Salute.
- **Nessuna fotocamera, foto, microfono, posizione o contatto.** L'app non richiede queste autorizzazioni.
- **Nessun tracciamento tra app o siti web**, identificativo pubblicitario, pubblicità nell'app o vendita o cessione di dati a intermediari di dati.
- **Nessun server per le notifiche push.** I promemoria di Ranked sono programmati localmente sul telefono; nulla che li riguarda lascia il dispositivo. Ti viene chiesto il permesso prima che sia programmato il primo, e puoi disattivarli in qualsiasi momento nelle impostazioni di iOS.

---

## 5. Base giuridica (GDPR e revDSG svizzera)

| Trattamento | Base giuridica |
|---|---|
| Acquisti e verifica dell'abbonamento (§3.3) | Esecuzione di un contratto |
| Statistiche d'uso (§3.1) | Interesse legittimo a comprendere e migliorare l'app; puoi opporti in qualsiasi momento disattivandole, vedi §8 |
| Attribuzione Search Ads (§3.2) | Interesse legittimo a conoscere l'efficacia degli annunci; opposizione come sopra |

**Si applicano due leggi, non una sola.** Ranked è gestita dalla Svizzera, quindi il trattamento è disciplinato dalla legge federale svizzera riveduta sulla protezione dei dati (**revDSG**, in vigore da settembre 2023). Il **GDPR** si applica inoltre quando l'app è usata dall'Unione europea o dal Regno Unito. In caso di differenze, seguiamo la norma più rigorosa. I residenti in Svizzera godono degli stessi diritti fondamentali elencati al §8 ai sensi dell'articolo 25 e seguenti della revDSG.

---

## 6. Dove sono trattati i dati

- **PostHog** tratta le statistiche d'uso nell'Unione europea.
- **RevenueCat, Inc.** ha sede negli Stati Uniti e vi tratta i dati di acquisto descritti al §3.3.
- **Apple** tratta l'acquisto e la richiesta di attribuzione Search Ads secondo la propria informativa sulla privacy, applicabile al tuo Apple Account indipendentemente da questa app.

---

## 7. Per quanto tempo sono conservati

Le statistiche d'uso sono conservate per il periodo di conservazione previsto dal nostro piano PostHog. Non promettiamo un numero fisso di mesi, perché PostHog non ci consente di impostarlo: indicare un termine impossibile da rispettare sarebbe peggio che non indicarne uno.

RevenueCat conserva le registrazioni degli acquisti finché esistono l'abbonamento e la sua cronologia, come richiesto per verificare un abbonamento.

I dati sul dispositivo rimangono lì finché non elimini l'app.

---

## 8. I tuoi diritti

Puoi, in qualsiasi momento:

- **Disattivare le statistiche d'uso** in Impostazioni ▸ Privacy. È il tuo diritto di opposizione e, quando il trattamento si basa sul consenso, di revocarlo; la scelta ha effetto immediato e non richiede motivazioni.
- **Eliminare i tuoi dati.** Poiché Ranked non conserva dati che ti riguardano su un server, eliminando l'app rimuovi tutto ciò che essa memorizza.
- **Chiedere la cancellazione del tuo profilo di analisi anonimo.** Non possiamo trovarlo tramite il nome, perché non ne ha uno; se ci scrivi indicando la data approssimativa del primo utilizzo e il dispositivo usato, lo cercheremo manualmente e lo cancelleremo.
- **Chiedere una copia** dei dati detenuti da un servizio sotto il tuo identificativo, chiederne la **rettifica** o la **limitazione** del trattamento mentre esaminiamo la richiesta.
- **Presentare reclamo a un'autorità di controllo** nel tuo Paese; in Svizzera, all'Incaricato federale della protezione dei dati e della trasparenza (IFPDT).

Per esercitare questi diritti scrivi a **dylan.schmid538@gmail.com**.

---

## 9. Minori

Ranked è destinata a persone di **almeno 16 anni**. L'app chiede la tua età durante la configurazione perché la formula del rango ne dipende e non è rivolta a persone più giovani. Non raccogliamo consapevolmente dati di minori di 16 anni.

---

## 10. Modifiche

La versione pubblicata a questo indirizzo è quella in vigore; la data in alto indica l'ultimo aggiornamento. Le versioni precedenti restano visibili nella cronologia pubblica del repository da cui queste pagine vengono pubblicate, così puoi vedere cosa è cambiato e quando.

---

> **⚠️ Non è una consulenza legale.** Questo documento è stato redatto da un ingegnere sulla base del codice sorgente dell'app, non da un avvocato. Descrive il sistema alla data sopra indicata: ogni affermazione è stata verificata rispetto ai dati effettivamente inviati dall'app. **Non è stato esaminato** per la conformità al GDPR, alla revDSG svizzera, al CCPA o ad altre normative. La pubblicazione soddisfa i requisiti di Apple, ma non garantisce la conformità. Fallo esaminare da un avvocato quando l'app inizierà a generare entrate.
