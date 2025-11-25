#!/bin/bash
#
# Darkapp - Quick Installation Script
# Single File Edition
#

set -e

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "   🚀 Darkapp - Quick Installation Script 🚀"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Check Python
echo -e "${CYAN}[1/4] Checking Python installation...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 not found. Please install Python 3.8+${NC}"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo -e "${GREEN}✅ Python ${PYTHON_VERSION} found${NC}"
echo ""

# Check pip
echo -e "${CYAN}[2/4] Checking pip installation...${NC}"
if ! command -v pip3 &> /dev/null; then
    echo -e "${RED}❌ pip3 not found. Please install pip${NC}"
    exit 1
fi

echo -e "${GREEN}✅ pip3 found${NC}"
echo ""

# Install dependencies
echo -e "${CYAN}[3/4] Installing dependencies...${NC}"
echo -e "${YELLOW}This may take a few minutes...${NC}"

# Check if requirements file exists
if [ -f "darkapp-requirements.txt" ]; then
    pip3 install -r darkapp-requirements.txt --quiet
else
    # Install minimal requirements
    pip3 install rich requests beautifulsoup4 phonenumbers --quiet
fi

echo -e "${GREEN}✅ Dependencies installed${NC}"
echo ""

# Make executable
echo -e "${CYAN}[4/4] Setting up Darkapp...${NC}"
if [ -f "darkapp-consolidated.py" ]; then
    chmod +x darkapp-consolidated.py
    echo -e "${GREEN}✅ Darkapp is now executable${NC}"
else
    echo -e "${RED}❌ darkapp-consolidated.py not found in current directory${NC}"
    exit 1
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${GREEN}   ✅ Installation Complete! ✅${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo -e "${CYAN}To run Darkapp:${NC}"
echo -e "  ${YELLOW}./darkapp-consolidated.py${NC}"
echo ""
echo -e "${CYAN}For help:${NC}"
echo -e "  ${YELLOW}./darkapp-consolidated.py --help${NC}"
echo ""
echo -e "${CYAN}For custom engagement:${NC}"
echo -e "  ${YELLOW}./darkapp-consolidated.py --engagement \"My Assessment 2025\"${NC}"
echo ""
echo -e "${RED}⚠️  REMEMBER: Only use with proper authorization! ⚠️${NC}"
echo ""
