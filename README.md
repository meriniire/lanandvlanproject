# lanandvlanproject
🔒 Secure LAN Simulator - Learn VLANs (IEEE 802.1Q) &amp; firewalls. Design topologies, configure VLANs, set firewall rules, simulate packets with 802.1Q tagging. Includes assessments &amp; logging. Python/Streamlit.

# 🔒 Secure LAN Simulator

**Design and Implementation of a Secure LAN Using VLANs and Firewalls** | IEEE 802.1Q Compliant

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![IEEE 802.1Q](https://img.shields.io/badge/IEEE-802.1Q-green.svg)](https://ieeexplore.ieee.org/document/6547019)

## 📋 Overview

Enterprise-grade network security training platform demonstrating VLANs and firewall configurations through interactive simulation. Perfect for networking students, IT professionals, and security enthusiasts.

## ✨ Key Features

- **VLAN Configuration** - IEEE 802.1Q compliant, supports up to 4094 VLANs
- **Firewall Rules** - Priority-based processing with implicit deny
- **Packet Simulation** - Real-time visualization with 802.1Q tagging
- **Topology Builder** - Multiple isolated network environments
- **Inter-VLAN Routing** - Router-on-a-stick simulation
- **Audit Logging** - Complete packet history for analysis
- **Assessments** - Built-in quizzes and troubleshooting scenarios
- **9 Database Tables** - Full data persistence with CSV storage

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/secure-lan-simulator.git
cd secure-lan-simulator

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
