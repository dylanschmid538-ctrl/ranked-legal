---
title: Privacy Policy
permalink: /privacy/
---

# Privacy Policy · Calisthenics Skills – Ranked

**Last updated: 17 August 2026**

This policy describes what Ranked collects, where it goes, and what you can do about it. It was
written against the app's actual code and database schema, not from a template — if something here
is wrong, the code is the thing to check.

Ranked is operated by **Monica Dede Schmid, Fluhmattstrasse 40, 6004 Luzern, Switzerland**, contact **dylan.schmid538@gmail.com**.

---

## 1. The short version

Almost everything Ranked knows about your training stays on your phone. Your workout history, your
progress through every skill, your rank and your body map are stored locally and are never uploaded.

Four things do leave your device: your sign-in identity, a small profile used for the leaderboards,
records that you completed a verified attempt, and anonymous usage analytics. Each is explained
below.

**Your Verified Attempt videos never leave your device.** Only a fingerprint of the file is sent.

---

## 2. What stays on your device

Stored locally in the app's own database and never transmitted:

- Every workout, set, repetition, hold and added weight you log
- Your progress through each skill and stage, and your rank history
- Your training plan, schedule and preferences
- Your body measurements as you entered them (age, sex, height, bodyweight) — a copy of some of
  these is also sent to the leaderboard service, see §3.2
- **The video files from Verified Attempts.** These are written to the app's private storage. They
  are not uploaded, not backed up to our servers, and not accessible to us.

Deleting the app deletes all of this. We cannot recover it.

---

## 3. What leaves your device

### 3.1 Your account
When you sign in with Apple or Google, we receive and store a user identifier and, depending on
what you allow at sign-in, an email address. This is handled by **Supabase**, which hosts our
database and authentication.

An Apple refresh token has one purpose only: so that deleting your account can also revoke
Ranked's access to your Apple ID, as Apple requires. This link to Apple is not active yet — until
it is, no refresh token is stored at all, and there is nothing to revoke.

### 3.2 Your leaderboard profile
To place you on a leaderboard and to compare you against people of a similar build, the following
is stored on our server:

- a randomly generated **friend code**
- your **age**, **sex** and **bodyweight**
- the date your profile was created

**Note on visibility:** any signed-in Ranked user can look up a profile by its friend code. That is
the purpose of a friend code — it exists to be handed to someone. Do not share yours with anyone
you would not want seeing your entry. What other users can see is your friend code and your
position on a leaderboard — nothing else. Your age, sex and bodyweight are used for the
comparison on the server and are never shown to, or downloadable by, other users.

Your **height** is not sent. Your workout history is not sent.

### 3.3 Verified Attempts
When you record a Verified Attempt, we store: your user id, which skill and stage the attempt was
for, a **cryptographic hash of the video file**, and the time it was recorded.

The hash is a fingerprint. It cannot be turned back into the video. It exists so an attempt can be
tied to a specific recording without that recording ever leaving your phone.

### 3.4 Friends
If you add someone by their friend code, we store the connection between your account and theirs,
and your membership in any friend group.

### 3.5 Usage analytics
We use **PostHog**, hosted in the **European Union**, to understand how the app is used. We record
events such as which onboarding step you reached, when a workout was completed, when a rank
changed, and whether a purchase screen was shown or dismissed.

These events carry your rank and your progress through the app. They do **not** carry your name,
email, height, or the contents of your workouts.

---

## 4. Purchases

Subscriptions are processed by **Apple**. We never see your payment details. **RevenueCat**
manages your subscription status on our behalf and receives a pseudonymous identifier and your
subscription state. The purchase screen itself is part of the app; no third party decides which
one you are shown.

---

## 5. Camera and microphone

Ranked asks for camera and microphone access for one feature: recording a Verified Attempt. The
recording is saved to your device. It is never uploaded. If you decline, every other part of the
app continues to work.

---

## 6. Health data

Ranked does **not** read from or write to Apple Health.

Your age, sex and bodyweight are health-adjacent data, and under the GDPR they can qualify as data
concerning health. We collect them for one purpose — the rank formula normalises performance by
build, so a 95 kg athlete and a 60 kg athlete holding the same lever are not scored as if they did
the same thing — and we send the minimum of them to the server that the leaderboard comparison
needs.

---

## 7. Legal basis (GDPR and Swiss revDSG)

| What | Basis |
|---|---|
| Account and sign-in | Performance of a contract — the app requires an account |
| Leaderboard profile | Consent, given by using the leaderboard feature |
| Verified attempt records | Consent, given by recording an attempt |
| Purchases | Performance of a contract |
| Analytics | Legitimate interest in improving the app; you may object, see §9 |

**Two laws apply here, not one.** Ranked is operated from Switzerland, so the revised Swiss
Federal Act on Data Protection (**revDSG**, in force since September 2023) governs this
processing. The **GDPR** applies in addition wherever the app is used from the European Union
or the United Kingdom. Where the two differ, we follow the stricter one. Swiss residents have
the same core rights listed in §9 — access, correction, deletion, portability and objection —
under Article 25 ff. revDSG.

---

## 8. How long we keep it

Account, profile, friends and verified attempt records are kept until you delete your account.
Deleting the account removes them.

Analytics events are kept for as long as PostHog's own retention applies to our plan. **Deleting
your account does not delete them**, and we are being explicit about that rather than implying
otherwise: the analytics profile is not connected to your account — it uses a separate,
app-generated identifier — so there is no link by which we could find and remove it. What it
contains is listed in §3.5: usage events, your rank, and the age, sex and bodyweight you entered.
It carries no name, no email and no account id.

If you want that profile removed as well, write to us with the approximate date you first used the
app and we will locate and delete it by hand.

---

## 9. Your rights

You can, at any time:

- **Delete your account** from Settings in the app. This deletes your server-side profile, your
  friend connections and your verified attempt records. Where an Apple refresh token is stored
  for your account (see §3.1), it also revokes Ranked's access to your Apple ID. Data stored
  only on your device is removed by deleting the app.
- **Request a copy** of the data we hold about you, or ask us to correct it.
- **Object to analytics.**
- **Complain to a supervisory authority** in your country.

Write to **dylan.schmid538@gmail.com** for any of these.

---

## 10. Children

Ranked is not directed at children under 13, and we do not knowingly collect their data.

---

## 11. Changes

If this policy changes materially, the app will tell you before the change takes effect.

---

> **⚠️ Not legal advice.** This document was drafted from the app's source code and database schema
> by an engineer, not a lawyer. It describes the system accurately as of the date above — every
> claim in it was checked against what the app actually sends. It has **not** been reviewed for
> compliance with the GDPR, the Swiss revDSG, the CCPA or any other regime. Publishing it satisfies
> Apple; it does not make you compliant. Have a lawyer read it once the app earns money.
