# Design Doc: Client-Funnel Homepage Redesign

**Date:** 2026-08-22
**Status:** Approved (Approach A)

## Goals

- Make Hussain-Nazary.github.io read as a professional consultant profile aimed at **business clients**.
- Fix the overloaded homepage (11 sections) that "bores people".
- Drive every visitor toward one action: **email hussainnazary475@gmail.com** ("Discuss Your Project").
- Keep all SEO/AEO value by *moving* detailed product content to new dedicated pages instead of deleting it.
- Visual direction: **polished light theme** — same family as today, but refined typography scale, consistent spacing, disciplined color.

## Information Architecture

### Home page (`index.html`) — 6-section funnel

1. **Hero** — eyebrow, one-line value proposition ("I build AI that runs where your data lives."), short subtitle, primary CTA `mailto:` Discuss Your Project, secondary CTA View My Work (#work). Signature element: a mono-styled "spec sheet" card summarizing deployment/egress/languages — encodes the offline-AI value prop at a glance.
2. **Services (`#services`)** — 3 cards: Private & Local AI Systems · RAG & Knowledge Systems · SEO / GEO / AEO (sold service). Key phrases from cut sections fold into this copy.
3. **Selected Work (`#work`)** — 3 typographic case-study rows (Lawyer Assistant, GPT Calendar, GGUFLoader), each linking to its new project page + external site; spec chips per row. Footer line links to GitHub for smaller tools.
4. **About (`#about`)** — trimmed lead paragraph + credentials row (2024–present Independent AI Consultant · 2018–2021 Technical Lead P2P Crypto, Arta Services · Languages).
5. **Blog teaser (`#blog`)** — 2 sentences + Read the Blog button.
6. **Contact (`#contact`)** — email-first CTA block, plain-text email shown, GitHub secondary.

### New project pages (absorb today's flagship content)

- `lawyer-assistant-project.html` — screenshot, challenges, differentiators, benchmark stat bars, CTAs (site + GitHub).
- `gpt-calendar-project.html` — screenshot row, challenges, differentiators, simplified stats, CTAs.
- `ggufloader-project.html` — challenges, differentiators, by-the-numbers grid, CTAs.

Each page: own title/description/canonical/OG tags, breadcrumb-style back link, closing "Building something similar?" email CTA, shared navbar/footer.

### Removed from home (content relocated or folded)

Skills 6-card grid, Engineering Approach cards, Unified Architecture diagram, Why Local-First quotes, Programs & Applications cards (→ GitHub link), SEO websites list (→ Services card), mega flagship sections (→ project pages).

### Other pages

- `blog.html`: navbar updated to match new IA (Work / Services / About / Blog / Contact); blog styles preserved.
- `simple-portfolio.html`: legacy archive; keeps working via retained generic classes in stylesheet.
- `sitemap.xml`: 3 project pages added.

## Design tokens (polished light theme)

- **Palette:** ink `#14212B`, slate text `#44546A`, paper `#FFFFFF`, mist section bg `#F3F7F9`, hairline border `#DCE5EA`, accent deep teal `#0E7490` (trust/technical; replaces default blue #3498db).
- **Type:** Sora (display, headings) / Inter (body, unchanged load) / IBM Plex Mono (eyebrows, labels, spec chips, stats — engineering vernacular).
- **Layout:** max-width 1100px; sections separated by hairlines instead of alternating gray slabs; section header = mono eyebrow + H2; generous whitespace (~96px section padding desktop).
- **Signature:** mono "spec sheet" motif reused across hero card and work rows.
- **Quality floor:** responsive to mobile (hamburger menu), visible keyboard focus, prefers-reduced-motion respected.

## Files changed

| File | Change |
|---|---|
| `index.html` | Rewritten body per funnel; head/meta/JSON-LD kept |
| `simple-styles.css` | Full rewrite of design system; retains every class used by `blog.html` & `simple-portfolio.html`; adds new components |
| `lawyer-assistant-project.html` | New |
| `gpt-calendar-project.html` | New |
| `ggufloader-project.html` | New |
| `blog.html` | Nav links only |
| `sitemap.xml` | +3 URLs |

## Testing

Serve locally; browser screenshots desktop (1280px) + mobile (390px) for home, one project page, blog; verify anchors, mailto link, no broken images; check focus states.
