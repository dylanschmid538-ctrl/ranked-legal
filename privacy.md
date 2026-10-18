---
title: Privacy Policy
permalink: /privacy/
---

> **Other languages:** [العربية](ar/) · [Català](ca/) · [Čeština](cs/) · [Dansk](da/) · [Deutsch](de/) · [Ελληνικά](el/) · [Español](es/) · [Suomi](fi/) · [Français](fr/) · [עברית](he/) · [Hrvatski](hr/) · [Magyar](hu/) · [Bahasa Indonesia](id/) · [Italiano](it/) · [日本語](ja/) · [한국어](ko/) · [Bahasa Melayu](ms/) · [Nederlands](nl/) · [Norsk](no/) · [Polski](pl/) · [Português](pt/) · [Română](ro/) · [Русский](ru/) · [Slovenčina](sk/) · [Slovenščina](sl/) · [Svenska](sv/) · [ไทย](th/) · [Türkçe](tr/) · [Tiếng Việt](vi/) · [中文（简体）](zh-Hans/) · [中文（繁體）](zh-Hant/) · [Lietuvių](lt/) · [Latviešu](lv/)

# Privacy Policy · Calisthenics Skills – Ranked

**Last updated: 2026-10-18**

This policy describes what Ranked collects, where it goes, and what you can do about it.

Ranked is operated by **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Switzerland**,
contact **dylan.schmid538@gmail.com**. She is the controller for the processing described here.

---

## 1. The short version

**Your age, sex, height and bodyweight never leave your device.** The rank formula uses them on
your phone. They are not sent to us, and they are not sent to the analytics service.

Three kinds of data can leave your device:

1. **Usage statistics**, only if you choose to share them during setup or later in Settings.
   Sharing is off unless you choose it, and you can withdraw your choice at any time.
2. **Purchase data**, so the App Store subscription can be verified. Apple handles the payment;
   we never see your payment details.
3. **Feedback and support messages**, only when you choose to send one. You may also give an email address or phone number with consent for a reply.

Ranked asks for Apple's tracking permission on first launch because it links app activity with
Apple Search Ads campaign data to measure campaign results. It does not use the advertising
identifier (IDFA), show ads, or read Apple Health.

---

## 2. What stays on your device

Stored in the app's own database on your phone and never transmitted:

- Every workout, set, repetition, hold and added weight you log
- Your training plan, schedule, reminders and preferences
- Your body measurements as you entered them (age, sex, height, bodyweight)
- Your training notes

The app does not exclude this database from your device backup. If you use iCloud Backup or a
computer backup, your training data is part of that backup and comes back when you restore it — on
Apple's terms, not ours.

Deleting the app deletes all of this from the device. We cannot recover it, because we never had
it.

---

## 3. What leaves your device

### 3.1 Usage statistics (PostHog)

We use **PostHog**, hosted in the **European Union**, to understand how the app is used. The app
sends it a fixed list of events:

- which setup step you reached, completed or went back from, and how long each took;
- what the initial assessment produced: how many skill lines and stages you claimed, which skill
  you chose as your goal, your starting rank and the rank of each of your six body regions;
- when the purchase screen was shown or dismissed, and when a purchase was started, completed or
  restored — with the product and offer it concerned; when the app later observes an active trial
  or paid subscription period, with the product and whether it is a sandbox purchase (this is not
  a record of every charge, and it is not sent while the app is closed);
- when your rank changed, and which skill triggered it;
- when you cleared a stage — which skill, which stage, and whether it came from a logged set, a
  back-filled workout or a manual claim;
- which screens you open, and when a live workout starts, ends or is abandoned. These workout
  events include elapsed seconds, the number of logged sets, the number of distinct skills used,
  and whether this was your first completed live workout. They do not include individual exercise
  names, repetitions, holds, added weights or notes.

The PostHog software inside the app also attaches standard technical information to each event —
such as your device model, iOS version, app version, language and time zone. Like any internet service, PostHog receives the IP
address of the request; it may derive an approximate location (country or city) from it.

**What is not in there:** no name, no contact details from the feedback form, no account
identifier (there is none), no age, sex, height or bodyweight, and no individual workout entries.

**How you are identified:** After you choose to share usage data, PostHog generates a random identifier and
stores it on your device. All events are grouped under that identifier. The app never tells
PostHog who you are. Contact details from feedback are not passed to PostHog.

**Your choice:** On first launch, iOS shows Apple's standard tracking permission dialog before
Ranked starts PostHog analytics or requests Apple Search Ads attribution. If you allow tracking,
usage sharing starts automatically and remains on until you switch *Share usage data* off in
Ranked's Settings ▸ Data & privacy. If you deny tracking or later revoke it in iOS Settings,
Ranked sends no analytics events or campaign attribution. Either choice stops new data from being
sent; it does not erase events already sent.

### 3.2 Apple Search Ads attribution

If tracking permission is granted and usage sharing is enabled, and you installed Ranked after
tapping an Apple Search Ads advertisement, the app asks Apple once where the install came from.
Apple answers with the campaign, ad group, keyword
and creative set of that ad, the country or region of the click, the date of the click, and
whether this was a new download or a re-download. The app attaches these values to the anonymous
PostHog identifier described in §3.1, so every later event can be grouped by the ad that brought
you.

This uses Apple's **AdServices** framework and does not use the advertising identifier (IDFA).
Ranked links campaign details with app and subscription events to measure campaign results, so
this data flow runs only while tracking permission and usage sharing are enabled. If you did not
arrive through an ad, Apple says so and nothing else is attached. Revoking tracking permission or
turning off usage sharing (§3.1) stops further attribution requests and sends.

### 3.3 Purchases (Apple and RevenueCat)

Subscriptions are sold and billed by **Apple** through the App Store. We never see your payment
details, your Apple Account or your name.

To check whether your subscription is active, the app uses **RevenueCat**. RevenueCat receives the
App Store purchase record for your subscription — the product bought, when it started and when it
expires — together with standard technical information such as your iOS version and the app
version. It identifies your installation by a random identifier it generates itself and stores on
your device. We do not give RevenueCat your name, your email address or any other identity, and
because Ranked has no accounts, there is none to give.

When you tap **Restore Purchases**, the app asks Apple for the purchases made with the Apple
Account signed in on the device and passes the result to RevenueCat in the same way.

### 3.4 Feedback and support (Cloudflare and CloudKit)

If you choose to send feedback or a support request, Ranked sends the message, its category and source to a Cloudflare Worker. The Worker stores them in Apple's CloudKit public database using a private server key. You do not need to sign in to iCloud to send a message. The Cloudflare Worker uses the request's network address for a technical abuse limit; neither the raw address nor a hash of it is stored in the CloudKit feedback record. You may separately agree to include an email address or phone number so we can reply outside the app. Messages and contact details are not sent to PostHog or RevenueCat and are not tied to an app account. We process the message to answer your request and optional contact details with your consent. No fixed automatic deletion period is currently enforced for messages or contact details. You can request access or deletion by emailing **dylan.schmid538@gmail.com**.

---

## 4. What Ranked does not do

- **No accounts.** You never sign in. There is no profile of you on any server.
- **No Apple Health.** Ranked neither reads from nor writes to the Health app.
- **No camera, no photos, no microphone, no location, no contacts.** The app does not request any
  of these permissions.
- **No advertising identifier (IDFA) and no ads inside the app.** Ranked asks for Apple's tracking
  permission because it links app activity with Apple Search Ads campaign data for advertising
  measurement. It does not sell data or share it with data brokers.
- **No push server.** The reminders Ranked can send are scheduled locally on your phone; nothing
  about them leaves the device. You are asked before the first one is scheduled, and you can turn
  them off in iOS Settings at any time.

---

## 5. Legal basis (GDPR and Swiss revDSG)

| What | Basis |
|---|---|
| Purchases and subscription verification (§3.3) | Performance of a contract |
| Usage statistics and Search Ads attribution (§3.1–3.2) | Apple's tracking permission; future sharing can be stopped in iOS Settings or by switching off Ranked usage sharing, see §8 |

**Two laws apply here, not one.** Ranked is operated from Switzerland, so the revised Swiss
Federal Act on Data Protection (**revDSG**, in force since September 2023) governs this
processing. The **GDPR** applies in addition wherever the app is used from the European Union
or the United Kingdom. Where the two differ, we follow the stricter one. Swiss residents have
the same core rights listed in §8 under Article 25 ff. revDSG.

---

## 6. Where the data is processed

- **PostHog** processes the usage statistics in the European Union.
- **RevenueCat, Inc.** is based in the United States and processes the purchase data described in
  §3.3 there.
- **Apple** processes the purchase itself and the Search Ads attribution request under Apple's
  own privacy policy, which applies to your Apple Account regardless of this app.

---

## 7. How long we keep it

Usage statistics are kept for as long as PostHog's retention for our plan applies. We do not
promise a fixed number of months, because PostHog does not let us set one — and a number nobody
can keep is worse in a privacy policy than none.

Purchase records are kept by RevenueCat for as long as the subscription and its history exist,
which is what verifying a subscription requires.

Everything on your device stays there until you delete the app.

---

## 8. Your rights

You can, at any time:

- **Stop analytics sharing** by turning off *Share usage data* in Settings ▸ Data & privacy or
  revoking tracking permission in iOS Settings. This stops new analytics and campaign data; it does
  not cancel your subscription or erase events already sent.
- **Delete local training data** in Settings ▸ Data & privacy ▸ *Delete local training data*, or delete the
  app. This removes the app's local records; it does not cancel your App Store subscription.
- **Ask us about data already sent to PostHog.** Because Ranked has no account linked to its
  random analytics identifier, an approximate date or device model alone may not let us identify
  your profile reliably. Contact us and we will explain what we can identify and process any
  verifiable access, correction or deletion request. Do not email your Apple Account credentials.
- **Request a copy** of the data a service holds under your identifier, ask us to **correct** it,
  or ask us to **restrict** its processing while a request is being looked at.
- **Complain to a supervisory authority** in your country — in Switzerland the Federal Data
  Protection and Information Commissioner (FDPIC).

Write to **dylan.schmid538@gmail.com** for any of these.

---

## 9. Children

Ranked is for people aged **16 and over**. The app asks for your age during setup because the rank
formula depends on it, and it is not directed at anyone younger. We do not knowingly collect data
from anyone under 16.

---

## 10. Changes

The version published at this address is the current one, and the date at the top tells you when
it last changed. Earlier versions remain visible in the public history of the repository these
pages are published from, so you can see what changed and when.

---
