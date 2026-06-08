# 🔥 Devil Agent - AI-Powered Assistant Platform

<div align="center">

![Devil Agent Banner](./assets/banner.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![React](https://img.shields.io/badge/React-19+-61DAFB.svg)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-009688.svg)](https://fastapi.tiangolo.com/)

**The Next-Generation AI Assistant with Unique 40-Word Key Authentication**

[🌐 Live Demo](https://your-domain.com) | [📖 Documentation](#documentation) | [🚀 Quick Start](#quick-start) | [🤝 Contributing](#contributing)

</div>

---

## 🚀 About Devil Agent

Devil Agent is a revolutionary AI-powered assistant platform that combines cutting-edge security with powerful AI capabilities. Unlike traditional authentication systems, Devil Agent uses a **unique 40-word key authentication** mechanism, providing unparalleled security and privacy.

### ✨ Key Features

- 🔐 **Unique 40-Word Key Authentication** - No email, no password, just a secure 40-word passphrase
- 🤖 **Powered by NVIDIA Qwen 80B** - State-of-the-art AI model for intelligent conversations
- 💬 **Real-Time AI Chat** - Instant responses with conversation history
- 📝 **Skills Management** - Store and manage code snippets, scripts, and knowledge
- 🎯 **User Tier System** - Free, Pro, and Enterprise tiers with different limits
- 🔒 **Encrypted API Keys** - All sensitive data encrypted at rest
- ⚡ **Optimized Performance** - Connection pooling, caching, and indexed lookups
- 🎨 **Beautiful Dark-Themed UI** - Modern, responsive interface with red/orange gradients
- 🌐 **WebSocket Terminal** - Execute commands remotely via secure WebSocket
- 📊 **Usage Analytics** - Track your AI usage and statistics
- 🔍 **Advanced Search** - Search through conversations and skills
- 📤 **Export Conversations** - Export chats as PDF or Markdown
- 🏷️ **Skill Categorization** - Organize skills with tags and categories
- 🚫 **Rate Limiting** - Built-in protection against abuse

---



---

## 🧠 Agent Core (the AI brain)

In addition to the web app, this repo ships **`agent_core/`** — a full autonomous agent runtime (Devil Agent) with tool use, skills, plugins, browser, terminal, memory and an **OpenAI-compatible HTTP API**.

🔗 **Live API**: `https://your-domain.com/agent/v1` (Bearer auth)

```bash
curl https://your-domain.com/agent/health
curl https://your-domain.com/agent/v1/models -H "Authorization: Bearer $API_SERVER_KEY"

curl -X POST https://your-domain.com/agent/v1/chat/completions \
  -H "Authorization: Bearer $API_SERVER_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"meta/llama-3.3-70b-instruct","messages":[{"role":"user","content":"hello"}]}'
```

CLI on the VPS: `devil` (interactive) or `devil -q "your question" -t web,terminal`.

Full how-to-use guide -> **[docs/AGENT_CORE_USAGE.md](docs/AGENT_CORE_USAGE.md)**

---
## 🎯 Why Choose Devil Agent?

### 🆚 Comparison with Competitors

| Feature | Devil Agent | ChatGPT | Claude | Gemini | GitHub Copilot |
|---------|-------------|---------|--------|--------|----------------|
| **40-word Key Auth** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Skills Management** | ✅ | ❌ | ❌ | ❌ | ⚠️ Limited |
| **WebSocket Terminal** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Free Tier** | ✅ Generous | 🔸 Limited | 🔸 Limited | 🔸 Limited | ❌ |
| **Open Source** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Custom API Integration** | ✅ | 💰 Paid | 💰 Paid | 💰 Paid | 💰 Paid |
| **Conversation Export** | ✅ | 💰 Paid | ❌ | ❌ | ❌ |
| **Self-Hosting** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Data Privacy** | ✅ Full Control | ⚠️ Cloud | ⚠️ Cloud | ⚠️ Cloud | ⚠️ Cloud |
| **No Email Required** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **Encrypted Storage** | ✅ | 🔸 Partial | 🔸 Partial | 🔸 Partial | 🔸 Partial |
| **Multi-Model Support** | ✅ | ❌ | ❌ | ❌ | ❌ |
| **API Rate Limits** | 🎯 Configurable | 🔸 Fixed | 🔸 Fixed | 🔸 Fixed | 🔸 Fixed |
| **Team Workspaces** | 🔜 Coming Soon | ✅ | ✅ | ❌ | ✅ |

### 💰 Pricing Comparison

| Service | Free Tier | Basic Plan | Pro Plan | Enterprise |
|---------|-----------|------------|----------|------------|
| **Devil Agent** | ✅ Unlimited | 🔜 TBD | 🔜 TBD | 🔜 TBD |
| **ChatGPT** | ✅ Limited | $20/mo | $40/mo | Custom |
| **Claude Pro** | ✅ Very Limited | $20/mo | N/A | Custom |
| **Gemini Advanced** | ✅ Limited | $19.99/mo | N/A | Custom |
| **GitHub Copilot** | ❌ | $10/mo | $19/mo/user | $39/mo/user |

**Why Devil Agent is Better:**
- 🎁 More generous free tier
- 🔓 Open source - inspect and modify the code
- 🏠 Self-hosting option - full data control
- 🚀 Better performance with optimized architecture
- 🔐 Superior security with 40-word key system
- 💾 Your data, your infrastructure, your control

---

## 🛠️ Technology Stack

### **Backend**
- ⚡ **FastAPI** (Python) - Modern, fast web framework
- 🗄️ **MongoDB** - NoSQL database with sharding support
- 🔐 **JWT + bcrypt** - Secure authentication
- 🔥 **NVIDIA API** - Qwen 80B model integration
- 🔒 **Cryptography** - Fernet encryption for API keys
- 📊 **Connection Pooling** - Optimized database performance
- 🚀 **Async/Await** - Non-blocking I/O for high performance

### **Frontend**
- ⚛️ **React 19** - Latest React with concurrent features
- 📘 **TypeScript** - Type-safe development
- 🎨 **Tailwind CSS** - Utility-first CSS framework
- 🎭 **Lucide React** - Beautiful icon library
- 📝 **React Markdown** - Markdown rendering in chat
- 🌈 **Syntax Highlighting** - Code highlighting in conversations
- 🔌 **WebSocket** - Real-time terminal access

### **Infrastructure**
- 🐧 **Ubuntu 22.04** - Server operating system
- 🌐 **Nginx** - Reverse proxy and static file serving
- 🔒 **Let's Encrypt** - Free SSL/TLS certificates
- 🔄 **Systemd** - Service management
- ☁️ **Cloudflare** - DNS and DDoS protection

---

## 📸 Screenshots

### Landing Page
![Landing Page](./assets/landing.png)

### Signup - Get Your 40-Word Key
![Signup](./assets/signup.png)

### Dashboard - AI Chat
![Chat Interface](./assets/chat.png)

### Skills Management
![Skills](./assets/skills.png)

### Settings & Profile
![Settings](./assets/settings.png)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- Node.js 16 or higher
- MongoDB 4.4 or higher
- Nginx (for production deployment)

### Local Development

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/devil-agent-ai-platform.git
cd devil-agent-ai-platform
```

#### 2️⃣ Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env and add your configuration

# Generate encryption key
python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
# Add the generated key to .env as ENCRYPTION_KEY

# Start the backend
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

#### 3️⃣ Frontend Setup

```bash
cd ../frontend

# Install dependencies
npm install

# Create .env.local file
echo "REACT_APP_API_URL=http://localhost:8001/api" > .env.local
echo "REACT_APP_WS_URL=ws://localhost:8001/ws" >> .env.local

# Start the frontend
npm start
```

#### 4️⃣ Access the Application

Open your browser and navigate to:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8001
- API Docs: http://localhost:8001/docs

---

## 🔧 Configuration

### Environment Variables

#### Backend (.env)

```bash
# MongoDB Configuration
MONGO_URL=mongodb://localhost:27017
DB_NAME=devil_web

# JWT Configuration
JWT_SECRET=your-secure-jwt-secret-key-here

# Encryption Key (for API keys storage)
ENCRYPTION_KEY=your-fernet-encryption-key-here

# NVIDIA API Configuration
NVIDIA_API_KEY=nvapi-your-key-here

# CORS Configuration (comma-separated)
ALLOWED_ORIGINS=https://yourdomain.com,http://localhost:3000
```

#### Frontend (.env.production)

```bash
REACT_APP_API_URL=https://yourdomain.com/api
REACT_APP_WS_URL=wss://yourdomain.com/ws
```

---

## 📖 API Documentation

### Authentication

#### Signup
```http
POST /api/auth/signup
```
**Response:**
```json
{
  "token": "jwt_token_here",
  "user_id": "user_id_here",
  "key": "40-word-key-here",
  "message": "SAVE THIS KEY! It cannot be recovered."
}
```

#### Login
```http
POST /api/auth/login
Content-Type: application/json

{
  "key": "your-40-word-key-here"
}
```

### Chat

#### Send Message
```http
POST /api/chat
Authorization: Bearer <token>
Content-Type: application/json

{
  "conversation_id": "optional_conversation_id",
  "message": "Your message here",
  "model": "qwen/qwen3-next-80b-a3b-instruct"
}
```

### Skills

#### List Skills
```http
GET /api/skills?skip=0&limit=50&search=python&category=code
Authorization: Bearer <token>
```

#### Create Skill
```http
POST /api/skills
Authorization: Bearer <token>
Content-Type: application/json

{
  "name": "My Skill",
  "description": "Description here",
  "code": "print('Hello World')",
  "language": "python",
  "category": "automation",
  "tags": ["python", "automation"]
}
```

📘 **Full API documentation available at:** `https://yourdomain.com/docs`

---

## 🚀 Production Deployment

### VPS Deployment (Ubuntu)

#### 1️⃣ Prepare the Server

```bash
# Update system
sudo apt-get update && sudo apt-get upgrade -y

# Install dependencies
sudo apt-get install -y python3-pip python3-venv nginx mongodb certbot python3-certbot-nginx

# Install Node.js
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
```

#### 2️⃣ Clone and Setup

```bash
# Clone repository
cd /home/ubuntu
git clone https://github.com/YOUR_GITHUB_USERNAME/devil-agent-ai-platform.git devil_agent
cd devil_agent

# Backend setup
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with production values
deactivate

# Frontend setup
cd ../frontend
npm install --legacy-peer-deps
npm run build
```

#### 3️⃣ Create Systemd Service

```bash
sudo tee /etc/systemd/system/devil-backend.service > /dev/null <<EOF
[Unit]
Description=Devil Agent Backend API
After=network.target mongod.service

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/devil_agent/backend
Environment="PATH=/home/ubuntu/devil_agent/backend/venv/bin"
ExecStart=/home/ubuntu/devil_agent/backend/venv/bin/uvicorn server:app --host 0.0.0.0 --port 8001 --workers 4
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable devil-backend
sudo systemctl start devil-backend
```

#### 4️⃣ Configure Nginx

```bash
sudo tee /etc/nginx/sites-available/devil_agent > /dev/null <<'EOF'
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    client_max_body_size 50M;
    
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_types text/plain text/css text/xml text/javascript application/json application/javascript;
    
    location / {
        root /home/ubuntu/devil_agent/frontend/build;
        try_files $uri $uri/ /index.html;
    }
    
    location /api/ {
        proxy_pass http://localhost:8001/api/;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    
    location /ws/ {
        proxy_pass http://localhost:8001/ws/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
EOF

sudo ln -sf /etc/nginx/sites-available/devil_agent /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

#### 5️⃣ Setup SSL

```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        Cloudflare                            │
│                     (DNS + DDoS Protection)                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      Nginx (Port 443)                        │
│                  (Reverse Proxy + SSL)                       │
└─────────────────────────────────────────────────────────────┘
                              │
                ┌─────────────┴─────────────┐
                │                           │
                ▼                           ▼
    ┌───────────────────┐       ┌───────────────────┐
    │   React Frontend  │       │  FastAPI Backend  │
    │   (Port 3000)     │       │   (Port 8001)     │
    │   - Static Files  │       │   - JWT Auth      │
    │   - SPA           │       │   - NVIDIA API    │
    └───────────────────┘       └───────────────────┘
                                            │
                                            ▼
                                ┌───────────────────┐
                                │     MongoDB       │
                                │   (Port 27017)    │
                                │   - Users         │
                                │   - Conversations │
                                │   - Skills        │
                                └───────────────────┘
```

---

## 🔐 Security Features

- 🔑 **40-Word Key Authentication** - Unique, memorable, and secure
- 🔒 **Encrypted API Keys** - Fernet encryption for sensitive data
- 🛡️ **JWT Tokens** - Stateless authentication with expiration
- 🚫 **Rate Limiting** - Protection against brute-force attacks
- 🔍 **Input Sanitization** - Prevention of injection attacks
- 📝 **Security Logs** - Audit trail for suspicious activities
- 🌐 **HTTPS Only** - SSL/TLS encryption for all traffic
- 🎯 **CORS Whitelist** - Restricted origin access
- 🔐 **bcrypt Hashing** - Secure password hashing
- 🏗️ **Indexed Lookups** - O(1) authentication performance

---

## 📊 Performance Optimizations

### Backend
- ✅ **O(1) Login Performance** - Key prefix indexing (fixed from O(n))
- ✅ **Connection Pooling** - MongoDB connection pooling (10-50 connections)
- ✅ **Database Indexing** - Optimized compound indexes
- ✅ **Async I/O** - Non-blocking operations with asyncio
- ✅ **Response Compression** - Gzip compression enabled
- ✅ **Caching** - In-memory caching for user data (5-min TTL)
- ✅ **Pagination** - Efficient data loading for large datasets
- ✅ **Rate Limiting** - Per-user request throttling

### Frontend
- ✅ **Code Splitting** - Lazy loading of routes
- ✅ **Asset Optimization** - Minified CSS/JS bundles
- ✅ **React 19 Features** - Concurrent rendering
- ✅ **Optimized Re-renders** - React.memo and useMemo
- ✅ **Static Asset Caching** - 1-year cache for immutable assets
- ✅ **Bundle Size** - Optimized build (< 500KB gzipped)

---

## 🧪 Testing

### Run Backend Tests
```bash
cd backend
pytest tests/ -v --cov=server
```

### Run Frontend Tests
```bash
cd frontend
npm test
```

### E2E Tests
```bash
npm run test:e2e
```

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create your feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 for Python code
- Use ESLint and Prettier for TypeScript/React code
- Write tests for new features
- Update documentation as needed
- Keep commits atomic and well-documented

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Team

**Lead Developer:** Vikrant  
**Organization:** [YOUR_GITHUB_USERNAME](https://github.com/YOUR_GITHUB_USERNAME)

---

## 🙏 Acknowledgments

- [NVIDIA](https://www.nvidia.com/) for providing the Qwen 80B model API
- [FastAPI](https://fastapi.tiangolo.com/) for the amazing web framework
- [React](https://reactjs.org/) team for the best UI library
- [MongoDB](https://www.mongodb.com/) for the flexible database
- [Tailwind CSS](https://tailwindcss.com/) for the utility-first CSS framework
- The open-source community for inspiration and tools

---

## 📞 Support

Need help? Here's how to get support:

- 📧 **Email:** support@your-domain.com
- 💬 **Discord:** [Join our community](#)
- 🐛 **Issues:** [GitHub Issues](https://github.com/YOUR_GITHUB_USERNAME/devil-agent-ai-platform/issues)
- 📚 **Docs:** [Full Documentation](https://docs.your-domain.com)

---

## 🗺️ Roadmap

### Q2 2026
- [x] Core platform launch
- [x] 40-word key authentication
- [x] NVIDIA Qwen 80B integration
- [x] Skills management
- [ ] Team workspaces
- [ ] Conversation sharing

### Q3 2026
- [ ] Multi-model support (GPT-5, Claude, Gemini)
- [ ] Voice input/output
- [ ] Mobile apps (iOS/Android)
- [ ] Plugin system
- [ ] Advanced analytics

### Q4 2026
- [ ] Marketplace for skills
- [ ] AI model fine-tuning
- [ ] Enterprise SSO integration
- [ ] Advanced collaboration features
- [ ] API rate plans

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=YOUR_GITHUB_USERNAME/devil-agent-ai-platform&type=Date)](https://star-history.com/#YOUR_GITHUB_USERNAME/devil-agent-ai-platform&Date)

---

<div align="center">

**Made with ❤️ and AI**

[⬆ Back to Top](#-devil-agent---ai-powered-assistant-platform)

</div>
