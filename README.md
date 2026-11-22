# Google News Headlines & Articles Scraper

Extract real-time global news headlines, publisher details, publication dates, article URLs, and clean snippets directly from [Google News](https://news.google.com/) into clean JSON, CSV, or Excel in milliseconds.

Powered by a lightweight HTTP/RSS engine running on just **128 MB RAM** with zero browser overhead.

---

## ⚡ Speed & Cost Efficiency Comparison

Traditional Google News scrapers rely on heavy headless browsers (Puppeteer or Playwright), consuming 2–4 GB RAM, spinning up complex browser tabs, and suffering from slow DOM rendering, captchas, and frequent timeouts. Our Google News Scraper connects directly to live XML/RSS feeds with TLS fingerprint impersonation, delivering extreme speed at a fraction of the compute cost.

| Metric | Traditional Puppeteer / Playwright | Google News Scraper (This Actor) |
| :--- | :--- | :--- |
| **Memory Requirement** | 2,048 MB – 4,096 MB RAM | **128 MB RAM** |
| **Speed per 50 Articles** | 25 – 45 seconds | **0.2 – 0.8 seconds** |
| **Compute Overhead** | ~$0.08 per run | **$0.0001 per run** |
| **Pricing Model** | $30 – $50 / month subscription | **Pay-Per-Event ($0.005 / item)** |
| **Cloud Reliability** | 78% (timeouts, DOM crashes) | **99.9% (zero browser dependencies)** |
| **AI / MCP Compatibility**| ❌ Complex DOM output | ✅ **100% Typed Clean JSON** |

---

## 📋 Sample JSON Output

Every extracted news article includes verified headlines, publisher names, source URLs, publication timestamps, and clean summaries:

```json
{
  "title": "Anthropic Mathematician Claims to Solve Riemann Hypothesis With Help From Claude - The New York Times",
  "link": "https://news.google.com/rss/articles/CBMijAFBVV95cUxQMU96R3p...",
  "source": "The New York Times",
  "sourceUrl": "https://www.nytimes.com",
  "publishedAt": "Fri, 20 Nov 2026 21:46:33 GMT",
  "snippet": "Anthropic Mathematician Claims to Solve Riemann Hypothesis With Help From Claude The New York Times",
  "topic": "Technology & AI",
  "searchQuery": "artificial intelligence",
  "guid": "CBMijAFBVV95cUxQMU96R3p..."
}
```

---

## 🎯 Key Use Cases

1. **Brand & PR Sentiment Monitoring**: Track mentions of your company, founders, competitors, or client brands across thousands of global news publications in real time.
2. **Financial Market & Macro Signals**: Feed breaking macroeconomic, earnings, and industry headlines into quantitative sentiment models and automated trading strategies.
3. **AI Agent Research & MCP Tools**: Provide LLM assistants (Claude, Cursor, LangChain) with real-time world events and curated news briefings in under 1 second.
4. **Content Curation & Industry Newsletters**: Automatically aggregate top weekly news stories for specialized tech, AI, healthcare, or crypto newsletters via n8n or Make.com.
5. **SEO & Competitor Intelligence**: Monitor which media outlets and journalists are writing about specific industry keywords to identify PR outreach targets.

---

## ⚙️ Input Parameters

| Field | Type | Description | Default | Prefill |
| :--- | :--- | :--- | :--- | :--- |
| `search` | String | Keyword, topic, or company to search (e.g. `artificial intelligence`, `nvidia`). Leave empty for top stories. | `""` | `"artificial intelligence"` |
| `topic` | String | Pre-filtered news category: `NONE` (search / top stories), `TECHNOLOGY`, `BUSINESS`, `WORLD`, `SCIENCE`, `HEALTH`, `ENTERTAINMENT`, `SPORTS`. | `"NONE"` | `"NONE"` |
| `timeRange` | String | Filter articles by publication time: `any`, `1h` (past hour), `1d` (past 24h), `7d` (past week), `30d`, `1y`. | `"any"` | `"any"` |
| `language` | String | Google News language code (e.g. `en-US`, `uk-UA`, `de-DE`, `fr-FR`, `es-ES`). | `"en-US"` | `"en-US"` |
| `country` | String | Google News regional edition country code (e.g. `US`, `UA`, `GB`, `DE`, `FR`). | `"US"` | `"US"` |
| `maxItems` | Integer | Maximum number of news articles to extract. | `20` | `5` |

---

## 🤖 AI Agents & Apify MCP Server Integration

This Actor produces pure typed JSON ideal for AI agents running on Cursor, Claude Desktop, or LangChain via the **Apify MCP Server**.

### Claude Desktop / Cursor Config (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": ["-y", "@apify/mcp-server"],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

### Prompt Example for AI Agent:
> *"Fetch the top 5 breaking technology news articles about Artificial Intelligence published in the past 24 hours from Google News and summarize key developments."*

---

## 🔄 Automated No-Code Sync (n8n & Make)

Included inside `workflows/n8n_template.json` is a ready-to-import workflow template that triggers on a schedule, extracts news by keyword via Apify, and delivers updates directly to Google Sheets, Slack, Discord, or Notion.

---

## ❓ Frequently Asked Questions (FAQ)

### Is scraping Google News legal?
Yes. Google News syndicates publicly indexed headlines, publisher names, and article snippets via public RSS feeds. This Actor only extracts public metadata and does not bypass paywalls or access private data.

### How much does it cost to extract 1,000 news articles?
With our Pay-Per-Event pricing of **$0.005 per article**, extracting 1,000 records costs just **$5.00** (with automatic volume discounts for Bronze, Silver, and Gold tiers). There are zero monthly commitments or recurring platform subscriptions.

### Can I monitor breaking news from the past hour?
Yes. Select `timeRange` as `1h` (or pass `when:1h` in your query) to fetch breaking stories published within the last 60 minutes.

### Does this scraper support international languages and countries?
Yes. You can customize `language` (e.g. `de-DE`, `uk-UA`, `fr-FR`) and `country` (e.g. `DE`, `UA`, `FR`, `GB`) to extract localized regional editions worldwide.

### Does this scraper require proxies?
No manual proxy configuration is required. The Actor runs seamlessly with built-in zero-configuration proxy routing on the Apify platform.

---

## 🔗 Explore More High-Speed B2B Scrapers & Enrichers by Our Team

| Actor Name | Best Use Case | Pricing Model | Link |
| :--- | :--- | :--- | :--- |
| **Devpost Hackathons Scraper** | Global AI Competitions, Bounties & Cash Prizes | Pay-Per-Event ($0.005) | [Apify Store](https://apify.com/archibald322/devpost-hackathons-scraper) |
| **CoinMarketCap Crypto Scraper** | Live Crypto Prices, Market Cap, 24h Vol | Pay-Per-Event ($0.005) | [Apify Store](https://apify.com/archibald322/coinmarketcap-scraper) |
| **Peerlist Tech Jobs & Salaries** | Tech & AI Career Feeds, Verified Salaries | Pay-Per-Event ($0.005) | [Apify Store](https://apify.com/archibald322/peerlist-jobs-scraper) |
| **Hacker News Posts & Startups** | Tech Trends, Show HN Startups, Hiring Threads | Pay-Per-Event ($0.005) | [Apify Store](https://apify.com/archibald322/hackernews-posts-scraper) |
| **Substack Newsletter Scraper** | Top Newsletters, Posts, Authors & Intel | Pay-Per-Event ($0.005) | [Apify Store](https://apify.com/archibald322/substack-newsletter-scraper) |
| **RemoteOK Tech Jobs Scraper** | Global Remote Engineering & AI Roles | Pay-Per-Event ($0.005) | [Apify Store](https://apify.com/archibald322/remoteok-jobs-scraper) |
| **Y Combinator Startups Scraper** | 6,400+ YC Companies, Founders, Socials | Pay-Per-Event ($0.008) | [Apify Store](https://apify.com/archibald322/ycombinator-startups-scraper) |
| **TrustMRR SaaS Revenue Scraper** | Verified Micro-SaaS ARR, Multiples & Deals | Pay-Per-Event ($0.005) | [Apify Store](https://apify.com/archibald322/trustmrr-startups-scraper) |
| **Hugging Face AI Models Scraper** | 1M+ Open-Source LLMs, Weights & Datasets | Pay-Per-Event ($0.005) | [Apify Store](https://apify.com/archibald322/huggingface-models-scraper) |
| **Ashby ATS Tech Jobs Scraper** | High-growth Tech & AI Startup Vacancies | Pay-Per-Event ($0.005) | [Apify Store](https://apify.com/archibald322/ashby-jobs-scraper) |
| **Greenhouse ATS Jobs Scraper** | Enterprise Careers & Tech Vacancies | Pay-Per-Event ($0.005) | [Apify Store](https://apify.com/archibald322/greenhouse-jobs-scraper) |
| **Lever ATS Jobs Scraper** | Enterprise Tech & AI Talent Recruitment | Pay-Per-Event ($0.005) | [Apify Store](https://apify.com/archibald322/lever-jobs-scraper) |
| **Clutch B2B Agencies Scraper** | Software Agencies, Verified B2B Reviews | Pay-Per-Event ($0.008) | [Apify Store](https://apify.com/archibald322/clutch-agencies-scraper) |
| **Wellfound Startups & Jobs** | AngelList Startup Ecosystem & Jobs | Pay-Per-Event ($0.008) | [Apify Store](https://apify.com/archibald322/wellfound-jobs-scraper) |
| **Bulldogjob Tech Jobs Scraper** | European IT Careers & Verified Salaries | Pay-Per-Event ($0.005) | [Apify Store](https://apify.com/archibald322/bulldogjob-scraper) |
| **TheProtocol Tech Jobs Scraper** | IT Job Postings, Salaries & Tech Stacks | Pay-Per-Event ($0.005) | [Apify Store](https://apify.com/archibald322/theprotocol-scraper) |
