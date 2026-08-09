# Wire all newly written blog posts into the portfolios, sitemap, and tracker.
import re, os, glob, csv, io

POSTS = [
    # Batch 1 — buyer-intent legal + compliance posts (2026-08-09)
    ("ai-waived-attorney-client-privilege-court.html", "Legal AI", "AI Waives Privilege in Court"),
    ("is-it-ethical-to-use-chatgpt-for-contract-review.html", "Legal AI", "ChatGPT Contract Review Ethics"),
    ("attorney-client-privilege-and-ai-plain-english-guide.html", "Legal AI", "Privilege and AI Guide"),
    ("gdpr-compliant-ai-2026-cloud-llms-fail.html", "Compliance", "GDPR-Compliant AI 2026"),
    # Batch 2 — legal AI evergreen + regulated industries (2026-08-09)
    ("ai-contract-review-for-lawyers.html", "Legal AI", "AI Contract Review for Lawyers"),
    ("private-legal-research-local-ai.html", "Legal AI", "Private Legal Research With Local AI"),
    ("document-qa-with-citations-law-firms.html", "Legal AI", "Document Q&A With Citations for Law Firms"),
    ("lawyers-ai-confidentiality-5-rules.html", "Legal AI", "AI Confidentiality: The 5 Rules for Lawyers"),
    ("review-100-contracts-ai.html", "Legal AI", "Review 100 Contracts in a Day With AI"),
    ("on-premise-ai-60-percent-market.html", "Compliance", "On-Premise AI Is Now 60% of the Market"),
    ("cloud-act-vs-gdpr-ai-data.html", "Compliance", "US Cloud Act vs EU GDPR for AI Data"),
    ("private-rag-regulated-industries-playbook.html", "Compliance", "Private RAG for Regulated Industries"),
    ("what-is-on-premise-llm-deployment.html", "Compliance", "What Is On-Premise LLM Deployment?"),
    ("deploy-llm-security-boundary.html", "Compliance", "Deploy an LLM Inside Your Security Boundary"),
    ("ai-regulated-industries-hipaa-soc2-gdpr.html", "Compliance", "AI for Regulated Industries: HIPAA, SOC 2, GDPR"),
    ("data-sovereignty-local-ai.html", "Compliance", "Data Sovereignty: AI Where Your Data Lives"),
    # Batch 3 — business owners & non-technical teams (2026-08-09)
    ("local-ai-without-cli.html", "Local AI", "Local AI Without a CLI"),
    ("laptop-ai-workstation-2026.html", "Local AI", "Your Laptop Is an AI Workstation"),
    ("stop-paying-per-seat-ai-fees.html", "Local AI", "Stop Paying Per-Seat AI Fees"),
    ("run-ai-own-computer-beginners.html", "Local AI", "Run AI on Your Own Computer: Beginner's Guide"),
    ("local-llm-small-business-10-use-cases.html", "Local AI", "Local LLMs for Small Business: 10 Use Cases"),
    ("how-much-ram-local-ai.html", "Local AI", "How Much RAM Do You Need for Local AI?"),
    ("8gb-vs-16gb-ram-local-llm.html", "Local AI", "8GB vs 16GB RAM for Local LLMs"),
    # Batch 4 — multilingual (2026-08-09)
    ("why-ai-ignores-pashto-dari.html", "Multilingual", "Why AI Ignores Pashto and Dari"),
    ("persian-ai-2026-local-models.html", "Multilingual", "Persian AI: Best Local Models for Farsi"),
    ("pashto-ai-assistant-own-device.html", "Multilingual", "Run a Pashto AI Assistant on Your Device"),
    ("ai-translation-dari-pashto-persian-urdu.html", "Multilingual", "AI Translation for Dari, Pashto, Persian, Urdu"),
    ("why-ai-fails-low-resource-languages.html", "Multilingual", "Why AI Fails Low-Resource Languages"),
    ("multilingual-assistant-underrepresented-language.html", "Multilingual", "Build a Multilingual AI Assistant"),
    # Batch 5 — enterprise RAG / agents (2026-08-09)
    ("rag-citations-table-stakes.html", "RAG", "RAG With Citations Is Table Stakes"),
    ("agentic-ai-2026-worth-building.html", "Agents", "Agentic AI in 2026: Worth Building?"),
    ("rag-answers-from-documents-proves-it.html", "RAG", "RAG That Answers From Your Documents"),
    ("hybrid-search-keyword-semantic.html", "RAG", "Hybrid Search: Keyword + Semantic"),
    ("rag-vs-fine-tuning-decision.html", "RAG", "The RAG vs Fine-Tuning Decision"),
    ("evaluate-rag-system.html", "RAG", "How to Evaluate a RAG System"),
    # Batch 6 — direct lead-gen (2026-08-09)
    ("custom-local-ai-system-cost-2026.html", "Lead Gen", "Custom Local AI System Cost in 2026"),
    ("hiring-ai-developer-10-questions.html", "Lead Gen", "Hiring an AI Developer? 10 Questions"),
    ("what-to-look-for-offline-ai-engineer.html", "Lead Gen", "What to Look for in an Offline AI Engineer"),
    ("ai-consulting-regulated-businesses.html", "Lead Gen", "AI Consulting for Regulated Businesses"),
]

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file_crlf(path, data):
    data = data.replace("\r\n", "\n").replace("\n", "\r\n")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(data)

def extract_meta(html):
    title = re.search(r"<title>(.*?)</title>", html, re.S)
    desc = re.search(r'<meta name="description" content="(.*?)">', html, re.S)
    return (title.group(1).strip() if title else ""), (desc.group(1).strip() if desc else "")

def make_card(fname, category, title, desc):
    return ('                <div class="blog-post">\r\n'
            '                    <div class="post-header">\r\n'
            f'                        <div class="post-category">{category}</div>\r\n'
            '                        <div class="post-date">August 2026</div>\r\n'
            '                    </div>\r\n'
            '                    <div class="post-content">\r\n'
            f'                        <h3>{title}</h3>\r\n'
            f'                        <p>{desc}</p>\r\n'
            f'                        <a href="{fname}" class="post-link">Read more <i class="fas fa-arrow-right"></i></a>\r\n'
            '                    </div>\r\n'
            '                </div>\r\n')

# 1. Build cards from actual file metadata
cards = []
for fname, category, _ in POSTS:
    if not os.path.exists(fname):
        print(f"MISSING FILE: {fname}")
        continue
    html = read_file(fname)
    title, desc = extract_meta(html)
    if not title or not desc:
        print(f"NO META: {fname}")
        continue
    cards.append((fname, category, title, desc))

print(f"Built {len(cards)} cards")

# 2. Insert cards into blog.html after the blog-grid opening
for page in ["blog.html"]:
    html = read_file(page)
    anchor = '            <div class="blog-grid">\r\n'
    if anchor not in html:
        anchor = '            <div class="blog-grid">\n'
    block = "".join(make_card(f, c, t, d) for f, c, t, d in cards)
    new_html = html.replace(anchor, anchor + block, 1)
    if new_html == html:
        print(f"ANCHOR NOT FOUND in {page}")
    else:
        write_file_crlf(page, new_html)
        print(f"Inserted {len(cards)} cards into {page}")

# 3. Add sitemap entries (skip existing)
sitemap = read_file("sitemap.xml")
existing = set(re.findall(r"<loc>(.*?)</loc>", sitemap))
added = 0
for fname, _, _, _ in cards:
    loc = f"https://Hussain-Nazary.github.io/{fname}"
    if loc in existing:
        continue
    entry = ('  <url>\r\n'
             f'    <loc>{loc}</loc>\r\n'
             '    <priority>0.9</priority>\r\n'
             '    <changefreq>monthly</changefreq>\r\n'
             '    <lastmod>2026-08-09</lastmod>\r\n'
             '  </url>\r\n')
    # insert before closing urlset
    sitemap = sitemap.replace("</urlset>", entry + "</urlset>", 1)
    added += 1
write_file_crlf("sitemap.xml", sitemap)
print(f"Added {added} sitemap entries")

# 4. Update tracker rows to published by matching the filename in column 7 (url)
#    Columns: 0 id, 1 cluster, 2 title, 3 primary_keyword, 4 status, 5 date, 6 url
tracker_lines = read_file("blog-tracker.csv").splitlines()
updated = 0
for fname, _, _, _ in cards:
    done = False
    for i, line in enumerate(tracker_lines):
        cols = next(csv.reader(io.StringIO(line)))
        if len(cols) >= 7 and cols[6].strip() == fname and cols[4].strip() == "planned":
            cols[4] = "published"
            cols[5] = "2026-08-09"
            out = io.StringIO()
            csv.writer(out, lineterminator="\n").writerow(cols)
            tracker_lines[i] = out.getvalue().rstrip("\n")
            updated += 1
            done = True
            break
    if not done:
        print(f"TRACKER ROW NOT FOUND for {fname}")
tracker_out = "\n".join(tracker_lines) + "\n"
write_file_crlf("blog-tracker.csv", tracker_out)
print(f"Updated {updated} tracker rows to published")
