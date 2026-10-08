---
title: Política de privacitat · Calisthenics Skills – Ranked
permalink: /privacy/ca/
---

> Aquesta és una traducció. En cas de discrepància, preval la [versió anglesa](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/).

# Política de privacitat · Calisthenics Skills – Ranked

**Última actualització: 2026-10-08**

Aquesta política explica quines dades recull Ranked, on van i què podeu fer al respecte.

Ranked és operada per **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Suïssa**, contacte **dylan.schmid538@gmail.com**. Ella és la responsable del tractament descrit aquí.

---

## 1. Resum

**La vostra edat, sexe, alçada i pes corporal no surten mai del dispositiu.** La fórmula del rang els fa servir al telèfon. No s'envien ni a nosaltres ni al servei d'anàlisi.

Només surten del dispositiu dues classes de dades:

1. **Estadístiques d'ús**, per saber com s'utilitza l'aplicació. Les podeu desactivar en qualsevol moment dins l'aplicació.
2. **Dades de compra**, per verificar la subscripció de l'App Store. Apple gestiona el pagament; nosaltres no en veiem mai els detalls.

Ranked no us segueix entre altres aplicacions o llocs web, no mostra publicitat i no llegeix res d'Apple Health.

---

## 2. Què es queda al dispositiu

Les dades següents es desen a la base de dades de l'aplicació al telèfon i no es transmeten mai:

- Cada entrenament, sèrie, repetició, manteniment i pes afegit que registreu
- El pla i el calendari d'entrenament, els recordatoris i les preferències
- Les mesures corporals que heu introduït (edat, sexe, alçada i pes corporal)
- Les notes d'entrenament

L'aplicació no exclou aquesta base de dades de la còpia de seguretat del dispositiu. Si feu servir iCloud Backup o una còpia a l'ordinador, les dades d'entrenament s'hi inclouen i es restauren amb la còpia, segons les condicions d'Apple, no les nostres.

En esborrar l'aplicació, tot això s'esborra del dispositiu. No ho podem recuperar perquè no ho hem tingut mai.

---

## 3. Què surt del dispositiu

### 3.1 Estadístiques d'ús (PostHog)

L'anàlisi és desactivada per defecte. Només si hi consentiu expressament durant la configuració o després a Configuració, Ranked envia a PostHog a la UE esdeveniments de configuració, avaluació inicial, canvis de rang i etapa (amb habilitat i etapa), pantalla de compra, compres i pantalles obertes. Els esdeveniments d'entrenament en directe inclouen inici, finalització o abandonament, segons transcorreguts, nombre de sèries registrades, nombre d'habilitats diferents i si era el primer entrenament acabat. No inclouen exercicis individuals, repeticions, pesos ni notes. No s'envien edat, sexe, alçada ni pes corporal. PostHog també rep dades tècniques habituals del dispositiu, iOS, l'app i l'idioma, i l'adreça IP, de la qual es pot deduir una ubicació aproximada. L'identificador aleatori d'anàlisi es crea després del consentiment. Podeu retirar-lo a Configuració ▸ Dades i privadesa; els nous enviaments s'aturen, però les dades ja enviades no s'esborren automàticament.

### 3.2 Atribució d'Apple Search Ads

Només després del consentiment per a l'anàlisi, Ranked consulta una vegada AdServices d'Apple per atribuir una instal·lació procedent d'Apple Search Ads. Si heu premut un anunci, campanya, grup, paraula clau, creativitat, país o regió, data del clic i tipus de descàrrega es poden vincular a l'identificador aleatori de PostHog. No s'utilitza l'identificador publicitari IDFA. La retirada del consentiment atura els enviaments futurs.

### 3.3 Compres (Apple i RevenueCat)

**Apple** ven i factura les subscripcions a través de l'App Store. No veiem mai les vostres dades de pagament, el vostre Compte d'Apple ni el vostre nom.

Per comprovar si la subscripció està activa, l'aplicació fa servir **RevenueCat**. RevenueCat rep el registre de compra de l'App Store —el producte comprat, quan va començar i quan venç— juntament amb informació tècnica habitual com la versió d'iOS i de l'aplicació. Identifica la instal·lació amb un identificador aleatori que genera ella mateixa i desa al dispositiu. No facilitem a RevenueCat el vostre nom, correu electrònic ni cap altra identitat; com que Ranked no té comptes, no hi ha cap identitat d'aquest tipus per facilitar.

Quan toqueu **Restaura les compres**, l'aplicació demana a Apple les compres fetes amb el Compte d'Apple amb què s'ha iniciat sessió al dispositiu i passa el resultat a RevenueCat de la mateixa manera.

---

## 4. Què no fa Ranked

- **Sense comptes.** No inicieu sessió mai. No hi ha cap perfil vostre en cap servidor.
- **Sense Apple Health.** Ranked no llegeix ni escriu a l'aplicació Salut.
- **Sense càmera, fotos, micròfon, ubicació ni contactes.** L'aplicació no demana aquests permisos.
- **Sense seguiment entre aplicacions o llocs web**, identificador publicitari, anuncis dins l'aplicació ni dades venudes o cedides a intermediaris de dades.
- **Sense servidor de notificacions push.** Els recordatoris es programen localment al telèfon; res que hi tingui relació no surt del dispositiu. Us demanem permís abans de programar-ne el primer, i els podeu desactivar quan vulgueu a la configuració d'iOS.

---

## 5. Base jurídica (RGPD i revDSG suïssa)

| Tractament | Base |
|---|---|
| Compres i verificació de la subscripció (§3.3) | Execució d'un contracte |
| Estadístiques d'ús (§3.1) | El vostre consentiment, revocable en qualsevol moment a Configuració ▸ Dades i privadesa |
| Atribució de Search Ads (§3.2) | El vostre consentiment, revocable en qualsevol moment a Configuració ▸ Dades i privadesa |

**Aquí s'apliquen dues lleis, no una.** Ranked s'opera des de Suïssa; per tant, la Llei federal suïssa de protecció de dades revisada (**revDSG**, vigent des del setembre de 2023) regeix aquest tractament. L'**RGPD** també s'aplica quan l'aplicació s'utilitza des de la Unió Europea o el Regne Unit. Si divergeixen, seguim la norma més estricta. Els residents a Suïssa tenen els mateixos drets bàsics indicats al §8 en virtut de l'article 25 i següents de la revDSG.

---

## 6. On es tracten les dades

- **PostHog** tracta les estadístiques d'ús a la Unió Europea.
- **RevenueCat, Inc.** té la seu als Estats Units i hi tracta les dades de compra descrites al §3.3.
- **Apple** tracta la compra i la petició d'atribució de Search Ads segons la seva política de privacitat, aplicable al vostre Compte d'Apple independentment d'aquesta aplicació.

---

## 7. Quant de temps les conservem

Les estadístiques d'ús es conserven durant el període de retenció de PostHog aplicable al nostre pla. No prometem un nombre fix de mesos, perquè PostHog no ens deixa establir-lo; una durada que ningú no pot complir és pitjor en una política de privacitat que no indicar-ne cap.

RevenueCat conserva els registres de compra mentre existeixen la subscripció i el seu historial, cosa necessària per verificar-la.

Tot el que hi ha al dispositiu s'hi queda fins que esborreu l'aplicació.

---

## 8. Els vostres drets

Podeu retirar en qualsevol moment el consentiment per a l'anàlisi a Configuració ▸ Dades i privadesa, sense donar cap motiu. S'aturen immediatament els esdeveniments nous, però no s'esborren automàticament les dades ja enviades ni es cancel·la la subscripció de l'App Store.

Podeu eliminar les dades d'entrenament locals a Configuració ▸ Dades i privadesa ▸ *Suprimeix les dades locals d’entrenament*, o bé eliminant l'app. La subscripció es gestiona i es cancel·la per separat al vostre compte d'Apple.

Per a les dades ja enviades a PostHog, escriviu a **dylan.schmid538@gmail.com**. Ranked no vincula l'identificador aleatori a cap compte. Una data aproximada o un model de dispositiu pot no ser suficient per trobar el perfil de manera fiable. Explicarem què podem identificar i atendrem sol·licituds verificables d'accés, rectificació o supressió. No envieu credencials del compte d'Apple.

Podeu demanar la limitació del tractament i presentar una reclamació davant l'autoritat de protecció de dades del vostre país; a Suïssa és el Comissionat Federal de Protecció de Dades i Transparència (FDPIC).

---

## 9. Menors

Ranked s'adreça a persones de **16 anys o més**. L'aplicació demana l'edat durant la configuració perquè la fórmula del rang en depèn, i no s'adreça a persones més joves. No recopilem conscientment dades de menors de 16 anys.

---

## 10. Canvis

La versió publicada en aquesta adreça és la vigent; la data de dalt indica quan es va modificar per darrera vegada. Les versions anteriors continuen visibles a l'historial públic del repositori des del qual es publiquen aquestes pàgines, perquè pugueu veure què va canviar i quan.

---
