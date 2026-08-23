---
title: Politique de confidentialité
permalink: /privacy/fr/
---

*Ceci est une traduction. En cas de divergence, la version anglaise disponible à l'adresse https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/ fait foi.*

# Politique de confidentialité · Calisthenics Skills – Ranked

**Dernière mise à jour : 18 août 2026**

La présente politique décrit ce que Ranked collecte, où ces données sont transmises et ce que vous
pouvez faire à ce sujet. Elle a été rédigée à partir du code source et du schéma de base de données
réels de l'application, et non à partir d'un modèle — si quelque chose y est inexact, c'est le code
qu'il faut vérifier.

Ranked est exploitée par **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Suisse**, contact **dylan.schmid538@gmail.com**.

---

## 1. En bref

Presque tout ce que Ranked sait de votre entraînement reste sur votre téléphone. Votre historique
d'entraînement, votre progression dans chaque compétence, votre rang et votre carte corporelle sont
enregistrés localement et ne sont jamais transmis.

Quatre éléments quittent votre appareil : votre identité de connexion, un profil réduit utilisé pour
les classements, l'enregistrement du fait que vous avez réalisé une tentative vérifiée, et des
statistiques d'utilisation anonymes. Chacun est expliqué ci-dessous.

**Les vidéos de vos Tentatives vérifiées ne quittent jamais votre appareil.** Seule une empreinte du
fichier est transmise.

---

## 2. Ce qui reste sur votre appareil

Enregistré localement dans la base de données propre à l'application et jamais transmis :

- Chaque séance, série, répétition, maintien et charge additionnelle que vous enregistrez
- Votre progression dans chaque compétence et chaque palier, ainsi que l'historique de votre rang
- Votre plan d'entraînement, votre calendrier et vos préférences
- Vos mesures corporelles telles que vous les avez saisies (âge, sexe, taille, poids corporel) — une
  copie de certaines d'entre elles est également transmise au service de classement, voir §3.2
- **Les fichiers vidéo des Tentatives vérifiées.** Ils sont écrits dans l'espace de stockage privé de
  l'application. Ils ne sont pas transmis, ne sont pas sauvegardés sur nos serveurs et ne nous sont
  pas accessibles.

La suppression de l'application supprime l'ensemble de ces données. Nous ne pouvons pas les
récupérer.

---

## 3. Ce qui quitte votre appareil

### 3.1 Votre compte
Lorsque vous vous connectez avec Apple ou Google, nous recevons et conservons un identifiant
d'utilisateur et, selon ce que vous autorisez lors de la connexion, une adresse e-mail. Ce
traitement est assuré par **Supabase**, qui héberge notre base de données et notre authentification.

Lorsque vous vous connectez avec Apple, nous conservons également le jeton d'actualisation (refresh
token) qu'Apple nous remet à ce moment-là. Il n'a qu'une seule finalité : la suppression de votre
compte révoque également l'accès de Ranked à votre identifiant Apple, comme Apple l'exige. Pour les
comptes dont la dernière connexion est antérieure à la mise en place de cette collecte, aucun jeton
n'est conservé — la suppression omet alors simplement l'étape de révocation.

### 3.2 Votre profil de classement
Afin de vous positionner dans un classement et de vous comparer à des personnes de gabarit
similaire, les éléments suivants sont conservés sur notre serveur :

- un **code ami** généré aléatoirement
- votre **âge**, votre **sexe** et votre **poids corporel**
- la date de création de votre profil

**Remarque sur la visibilité :** tout utilisateur de Ranked connecté peut consulter un profil à
partir de son code ami. C'est précisément la fonction d'un code ami : il existe pour être
communiqué à quelqu'un. Ne partagez pas le vôtre avec une personne dont vous ne souhaiteriez pas
qu'elle voie votre inscription. Ce que les autres utilisateurs peuvent voir, c'est votre code ami et
votre position dans un classement — rien d'autre. Votre âge, votre sexe et votre poids corporel sont
utilisés pour la comparaison sur le serveur et ne sont jamais montrés aux autres utilisateurs ni
téléchargeables par eux.

Votre **taille** n'est pas transmise. Votre historique d'entraînement n'est pas transmis.

### 3.3 Tentatives vérifiées
Lorsque vous enregistrez une Tentative vérifiée, nous conservons : votre identifiant d'utilisateur,
la compétence et le palier concernés par la tentative, une **empreinte cryptographique (hash) du
fichier vidéo** et l'heure de l'enregistrement.

L'empreinte est une signature. Elle ne peut pas être reconvertie en vidéo. Elle existe pour qu'une
tentative puisse être rattachée à un enregistrement précis sans que cet enregistrement ne quitte
jamais votre téléphone.

### 3.4 Amis
Si vous ajoutez une personne au moyen de son code ami, nous conservons le lien entre votre compte et
le sien, ainsi que votre appartenance à d'éventuels groupes d'amis.

### 3.5 Statistiques d'utilisation
Nous utilisons **PostHog**, hébergé dans l'**Union européenne**, pour comprendre comment
l'application est utilisée. Nous enregistrons des événements tels que l'étape d'intégration
atteinte, l'achèvement d'une séance, le changement d'un rang, ainsi que l'affichage ou la fermeture
d'un écran d'achat.

Ces événements comportent votre rang et votre progression dans l'application. Ils ne comportent
**pas** votre nom, votre e-mail, votre taille, ni le contenu de vos séances.

---

## 4. Achats

Les abonnements sont traités par **Apple**. Nous ne voyons jamais vos données de paiement.
**RevenueCat** gère l'état de votre abonnement pour notre compte et reçoit un identifiant
pseudonyme ainsi que l'état de votre abonnement. L'écran d'achat lui-même fait partie de
l'application ; aucun tiers ne décide de celui qui vous est présenté.

---

## 5. Caméra et microphone

Ranked demande l'accès à la caméra et au microphone pour une seule fonctionnalité :
l'enregistrement d'une Tentative vérifiée. L'enregistrement est sauvegardé sur votre appareil. Il
n'est jamais transmis. Si vous refusez, toutes les autres parties de l'application continuent de
fonctionner.

---

## 6. Données de santé

Ranked ne lit **pas** les données d'Apple Health et n'y écrit pas.

Votre âge, votre sexe et votre poids corporel sont des données proches de la santé et peuvent, au
sens du RGPD, constituer des données concernant la santé. Nous les collectons dans une seule
finalité — la formule de rang normalise la performance en fonction du gabarit, afin qu'un athlète de
95 kg et un athlète de 60 kg tenant le même levier ne soient pas notés comme s'ils avaient accompli
la même chose — et nous n'en transmettons au serveur que le minimum nécessaire à la comparaison des
classements.

---

## 7. Base légale (RGPD et revDSG suisse)

| Quoi | Base |
|---|---|
| Compte et connexion | Exécution d'un contrat — l'application requiert un compte |
| Profil de classement | Consentement, donné par l'utilisation de la fonction de classement |
| Enregistrements des tentatives vérifiées | Consentement, donné par l'enregistrement d'une tentative |
| Achats | Exécution d'un contrat |
| Statistiques d'utilisation | Intérêt légitime à améliorer l'application ; vous pouvez vous y opposer, voir §9 |

**Deux lois s'appliquent ici, et non une seule.** Ranked est exploitée depuis la Suisse ; la loi
fédérale suisse révisée sur la protection des données (**revDSG**, en vigueur depuis septembre
2023) régit donc ce traitement. Le **RGPD** s'applique en outre partout où l'application est
utilisée depuis l'Union européenne ou le Royaume-Uni. Lorsque les deux divergent, nous appliquons la
plus stricte. Les personnes résidant en Suisse disposent des mêmes droits fondamentaux que ceux
énumérés au §9 — accès, rectification, effacement, portabilité et opposition — en vertu des articles
25 ss revDSG.

---

## 8. Durée de conservation

Les données de compte, de profil, d'amis et des enregistrements de tentatives vérifiées sont
conservées jusqu'à la suppression de votre compte. La suppression du compte les supprime.

Les événements analytiques sont conservés aussi longtemps que la durée de conservation propre à
PostHog s'applique à notre offre. **La suppression de votre compte ne les supprime pas**, et nous
le disons explicitement plutôt que de laisser entendre le contraire : le profil analytique n'est pas
relié à votre compte — il repose sur un identifiant distinct, généré par l'application — de sorte
qu'il n'existe aucun lien nous permettant de le retrouver et de le supprimer. Son contenu est
énuméré au §3.5 : événements d'utilisation, votre rang, ainsi que l'âge, le sexe et le poids
corporel que vous avez saisis. Il ne comporte ni nom, ni e-mail, ni identifiant de compte.

Si vous souhaitez que ce profil soit également supprimé, écrivez-nous en indiquant la date
approximative à laquelle vous avez utilisé l'application pour la première fois ; nous le
localiserons et le supprimerons manuellement.

---

## 9. Vos droits

Vous pouvez, à tout moment :

- **Supprimer votre compte** depuis les Réglages de l'application. Cela supprime votre profil
  côté serveur, vos liens d'amitié et les enregistrements de vos tentatives vérifiées. Lorsqu'un
  jeton d'actualisation Apple est conservé pour votre compte (voir §3.1), cela révoque également
  l'accès de Ranked à votre identifiant Apple. Les données stockées uniquement sur votre appareil
  sont supprimées en désinstallant l'application.
- **Demander une copie** des données que nous détenons à votre sujet, ou nous demander de les
  rectifier.
- **Vous opposer aux statistiques d'utilisation.**
- **Introduire une réclamation auprès d'une autorité de contrôle** de votre pays.

Écrivez à **dylan.schmid538@gmail.com** pour l'un quelconque de ces droits.

---

## 10. Enfants

Ranked ne s'adresse pas aux enfants de moins de 13 ans et nous ne collectons pas sciemment leurs
données.

---

## 11. Modifications

Si la présente politique fait l'objet de modifications substantielles, l'application vous en
informera avant leur entrée en vigueur.

---

> **⚠️ Ne constitue pas un conseil juridique.** Le présent document a été rédigé à partir du code
> source et du schéma de base de données de l'application par un ingénieur, et non par un juriste.
> Il décrit fidèlement le système à la date indiquée ci-dessus — chaque affirmation qu'il contient a
> été vérifiée par rapport à ce que l'application transmet réellement. Il n'a **pas** fait l'objet
> d'un examen de conformité au RGPD, à la revDSG suisse, au CCPA ou à tout autre régime. Sa
> publication satisfait Apple ; elle ne vous rend pas conforme. Faites-le relire par un juriste dès
> lors que l'application génère des revenus.
