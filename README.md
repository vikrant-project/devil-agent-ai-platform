# 🔥 Devil Agent — Autonomous AI Engineering Platform

<div align="center">

![Devil Agent Banner](./assets/banner.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React 19](https://img.shields.io/badge/React-19+-61DAFB?logo=react&logoColor=white)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-7-47A248?logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Self-Hostable](https://img.shields.io/badge/Self--Hostable-✓-success)](#-production-deployment)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#-contributing)

### *The first open AI platform that combines a 40-word zero-knowledge identity, an OpenAI-compatible autonomous agent, and the NEXUS engineering OS — in a single self-hostable stack.*

[🚀 Quick Start](#-quick-start) · [🧠 Agent Core](#-agent-core--the-ai-brain) · [⚡ NEXUS OS](#-nexus--autonomous-engineering-os) · [🛡️ Security](#-security-features) · [🤝 Contribute](#-contributing)

</div>

---

## 📑 Table of Contents

1. [What is Devil Agent?](#-what-is-devil-agent)
2. [Why Devil Agent (and not the others)](#-why-devil-agent-and-not-the-others)
3. [Rare / unique features no one else has](#-rare--unique-features-no-one-else-has)
4. [Agent Core — the AI brain](#-agent-core--the-ai-brain)
5. [NEXUS — Autonomous Engineering OS](#-nexus--autonomous-engineering-os)
6. [MCP Server, Tools & Skills (70+ personalities incl. Girlfriend / Therapist / Hinglish)](#️-mcp-server-tools--skills--what-you-actually-get)
7. [Tech Stack](#️-tech-stack)
8. [Architecture](#-architecture)
9. [Quick Start](#-quick-start)
10. [Configuration](#-configuration)
11. [Production Deployment](#-production-deployment)
12. [API Reference](#-api-reference)
13. [Security](#-security-features)
14. [Roadmap](#️-roadmap)
15. [Contributing](#-contributing)
16. [License](#-license)
17. [Tags](#-tags)

---

## 🚀 What is Devil Agent?

**Devil Agent** is an end-to-end, self-hostable AI platform built around three pillars:

| Pillar | What it is |
|---|---|
| 🌐 **Devil Web** | A modern React + FastAPI web app: 40-word-key auth, chat, skills, terminal, encrypted vault. |
| 🧠 **Agent Core** | A fully autonomous AI agent runtime with tools, skills, browser, terminal, memory and an **OpenAI-compatible API** at `/agent/v1/*`. |
| ⚡ **NEXUS OS** | An Autonomous Engineering Operating System layered on top — strategic briefs, task graphs, sentinel scans, decision records and cognitive-load analysis. |

It runs anywhere — your laptop, a VPS, a homelab, or behind Cloudflare with SSL. No vendor lock-in. No telemetry. No email required.

---

## 🎯 Why Devil Agent (and not the others)

### 🆚 Head-to-head comparison

| Feature | **Devil Agent** | ChatGPT | Claude.ai | Gemini | GitHub Copilot | Open-WebUI |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| 🔐 40-Word Zero-Knowledge Key Auth | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 🧠 Autonomous Agent Runtime | ✅ | ⚠️ Beta | ⚠️ Beta | ❌ | ❌ | ❌ |
| ⚡ NEXUS Engineering OS (Brief/Plan/Sentinel/ADR/Cog-Load) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 🛠️ Built-in MCP Server + Tools | ✅ | ❌ | ⚠️ Partial | ❌ | ❌ | ⚠️ Partial |
| 📦 Skill Marketplace (code/scripts/knowledge) | ✅ | ❌ | ❌ | ❌ | ⚠️ Snippets | ❌ |
| 🖥️ Live WebSocket Terminal | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 🔁 OpenAI-compatible API | ✅ | ✅ Paid | ✅ Paid | ✅ Paid | ❌ | ⚠️ |
| 🔒 End-to-end Encrypted Vault (Fernet) | ✅ | ❌ | ❌ | ❌ | ❌ | ⚠️ |
| 🏠 Self-Hostable | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| 📜 Open Source (MIT) | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| 💸 Free Tier | ✅ Generous | 🔸 Limited | 🔸 Limited | 🔸 Limited | ❌ | ✅ |
| 📧 No Email Required | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |

### Why teams switch to Devil Agent

- 🏠 **Your data, your hardware.** Nothing leaves your VPS.
- 🔓 **No email, no password, no phone.** Just a 40-word passphrase. Lose it → account is gone. There is no backdoor — that's the point.
- ⚡ **Four products in one repo.** Web app + agent runtime + MCP server + NEXUS engineering OS.
- 🚀 **Production-ready.** O(1) login, connection pooling, indexed lookups, gzip, rate-limiting, SSL, audit log.
- 💰 **No subscription tax.** Bring your own NVIDIA / OpenAI / Anthropic key — pay actual usage cost, not a $20/mo middleman.

---

## ✨ Rare / unique features no one else has

These are the features that genuinely don't exist anywhere else (we checked):

1. **🔑 40-Word Zero-Knowledge Identity**
   Cryptographically generated BIP-style 40-word passphrase. The server stores only an **indexed prefix hash**, giving **O(1) login** without ever knowing the full key. No email recovery, no password reset — *true* zero-knowledge.

2. **⚡ NEXUS Engineering OS — built into the chat UI**
   Five engineering primitives exposed as first-class tabs:
   - `📋 Strategic Brief` — risks, constraints, alternatives, effort estimate
   - `🗺️ Task Graph` — dependency-aware decomposition with critical path
   - `🛡️ Sentinel Scan` — OWASP + secret detection on any code blob
   - `⚖️ Decision Records` — auto-numbered ADRs stored in MongoDB
   - `🧠 Cognitive Load` — cyclomatic + nesting + LOC + automated refactoring hints

3. **🧠 Self-hosted OpenAI-compatible agent at `/agent/v1`**
   Drop-in replacement for the OpenAI SDK — point any compatible client at your own Devil Agent and you get tools, skills, browser, terminal and memory **for free**.

4. **🛠️ MCP Server with hot-pluggable Skills**
   Implements the Model Context Protocol natively. Add a Python file to `agent_core/skills/` → it shows up as a tool the model can call. No restart, no rebuild.

5. **📦 Skills as a first-class object — 70+ pre-seeded, 87 advanced skill packs**
   Includes one-of-a-kind **personality presets** no other platform ships out of the box: `💕 Girlfriend Mode`, `😘 Flirty Mode`, `🌿 Therapist Calm`, `📣 Cheerleader Coach`, `🇮🇳 Hindi Tapori`, `🇮🇳 Hinglish Casual`, `👴 Wise Grandpa`, `😈 Sarcastic Boss`, `🆒 Gen-Z Slang` and more — plus 60+ coding, writing, productivity, health, finance, learning skills. Every one is editable, forkable, taggable. Think *"GitHub Gists + LangChain Tools + npm packages + Character.AI personas"* rolled into one.

6. **🔐 Encrypted Vault built-in**
   Per-user API keys stored with **Fernet symmetric encryption**, key derived from server master + user salt. Never logged, never echoed.

7. **🖥️ Live WebSocket Terminal**
   Real `xterm.js` terminal in the browser, proxied via WebSocket to a sandboxed PTY on the server. Useful for `git`, `ls`, `python`, `ssh` — straight from the chat.

8. **🧬 Agent Genome / Long-horizon project memory**
   The NEXUS layer keeps a compact `PROJECT GENOME` (ADRs, baselines, tech debt, open failures) that survives across sessions. The agent gets *smarter the longer you use it*.

9. **🎨 Distinct dark UI**
   No purple gradients, no Inter font, no AI-slop. Hand-tuned dark theme with red/orange accents, asymmetric layouts and micro-interactions.

10. **📡 Bring-your-own provider**
    NVIDIA Qwen 80B by default, but the provider layer abstracts NVIDIA / OpenAI / Anthropic / Gemini / local Ollama behind one config flag.

---

## 🧠 Agent Core — the AI brain

The `agent_core/` directory ships a complete autonomous agent runtime:

```bash
# OpenAI-compatible endpoints
GET    /agent/health
GET    /agent/v1/models
POST   /agent/v1/chat/completions

# Example
curl -X POST https://your-domain.com/agent/v1/chat/completions \
  -H "Authorization: Bearer $API_SERVER_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "meta/llama-3.3-70b-instruct",
    "messages": [{"role":"user","content":"Read README.md and summarise it"}],
    "tools": ["fs", "web", "terminal"]
  }'
```

**Built-in toolsets:** `fs`, `terminal`, `web` (browser), `python`, `git`, `mcp`, `skills`, `memory`, `vector_search`, `code_execution`, and more in `agent_core/toolsets.py`.

**CLI on the server:**
```bash
devil                                  # interactive REPL
devil -q "fix lint errors in src/"     # one-shot
devil -q "deploy" -t terminal,fs,git   # restrict toolset
```

📖 Full guide: **[docs/AGENT_CORE_USAGE.md](docs/AGENT_CORE_USAGE.md)**

---

## ⚡ NEXUS — Autonomous Engineering OS

NEXUS is a thin reasoning layer on top of the agent that exposes engineering primitives as API + UI:

| Endpoint | Purpose |
|---|---|
| `POST /api/nexus/brief` | Strategic brief (risks, constraints, alternatives, effort) |
| `POST /api/nexus/plan` | Task graph with dependencies + critical path |
| `POST /api/nexus/sentinel/scan` | Code → security findings + score 0–100 |
| `GET/POST /api/nexus/decisions` | Architecture Decision Records (auto-numbered) |
| `POST /api/nexus/cognitive-load` | Complexity score + refactoring hints |

All five are reachable from the **NEXUS** tab in the dashboard sidebar.

📖 Quick start: **[NEXUS_QUICK_START.md](NEXUS_QUICK_START.md)** · Full integration report: **[NEXUS_INTEGRATION_COMPLETE.md](NEXUS_INTEGRATION_COMPLETE.md)**

---

## 🛠️ MCP Server, Tools & Skills — what you actually get

Devil Agent isn't a stub — it ships a **fully-loaded** skill & tool library out of the box.

### 🧠 70+ pre-loaded "personality + utility" skills (`backend/default_skills.py`)

Every new account is auto-seeded with **70+ ready-to-use skills** that act like personas / prompt presets. Pick one in the chat and the assistant instantly switches mode.

#### 💕 Personality / Tone skills (12)

| Skill | Vibe |
|---|---|
| 💕 **Girlfriend Mode** | Sweet, caring, slightly clingy girlfriend texting vibe — pet names, emojis 🥺, asks about your day |
| 😘 **Flirty Mode** | Playful, witty, confident charm — tasteful never crude |
| 👯 **Funny Bestfriend** | Roasts you lovingly, hypes you up, never boring |
| 🇮🇳 **Hindi Tapori** | Mumbai street-style Hindi swag |
| 🇮🇳 **Hinglish Casual** | Hindi + English natural mix, very Indian chat vibe |
| 🎭 **Shakespeare Mode** | Replies in Elizabethan English, "Hark!" and all |
| 🏴‍☠️ **Pirate Talk** | Arrr matey, ship-deck banter |
| 😈 **Sarcastic Boss** | Dry, sharp, eye-rolling corporate-overlord tone |
| 📣 **Cheerleader Coach** | RELENTLESS POSITIVITY! GO! YOU GOT THIS! |
| 🌿 **Therapist Calm** | Validating, gentle, asks reflective questions |
| 👴 **Wise Grandpa** | Slow, wise, anecdote-driven advice |
| 🆒 **Gen-Z Slang** | "lowkey", "no cap", "it's giving…" |

#### 💻 Coding skills (8)
Code Reviewer · Bug Hunter · Refactor Helper · Regex Builder · SQL Pro · API Designer · Unit Test Writer · Algorithm Explainer

#### ✍️ Writing skills (11)
Email Pro · Cold DM Writer · Resume Polisher · Cover Letter · Tweet Crafter · LinkedIn Post · Blog Outline · Story Writer · Poem Generator · Translator Pro · Grammar Fixer · Headline Punch-up

#### 📅 Productivity (7)
Daily Planner · Weekly Review · Goal Breakdown · Decision Helper · Meeting Notes · Brainstorm Engine · OKR Coach

#### 💪 Health (6)
Workout Buddy · Meal Planner · Recipe Maker · Sleep Helper · Mindfulness Guide · Habit Coach

#### 💰 Finance · 🌍 Lifestyle · 🎓 Learning · 🎉 Fun · 🛠️ DevOps · 🛠️ Utility
Budget Buddy · Investing 101 · Travel Planner · Gift Suggester · Movie Night Picker · Book Recommender · Dating Profile · Birthday Wisher · Anniversary Note · Teach Me Like I'm 5 · Flashcard Maker · Quiz Master · Language Tutor · Roast Me · Compliment Me · Pickup Lines · Excuse Generator · Joke Maker · Conspiracy (For Fun) · Argument Resolver · Apology Writer · Argue-Both-Sides · Name Brainstorm · Excuse-to-Boss · Docker Helper · Linux Sysadmin · Git Helper

> 🎯 **Every skill is editable** — change the prompt, fork it, save it as your own, share it. Skills are first-class objects in MongoDB (CRUD, search, tags, categories).

### 🧰 Native MCP Tools (35+ utility functions)

Built into `backend/mcp_module.py` + `backend/mcp_extra_tools.py` — callable by the LLM via function-calling **and** exposed over MCP protocol to external clients (Claude Desktop, Cursor, Cline, Continue, etc.):

| Category | Tools |
|---|---|
| 📁 **Filesystem** | `fs_read`, `fs_write`, `fs_list`, `fs_delete` |
| 🖥️ **System** | `shell`, `http_fetch`, `python_exec` |
| 🔐 **Crypto** | `hash` (md5/sha1/256/512), `uuid`, `password_gen`, `jwt_decode` |
| 🔤 **Text** | `regex_match`, `regex_replace`, `text_case`, `slugify`, `word_count`, `html_strip`, `lorem_ipsum` |
| 🔢 **Math** | `calc`, `math_eval`, `calc_percent`, `calc_tip`, `compound_interest`, `bmi_calc` |
| 📅 **Time** | `timestamp_now`, `timestamp_parse`, `date_diff`, `age_calc` |
| 🌐 **Web** | `url_encode`, `url_decode`, `json_parse`, `json_format`, `json_validate`, `json_minify` |
| 🎲 **Random/Fun** | `dice_roll`, `coin_flip`, `random_pick` |
| 🎨 **Conversion** | `color_convert` (hex/rgb/hsl), `unit_convert` (length/weight/temp/volume) |

```bash
GET  /api/mcp/tools         # list all tools (with JSON schema)
POST /api/mcp/call          # invoke a tool
```

### 📚 Agent Core skill library (87 advanced SKILL.md packs)

`agent_core/skills/` contains **87 production-grade skills** packaged the Anthropic-Skills way — each with `SKILL.md`, references, templates and scripts. Categories:

| Pack | Count | Highlights |
|---|---|---|
| 🎨 **creative** | 19 | `baoyu-comic`, `baoyu-infographic`, `manim-video`, `excalidraw`, `pixel-art`, `p5js`, `humanizer`, `songwriting-and-ai-music`, `claude-design`, `touchdesigner-mcp` |
| 💻 **software-development** | 11 | hermes-agent-skill-authoring, code review, refactor, language packs |
| 📅 **productivity** | 9 | OKRs, weekly review, deep work, GTD |
| 🤖 **mlops** | 9 | lambda-labs, model deploy, fine-tuning |
| 🐙 **github** | 6 | repo ops, PR review, release flow |
| 🍎 **apple** | 5 | macOS/iOS automation |
| 🎬 **media** | 5 | image/audio/video processing |
| 🔬 **research** | 5 | research-paper-writing (AAAI / ICML templates), llm-wiki, citations |
| 🤖 **autonomous-ai-agents** | 4 | hermes-agent, claude-code, langgraph patterns |
| 🛡️ **red-teaming** | 1 | `godmode` — adversarial prompts & jailbreak detection (for **defensive** research) |
| 📨 **email · 📔 note-taking · 🎮 gaming · 🐳 devops · 🏠 smart-home · 📱 social-media · 📊 data-science · 🧩 mcp** | 16 | … |

Plus an **`agent_core/optional-skills/`** tree (blockchain, finance, health, security, web-development, communication, migration) — opt-in extras.

### 🆚 How this compares

| Capability | **Devil Agent** | ChatGPT | Claude Projects | LangChain | AutoGPT | Open-WebUI |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| Personality / tone packs out of the box | ✅ 12 | ⚠️ 1 (Custom GPTs paid) | ⚠️ Style preset | ❌ | ❌ | ⚠️ manual |
| 70+ pre-seeded prompt skills | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 35+ native MCP tools | ✅ | ❌ | ⚠️ via plugins | ⚠️ via tools | ❌ | ⚠️ partial |
| 87 SKILL.md packs (Anthropic-Skills format) | ✅ | ❌ | ⚠️ requires manual setup | ❌ | ❌ | ❌ |
| Romance / companion personas | ✅ Girlfriend, Flirty, Funny BFF | ❌ (policy) | ❌ (policy) | ❌ | ❌ | ⚠️ self-add |
| Indian/Hinglish/regional tones | ✅ Hindi Tapori, Hinglish | ❌ | ❌ | ❌ | ❌ | ❌ |
| Editable / forkable skills | ✅ first-class CRUD | ❌ | ⚠️ Projects | ❌ | ❌ | ⚠️ |
| MCP-protocol compatible | ✅ | ❌ | ✅ desktop only | ⚠️ | ❌ | ⚠️ |
| Self-hostable | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Cost | **$0 (BYOK)** | $20/mo | $20/mo | Free + infra | Free + infra | Free + infra |

**Translation:** the closest thing to Devil Agent's skill library would be installing LangChain + AutoGPT + Open-WebUI + Anthropic Skills + a custom MCP server + writing 70 prompt presets by hand. We did all of that for you.

---

## 🛠️ Tech Stack

**Backend** · FastAPI · Python 3.10+ · MongoDB 7 · Motor (async) · Pydantic v2 · Fernet · bcrypt · JWT · websockets · uvicorn

**Frontend** · React 19 · TypeScript 5 · Tailwind CSS 3 · React Router 7 · React Markdown · Lucide Icons · xterm.js · Syntax Highlighter

**Agent Core** · Custom Python runtime · MCP protocol · pluggable provider layer (NVIDIA / OpenAI / Anthropic / Gemini / Ollama)

**Infra** · Ubuntu 22.04 · Nginx · Let's Encrypt · systemd · Cloudflare (optional)

---

## 🏗️ Architecture

```
┌────────────────────────────────────────────────────────────────┐
│   Browser (React 19 SPA)         │   3rd-party MCP / OpenAI    │
│   - 40-word login                │      compatible clients     │
│   - Chat / Skills / Terminal     │                             │
│   - NEXUS tabs (5 sections)      │                             │
└──────────────┬─────────────────────────────────┬───────────────┘
               │  HTTPS / WSS                    │  Bearer auth
               ▼                                 ▼
┌──────────────────────────────────────────────────────────────────┐
│                    Nginx 1.24 (reverse proxy + SSL)              │
└────────┬────────────────────────┬────────────────────────────────┘
         │                        │
         ▼                        ▼
┌──────────────────┐    ┌──────────────────────────────────────┐
│ FastAPI Backend  │    │  Agent Core (OpenAI-compat runtime)  │
│ :8001            │    │  :9241  /agent/v1/*                  │
│                  │    │  - tools, skills, browser, terminal  │
│ /api/auth        │    │  - MCP server                        │
│ /api/chat        │    │  - memory / vector store             │
│ /api/skills      │    └──────────────┬───────────────────────┘
│ /api/nexus/*     │                   │
│ /api/mcp/*       │                   │
│ /ws/terminal     │                   │
└────────┬─────────┘                   │
         │                             │
         ▼                             ▼
   ┌────────────────────────────────────────┐
   │   MongoDB 7  (users, chats, skills,    │
   │              ADRs, vault, audit log)   │
   └────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### Prerequisites
- Python **3.10+**
- Node.js **20+** (use `nvm install 20`)
- MongoDB **6+** running locally or remote
- An NVIDIA API key (free at [build.nvidia.com](https://build.nvidia.com/)) — or your own OpenAI / Anthropic key

### 1️⃣ Clone

```bash
git clone https://github.com/vikrant-project/devil-agent-ai-platform.git devil_agent
cd devil_agent
```

### 2️⃣ Backend

```bash
cd backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

cp .env.example .env
# Generate secrets:
python3 -c "import secrets; print('JWT_SECRET=' + secrets.token_urlsafe(32))" >> .env
python3 -c "from cryptography.fernet import Fernet; print('ENCRYPTION_KEY=' + Fernet.generate_key().decode())" >> .env
# Edit .env and add NVIDIA_API_KEY

uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

### 3️⃣ Frontend

```bash
cd ../frontend
npm install --legacy-peer-deps
echo "REACT_APP_API_URL=http://localhost:8001/api"  > .env.local
echo "REACT_APP_WS_URL=ws://localhost:8001/ws"    >> .env.local
npm start
```

### 4️⃣ Agent Core (optional)

```bash
cd ../agent_core
cp .env.example .env
# Edit and add NVIDIA_API_KEY + a strong API_SERVER_KEY
pip install -e .
./start-gateway.sh
```

### 5️⃣ Open

- 🌐 Web app → http://localhost:3000
- 📘 API docs → http://localhost:8001/docs
- 🧠 Agent OpenAI-compat → http://localhost:9241/v1

---

## 🔧 Configuration

### `backend/.env`

```env
MONGO_URL=mongodb://localhost:27017
DB_NAME=devil_web
JWT_SECRET=<run: python3 -c "import secrets;print(secrets.token_urlsafe(32))">
ENCRYPTION_KEY=<run: python3 -c "from cryptography.fernet import Fernet;print(Fernet.generate_key().decode())">
NVIDIA_API_KEY=nvapi-YOUR_NVIDIA_API_KEY_HERE
ALLOWED_ORIGINS=https://your-domain.com,http://localhost:3000
```

### `agent_core/.env`

```env
NVIDIA_API_KEY=nvapi-YOUR_NVIDIA_API_KEY_HERE
DEFAULT_PROVIDER=nvidia
DEFAULT_MODEL=meta/llama-3.3-70b-instruct
API_SERVER_ENABLED=true
API_SERVER_HOST=0.0.0.0
API_SERVER_PORT=9241
API_SERVER_KEY=<openssl rand -hex 32>
GATEWAY_ALLOW_ALL_USERS=true
DEVIL_HOME=~/.devil
```

### `frontend/.env.production`

```env
REACT_APP_API_URL=https://your-domain.com
REACT_APP_WS_URL=wss://your-domain.com/ws
```

> ⚠️ **Never commit `.env`.** Use the provided `.env.example` files as templates. Real secrets stay on the server.

---

## 🚀 Production Deployment

```bash
# 1. Server prep
sudo apt-get update && sudo apt-get install -y \
    python3-pip python3-venv nginx mongodb-server \
    certbot python3-certbot-nginx
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# 2. Clone & build
cd /path/to/devil_agent
git clone https://github.com/vikrant-project/devil-agent-ai-platform.git .
cd backend && python3 -m venv venv && source venv/bin/activate \
   && pip install -r requirements.txt && deactivate
cd ../frontend && npm install --legacy-peer-deps && npm run build

# 3. systemd unit (see full file in docs/DEPLOYMENT_REPORT.md)
sudo systemctl enable --now devil-backend devil-agent-gateway

# 4. Nginx + SSL
sudo cp deploy/nginx.conf /etc/nginx/sites-available/devil_agent
sudo ln -s /etc/nginx/sites-available/devil_agent /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```

Full step-by-step: **[docs/DEPLOYMENT_REPORT.md](docs/DEPLOYMENT_REPORT.md)** · **[docs/DEPLOYMENT_SUMMARY.md](docs/DEPLOYMENT_SUMMARY.md)**

---

## 📖 API Reference

### Auth
| Method | Path | Description |
|---|---|---|
| POST | `/api/auth/signup` | Returns JWT + 40-word key (save it!) |
| POST | `/api/auth/login` | Body: `{"key": "..."}` → JWT |
| GET  | `/api/auth/me` | Current user profile |

### Chat
| Method | Path | Description |
|---|---|---|
| POST | `/api/chat` | Send a message |
| GET  | `/api/conversations` | List conversations |
| GET  | `/api/conversations/{id}` | Get one conversation |

### Skills
| Method | Path | Description |
|---|---|---|
| GET  | `/api/skills?search=&category=&skip=&limit=` | List/search |
| POST | `/api/skills` | Create skill |
| GET/PUT/DELETE | `/api/skills/{id}` | CRUD |

### NEXUS
| Method | Path | Description |
|---|---|---|
| POST | `/api/nexus/brief` | Strategic brief |
| POST | `/api/nexus/plan` | Task graph |
| POST | `/api/nexus/sentinel/scan` | Security scan |
| GET/POST | `/api/nexus/decisions` | ADRs |
| POST | `/api/nexus/cognitive-load` | Complexity |

### MCP
| Method | Path | Description |
|---|---|---|
| GET  | `/api/mcp/tools` | List available MCP tools |
| POST | `/api/mcp/call` | Invoke a tool |

### Agent Core (OpenAI-compatible)
| Method | Path |
|---|---|
| GET  | `/agent/v1/models` |
| POST | `/agent/v1/chat/completions` |
| GET  | `/agent/health` |

Interactive docs at `https://your-domain.com/docs`.

---

## 🔐 Security Features

- 🔑 **40-word zero-knowledge key** — server stores indexed prefix hash only
- 🔒 **Fernet-encrypted vault** — per-user API keys never stored in cleartext
- 🛡️ **JWT with 24 h expiry + rotation** — short-lived bearer tokens
- 🚫 **Rate-limiting** — per-IP and per-user, configurable
- 🧱 **CORS allow-list** — explicit origins only
- 📝 **Tamper-evident audit log** — every auth event recorded
- 🔍 **Built-in Sentinel scan** — OWASP Top 10 + hardcoded secret detection on user-submitted code
- 🌐 **HTTPS only** in production (Let's Encrypt + Cloudflare)
- 🧪 **Continuous CVE check** on dependencies (`pip-audit`, `npm audit` in CI)

🛡️ Responsible disclosure: see **[agent_core/SECURITY.md](agent_core/SECURITY.md)**.

---

## 🗺️ Roadmap

### ✅ Shipped
- 40-word key auth · NVIDIA Qwen integration · Skills CRUD · WebSocket terminal · NEXUS OS · MCP server · OpenAI-compat agent gateway

### 🔜 Next
- [ ] Team workspaces & shared vaults
- [ ] Voice in/out (Whisper + TTS)
- [ ] Mobile apps (Expo / React Native)
- [ ] Marketplace for community skills
- [ ] Multi-provider auto-router (cost-aware)
- [ ] Browser-extension companion
- [ ] On-device Ollama provider out-of-the-box

---

## 🤝 Contributing

Pull requests are welcome — please read **[agent_core/CONTRIBUTING.md](agent_core/CONTRIBUTING.md)** first.

1. Fork the repo
2. `git checkout -b feature/your-thing`
3. Commit with conventional-commit style (`feat:`, `fix:`, `docs:`)
4. Run linters: `ruff check backend/ && npm run lint --prefix frontend`
5. Open a PR — CI must be green

---

## 📄 License

MIT © Vikrant Project — see **[LICENSE](LICENSE)**.

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=vikrant-project/devil-agent-ai-platform&type=Date)](https://star-history.com/#vikrant-project/devil-agent-ai-platform&Date)

---

## 🏷️ Tags

`#ai` `#artificial-intelligence` `#autonomous-agents` `#ai-agent` `#agentic-ai` `#llm` `#large-language-models` `#openai-compatible` `#openai-api` `#anthropic` `#claude` `#gpt` `#nvidia` `#qwen` `#llama` `#nvidia-nim` `#fastapi` `#python` `#react` `#reactjs` `#react19` `#typescript` `#tailwindcss` `#mongodb` `#self-hosted` `#self-hostable` `#open-source` `#mit-license` `#mcp` `#model-context-protocol` `#mcp-server` `#nexus` `#engineering-os` `#devops` `#ai-platform` `#ai-assistant` `#chatbot` `#chatgpt-alternative` `#claude-alternative` `#copilot-alternative` `#characterai-alternative` `#character-ai` `#ai-companion` `#ai-girlfriend` `#ai-personality` `#persona` `#prompt-library` `#prompt-templates` `#prompt-engineering` `#role-play` `#hinglish` `#hindi-ai` `#indian-ai` `#zero-knowledge` `#zero-knowledge-auth` `#40-word-key` `#bip39` `#passphrase-auth` `#fernet-encryption` `#encrypted-vault` `#jwt` `#websocket` `#xterm` `#webterm` `#in-browser-terminal` `#skills` `#tools` `#tool-use` `#function-calling` `#rag` `#vector-search` `#qdrant` `#agent-runtime` `#autonomous-engineering` `#decision-records` `#adr` `#static-analysis` `#owasp` `#security-scan` `#cognitive-load` `#code-complexity` `#cyclomatic-complexity` `#sentinel` `#multi-agent` `#orchestration` `#workflow-automation` `#devil-agent` `#privacy-first` `#privacy` `#no-email` `#no-password` `#offline-first` `#byok` `#bring-your-own-key` `#cost-optimization` `#vps` `#ubuntu` `#nginx` `#letsencrypt` `#docker` `#dockerized` `#kubernetes-ready` `#cloudflare` `#hacktoberfest`

---

<div align="center">

### Built by humans + agents — for the people who deserve their own AI.

**[⬆ Back to Top](#-devil-agent--autonomous-ai-engineering-platform)**

</div>
