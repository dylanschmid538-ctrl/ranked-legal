# Feedback privacy handoff · 2026-10-13

Draft for the in-app feedback release. Do not publish these pages before the app and private inbox are ready. The public site currently has 34 privacy languages and one English support page.

| Data | Purpose and basis | Stored by / access | Retention |
|---|---|---|---|
| Voluntary message, category, source, request ID, submission time | Answer feedback or support request; handling the user's request | Supabase `feedback_submissions`; service role only | No fixed automatic deletion period is enforced |
| Optional email **or** phone, plus contact consent | Reply outside the app; consent | Same private Supabase table; not sent to PostHog or RevenueCat | No fixed automatic deletion period is enforced |
| Salted SHA-256 hash of network address, rate window and count | Limit abuse; legitimate interest | Supabase `feedback_rate_limits`; service role only; raw address is not stored in this table | Rows older than two days are pruned during a later submission, so two days is **not** a guaranteed deletion deadline |

Source contract: `ranked-messages-recovery/Sources/Features/Support/CustomerFeedbackView.swift`, `CustomerFeedbackService.swift`, `supabase/functions/submit-feedback/index.ts`, and `supabase/migrations/20261013170000_feedback_inbox.sql` as inspected on 2026-10-13. The form has no account and a reply requires the separate contact toggle. The exact Supabase hosting region and any provider-level network logs were not established here; verify before making a location or raw-IP retention claim. The existing policy's PostHog and RevenueCat sections continue to apply to their separate flows.

**Before release:** Update App Store Connect App Privacy for optional **Contact Info → Email Address / Phone Number**, **User Content → Customer Support** for support messages, and consider **Other User Content** for product ideas; purpose **App Functionality**. Review the network-address hash against Apple's data-type definitions rather than guessing a category. Apple's field guidance: https://developer.apple.com/app-store/app-privacy-details/ . Reconcile the final label against the exact release build, then publish the privacy and support pages together. Keep the email route for access and deletion requests.

Wording decision: no fixed message-retention promise because no scheduled deletion exists. The rate-limit cleanup is opportunistic. The privacy pages say the raw address is not stored in the **feedback database**, not that a network provider cannot log it.
