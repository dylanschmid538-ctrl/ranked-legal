---
title: Política de privacitat · Calisthenics Skills – Ranked
permalink: /privacy/ca/
---

> Aquesta és una traducció. En cas de discrepància, preval la [versió anglesa](https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/).

# Política de privacitat · Calisthenics Skills – Ranked

**Última actualització: 2026-10-02**

Aquesta política explica quines dades recull Ranked, on van i què podeu fer al respecte. S'ha redactat a partir del codi real de l'aplicació, no d'una plantilla; si alguna cosa és incorrecta, cal comprovar el codi.

Ranked és operada per **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Suïssa**, contacte **dylan.schmid538@gmail.com**. Ella és la responsable del tractament descrit aquí.

---

## 1. Resum

**La vostra edat, sexe, alçada i pes corporal no surten mai del dispositiu.** La fórmula del rang els fa servir al telèfon. No s'envien ni a nosaltres ni al servei d'anàlisi.

Només surten del dispositiu dues classes de dades:

1. **Estadístiques anònimes d'ús**, per saber com s'utilitza l'aplicació. Les podeu desactivar en qualsevol moment dins l'aplicació.
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

Fem servir **PostHog**, allotjat a la **Unió Europea**, per entendre com s'utilitza l'aplicació. L'aplicació li envia una llista fixa d'esdeveniments:

- a quin pas de configuració heu arribat, quin heu completat o de quin heu tornat enrere, i quant ha durat cadascun;
- el resultat de l'avaluació inicial: quantes línies d'habilitats i etapes heu indicat que teniu assolides, quina habilitat heu triat com a objectiu, el rang inicial i el rang de cadascuna de les sis regions corporals;
- quan s'ha mostrat o tancat la pantalla de compra i quan s'ha iniciat, completat o restaurat una compra, amb el producte i l'oferta corresponents; quan l'aplicació detecta més endavant un període de prova o de subscripció de pagament actiu, amb el producte i si es tracta d'una compra de prova (no és un registre de tots els càrrecs i no s'envia mentre l'aplicació està tancada);
- quan ha canviat el vostre rang i quina habilitat n'ha estat la causa;
- quan heu superat una etapa: quina habilitat i etapa, i si prové d'una sèrie registrada, d'un entrenament afegit posteriorment o d'una indicació manual;
- quines pantalles obriu i quan acaba un entrenament. L'esdeveniment de finalització no conté detalls: ni exercicis, ni sèries, ni xifres.

El programari de PostHog dins l'aplicació també afegeix informació tècnica estàndard a cada esdeveniment, com el model del dispositiu, les versions d'iOS i de l'aplicació, l'idioma i la zona horària, i registra quan s'obre l'aplicació o passa a segon pla. Com qualsevol servei d'internet, PostHog rep l'adreça IP de la petició; en pot deduir una ubicació aproximada (país o ciutat).

**Què no hi ha:** ni nom, ni adreça electrònica (l'aplicació no la demana mai), ni identificador de compte (no n'hi ha), ni edat, sexe, alçada, pes corporal o contingut dels entrenaments.

**Com se us identifica:** PostHog genera un identificador aleatori quan l'aplicació s'executa per primer cop i el desa al dispositiu. Tots els esdeveniments s'agrupen sota aquest identificador. L'aplicació no diu mai a PostHog qui sou, ni té cap compte o correu electrònic que li pugui comunicar.

**Com desactivar-ho:** Configuració ▸ Privacitat ▸ *Comparteix dades d'ús anònimes*. Desactivar-ho atura l'enviament d'esdeveniments des d'aquell moment. La configuració es desa al dispositiu i es manté després de les actualitzacions.

### 3.2 Atribució d'Apple Search Ads

Si heu instal·lat Ranked després de tocar un anunci d'Apple Search Ads, la primera vegada que s'obre l'aplicació pregunta a Apple, una sola vegada, d'on ha vingut la instal·lació. Apple respon amb la campanya, el grup d'anuncis, la paraula clau i el conjunt creatiu de l'anunci, el país o regió i la data del clic, i si és una descàrrega nova o una descàrrega repetida. L'aplicació adjunta aquests valors a l'identificador anònim de PostHog descrit al §3.1, de manera que els esdeveniments posteriors es puguin agrupar segons l'anunci que us hi va portar.

Això fa servir el framework **AdServices** d'Apple, que no implica l'identificador publicitari (IDFA) i que Apple no considera seguiment; per tant, no apareix cap diàleg de permís de seguiment. Si no heu arribat a través d'un anunci, Apple ho indica i no s'hi adjunta res més. Desactivar les estadístiques d'ús (§3.1) també ho atura.

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
| Estadístiques d'ús (§3.1) | Interès legítim a entendre i millorar l'aplicació; us hi podeu oposar en qualsevol moment desactivant-les, vegeu §8 |
| Atribució de Search Ads (§3.2) | Interès legítim a saber quina publicitat funciona; oposició com s'indica més amunt |

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

En qualsevol moment podeu:

- **Desactivar les estadístiques d'ús** a Configuració ▸ Privacitat. És el vostre dret d'oposició i, quan el tractament es basa en el consentiment, de retirar-lo. Té efecte immediat i no cal donar cap motiu.
- **Esborrar les vostres dades.** Com que Ranked no conserva res de vosaltres en un servidor, esborrar l'aplicació elimina tot el que ella mateixa desa.
- **Demanar-nos que eliminem el vostre perfil analític anònim.** No el podem trobar pel nom, perquè no en té; si ens escriviu amb la data aproximada del primer ús i el dispositiu que vau utilitzar, el localitzarem manualment i l'eliminarem.
- **Sol·licitar una còpia** de les dades que un servei conserva sota el vostre identificador, demanar-ne la **rectificació** o **limitar-ne** el tractament mentre s'examina una sol·licitud.
- **Presentar una reclamació davant l'autoritat de control** del vostre país; a Suïssa, el Comissionat Federal de Protecció de Dades i Informació (FDPIC).

Escriviu a **dylan.schmid538@gmail.com** per a qualsevol d'aquestes qüestions.

---

## 9. Menors

Ranked s'adreça a persones de **16 anys o més**. L'aplicació demana l'edat durant la configuració perquè la fórmula del rang en depèn, i no s'adreça a persones més joves. No recopilem conscientment dades de menors de 16 anys.

---

## 10. Canvis

La versió publicada en aquesta adreça és la vigent; la data de dalt indica quan es va modificar per darrera vegada. Les versions anteriors continuen visibles a l'historial públic del repositori des del qual es publiquen aquestes pàgines, perquè pugueu veure què va canviar i quan.

---

> **⚠️ No és assessorament jurídic.** Aquest document l'ha redactat un enginyer a partir del codi font de l'aplicació, no un advocat. Descriu el sistema amb precisió a la data indicada; cada afirmació s'ha contrastat amb allò que l'aplicació envia realment. **No** s'ha revisat el compliment de l'RGPD, la revDSG suïssa, la CCPA ni cap altre règim. Publicar-lo satisfà Apple, però no garanteix el compliment legal. Feu-lo revisar per un advocat quan l'aplicació generi ingressos.
