# Customer Center privacy delta · 2026-11-09

Unpublished source draft for the new client support route. Do not publish before the corresponding client is ready and device/provider behavior has been checked. Source wording describes the current feedback feature flag as OFF: survey answers are not sent to PostHog. Enabling that flag requires another policy/label review. No prices, legal basis, retention promise, recipient or rights clause is invented.

Translation deltas are reviewed per target language, then inserted before section3.3 of the existing policy. The existing free-text Cloudflare/CloudKit paragraph stays separate. Locale routes and page metadata remain intact. Support changes apply to the English support page, which is the existing shared route. No website deployment or merge is authorized by this draft alone.

## Review scope

All33 target-language deltas were translated one target per run, then independently cross-read in groups of17 and16. Both reviews found no material recipient, consent, survey, cancellation or refund drift. Brands and §3.3 matched in33/33. This is semantic review, not certification by a native legal professional.

An independent cold source review matched the English delta to the current app and installed SDK: RevenueCat processes its own survey and purchase reference; PostHog actions require usage+purchase-link consent; survey reasons additionally require the feedback feature flag, OFF in both project.yml and Info.plist. The separate form uses Cloudflare/CloudKit. Opening Apple management is not cancellation; completing a refund request is not Apple approval. Enabling the survey feature gate requires a new disclosure/label check.

Support uses the actual fallback label **Manage Subscription** with the Apple logo. No App Store metadata changed and nothing was published.
