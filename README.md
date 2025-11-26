[
](https://sinx-darksec-1.tailcfc068.ts.net/)

# Darkapp
A powerful Open Source Intelligence (OSINT) toolkit for WhatsApp reconnaissance and metadata collection during authorized penetration testing engagements.
# Darkapp

<img width="1353" height="621" alt="Screenshot From 2025-11-25 00-06-47" src="https://github.com/user-attachments/assets/7d438dc6-85e6-42f3-b274-52c03414deab" />



A powerful Open Source Intelligence (OSINT) toolkit for WhatsApp reconnaissance and metadata collection during authorized penetration testing engagements.

## ⚠️ Legal Disclaimer

**FOR AUTHORIZED PENETRATION TESTING ONLY**

This toolkit is designed exclusively for:
- Authorized penetration testing engagements with written permission
- Security research with proper authorization
- Educational purposes in controlled environments
- Defensive security operations

**You MUST have:**
- Written authorization from the target organization
- Documented scope of testing
- Compliance with all applicable laws and regulations

Unauthorized use may violate:
- Computer Fraud and Abuse Act (CFAA)
- WhatsApp Terms of Service
- Privacy laws (GDPR, CCPA, etc.)
- Local and international laws

**The authors assume no liability for misuse of this tool.**

## 🚀 Features

### 1. Phone Number Validator
- ✓ Check if phone numbers are registered on WhatsApp
- ✓ Bulk validation from file
- ✓ Extract basic profile information
- ✓ Export results (JSON, CSV)

### 2. Profile Scraper
- ✓ Extract profile pictures
- ✓ Scrape "About" sections
- ✓ Collect status messages
- ✓ Gather profile metadata
- ✓ Bulk profile scraping

### 3. Activity Tracker
- ✓ Real-time online/offline monitoring
- ✓ Activity pattern analysis
- ✓ Typing status detection
- ✓ Last seen information
- ✓ Duration-based tracking with statistics
- ✓ Live dashboard display

### 4. Group Intelligence
- ✓ List all groups
- ✓ Extract group member lists
- ✓ Identify group administrators
- ✓ Scrape group descriptions
- ✓ Analyze group invite links

### 5. Advanced Reporting
- ✓ Comprehensive HTML reports
- ✓ JSON export for automation
- ✓ CSV export for spreadsheet analysis
- ✓ Visual activity timelines
- ✓ Statistical analysis

### 6. Stealth Features
- ✓ Random delays between actions
- ✓ User agent rotation
- ✓ Rate limiting
- ✓ Persistent sessions
- ✓ Headless mode support

## 📋 Requirements

- Python 3.8+
- Google Chrome browser
- ChromeDriver (automatically managed)
- WhatsApp account for Web access

## 🛠️ Installation

### Quick Install

```bash
cd Darkapp
pip install -r requirements.txt
chmod +x darkapp.py
```

### Manual Installation

```bash
# Install Python dependencies
pip install selenium webdriver-manager requests beautifulsoup4 pandas
pip install openpyxl python-dotenv colorama rich pillow phonenumbers
pip install aiohttp qrcode pyfiglet tqdm

# Install Chrome (if not already installed)
# Ubuntu/Debian:
sudo apt update && sudo apt install -y google-chrome-stable

# Arch Linux:
sudo pacman -S chromium
```

## 📖 Usage

### Basic Usage

```bash
# Start the toolkit
python3 darkapp.py

# Run in headless mode (no GUI)
python3 darkapp.py --headless

# Specify engagement name
python3 darkapp.py --engagement "ClientName Pentest 2025"
```

### First Time Setup

1. **Launch the toolkit:**
   ```bash
   python3 darkapp.py
   ```

2. **Scan QR Code:**
   - WhatsApp Web will open in Chrome
   - Scan the QR code with your phone
   - The session will be saved for future use

3. **Navigate the menu:**
   - Select operations from the interactive menu
   - Follow on-screen prompts

### Module Usage

#### Phone Number Validation

```
1. Select "Phone Validator" from main menu
2. Choose single or bulk validation
3. For bulk: prepare a text file with numbers (one per line)
   Example format:
   +1234567890
   +447700900000
   +919876543210
4. Export results in JSON or CSV format
```

#### Profile Scraping

```
1. Select "Profile Scraper"
2. Enter target phone number(s)
3. Tool will extract:
   - Profile name
   - Profile picture (saved to data/)
   - About/Status
   - Metadata
4. Export scraped profiles
```

#### Activity Tracking

```
1. Select "Activity Tracker"
2. Enter target phone number
3. Specify:
   - Duration (minutes)
   - Check interval (seconds)
4. Monitor real-time activity:
   - Online/Offline status
   - Typing indicators
   - Last seen times
5. View statistical analysis
6. Export activity log
```

#### Group Intelligence

```
1. Select "Group Intelligence"
2. Options:
   - List all groups you're part of
   - Get detailed info on specific group
   - Analyze group invite links
3. Extract:
   - Member lists
   - Admin identities
   - Group metadata
4. Export group data
```

#### Report Generation

```
1. Collect data using various modules
2. Select "Generate Report"
3. Choose format:
   - JSON: For automation/parsing
   - CSV: For spreadsheet analysis
   - HTML: Professional presentation report
   - All: Generate all formats
4. Reports saved to exports/ directory
```

## 📁 Project Structure

```
Darkapp/
├── darkapp.py                  # Main CLI interface
├── config.py                   # Configuration settings
├── utils.py                    # Utility functions
├── requirements.txt            # Python dependencies
├── README.md                   # Documentation
├── modules/
│   ├── phone_validator.py      # Phone validation module
│   ├── profile_scraper.py      # Profile scraping module
│   ├── activity_tracker.py     # Activity monitoring module
│   ├── group_intel.py          # Group intelligence module
│   └── report_generator.py     # Report generation module
├── data/                       # Profile pictures and data
├── logs/                       # Activity logs
├── exports/                    # Generated reports
└── chrome_profile/             # Persistent Chrome session
```

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# Rate limiting (seconds)
MIN_DELAY = 2
MAX_DELAY = 5

# Tracking settings
TRACKING_INTERVAL = 30
MAX_TRACKING_DURATION = 3600

# Browser settings
HEADLESS_MODE = False
IMPLICIT_WAIT = 10

# Export format
EXPORT_FORMAT = "all"  # json, csv, html, all
```

## 🎯 Use Cases

### Authorized Penetration Testing
- Enumerate employee WhatsApp accounts
- Map organizational communication channels
- Identify key personnel and hierarchies
- Test social engineering attack surfaces

### Security Awareness Training
- Demonstrate OSINT capabilities
- Show metadata exposure risks
- Educate on privacy settings

### Red Team Operations
- Reconnaissance phase intelligence gathering
- Target profiling and behavior analysis
- Communication pattern mapping

## 🔒 Operational Security

**Best Practices:**
1. **Use a dedicated phone number** for OSINT operations
2. **Create a separate WhatsApp account** not linked to personal identity
3. **Use VPN** to mask IP address
4. **Enable headless mode** to reduce fingerprinting
5. **Respect rate limits** to avoid detection
6. **Document all activities** for engagement reporting
7. **Delete sensitive data** after engagement completion

## 📊 Export Formats

### JSON
```json
{
  "engagement": "Assessment Name",
  "generated": "2025-01-15 14:30:00",
  "phone_validation": [...],
  "profiles": [...],
  "activity_logs": [...],
  "groups": [...]
}
```

### CSV
Separate CSV files for each data type:
- `phone_validation_20250115.csv`
- `profiles_20250115.csv`
- `activity_log_20250115.csv`
- `groups_20250115.csv`

### HTML
Professional HTML report with:
- Executive summary
- Visual timelines
- Statistical analysis
- Detailed findings
- Recommendations

## 🐛 Troubleshooting

### Issue: QR Code Won't Load
**Solution:** Update Chrome and ChromeDriver to latest versions

### Issue: "Element not found" errors
**Solution:** Increase `IMPLICIT_WAIT` in config.py

### Issue: Too many requests / Getting blocked
**Solution:** Increase delays in config.py, use headless mode

### Issue: Profile pictures not downloading
**Solution:** Check permissions on data/ directory

### Issue: Session expires frequently
**Solution:** Ensure chrome_profile/ directory is persistent

## 🔧 Advanced Usage

### Python API

```python
from modules.phone_validator import PhoneValidator
from modules.profile_scraper import ProfileScraper

# Initialize
validator = PhoneValidator(headless=True)
validator.start()

# Check numbers
result = validator.check_number("+1234567890")
print(result)

# Scrape profile
scraper = ProfileScraper(driver=validator.driver)
profile = scraper.scrape_profile("+1234567890")

# Cleanup
validator.stop()
```

### Automation Script

```python
#!/usr/bin/env python3
import sys
from modules.phone_validator import PhoneValidator
from modules.report_generator import ReportGenerator

# Load targets
targets = open("targets.txt").read().splitlines()

# Run validation
validator = PhoneValidator(headless=True)
validator.start()
results = validator.check_bulk(targets)
validator.stop()

# Generate report
report = ReportGenerator("Automated Scan")
report.add_data("phone_validation", results)
report.generate_html_report()
```

## 🤝 Contributing

This is a security research tool. Contributions welcome:
- Bug fixes
- New OSINT modules
- Improved stealth techniques
- Better reporting features

**DO NOT** contribute features that:
- Bypass WhatsApp security controls
- Enable mass surveillance
- Facilitate harassment or stalking

## 📄 License

This tool is provided for educational and authorized security testing purposes only.

## 🙏 Credits

Developed for the penetration testing community.

Built with:
- Selenium WebDriver
- Rich CLI framework
- Pandas data analysis
- Beautiful Soup parsing

## 📞 Support

For issues and questions:
- Check troubleshooting section
- Review logs in `logs/` directory
- Ensure proper authorization before use

---

**Remember: With great power comes great responsibility. Use ethically and legally.**
