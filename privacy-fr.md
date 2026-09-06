---
title: Politique de confidentialité · Calisthenics Skills – Ranked
permalink: /privacy/fr/
---

> *Ceci est une traduction. En cas de divergence, la version anglaise disponible à l'adresse
> https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/ fait foi.*

# Politique de confidentialité · Calisthenics Skills – Ranked

**Dernière mise à jour : 4 septembre 2026**

La présente politique décrit ce que Ranked collecte, où cela va et ce que vous pouvez y faire. Elle
a été rédigée à partir du code réel de l'application, et non d'un modèle — si quelque chose ici est
inexact, c'est le code qui fait référence.

Ranked est exploitée par **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Suisse**, contact
**dylan.schmid538@gmail.com**. Elle est la responsable du traitement décrit ici.

---

## 1. En bref

Ranked n'a **ni comptes utilisateur, ni serveur propre.** Tout ce qui concerne votre entraînement —
chaque série enregistrée, votre progression dans chaque compétence, votre rang, votre Power Level,
votre carte corporelle — est stocké sur votre téléphone et n'est jamais téléversé nulle part.

**Votre âge, votre sexe, votre taille et votre poids ne quittent jamais votre appareil.** La
formule de rang les utilise sur votre téléphone. Ils ne nous sont pas envoyés, et ils ne sont pas
envoyés au service d'analyse.

Deux choses quittent votre appareil, et seulement ces deux-là :

1. **Des statistiques d'utilisation anonymes**, afin que nous puissions voir comment l'application
   est utilisée. Vous pouvez les désactiver à tout moment dans l'application.
2. **Les données d'achat**, afin que l'abonnement App Store puisse être vérifié. Apple traite le
   paiement ; nous ne voyons jamais vos données de paiement.

Ranked ne vous suit pas à travers d'autres applications ou sites web, n'affiche aucune publicité et
ne lit rien depuis Apple Santé.

---

## 2. Ce qui reste sur votre appareil

Stocké dans la base de données propre à l'application sur votre téléphone et jamais transmis :

- Chaque séance, série, répétition, maintien et charge additionnelle que vous enregistrez
- Votre progression dans chaque compétence et chaque palier, l'historique de votre rang et votre
  Power Level
- Votre plan d'entraînement, votre calendrier, vos rappels et vos préférences
- Vos mesures corporelles telles que vous les avez saisies (âge, sexe, taille, poids)
- Vos notes d'entraînement

L'application n'exclut pas cette base de données de la sauvegarde de votre appareil. Si vous
utilisez la sauvegarde iCloud ou une sauvegarde sur ordinateur, vos données d'entraînement en font
partie et reviennent lors d'une restauration — selon les conditions d'Apple, pas les nôtres.

Supprimer l'application supprime tout cela de l'appareil. Nous ne pouvons rien récupérer, parce que
nous ne l'avons jamais eu.

---

## 3. Ce qui quitte votre appareil

### 3.1 Statistiques d'utilisation (PostHog)

Nous utilisons **PostHog**, hébergé dans l'**Union européenne**, pour comprendre comment
l'application est utilisée. L'application lui envoie une liste fixe d'événements :

- quelle étape de configuration vous avez atteinte, terminée ou quittée, et combien de temps chacune
  a duré ;
- ce qu'a donné l'évaluation initiale : combien de lignes de compétences et de paliers vous avez
  déclarés, quelle compétence vous avez choisie comme objectif, votre rang de départ et le rang de
  chacune de vos six régions corporelles ;
- quand l'écran d'achat a été affiché ou fermé, et quand un achat a été commencé, finalisé ou
  restauré — avec le produit et l'offre concernés ;
- quand votre rang a changé, et quelle compétence l'a déclenché ;
- quand vous avez validé un palier — quelle compétence, quel palier, et si cela venait d'une série
  enregistrée, d'une séance saisie après coup ou d'une déclaration manuelle ;
- quels écrans vous ouvrez, et quand une séance se termine. L'événement de fin de séance ne porte
  aucun détail : ni les exercices, ni les séries, ni les chiffres.

Le logiciel PostHog intégré à l'application joint également à chaque événement des informations
techniques standard — modèle d'appareil, version d'iOS, version de l'application, langue et fuseau
horaire — et enregistre les moments où l'application est ouverte et mise en arrière-plan. Comme tout
service Internet, PostHog reçoit l'adresse IP de la requête ; il peut en déduire une localisation
approximative (pays ou ville).

**Ce qui ne s'y trouve pas :** aucun nom, aucune adresse e-mail (l'application n'en demande jamais),
aucun identifiant de compte (il n'y en a pas), ni âge, ni sexe, ni taille, ni poids, et aucun
contenu de vos séances.

**Comment vous êtes identifié :** PostHog génère un identifiant aléatoire au premier lancement de
l'application et le stocke sur votre appareil. Tous les événements sont regroupés sous cet
identifiant. L'application ne dit jamais à PostHog qui vous êtes, et il n'y a rien — ni compte, ni
e-mail — qu'elle pourrait lui dire.

**Pour les désactiver :** Réglages ▸ Confidentialité ▸ *Partager des données d'utilisation
anonymes*. Désactiver cette option empêche l'application d'envoyer des événements à partir de ce
moment. Le réglage est stocké sur votre appareil et survit aux mises à jour.

### 3.2 Attribution Apple Search Ads

Si vous avez installé Ranked après avoir appuyé sur une publicité Apple Search Ads, l'application
demande une seule fois à Apple, au premier lancement, d'où vient l'installation. Apple répond avec
la campagne, le groupe d'annonces, le mot-clé et le visuel de cette publicité, le pays ou la région
du clic, la date du clic, et s'il s'agissait d'un nouveau téléchargement ou d'un retéléchargement.
L'application rattache ces valeurs à l'identifiant PostHog anonyme décrit au §3.1, afin que chaque
événement ultérieur puisse être regroupé selon la publicité qui vous a amené.

Cela passe par le framework **AdServices** d'Apple, qui n'implique pas l'identifiant publicitaire
(IDFA) et qu'Apple ne considère pas comme du suivi — aucune fenêtre d'autorisation de suivi n'est
donc affichée. Si vous n'êtes pas arrivé par une publicité, Apple le dit et rien n'est rattaché.
Désactiver les statistiques d'utilisation (§3.1) arrête également cela.

### 3.3 Achats (Apple et RevenueCat)

Les abonnements sont vendus et facturés par **Apple** via l'App Store. Nous ne voyons jamais vos
données de paiement, votre compte Apple ni votre nom.

Pour vérifier si votre abonnement est actif, l'application utilise **RevenueCat**. RevenueCat reçoit
l'enregistrement d'achat App Store de votre abonnement — le produit acheté, sa date de début et sa
date d'expiration — ainsi que des informations techniques standard telles que votre version d'iOS
et la version de l'application. Il identifie votre installation par un identifiant aléatoire qu'il
génère lui-même et stocke sur votre appareil. Nous ne donnons à RevenueCat ni votre nom, ni votre
adresse e-mail, ni aucune autre identité, et comme Ranked n'a pas de comptes, il n'y en a aucune à
donner.

Lorsque vous appuyez sur **Restaurer les achats**, l'application demande à Apple les achats
effectués avec le compte Apple connecté sur l'appareil et transmet le résultat à RevenueCat de la
même manière.

---

## 4. Ce que Ranked ne fait pas

- **Aucun compte.** Vous ne vous connectez jamais. Il n'existe aucun profil de vous sur un serveur.
- **Aucun accès à Apple Santé.** Ranked ne lit rien dans l'app Santé et n'y écrit rien.
- **Ni appareil photo, ni photos, ni microphone, ni localisation, ni contacts.** L'application ne
  demande aucune de ces autorisations.
- **Aucun suivi entre applications ou sites web**, aucun identifiant publicitaire, aucune publicité
  dans l'application, aucune donnée vendue ou transmise à des courtiers en données.
- **Aucun serveur de notifications.** Les rappels que Ranked peut envoyer sont programmés localement
  sur votre téléphone ; rien à leur sujet ne quitte l'appareil. On vous demande votre accord avant
  le premier, et vous pouvez les désactiver à tout moment dans les réglages d'iOS.

---

## 5. Base légale (RGPD et nLPD suisse)

| Quoi | Base |
|---|---|
| Achats et vérification de l'abonnement (§3.3) | Exécution d'un contrat |
| Statistiques d'utilisation (§3.1) | Intérêt légitime à comprendre et améliorer l'application ; vous pouvez vous y opposer à tout moment en les désactivant, voir §8 |
| Attribution Search Ads (§3.2) | Intérêt légitime à savoir quelle publicité fonctionne ; opposition comme ci-dessus |

**Deux droits s'appliquent ici, pas un.** Ranked est exploitée depuis la Suisse, de sorte que la loi
fédérale révisée sur la protection des données (**nLPD**, en vigueur depuis septembre 2023) régit ce
traitement. Le **RGPD** s'applique en outre partout où l'application est utilisée depuis l'Union
européenne ou le Royaume-Uni. Lorsque les deux divergent, nous suivons le plus strict. Les personnes
résidant en Suisse disposent des mêmes droits essentiels que ceux énumérés au §8, en vertu des
art. 25 ss nLPD.

---

## 6. Où les données sont traitées

- **PostHog** traite les statistiques d'utilisation dans l'Union européenne.
- **RevenueCat, Inc.** est établie aux États-Unis et y traite les données d'achat décrites au §3.3.
- **Apple** traite l'achat lui-même et la demande d'attribution Search Ads selon sa propre politique
  de confidentialité, qui s'applique à votre compte Apple indépendamment de cette application.

---

## 7. Durée de conservation

Les statistiques d'utilisation sont conservées aussi longtemps que s'applique la durée de rétention
de PostHog pour notre formule. Nous ne promettons pas un nombre de mois fixe, parce que PostHog ne
nous permet pas d'en définir un — et un chiffre que personne ne peut tenir est pire, dans une
politique de confidentialité, que pas de chiffre du tout.

Les enregistrements d'achat sont conservés par RevenueCat aussi longtemps que l'abonnement et son
historique existent, ce qu'exige la vérification d'un abonnement.

Tout ce qui se trouve sur votre appareil y reste jusqu'à ce que vous supprimiez l'application.

---

## 8. Vos droits

Vous pouvez, à tout moment :

- **Désactiver les statistiques d'utilisation** dans Réglages ▸ Confidentialité. C'est votre droit
  d'opposition et, lorsque le traitement repose sur le consentement, votre droit de le retirer —
  cela prend effet immédiatement et n'exige aucune justification.
- **Supprimer vos données.** Comme Ranked ne détient rien vous concernant sur un serveur, supprimer
  l'application supprime tout ce que l'application elle-même stocke.
- **Nous demander de supprimer votre profil d'analyse anonyme.** Nous ne pouvons pas le retrouver
  par un nom — il n'en a pas —, mais si vous nous écrivez en indiquant la date approximative de
  votre première utilisation et l'appareil utilisé, nous le localiserons à la main et le
  supprimerons.
- **Demander une copie** des données qu'un service détient sous votre identifiant, nous demander de
  les **corriger**, ou d'en **limiter** le traitement pendant l'examen d'une demande.
- **Déposer une réclamation auprès d'une autorité de contrôle** de votre pays — en Suisse, le
  Préposé fédéral à la protection des données et à la transparence (PFPDT).

Écrivez à **dylan.schmid538@gmail.com** pour toute demande de ce type.

---

## 9. Enfants

Ranked s'adresse aux personnes de **16 ans et plus**. L'application demande votre âge lors de la
configuration parce que la formule de rang en dépend, et elle ne s'adresse à personne de plus jeune.
Nous ne collectons pas sciemment de données concernant des personnes de moins de 16 ans.

---

## 10. Modifications

La version publiée à cette adresse est la version en vigueur, et la date en haut vous indique quand
elle a changé pour la dernière fois. Les versions antérieures restent visibles dans l'historique
public du dépôt à partir duquel ces pages sont publiées, de sorte que vous pouvez voir ce qui a
changé et quand.

---

> **⚠️ Ne constitue pas un conseil juridique.** Ce document a été rédigé à partir du code source de
> l'application par un ingénieur, et non par un juriste. Il décrit fidèlement le système à la date
> indiquée ci-dessus — chaque affirmation a été vérifiée par rapport à ce que l'application envoie
> réellement. Il n'a **pas** été examiné au regard du RGPD, de la nLPD suisse, du CCPA ou de tout
> autre régime. Sa publication satisfait Apple ; elle ne vous rend pas conforme. Faites-le relire
> par un juriste dès lors que l'application génère des revenus.
