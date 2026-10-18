---
title: Politique de confidentialité · Calisthenics Skills – Ranked
permalink: /privacy/fr/
---

> *Ceci est une traduction. En cas de divergence, la version anglaise disponible à l'adresse
> https://dylanschmid538-ctrl.github.io/ranked-legal/privacy/ fait foi.*

# Politique de confidentialité · Calisthenics Skills – Ranked

**Dernière mise à jour : 2026-10-18**

La présente politique décrit ce que Ranked collecte, où cela va et ce que vous pouvez y faire.

Ranked est exploitée par **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Suisse**, contact
**dylan.schmid538@gmail.com**. Elle est la responsable du traitement décrit ici.

---

## 1. En bref

**Votre âge, votre sexe, votre taille et votre poids ne quittent jamais votre appareil.** La
formule de rang les utilise sur votre téléphone. Ils ne nous sont pas envoyés, et ils ne sont pas
envoyés au service d'analyse.

Trois types de données peuvent quitter votre appareil :

1. **Statistiques d'utilisation**, afin que nous puissions voir comment l'application
   est utilisée. Vous pouvez les désactiver à tout moment dans l'application.
2. **Les données d'achat**, afin que l'abonnement App Store puisse être vérifié. Apple traite le
   paiement ; nous ne voyons jamais vos données de paiement.
3. **Messages et demandes d’aide**, uniquement si vous décidez de les envoyer. Vous pouvez aussi consentir à fournir une adresse e-mail ou un numéro de téléphone pour recevoir une réponse.

Ranked n'utilise pas l'identifiant publicitaire IDFA, n'affiche pas de publicité dans l'application et ne vend ni ne transmet de données à des courtiers en données. Les statistiques d'utilisation et l'attribution Apple Search Ads ne sont envoyées que si vous autorisez le suivi dans la demande ATT ; les envois continuent tant que l'analyse reste activée dans l'application. Ranked ne lit pas non plus les données d'Apple Santé.

---

## 2. Ce qui reste sur votre appareil

Stocké dans la base de données propre à l'application sur votre téléphone et jamais transmis :

- Chaque séance, série, répétition, maintien et charge additionnelle que vous enregistrez
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

Au premier lancement de l'application, iOS affiche la demande standard d'autorisation de suivi d'Apple (App Tracking Transparency, ATT). Ranked n'envoie des données d'utilisation à PostHog dans l'UE que si vous autorisez le suivi dans la demande ATT ; les envois continuent ensuite tant que l'analyse reste activée dans l'application. Les événements comprennent la configuration, l'évaluation initiale, le rang et les paliers (avec la compétence et le palier), l'écran d'achat, les achats et les écrans ouverts. Les événements de séance en direct indiquent le début, la fin ou l'abandon, le nombre de secondes écoulées, de séries enregistrées et de compétences distinctes, ainsi que s'il s'agit de la première séance terminée. Ils ne contiennent ni exercice individuel, ni répétition, ni charge, ni note. L'âge, le sexe, la taille et le poids ne sont pas transmis. PostHog reçoit aussi les informations techniques habituelles sur l'appareil, iOS, l'application et la langue, ainsi que l'adresse IP, qui peut révéler une localisation approximative. Lorsque vous autorisez le suivi et activez l'analyse, PostHog crée un identifiant aléatoire d'installation auquel sont associés les événements et les données d'attribution de campagne pour l'analyse et la mesure publicitaire. L'identifiant IDFA n'est pas utilisé. Vous pouvez désactiver l'analyse dans Réglages ▸ Données et confidentialité ou retirer l'autorisation de suivi dans les réglages d'iOS. La désactivation de l'une ou l'autre option arrête les futurs envois ; les données déjà envoyées ne sont pas automatiquement effacées.

### 3.2 Attribution Apple Search Ads

Ranked ne demande l'attribution Apple Search Ads et n'interroge AdServices que si vous autorisez le suivi dans la demande ATT et activez l'analyse dans l'application. Dans ce cas, les données de campagne, de groupe d'annonces, de mot-clé, de création publicitaire, de pays ou de région, de date du clic et de type de téléchargement peuvent être associées à l'identifiant aléatoire d'installation PostHog pour l'analyse et la mesure publicitaire. L'IDFA n'est pas utilisé. Si vous désactivez l'analyse ou retirez l'autorisation ATT, l'attribution et les futurs envois cessent ; les données antérieures ne sont pas automatiquement effacées.

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

### 3.4 Messages et demandes d’aide (Cloudflare et CloudKit)

Si vous envoyez un avis ou une demande d’aide, Ranked transmet le message, sa catégorie et son origine à un Cloudflare Worker. Celui-ci les enregistre dans la base de données publique d’Apple CloudKit au moyen d’une clé de serveur privée. Aucune connexion à iCloud n’est nécessaire pour envoyer un message. Le Cloudflare Worker utilise l’adresse réseau de la demande pour limiter techniquement les abus ; ni l’adresse d’origine ni son empreinte ne sont enregistrées dans la fiche CloudKit du message. Vous pouvez consentir séparément à fournir une adresse e-mail ou un numéro de téléphone afin de recevoir une réponse hors de l’application. Le message et les coordonnées ne sont transmis ni à PostHog ni à RevenueCat et ne sont liés à aucun compte dans l’application. Nous traitons le message pour répondre à votre demande et les coordonnées facultatives avec votre consentement. Aucune durée fixe de suppression automatique n’est actuellement appliquée aux messages et coordonnées. Pour demander l’accès ou l’effacement, écrivez à **dylan.schmid538@gmail.com**.

---

## 4. Suivi et autorisations dans Ranked

- **Aucun compte.** Vous ne vous connectez jamais. Il n'existe aucun profil de vous sur un serveur.
- **Aucun accès à Apple Santé.** Ranked ne lit rien dans l'app Santé et n'y écrit rien.
- **Ni appareil photo, ni photos, ni microphone, ni localisation, ni contacts.** L'application ne
  demande aucune de ces autorisations.
- **Ranked n'utilise pas l'identifiant publicitaire IDFA, n'affiche pas de publicité dans l'application et ne vend ni ne transmet de données à des courtiers en données. Les statistiques d'utilisation et l'attribution Apple Search Ads ne sont envoyées que si vous autorisez le suivi dans la demande ATT ; les envois continuent tant que l'analyse reste activée dans l'application.**
- **Aucun serveur de notifications.** Les rappels que Ranked peut envoyer sont programmés localement
  sur votre téléphone ; rien à leur sujet ne quitte l'appareil. On vous demande votre accord avant
  le premier, et vous pouvez les désactiver à tout moment dans les réglages d'iOS.

---

## 5. Base légale (RGPD et nLPD suisse)

| Quoi | Base |
|---|---|
| Achats et vérification de l'abonnement (§3.3) | Exécution d'un contrat |
| Statistiques d'utilisation (§3.1) | Votre consentement par l’autorisation ATT et le réglage d’analyse de Ranked ; vous pouvez désactiver l’une ou l’autre option à tout moment, voir §8 |
| Attribution Search Ads (§3.2) | Votre consentement par l’autorisation ATT et le réglage d’analyse de Ranked ; vous pouvez désactiver l’une ou l’autre option à tout moment, voir §8 |

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

Vous pouvez retirer à tout moment votre consentement à l'analyse dans Réglages ▸ Données et confidentialité, sans justification. Cela arrête immédiatement les nouveaux événements, sans effacer automatiquement les données déjà envoyées ni résilier votre abonnement App Store.

Vous pouvez supprimer vos données d'entraînement locales dans Réglages ▸ Données et confidentialité ▸ *Supprimer les données d’entraînement locales*, ou en supprimant l'application. Votre abonnement se gère et se résilie séparément avec votre compte Apple.

Pour les données déjà envoyées à PostHog, écrivez à **dylan.schmid538@gmail.com**. Ranked ne relie pas l'identifiant d'analyse aléatoire à un compte. Une date approximative ou un modèle d'appareil peut ne pas suffire pour retrouver votre profil de manière fiable. Nous expliquerons ce que nous pouvons identifier et traiterons toute demande vérifiable d'accès, de rectification ou d'effacement. Ne nous envoyez pas les identifiants de votre compte Apple.

Vous pouvez demander la limitation du traitement et déposer une réclamation auprès de l'autorité de contrôle de votre pays ; en Suisse, il s'agit du Préposé fédéral à la protection des données et à la transparence (PFPDT).

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
