# 🌐 Darkapp Web - Single File Web Edition

**Complete OSINT Intelligence Framework with Beautiful Web UI - All in ONE File!**

```
██████╗  █████╗ ██████╗ ██╗  ██╗ █████╗ ██████╗ ██████╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗
██║  ██║███████║██████╔╝█████╔╝ ███████║██████╔╝██████╔╝
██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██║██╔═══╝ ██╔═══╝
██████╔╝██║  ██║██║  ██║██║  ██╗██║  ██║██║     ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
```

## ⚠️ Legal Disclaimer

**FOR AUTHORIZED PENETRATION TESTING AND SECURITY RESEARCH ONLY**

This tool is designed exclusively for:
- ✅ Authorized penetration testing with written permission
- ✅ Security research with proper authorization
- ✅ Educational purposes in controlled environments
- ✅ Defensive security operations

**The authors assume NO LIABILITY for misuse of this tool.**

---

## 🎯 Features

### Complete Web-Based OSINT Framework
- 🌐 **Beautiful Modern Web UI** - Gradient design, responsive layout
- 📱 **25+ OSINT Modules** - ALL modules included in ONE file
- 🚀 **Easy Deployment** - Single file, runs anywhere
- 📊 **Real-Time Results** - AJAX-powered instant feedback
- 💾 **Export Capabilities** - JSON, HTML reports
- 🎨 **Professional Design** - Clean, intuitive interface

### Included Modules

#### Intelligence Gathering
1. 📱 **Phone Intelligence** - Validate, analyze phone numbers
2. 📧 **Email Intelligence** - DNS, MX, WHOIS, SPF, DMARC
3. 👤 **Username Search** - Search 20+ social platforms
4. 🔍 **Google Dorking** - Generate advanced queries
5. 🌐 **Network Intelligence** - Domain analysis, DNS lookup
6. 👥 **People Search** - FastPeopleSearch integration
7. 📧 **Email OSINT** - Additional email reconnaissance

#### Social Media & Profiles
8. 📱 **Social Media Scraper** - Deep profile scraping
9. 👤 **Profile Scraper** - Extract profile data
10. 👥 **Group Intelligence** - Group analysis
11. 📊 **Activity Tracker** - Monitor online activity

#### Security Analysis
12. 🛡️ **Breach Checker** - Data breach detection
13. 🔒 **Link Tracker** - Track and analyze links
14. 🕸️ **Dark Web OSINT** - Dark web intelligence

#### Media & Documents
15. 📷 **Image Intelligence** - EXIF metadata extraction
16. 🔍 **Reverse Image Search** - Multi-engine search
17. 📄 **Document Intelligence** - Document metadata

#### Advanced Features
18. 🗺️ **Geolocation Intelligence** - Location analysis
19. 🤖 **AI Analyzer** - AI-powered analysis
20. 📡 **Network Intelligence** - Network reconnaissance
21. 💾 **Database Manager** - Data management
22. 🔗 **Data Correlator** - Cross-reference data
23. 📢 **Webhook System** - Notifications
24. 📋 **Campaign Manager** - Manage investigations
25. 📄 **Report Generator** - Comprehensive reports

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Install required packages
pip install flask requests beautifulsoup4 phonenumbers

# OR install all features
pip install -r darkapp-web-requirements.txt
```

### 2. Run the Server

```bash
# Start Darkapp Web
python3 darkapp-web.py

# OR make it executable
chmod +x darkapp-web.py
./darkapp-web.py
```

### 3. Access Web Interface

```
🌐 Open browser: http://localhost:5000
```

---

## 📦 Installation

### Method 1: Quick Install

```bash
# One-liner install and run
pip install flask requests beautifulsoup4 phonenumbers && python3 darkapp-web.py
```

### Method 2: Full Installation

```bash
# Clone or download darkapp-web.py
wget https://raw.githubusercontent.com/yourusername/darkapp/main/darkapp-web.py

# Install dependencies
pip install -r darkapp-web-requirements.txt

# Run
python3 darkapp-web.py
```

### Method 3: Production Deployment

```bash
# Install production dependencies
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 darkapp-web:app
```

---

## 💻 Usage

### Using the Web Interface

1. **Start the server:**
   ```bash
   python3 darkapp-web.py
   ```

2. **Open browser:**
   - Navigate to `http://localhost:5000`

3. **Select module:**
   - Click on any module button in navigation bar

4. **Enter data:**
   - Fill in the required fields

5. **View results:**
   - Results appear in real-time below the form

### Example Workflows

#### Workflow 1: Phone Investigation
```
1. Click "Phone Intelligence"
2. Enter: +1234567890
3. Click "Analyze Phone Number"
4. View comprehensive analysis:
   - Validation status
   - Country/region
   - Carrier info
   - Number type
   - Timezone
```

#### Workflow 2: Email Analysis
```
1. Click "Email Intelligence"
2. Enter: target@example.com
3. Click "Analyze Email"
4. View results:
   - Format validation
   - MX records
   - SPF/DMARC
   - WHOIS data
```

#### Workflow 3: Username Search
```
1. Click "Username Search"
2. Enter: johndoe
3. Click "Search Across Platforms"
4. View found profiles across 20+ platforms
```

---

## 🎨 Screenshots

### Main Interface
```
╔══════════════════════════════════════════════════╗
║         🎯 DARKAPP WEB                           ║
║   Advanced OSINT Intelligence Framework          ║
║         Version 3.0.0-web                        ║
╠══════════════════════════════════════════════════╣
║  ⚠️  FOR AUTHORIZED TESTING ONLY ⚠️              ║
╠══════════════════════════════════════════════════╣
║  [📱 Phone] [📧 Email] [👤 Username] [🔍 Google] ║
║  [🛡️ Breach] [📷 Image] [🌐 Network] [📱 Social]║
║  [🗺️ Geo] [🕸️ DarkWeb] [📄 Reports]             ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  [Module Content Area]                           ║
║                                                  ║
╚══════════════════════════════════════════════════╝
```

---

## 🔧 Configuration

### Environment Variables

```bash
# Optional: Custom port
export DARKAPP_PORT=8080

# Optional: Debug mode (development only)
export FLASK_DEBUG=1
```

### File Locations

```
~/.darkapp-web/
├── data/       # Collected intelligence data
├── logs/       # Application logs
├── exports/    # Generated reports
└── uploads/    # Uploaded files (images, etc.)
```

---

## 🌐 Deployment

### Local Development

```bash
python3 darkapp-web.py
# Access: http://localhost:5000
```

### Production with Gunicorn

```bash
# Install Gunicorn
pip install gunicorn

# Run with 4 workers
gunicorn -w 4 -b 0.0.0.0:5000 darkapp-web:app

# With logging
gunicorn -w 4 -b 0.0.0.0:5000 darkapp-web:app --access-logfile - --error-logfile -
```

### Docker Deployment

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY darkapp-web.py .
COPY darkapp-web-requirements.txt .

RUN pip install -r darkapp-web-requirements.txt

EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "darkapp-web:app"]
```

```bash
# Build and run
docker build -t darkapp-web .
docker run -p 5000:5000 darkapp-web
```

### Nginx Reverse Proxy

```nginx
server {
    listen 80;
    server_name darkapp.yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## 🔒 Security

### Best Practices

1. **Authentication** - Add authentication for production
2. **HTTPS** - Use SSL/TLS in production
3. **Firewall** - Restrict access to authorized IPs
4. **Rate Limiting** - Implement rate limiting
5. **Logging** - Monitor all activities
6. **Updates** - Keep dependencies updated

### Adding Basic Authentication

```python
# Add to darkapp-web.py
from functools import wraps
from flask import request, Response

def check_auth(username, password):
    return username == 'admin' and password == 'your_password'

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return Response('Authentication required', 401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'})
        return f(*args, **kwargs)
    return decorated

# Add @requires_auth decorator to routes
@app.route('/')
@requires_auth
def index():
    # ... existing code
```

---

## 📊 API Endpoints

All modules accessible via REST API:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/phone` | POST | Phone intelligence |
| `/api/email` | POST | Email analysis |
| `/api/username` | POST | Username search |
| `/api/google-dorks` | POST | Generate dorks |
| `/api/breach` | POST | Breach check |
| `/api/image` | POST | Image analysis |
| `/api/network` | POST | Network intelligence |
| `/api/social-scrape` | POST | Social media scrape |
| `/api/geolocation` | POST | Geo analysis |
| `/api/darkweb` | POST | Dark web search |
| `/api/generate-report` | POST | Generate report |

### Example API Usage

```bash
# Phone Intelligence
curl -X POST http://localhost:5000/api/phone \
  -H "Content-Type: application/json" \
  -d '{"phone": "+1234567890"}'

# Email Intelligence
curl -X POST http://localhost:5000/api/email \
  -H "Content-Type: application/json" \
  -d '{"email": "target@example.com"}'

# Username Search
curl -X POST http://localhost:5000/api/username \
  -H "Content-Type: application/json" \
  -d '{"username": "johndoe"}'
```

---

## 🐛 Troubleshooting

### Issue: Port already in use
**Solution:**
```bash
# Kill process on port 5000
sudo lsof -ti:5000 | xargs kill -9

# OR use different port
export FLASK_RUN_PORT=8080
python3 darkapp-web.py
```

### Issue: Module not found
**Solution:**
```bash
pip install flask requests beautifulsoup4 phonenumbers
```

### Issue: Permission denied
**Solution:**
```bash
chmod +x darkapp-web.py
```

### Issue: DNS features not working
**Solution:**
```bash
pip install dnspython
```

### Issue: Image analysis fails
**Solution:**
```bash
pip install Pillow
```

---

## 📈 Performance

### Optimization Tips

1. **Use Gunicorn** for production (multi-worker)
2. **Enable caching** for repeated queries
3. **Rate limiting** to prevent abuse
4. **Async operations** for long-running tasks
5. **Database backend** for data persistence

---

## 🤝 Contributing

Contributions welcome! Please ensure:
- Code follows existing style
- All modules remain in single file
- Features enhance security research
- Proper documentation

---

## 📄 License

Educational & Authorized Testing Only

**The authors assume NO LIABILITY for misuse.**

---

## ⭐ Features

### Why Darkapp Web?

✅ **Single File** - Everything in one Python file
✅ **Beautiful UI** - Modern, responsive web interface
✅ **25+ Modules** - Complete OSINT toolkit
✅ **Easy Deploy** - Runs on any Python 3.8+ system
✅ **REST API** - Programmatic access
✅ **Real-Time** - Instant results
✅ **Professional** - Enterprise-grade reports
✅ **Portable** - One file to rule them all

---

## 🎓 Learn More

- Full Documentation: See this README
- Module Guide: All modules documented inline
- API Reference: See API Endpoints section
- Deployment Guide: See Deployment section

---

## 📞 Support

- 📖 Documentation: This README
- 🐛 Issues: GitHub Issues
- 💬 Discussions: GitHub Discussions

---

**Remember: With great power comes great responsibility. Use ethically and legally.**

```
 _____             _                         _    _      _
|  __ \           | |                       | |  | |    | |
| |  | | __ _ _ __| | ____ _ _ __  _ __    | |  | | ___| |__
| |  | |/ _` | '__| |/ / _` | '_ \| '_ \   | |/\| |/ _ \ '_ \
| |__| | (_| | |  |   < (_| | |_) | |_) |  \  /\  /  __/ |_) |
|_____/ \__,_|_|  |_|\_\__,_| .__/| .__/    \/  \/ \___|_.__/
                            | |   | |
                            |_|   |_|
```

---

**Version:** 3.0.0-web | **Release:** 2025 | **Status:** Stable | **Type:** Single File Web Edition
