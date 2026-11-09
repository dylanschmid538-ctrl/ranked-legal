# Independent legal delta verification · 2026-11-09

Verdict: focused unpublished source delta passes preservation/route checks and all 35 changed sections pass the limited standard-text Markdown preview. This is sufficient evidence for a draft review, not proof that the actual GitHub Pages deployment is ready to publish. No policy edits, commit, push or publish were performed by this tester.

| Observed check | Exact command (from repository root) | Result / exit | Evidence |
|---|---|---|---|
| Reversible privacy/support delta | `python3 _drafts/customer-center-20261109/evidence/verify_delta.py` | PASS, exit 0; 34 policies, 33 translations + English, 33 selector destinations, 37 dated regional entries, 2 RTL wrappers, 1 support page; 0 errors. Reran successfully after commit with fixed baseline `cf351655899bf53b64d256f4e4e6952a8050a327`. | `delta-check.json` |
| Test negative control | In-memory script variant changed expected page count 34→35; restored clean script was then rerun | Expected failure observed, exit 1; no source or fixture mutation. | `negative-control.json` |
| Actual Markdown parser | `ruby _drafts/customer-center-20261109/evidence/render_preview.rb` | PASS, exit 0; bundled RDoc parsed 35 changed sections; 10 HTML preview sheets | `preview-input.json`, `preview-1.html` … `preview-10.html` |
| Narrow Chrome previews + optional large-text smoke | `python3 _drafts/customer-center-20261109/evidence/check_browser.py` | Overall exit 1: 35/35 standard sections pass at 320px/16px; ar/de/he pass at 320px/24px; support has 6px overflow at 24px. Chrome subprocesses all exit 0. Same overflow reproduced in two runs. | `browser-check.json`; `preview-1.png` … `preview-10.png` |
| Visual inspection | Tester opened all 10 actual PNG files with image viewer | All 35 standard sections visible and wrapping; RTL ar/he flow visible. Large support URL visibly exceeds right edge. | PNGs above |

## Coverage

- Removing each one exact inserted paragraph and reverting the single date stamp reconstructs each baseline privacy policy byte-for-byte against fixed commit `cf351655899bf53b64d256f4e4e6952a8050a327`. This also proves no existing legal clauses, frontmatter, addresses, links, regional route, language selector or RTL wrapper changed.
- All 33 translated paragraph files occur exactly once in their matching policy, immediately before section 3.3; English exactly matches `source.md`. Each is one nonempty paragraph, without replacement/control characters, unfinished markers or unintended Markdown delimiters.
- 33 English selector links resolve locally to all translated permalinks. All 37 regional entries from the dated ASC evidence map to existing policy routes using the actual app resolver conventions, including nb→no, regional Spanish/Portuguese/French, and both Chinese scripts. Source inventory: `ranked-analytics-consent/docs/analytics/ab006-paywall-2026-10-11/preparation-2026-10-15/locale-map.json`; this was not a fresh ASC fetch.
- Support changed only cancellation/refund sections. The corrected fallback wording now matches `Label("Manage Subscription", systemImage: "apple.logo")` in current `SettingsView.swift`. Refund approval distinction and Apple fallback remain explicit. Existing support URL inventory is unchanged.
- Full Jekyll rendering was not substituted with this preview: only the changed paragraphs and following heading, plus changed support sections, were parsed by bundled RDoc. Simple preview CSS is not the production theme.

## Findings and limits

No remaining source-delta defect was observed. The initially observed incorrect fallback label “Manage in App Store” was reported to the parent, corrected by the author, and rechecked against app source; the tester made no production edit.

Optional large-text preview finding (confirmed twice): the existing unbroken `reportaproblem.apple.com` literal produces support scrollWidth=325 vs clientWidth=319 at outer width 320px and font 24px. Steps: run the renderer then Chrome script, open `preview-10.png`, inspect the support column. In a real page, text should fit or wrap without horizontal clipping. The same URL and bold formatting already existed before this delta. This is a preview-specific limitation, not a confirmed production regression; verify against the actual Jekyll theme before deciding whether a fix is needed. Standard text passes at scrollWidth=clientWidth=319.

An early browser test harness assertion confused a border box width (320px) with client width (319px). The assertion was corrected in test code to compare the actual outer width. No product content was changed to satisfy it.

## Not verified

Actual Jekyll/kramdown/theme build (no Jekyll or kramdown installed; repository has only `_config.yml`, no build/test manifest or CI command), deployed routes/HTTP status for unpublished content, current ASC inventory, legal/linguistic accuracy, actual RevenueCat/Apple/device flow and consent behavior. These cannot be claimed from a source/text preview. Agent knowledge index was absent at both `.Codex/agents/knowledge/index.md` and `.codex/agents/knowledge/index.md`.

1. Build the branch with the real GitHub Pages/Jekyll configuration in an unpublished preview. Open all 34 privacy routes and `/support/` at a 320px viewport with normal text; each new paragraph must be rendered once above section 3.3 and match its source. Verify the two RTL pages keep right-to-left flow.
2. In that actual theme preview, enlarge the support page text and inspect `reportaproblem.apple.com`; it should remain readable without horizontal clipping. This resolves whether the limited-preview observation applies to production.
3. On the corresponding app build, open Settings → Subscription → Manage Subscription. Confirm Customer Center opens and the Apple-logo Manage Subscription fallback remains visible if Customer Center fails to load. Open the fallback and verify Apple subscription management appears.
4. Test cancellation/refund paths with an appropriate sandbox account. Merely opening management, choosing a survey answer or completing a refund request must not display a confirmed cancellation/refund approval unless Apple reports that result.
