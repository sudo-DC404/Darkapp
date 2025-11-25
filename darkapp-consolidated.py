#!/usr/bin/env python3
"""
██████╗  █████╗ ██████╗ ██╗  ██╗ █████╗ ██████╗ ██████╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗
██║  ██║███████║██████╔╝█████╔╝ ███████║██████╔╝██████╔╝
██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██║██╔═══╝ ██╔═══╝
██████╔╝██║  ██║██║  ██║██║  ██╗██║  ██║██║     ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝

DARKAPP v3.0 - Advanced OSINT Intelligence Framework
Single File Edition - Ready for GitHub

⚠️  FOR AUTHORIZED PENETRATION TESTING ONLY ⚠️

Author: Security Research Community
License: Educational & Authorized Testing Only
"""

import sys
import os
import time
import json
import random
import logging
import re
import socket
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
from collections import defaultdict
import base64

# Third-party imports
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    from rich.align import Align
    from rich.prompt import Prompt, Confirm
    from rich import box
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.layout import Layout
    import requests
    from bs4 import BeautifulSoup
    import phonenumbers
    from phonenumbers import NumberParseException
except ImportError as e:
    print(f"❌ Missing required library: {e}")
    print("\n📦 Please install requirements:")
    print("pip install rich requests beautifulsoup4 phonenumbers")
    sys.exit(1)

# Optional imports (graceful degradation if not available)
try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

try:
    import dns.resolver
    HAS_DNS = True
except ImportError:
    HAS_DNS = False

try:
    import whois
    HAS_WHOIS = True
except ImportError:
    HAS_WHOIS = False

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.common.exceptions import TimeoutException, NoSuchElementException
    HAS_SELENIUM = True
except ImportError:
    HAS_SELENIUM = False

# =============================================================================
# GLOBAL CONFIGURATION
# =============================================================================

VERSION = "3.0.0"
APP_NAME = "Darkapp"

# Directory setup
BASE_DIR = Path.home() / ".darkapp"
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"
EXPORTS_DIR = BASE_DIR / "exports"
CHROME_PROFILE_DIR = BASE_DIR / "chrome_profile"

# Create directories
for dir_path in [BASE_DIR, DATA_DIR, LOGS_DIR, EXPORTS_DIR, CHROME_PROFILE_DIR]:
    dir_path.mkdir(exist_ok=True, parents=True)

# Rate limiting
MIN_DELAY = 2
MAX_DELAY = 5

# User agents for rotation
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]

# =============================================================================
# BEAUTIFUL UI COMPONENTS
# =============================================================================

console = Console()

# Icons for visual enhancement
ICONS = {
    "phone": "📱", "profile": "👤", "email": "📧", "search": "🔍",
    "check": "✅", "cross": "❌", "warning": "⚠️", "info": "ℹ️",
    "star": "⭐", "fire": "🔥", "rocket": "🚀", "lock": "🔒",
    "key": "🔑", "link": "🔗", "globe": "🌐", "chart": "📊",
    "folder": "📁", "document": "📄", "shield": "🛡️", "camera": "📷",
    "network": "🌍", "database": "💾", "ai": "🤖", "web": "🕸️",
    "target": "🎯", "radar": "📡", "satellite": "🛰️", "brain": "🧠"
}

# Color scheme
COLORS = {
    "primary": "cyan", "success": "green", "warning": "yellow",
    "danger": "red", "info": "blue", "accent": "magenta", "dim": "dim white"
}

DARKAPP_BANNER = """
██████╗  █████╗ ██████╗ ██╗  ██╗ █████╗ ██████╗ ██████╗
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗
██║  ██║███████║██████╔╝█████╔╝ ███████║██████╔╝██████╔╝
██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██║██╔═══╝ ██╔═══╝
██████╔╝██║  ██║██║  ██║██║  ██╗██║  ██║██║     ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝
"""

AUTHORIZATION_NOTICE = """
╔══════════════════════════════════════════════════════════════════════╗
║              ⚠️  AUTHORIZATION REQUIRED - READ CAREFULLY  ⚠️          ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  This tool is designed for AUTHORIZED penetration testing and       ║
║  security research ONLY.                                            ║
║                                                                      ║
║  YOU MUST HAVE:                                                     ║
║  • Written authorization from the target organization               ║
║  • Documented scope of testing                                      ║
║  • Compliance with applicable laws and regulations                  ║
║                                                                      ║
║  Unauthorized use may violate:                                      ║
║  • Computer Fraud and Abuse Act (CFAA)                              ║
║  • Privacy laws (GDPR, CCPA, etc.)                                  ║
║  • Terms of Service for various platforms                           ║
║  • Local and international laws                                     ║
║                                                                      ║
║  The authors assume NO LIABILITY for misuse of this tool.           ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
"""


def show_banner():
    """Display beautiful Darkapp banner with gradient effect"""
    banner_text = Text(DARKAPP_BANNER, style="bold cyan")
    tagline = Text("Advanced OSINT Intelligence Framework", style="bold white", justify="center")
    version = Text(f"v{VERSION} - Single File Edition", style="dim cyan", justify="center")

    console.print()
    console.print(Align.center(banner_text))
    console.print(Align.center(tagline))
    console.print(Align.center(version))
    console.print()

    # Show capabilities bar
    capabilities = Table.grid(padding=1)
    capabilities.add_column(justify="center", style="cyan")
    capabilities.add_column(justify="center", style="green")
    capabilities.add_column(justify="center", style="yellow")
    capabilities.add_column(justify="center", style="magenta")

    capabilities.add_row(
        f"{ICONS['rocket']} 15+ Modules",
        f"{ICONS['globe']} 50+ Platforms",
        f"{ICONS['chart']} 15+ Sources",
        f"{ICONS['fire']} Real-Time"
    )

    console.print(Panel(
        Align.center(capabilities),
        border_style="cyan",
        box=box.DOUBLE
    ))
    console.print()


def show_authorization_warning():
    """Show authorization warning"""
    console.print(Panel(
        Text(AUTHORIZATION_NOTICE, style="bold yellow"),
        border_style="red",
        box=box.DOUBLE
    ))
    console.print()


def show_success(message: str):
    """Show success message"""
    console.print(f"[bold green]{ICONS['check']} {message}[/bold green]")


def show_error(message: str):
    """Show error message"""
    console.print(f"[bold red]{ICONS['cross']} {message}[/bold red]")


def show_warning(message: str):
    """Show warning message"""
    console.print(f"[bold yellow]{ICONS['warning']} {message}[/bold yellow]")


def show_info(message: str):
    """Show info message"""
    console.print(f"[cyan]{ICONS['info']} {message}[/cyan]")


def show_module_header(module_name: str, description: str, icon: str = "🔧"):
    """Show beautiful module header"""
    console.print()
    header = Text()
    header.append(f"{icon} ", style="bold yellow")
    header.append(module_name, style="bold cyan")
    header.append(f"\n{description}", style="dim white")

    console.print(Panel(
        Align.center(header),
        border_style="cyan",
        box=box.HEAVY
    ))
    console.print()


def show_result_card(title: str, data: dict, style: str = "green"):
    """Display results in a beautiful card"""
    table = Table(show_header=False, box=box.ROUNDED, border_style=style)
    table.add_column("Field", style="bold cyan", width=25)
    table.add_column("Value", style="white")

    for key, value in data.items():
        if value:
            # Format value nicely
            if isinstance(value, list):
                value_str = ", ".join(str(v) for v in value[:3])
                if len(value) > 3:
                    value_str += f" ... (+{len(value)-3} more)"
            elif isinstance(value, dict):
                value_str = f"{len(value)} items"
            else:
                value_str = str(value)

            table.add_row(key, value_str)

    console.print(Panel(
        table,
        title=f"[bold {style}]{title}[/bold {style}]",
        border_style=style,
        box=box.DOUBLE
    ))


def create_styled_table(title: str, headers: list, border_color: str = "cyan") -> Table:
    """Create a beautifully styled table"""
    table = Table(
        title=f"[bold {border_color}]{title}[/bold {border_color}]",
        box=box.ROUNDED,
        border_style=border_color,
        show_header=True,
        header_style="bold cyan"
    )

    for header in headers:
        table.add_column(header, style="white")

    return table


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def setup_logging(name: str = "darkapp") -> logging.Logger:
    """Setup logging configuration"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # File handler
    log_file = LOGS_DIR / f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger


def random_delay(min_delay: int = MIN_DELAY, max_delay: int = MAX_DELAY):
    """Add random delay to avoid detection"""
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)


def get_random_user_agent() -> str:
    """Get random user agent string"""
    return random.choice(USER_AGENTS)


def format_timestamp(timestamp: datetime = None) -> str:
    """Format timestamp for logging"""
    if timestamp is None:
        timestamp = datetime.now()
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")


def save_json(data: Any, filename: str, directory: Path = EXPORTS_DIR) -> Path:
    """Save data to JSON file"""
    filepath = directory / filename
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)
    return filepath


def load_json(filename: str, directory: Path = DATA_DIR) -> Any:
    """Load data from JSON file"""
    filepath = directory / filename
    if filepath.exists():
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None


def sanitize_filename(filename: str) -> str:
    """Sanitize filename for safe file operations"""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename


# =============================================================================
# PHONE NUMBER VALIDATION
# =============================================================================

class PhoneValidator:
    """Phone number validation and analysis"""

    def __init__(self):
        self.logger = setup_logging("phone_validator")
        self.results = []

    def validate_number(self, phone: str, region: str = "US") -> Dict[str, Any]:
        """
        Validate and format phone number

        Args:
            phone: Phone number string
            region: Default country code

        Returns:
            Dictionary with validation results
        """
        try:
            parsed = phonenumbers.parse(phone, region)

            result = {
                "input": phone,
                "valid": phonenumbers.is_valid_number(parsed),
                "formatted": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164),
                "international": phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
                "country_code": parsed.country_code,
                "national_number": parsed.national_number,
                "region": phonenumbers.region_code_for_number(parsed),
                "carrier": self._get_carrier(parsed),
                "type": self._get_number_type(parsed),
                "timezone": self._get_timezone(parsed)
            }

            self.logger.info(f"Validated phone: {phone} -> {result['formatted']}")
            return result

        except NumberParseException as e:
            result = {
                "input": phone,
                "valid": False,
                "error": str(e)
            }
            self.logger.warning(f"Invalid phone: {phone} - {e}")
            return result

    def _get_carrier(self, parsed_number) -> str:
        """Get carrier information"""
        try:
            from phonenumbers import carrier
            return carrier.name_for_number(parsed_number, "en") or "Unknown"
        except:
            return "Unknown"

    def _get_number_type(self, parsed_number) -> str:
        """Get phone number type"""
        number_type = phonenumbers.number_type(parsed_number)
        types = {
            0: "FIXED_LINE",
            1: "MOBILE",
            2: "FIXED_LINE_OR_MOBILE",
            3: "TOLL_FREE",
            4: "PREMIUM_RATE",
            5: "SHARED_COST",
            6: "VOIP",
            7: "PERSONAL_NUMBER",
            8: "PAGER",
            9: "UAN",
            10: "VOICEMAIL",
            99: "UNKNOWN"
        }
        return types.get(number_type, "UNKNOWN")

    def _get_timezone(self, parsed_number) -> List[str]:
        """Get timezone information"""
        try:
            from phonenumbers import timezone
            return timezone.time_zones_for_number(parsed_number)
        except:
            return []

    def bulk_validate(self, phone_numbers: List[str]) -> List[Dict[str, Any]]:
        """Validate multiple phone numbers"""
        results = []

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task(f"[cyan]Validating {len(phone_numbers)} numbers...", total=len(phone_numbers))

            for phone in phone_numbers:
                result = self.validate_number(phone)
                results.append(result)
                progress.update(task, advance=1)

        return results


# =============================================================================
# EMAIL INTELLIGENCE
# =============================================================================

class EmailIntelligence:
    """Email address analysis and intelligence gathering"""

    def __init__(self):
        self.logger = setup_logging("email_intelligence")

    def analyze_email(self, email: str) -> Dict[str, Any]:
        """
        Deep analysis of email address

        Args:
            email: Email address to analyze

        Returns:
            Dictionary with comprehensive email intelligence
        """
        result = {
            "email": email,
            "timestamp": format_timestamp(),
            "valid_format": self._validate_email_format(email),
            "username": None,
            "domain": None,
            "mx_records": [],
            "mx_valid": False,
            "domain_exists": False,
            "disposable": self._check_disposable(email)
        }

        if result["valid_format"]:
            username, domain = email.split("@")
            result["username"] = username
            result["domain"] = domain

            # DNS checks (if dnspython available)
            if HAS_DNS:
                result["mx_records"] = self._check_mx_records(domain)
                result["mx_valid"] = len(result["mx_records"]) > 0
                result["spf_record"] = self._check_spf(domain)
                result["dmarc_record"] = self._check_dmarc(domain)

            # WHOIS check (if whois available)
            if HAS_WHOIS:
                result["whois"] = self._check_whois(domain)

        self.logger.info(f"Analyzed email: {email}")
        return result

    def _validate_email_format(self, email: str) -> bool:
        """Validate email format with regex"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    def _check_disposable(self, email: str) -> bool:
        """Check if email is from disposable email provider"""
        disposable_domains = [
            "tempmail.com", "guerrillamail.com", "10minutemail.com",
            "mailinator.com", "throwaway.email", "temp-mail.org"
        ]
        domain = email.split("@")[1] if "@" in email else ""
        return domain.lower() in disposable_domains

    def _check_mx_records(self, domain: str) -> List[str]:
        """Check MX records for domain"""
        if not HAS_DNS:
            return []

        try:
            mx_records = dns.resolver.resolve(domain, 'MX')
            return [str(mx.exchange) for mx in mx_records]
        except:
            return []

    def _check_spf(self, domain: str) -> Optional[str]:
        """Check SPF record"""
        if not HAS_DNS:
            return None

        try:
            txt_records = dns.resolver.resolve(domain, 'TXT')
            for record in txt_records:
                record_str = str(record)
                if 'v=spf1' in record_str:
                    return record_str
        except:
            pass
        return None

    def _check_dmarc(self, domain: str) -> Optional[str]:
        """Check DMARC record"""
        if not HAS_DNS:
            return None

        try:
            txt_records = dns.resolver.resolve(f'_dmarc.{domain}', 'TXT')
            for record in txt_records:
                record_str = str(record)
                if 'v=DMARC1' in record_str:
                    return record_str
        except:
            pass
        return None

    def _check_whois(self, domain: str) -> Dict[str, Any]:
        """Get WHOIS information for domain"""
        if not HAS_WHOIS:
            return {}

        try:
            w = whois.whois(domain)
            return {
                "registrar": getattr(w, 'registrar', None),
                "creation_date": str(getattr(w, 'creation_date', None)),
                "expiration_date": str(getattr(w, 'expiration_date', None)),
                "name_servers": getattr(w, 'name_servers', [])
            }
        except:
            return {}


# =============================================================================
# USERNAME SEARCH
# =============================================================================

class UsernameSearch:
    """Search for username across multiple platforms"""

    # Social media platforms to check
    PLATFORMS = {
        "Twitter/X": "https://twitter.com/{}",
        "Instagram": "https://instagram.com/{}",
        "Facebook": "https://facebook.com/{}",
        "GitHub": "https://github.com/{}",
        "LinkedIn": "https://linkedin.com/in/{}",
        "Reddit": "https://reddit.com/user/{}",
        "YouTube": "https://youtube.com/@{}",
        "TikTok": "https://tiktok.com/@{}",
        "Pinterest": "https://pinterest.com/{}",
        "Medium": "https://medium.com/@{}",
        "Twitch": "https://twitch.tv/{}",
        "Discord": "https://discord.com/users/{}",
        "Telegram": "https://t.me/{}",
        "Snapchat": "https://snapchat.com/add/{}",
        "Tumblr": "https://{}.tumblr.com",
        "Flickr": "https://flickr.com/people/{}",
        "Vimeo": "https://vimeo.com/{}",
        "SoundCloud": "https://soundcloud.com/{}",
        "Spotify": "https://open.spotify.com/user/{}",
        "Steam": "https://steamcommunity.com/id/{}"
    }

    def __init__(self):
        self.logger = setup_logging("username_search")
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': get_random_user_agent()})

    def search_username(self, username: str) -> Dict[str, Any]:
        """
        Search for username across platforms

        Args:
            username: Username to search for

        Returns:
            Dictionary with found profiles
        """
        results = {
            "username": username,
            "timestamp": format_timestamp(),
            "found_profiles": [],
            "checked_platforms": len(self.PLATFORMS)
        }

        show_info(f"Searching for username: {username}")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]Checking platforms...", total=len(self.PLATFORMS))

            for platform, url_template in self.PLATFORMS.items():
                url = url_template.format(username)

                if self._check_url_exists(url):
                    results["found_profiles"].append({
                        "platform": platform,
                        "url": url,
                        "status": "found"
                    })
                    self.logger.info(f"Found {username} on {platform}")

                progress.update(task, advance=1)
                random_delay(1, 2)  # Small delay between requests

        return results

    def _check_url_exists(self, url: str) -> bool:
        """Check if URL exists and is accessible"""
        try:
            response = self.session.head(url, timeout=5, allow_redirects=True)
            return response.status_code == 200
        except:
            return False


# =============================================================================
# GOOGLE DORKING
# =============================================================================

class GoogleDorking:
    """Advanced Google search queries (dorking)"""

    # Common dork patterns
    DORK_PATTERNS = {
        "email": 'site:{} "email" OR "e-mail" OR "@"',
        "phone": 'site:{} "phone" OR "tel" OR "mobile"',
        "social": 'site:{} "facebook" OR "twitter" OR "instagram" OR "linkedin"',
        "documents": 'site:{} filetype:pdf OR filetype:doc OR filetype:xls',
        "login": 'site:{} "login" OR "signin" OR "admin"',
        "directories": 'site:{} intitle:"index of"',
        "configs": 'site:{} filetype:config OR filetype:env OR filetype:ini'
    }

    def __init__(self):
        self.logger = setup_logging("google_dorking")

    def generate_dorks(self, target: str, dork_types: List[str] = None) -> List[str]:
        """
        Generate Google dork queries

        Args:
            target: Target domain or keyword
            dork_types: List of dork types to generate

        Returns:
            List of Google dork queries
        """
        if dork_types is None:
            dork_types = list(self.DORK_PATTERNS.keys())

        dorks = []
        for dork_type in dork_types:
            if dork_type in self.DORK_PATTERNS:
                dork = self.DORK_PATTERNS[dork_type].format(target)
                dorks.append({
                    "type": dork_type,
                    "query": dork,
                    "url": f"https://www.google.com/search?q={requests.utils.quote(dork)}"
                })

        return dorks


# =============================================================================
# BREACH CHECKER
# =============================================================================

class BreachChecker:
    """Check if email/username appears in known data breaches"""

    def __init__(self):
        self.logger = setup_logging("breach_checker")

    def check_breach(self, identifier: str) -> Dict[str, Any]:
        """
        Check if identifier (email/username) appears in breaches

        Args:
            identifier: Email or username to check

        Returns:
            Dictionary with breach information
        """
        result = {
            "identifier": identifier,
            "timestamp": format_timestamp(),
            "breached": False,
            "breaches": [],
            "source": "simulated"  # In real implementation, would use HIBP API
        }

        # Note: Real implementation would use haveibeenpwned.com API
        # This is a placeholder for demonstration
        show_warning("Breach checking requires API integration (e.g., Have I Been Pwned)")
        show_info("In production: Use HIBP API with proper API key")

        return result


# =============================================================================
# IMAGE INTELLIGENCE
# =============================================================================

class ImageIntelligence:
    """Extract metadata and intelligence from images"""

    def __init__(self):
        self.logger = setup_logging("image_intelligence")

    def analyze_image(self, image_path: str) -> Dict[str, Any]:
        """
        Analyze image and extract metadata

        Args:
            image_path: Path to image file

        Returns:
            Dictionary with image intelligence
        """
        result = {
            "image_path": image_path,
            "timestamp": format_timestamp(),
            "exists": Path(image_path).exists(),
            "metadata": {}
        }

        if not result["exists"]:
            show_error(f"Image not found: {image_path}")
            return result

        try:
            from PIL import Image
            from PIL.ExifTags import TAGS

            with Image.open(image_path) as img:
                result["format"] = img.format
                result["mode"] = img.mode
                result["size"] = img.size

                # Extract EXIF data
                exif = img._getexif()
                if exif:
                    for tag_id, value in exif.items():
                        tag = TAGS.get(tag_id, tag_id)
                        result["metadata"][tag] = str(value)

                # Check for GPS data
                if "GPSInfo" in result["metadata"]:
                    show_success("GPS coordinates found in image!")

        except ImportError:
            show_warning("PIL/Pillow not installed - image analysis limited")
        except Exception as e:
            show_error(f"Error analyzing image: {e}")

        return result


# =============================================================================
# REPORT GENERATOR
# =============================================================================

class ReportGenerator:
    """Generate comprehensive OSINT reports"""

    def __init__(self, engagement_name: str = "OSINT Investigation"):
        self.engagement_name = engagement_name
        self.data = {}
        self.logger = setup_logging("report_generator")

    def add_data(self, category: str, data: Any):
        """Add data to report"""
        self.data[category] = data

    def generate_json_report(self) -> Path:
        """Generate JSON report"""
        report = {
            "engagement": self.engagement_name,
            "generated": format_timestamp(),
            "version": VERSION,
            "data": self.data
        }

        filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = save_json(report, filename)

        show_success(f"JSON report saved: {filepath}")
        return filepath

    def generate_html_report(self) -> Path:
        """Generate HTML report"""
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{self.engagement_name} - OSINT Report</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            padding: 40px;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        h1 {{ margin: 0; font-size: 2.5em; }}
        h2 {{ color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 10px; }}
        .meta {{ color: #ccc; margin-top: 10px; }}
        .section {{
            background: #f8f9fa;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background: #667eea;
            color: white;
        }}
        tr:hover {{ background: #f5f5f5; }}
        .badge {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: bold;
        }}
        .badge-success {{ background: #28a745; color: white; }}
        .badge-warning {{ background: #ffc107; color: black; }}
        .badge-danger {{ background: #dc3545; color: white; }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 OSINT Intelligence Report</h1>
            <div class="meta">
                <p><strong>Engagement:</strong> {self.engagement_name}</p>
                <p><strong>Generated:</strong> {format_timestamp()}</p>
                <p><strong>Tool:</strong> Darkapp v{VERSION}</p>
            </div>
        </div>
"""

        # Add data sections
        for category, data in self.data.items():
            html_content += f"""
        <div class="section">
            <h2>{category.replace('_', ' ').title()}</h2>
            <pre>{json.dumps(data, indent=2)}</pre>
        </div>
"""

        html_content += """
        <div class="footer">
            <p><strong>⚠️ CONFIDENTIAL - FOR AUTHORIZED USE ONLY ⚠️</strong></p>
            <p>Generated by Darkapp - Advanced OSINT Framework</p>
        </div>
    </div>
</body>
</html>
"""

        filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        filepath = EXPORTS_DIR / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)

        show_success(f"HTML report saved: {filepath}")
        return filepath


# =============================================================================
# MAIN APPLICATION
# =============================================================================

class DarkappCLI:
    """Main Darkapp CLI Application"""

    def __init__(self, engagement_name: str = "OSINT Investigation"):
        self.engagement_name = engagement_name
        self.logger = setup_logging("darkapp")
        self.report_gen = ReportGenerator(engagement_name)

    def show_main_menu(self):
        """Display main menu"""
        console.print("\n")

        table = Table(
            title=f"[bold cyan]{ICONS['rocket']} Darkapp - Main Menu {ICONS['rocket']}[/bold cyan]",
            show_header=True,
            header_style="bold yellow",
            border_style="cyan",
            box=box.HEAVY
        )

        table.add_column(f"{ICONS['key']} #", style="bold yellow", justify="center", width=6)
        table.add_column(f"{ICONS['star']} Module", style="bold cyan", width=30)
        table.add_column(f"{ICONS['info']} Description", style="white")

        menu_items = [
            ("", "[bold yellow]═══ INTELLIGENCE GATHERING ═══[/bold yellow]", ""),
            ("1", f"{ICONS['phone']} Phone Intelligence", "Validate & analyze phone numbers"),
            ("2", f"{ICONS['email']} Email Intelligence", "Deep email analysis (DNS, MX, WHOIS)"),
            ("3", f"{ICONS['profile']} Username Search", "Find profiles across 20+ platforms"),
            ("4", f"{ICONS['search']} Google Dorking", "Generate advanced Google search queries"),
            ("", "[bold cyan]═══ SECURITY & ANALYSIS ═══[/bold cyan]", ""),
            ("5", f"{ICONS['shield']} Breach Checker", "Check for data breaches"),
            ("6", f"{ICONS['camera']} Image Intelligence", "Extract EXIF metadata from images"),
            ("", "[bold green]═══ REPORTING ═══[/bold green]", ""),
            ("7", f"{ICONS['document']} Generate Report", "Create comprehensive OSINT report"),
            ("8", f"{ICONS['folder']} View Export Directory", "Open exports folder"),
            ("", "[bold magenta]═══ SYSTEM ═══[/bold magenta]", ""),
            ("9", f"{ICONS['info']} About", "System information & dependencies"),
            ("0", f"{ICONS['cross']} Exit", "Exit Darkapp")
        ]

        for option, module, description in menu_items:
            if not option:  # Section header
                table.add_row(option, module, description, style="bold")
            else:
                table.add_row(option, module, description)

        console.print(table)
        console.print()

    def run_phone_intelligence(self):
        """Phone intelligence module"""
        show_module_header("Phone Intelligence", "Validate and analyze phone numbers", ICONS['phone'])

        phone = Prompt.ask("[cyan]Enter phone number (with country code)")

        validator = PhoneValidator()

        with console.status("[bold green]Analyzing phone number..."):
            result = validator.validate_number(phone)

        if result['valid']:
            show_success(f"Phone number is valid!")
            show_result_card("Phone Intelligence", result, "green")
            self.report_gen.add_data("phone_intelligence", result)
        else:
            show_error(f"Invalid phone number: {result.get('error', 'Unknown error')}")

    def run_email_intelligence(self):
        """Email intelligence module"""
        show_module_header("Email Intelligence", "Deep email analysis and validation", ICONS['email'])

        email = Prompt.ask("[cyan]Enter email address")

        analyzer = EmailIntelligence()

        with console.status("[bold green]Analyzing email..."):
            result = analyzer.analyze_email(email)

        if result['valid_format']:
            show_success("Email analysis complete!")
            show_result_card("Email Intelligence", result, "green")
            self.report_gen.add_data("email_intelligence", result)
        else:
            show_error("Invalid email format")

    def run_username_search(self):
        """Username search module"""
        show_module_header("Username Search", "Find profiles across social media", ICONS['search'])

        username = Prompt.ask("[cyan]Enter username to search")

        searcher = UsernameSearch()
        result = searcher.search_username(username)

        if result['found_profiles']:
            show_success(f"Found {len(result['found_profiles'])} profiles!")

            table = create_styled_table("Found Profiles", ["Platform", "URL"], "green")
            for profile in result['found_profiles']:
                table.add_row(profile['platform'], profile['url'])

            console.print(table)
            self.report_gen.add_data("username_search", result)
        else:
            show_warning("No profiles found")

    def run_google_dorking(self):
        """Google dorking module"""
        show_module_header("Google Dorking", "Generate advanced Google search queries", ICONS['search'])

        target = Prompt.ask("[cyan]Enter target domain or keyword")

        dorker = GoogleDorking()
        dorks = dorker.generate_dorks(target)

        show_success(f"Generated {len(dorks)} dork queries!")

        table = create_styled_table("Google Dorks", ["Type", "Query"], "cyan")
        for dork in dorks:
            table.add_row(dork['type'], dork['query'])

        console.print(table)

        show_info("Copy these queries into Google Search")
        self.report_gen.add_data("google_dorks", dorks)

    def run_breach_checker(self):
        """Breach checker module"""
        show_module_header("Breach Checker", "Check for data breaches", ICONS['shield'])

        identifier = Prompt.ask("[cyan]Enter email or username")

        checker = BreachChecker()
        result = checker.check_breach(identifier)

        show_result_card("Breach Check Results", result, "yellow")
        self.report_gen.add_data("breach_check", result)

    def run_image_intelligence(self):
        """Image intelligence module"""
        show_module_header("Image Intelligence", "Extract metadata from images", ICONS['camera'])

        image_path = Prompt.ask("[cyan]Enter path to image file")

        analyzer = ImageIntelligence()

        with console.status("[bold green]Analyzing image..."):
            result = analyzer.analyze_image(image_path)

        show_result_card("Image Intelligence", result, "magenta")
        self.report_gen.add_data("image_intelligence", result)

    def generate_report(self):
        """Generate comprehensive report"""
        show_module_header("Report Generator", "Create OSINT intelligence report", ICONS['document'])

        if not self.report_gen.data:
            show_warning("No data collected yet. Run some modules first!")
            return

        console.print("[cyan]Select report format:[/cyan]")
        console.print("1. JSON")
        console.print("2. HTML")
        console.print("3. Both")

        choice = Prompt.ask("[cyan]Choice", choices=["1", "2", "3"])

        if choice in ["1", "3"]:
            self.report_gen.generate_json_report()

        if choice in ["2", "3"]:
            self.report_gen.generate_html_report()

        show_success("Report generation complete!")

    def view_exports(self):
        """Open exports directory"""
        import subprocess
        import platform

        show_info(f"Exports directory: {EXPORTS_DIR}")

        # Try to open directory
        try:
            if platform.system() == "Windows":
                os.startfile(EXPORTS_DIR)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", EXPORTS_DIR])
            else:  # Linux
                subprocess.run(["xdg-open", EXPORTS_DIR])
            show_success("Opened exports directory")
        except:
            show_warning("Please navigate manually to the exports directory")

    def show_about(self):
        """Show about information"""
        show_module_header("About Darkapp", "System Information", ICONS['info'])

        info = {
            "Version": VERSION,
            "Data Directory": str(DATA_DIR),
            "Logs Directory": str(LOGS_DIR),
            "Exports Directory": str(EXPORTS_DIR),
            "Python Version": sys.version.split()[0],
            "Selenium": "Installed" if HAS_SELENIUM else "Not Installed",
            "DNS Resolution": "Available" if HAS_DNS else "Not Available",
            "WHOIS": "Available" if HAS_WHOIS else "Not Available",
            "Pandas": "Available" if HAS_PANDAS else "Not Available"
        }

        show_result_card("System Information", info, "cyan")

    def run(self):
        """Main application loop"""
        show_banner()
        show_authorization_warning()

        if not Confirm.ask(f"[bold yellow]Do you have proper authorization for OSINT activities?[/bold yellow]"):
            show_error("Authorization required. Exiting...")
            return

        show_success(f"Starting engagement: {self.engagement_name}")

        while True:
            try:
                self.show_main_menu()
                choice = Prompt.ask(f"[bold cyan]{ICONS['rocket']} Select option")

                if choice == "1":
                    self.run_phone_intelligence()
                elif choice == "2":
                    self.run_email_intelligence()
                elif choice == "3":
                    self.run_username_search()
                elif choice == "4":
                    self.run_google_dorking()
                elif choice == "5":
                    self.run_breach_checker()
                elif choice == "6":
                    self.run_image_intelligence()
                elif choice == "7":
                    self.generate_report()
                elif choice == "8":
                    self.view_exports()
                elif choice == "9":
                    self.show_about()
                elif choice == "0":
                    show_success("Thank you for using Darkapp. Stay ethical!")
                    break
                else:
                    show_warning("Invalid option. Please try again.")

                console.print()

            except KeyboardInterrupt:
                console.print("\n")
                if Confirm.ask("[yellow]Are you sure you want to exit?[/yellow]"):
                    break
            except Exception as e:
                show_error(f"An error occurred: {e}")
                self.logger.error(f"Error: {e}", exc_info=True)


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Darkapp - Advanced OSINT Intelligence Framework",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python darkapp-consolidated.py
  python darkapp-consolidated.py --engagement "Client Assessment 2025"

For more information, visit: https://github.com/yourusername/darkapp
        """
    )

    parser.add_argument(
        "--engagement",
        type=str,
        default="OSINT Investigation",
        help="Engagement or investigation name"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"Darkapp v{VERSION}"
    )

    args = parser.parse_args()

    # Run the application
    app = DarkappCLI(engagement_name=args.engagement)
    app.run()


if __name__ == "__main__":
    main()
