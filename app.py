"""
DESIGN AND IMPLEMENTATION OF A SECURE LAN USING VLANS AND FIREWALLS
===================================================================
Complete Streamlit Application with Full Database Integration
Tables: USERS, TOPOLOGIES, VLANS, FIREWALL_RULES, PACKET_LOGS, VLAN_MEMBERS, RULE_SEQUENCE
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import random
import time
import os
import hashlib

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="Secure LAN: VLAN + Firewall Simulation System",
    layout="wide",
    page_icon="🔒",
    initial_sidebar_state="expanded"
)

# ============================================================================
# APPLICATION HEADER
# ============================================================================
st.markdown("""
<div style="text-align: center; padding: 25px; background: linear-gradient(135deg, #3e2723 0%, #4e342e 100%); border-radius: 20px; margin-bottom: 20px; border-bottom: 4px solid #d4a017; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
    <h1 style="color: #ffffff; margin-bottom: 5px; font-size: 1.8rem;">🔒 DESIGN AND IMPLEMENTATION OF A SECURE LAN</h1>
    <h2 style="color: #f5d060; font-size: 1.2rem; margin-bottom: 10px;">Using VLANs and Firewalls | IEEE 802.1Q Compliant</h2>
    <p style="color: #e8d5a5; margin-top: 10px;">Network Security Simulation Platform | Enterprise-Grade Training System</p>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# PROFESSIONAL CSS STYLING - BROWN AND GOLDEN THEME WITH WHITE TEXT
# ============================================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #2c1810 0%, #3e2723 100%);
    }
    
    /* Main text color - WHITE for visibility */
    .stMarkdown, .stMarkdown p, .stText, .stCaption {
        color: #ffffff !important;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #4a2c1a 0%, #3e2723 100%) !important;
        border-right: 2px solid #d4a017;
    }
    
    /* Sidebar ALL text - WHITE */
    section[data-testid="stSidebar"] .stMarkdown,
    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] .stRadio label,
    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] .stRadio div,
    section[data-testid="stSidebar"] div[role="radiogroup"] label,
    section[data-testid="stSidebar"] .stSelectbox div,
    section[data-testid="stSidebar"] .stButton p {
        color: #ffffff !important;
    }
    
    /* Sidebar Headers - Gold */
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] .stMarkdown h1,
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: #f5d060 !important;
        border-bottom: 2px solid #d4a017;
    }
    
    /* Sidebar Radio Buttons - White text */
    section[data-testid="stSidebar"] .stRadio label {
        color: #ffffff !important;
        font-weight: 500;
    }
    
    section[data-testid="stSidebar"] .stRadio [data-baseweb="radio"]:checked + label {
        color: #f5d060 !important;
        background-color: rgba(212, 160, 23, 0.3);
        border-radius: 8px;
        padding: 8px 12px;
    }
    
    section[data-testid="stSidebar"] .stRadio [data-baseweb="radio"]:hover + label {
        background-color: rgba(212, 160, 23, 0.2);
        border-radius: 8px;
    }
    
    /* Sidebar Selectbox */
    section[data-testid="stSidebar"] .stSelectbox > div > div {
        background-color: #3e2723 !important;
        border: 1px solid #d4a017 !important;
        color: #ffffff !important;
    }
    
    section[data-testid="stSidebar"] .stSelectbox label {
        color: #f5d060 !important;
    }
    
    /* Sidebar Button */
    section[data-testid="stSidebar"] .stButton > button {
        color: #2c1810 !important;
    }
    
    /* Main Headers - White and Gold */
    h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #ffffff !important;
        font-weight: 700;
    }
    
    h1 {
        border-bottom: 2px solid #d4a017;
        padding-bottom: 10px;
    }
    
    /* Metric Cards */
    div[data-testid="stMetric"] {
        background: #4a2c1a;
        border-radius: 16px;
        padding: 20px;
        border: 1px solid #d4a017;
        transition: all 0.3s ease;
    }
    
    div[data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        border-color: #f5d060;
        box-shadow: 0 10px 25px rgba(212, 160, 23, 0.3);
    }
    
    div[data-testid="stMetricValue"] {
        color: #f5d060 !important;
        font-size: 2rem !important;
        font-weight: 800 !important;
    }
    
    div[data-testid="stMetricLabel"] {
        color: #e8d5a5 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-size: 0.7rem !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #d4a017 0%, #b8860b 100%);
        color: #2c1810 !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #f5d060 0%, #d4a017 100%);
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(212, 160, 23, 0.4);
    }
    
    /* Form Inputs */
    .stTextInput > div > div > input, 
    .stNumberInput > div > div > input, 
    .stSelectbox > div > div,
    .stTextArea > div > div > textarea {
        background-color: #3e2723 !important;
        border: 1px solid #d4a017 !important;
        border-radius: 10px !important;
        color: #ffffff !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #f5d060 !important;
        box-shadow: 0 0 0 2px rgba(212, 160, 23, 0.3);
    }
    
    /* Labels */
    .stTextInput label, .stNumberInput label, .stSelectbox label, .stTextArea label {
        color: #e8d5a5 !important;
        font-weight: 500 !important;
    }
    
    /* Dataframe Styling */
    .dataframe {
        border-radius: 12px !important;
        overflow: hidden !important;
    }
    
    .dataframe th {
        background: linear-gradient(135deg, #4a2c1a 0%, #3e2723 100%) !important;
        color: #f5d060 !important;
        font-weight: 600 !important;
        padding: 12px !important;
    }
    
    .dataframe td {
        background-color: #3e2723 !important;
        color: #ffffff !important;
        padding: 10px !important;
    }
    
    /* Alert Boxes */
    .stAlert {
        border-radius: 12px !important;
        border-left-width: 4px !important;
        background-color: #4a2c1a !important;
    }
    
    .stSuccess {
        border-left-color: #d4a017 !important;
        color: #ffffff !important;
    }
    
    .stWarning {
        border-left-color: #f5d060 !important;
        color: #ffffff !important;
    }
    
    .stError {
        border-left-color: #ef4444 !important;
        color: #ffffff !important;
    }
    
    .stInfo {
        border-left-color: #d4a017 !important;
        color: #ffffff !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #4a2c1a !important;
        border-radius: 10px !important;
        border-left: 3px solid #d4a017 !important;
        color: #f5d060 !important;
    }
    
    .streamlit-expanderContent {
        background-color: #3e2723 !important;
        color: #ffffff !important;
    }
    
    /* Code Block */
    .stCodeBlock {
        background-color: #2c1810 !important;
        border-radius: 10px !important;
        border: 1px solid #d4a017;
        color: #e8d5a5 !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 20px;
        color: #e8d5a5;
        font-size: 12px;
        border-top: 1px solid #d4a017;
        margin-top: 30px;
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #4a2c1a;
        border-radius: 10px 10px 0 0;
        color: #e8d5a5;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #d4a017 0%, #b8860b 100%);
        color: #2c1810 !important;
    }
    
    /* Slider */
    .stSlider > div > div > div {
        background-color: #5c3a21 !important;
    }
    
    .stSlider > div > div > div > div {
        background-color: #d4a017 !important;
    }
    
    .stSlider label {
        color: #e8d5a5 !important;
    }
    
    /* Download Button */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #d4a017 0%, #b8860b 100%);
        color: #2c1810 !important;
        border: none !important;
        font-weight: 600 !important;
    }
    
    /* Radio Buttons */
    .stRadio label {
        color: #ffffff !important;
    }
    
    .stRadio [data-baseweb="radio"]:checked + label {
        color: #f5d060 !important;
    }
    
    /* Checkbox */
    .stCheckbox label {
        color: #ffffff !important;
    }
    
    /* Selectbox in main area */
    .stSelectbox div[data-baseweb="select"] {
        color: #ffffff !important;
    }
    
    /* Info/Warning/Success/Error text */
    .stAlert p {
        color: #ffffff !important;
    }
    
    /* Metric delta */
    div[data-testid="stMetricDelta"] {
        color: #e8d5a5 !important;
    }
    
    /* Sidebar caption and small text */
    section[data-testid="stSidebar"] .stCaption,
    section[data-testid="stSidebar"] small,
    section[data-testid="stSidebar"] .stSmall {
        color: #e8d5a5 !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA DIRECTORY
# ============================================================================
DATA_DIR = "secure_lan_data"
os.makedirs(DATA_DIR, exist_ok=True)

# ============================================================================
# DATABASE INITIALIZATION - ALL TABLES FROM ERD
# ============================================================================
def init_all_tables():
    """Initialize all database tables matching the ERD schema"""
    
    # TABLE 1: USERS
    if not os.path.exists(os.path.join(DATA_DIR, "users.csv")):
        users = pd.DataFrame([{
            "user_id": 1,
            "username": "admin",
            "password": hashlib.sha256("admin123".encode()).hexdigest(),
            "role": "Administrator",
            "email": "admin@securelan.com",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }])
        users.to_csv(os.path.join(DATA_DIR, "users.csv"), index=False)
    
    # TABLE 2: TOPOLOGIES
    if not os.path.exists(os.path.join(DATA_DIR, "topologies.csv")):
        topologies = pd.DataFrame(columns=[
            "topology_id", "topology_name", "created_by", 
            "switch_count", "vlan_count", "rule_count", "created_at"
        ])
        topologies.to_csv(os.path.join(DATA_DIR, "topologies.csv"), index=False)
    
    # TABLE 3: VLANS
    if not os.path.exists(os.path.join(DATA_DIR, "vlans.csv")):
        vlans = pd.DataFrame(columns=[
            "vlan_id", "vlan_name", "topology_id", 
            "subnet", "gateway", "is_active", "created_at"
        ])
        vlans.to_csv(os.path.join(DATA_DIR, "vlans.csv"), index=False)
    
    # TABLE 4: FIREWALL_RULES
    if not os.path.exists(os.path.join(DATA_DIR, "firewall_rules.csv")):
        rules = pd.DataFrame(columns=[
            "rule_id", "topology_id", "source_vlan", "destination_vlan",
            "protocol", "source_port", "destination_port", "action", "priority", "created_at"
        ])
        rules.to_csv(os.path.join(DATA_DIR, "firewall_rules.csv"), index=False)
    
    # TABLE 5: PACKET_LOGS
    if not os.path.exists(os.path.join(DATA_DIR, "packet_logs.csv")):
        logs = pd.DataFrame(columns=[
            "log_id", "session_id", "source_vlan", "destination_vlan",
            "packet_size", "vlan_tag", "action", "protocol", "port", "timestamp"
        ])
        logs.to_csv(os.path.join(DATA_DIR, "packet_logs.csv"), index=False)
    
    # TABLE 6: VLAN_MEMBERS
    if not os.path.exists(os.path.join(DATA_DIR, "vlan_members.csv")):
        members = pd.DataFrame(columns=[
            "member_id", "vlan_id", "device_name", "mac_address", 
            "ip_address", "port_number", "status", "assigned_at"
        ])
        members.to_csv(os.path.join(DATA_DIR, "vlan_members.csv"), index=False)
    
    # TABLE 7: RULE_SEQUENCE
    if not os.path.exists(os.path.join(DATA_DIR, "rule_sequence.csv")):
        sequences = pd.DataFrame(columns=[
            "sequence_id", "rule_id", "priority_order", "description", "created_at"
        ])
        sequences.to_csv(os.path.join(DATA_DIR, "rule_sequence.csv"), index=False)
    
    # TABLE 8: SCENARIOS
    if not os.path.exists(os.path.join(DATA_DIR, "scenarios.csv")):
        scenarios = pd.DataFrame([
            {"scenario_id": 1, "name": "VLAN Segmentation Design", "difficulty": "Intermediate", 
             "description": "Design a VLAN structure for a company with Sales, Engineering, and HR departments", 
             "solution_hint": "Create separate VLANs for each department with inter-VLAN routing"},
            {"scenario_id": 2, "name": "Firewall Policy Implementation", "difficulty": "Advanced", 
             "description": "Configure firewall rules to allow only web traffic from Sales to DMZ", 
             "solution_hint": "Allow TCP port 80/443 from Sales VLAN to DMZ VLAN"},
            {"scenario_id": 3, "name": "Troubleshooting VLAN Connectivity", "difficulty": "Beginner", 
             "description": "Fix connectivity issues between devices on the same VLAN", 
             "solution_hint": "Check VLAN port assignments and trunk configurations"}
        ])
        scenarios.to_csv(os.path.join(DATA_DIR, "scenarios.csv"), index=False)
    
    # TABLE 9: ASSESSMENTS
    if not os.path.exists(os.path.join(DATA_DIR, "assessments.csv")):
        assessments = pd.DataFrame(columns=[
            "assessment_id", "user_id", "scenario_id", "score", "completed_at"
        ])
        assessments.to_csv(os.path.join(DATA_DIR, "assessments.csv"), index=False)


init_all_tables()

# ============================================================================
# DATABASE HELPER FUNCTIONS
# ============================================================================

def get_all_users():
    return pd.read_csv(os.path.join(DATA_DIR, "users.csv"))

def authenticate_user(username, password):
    users = get_all_users()
    hashed = hashlib.sha256(password.encode()).hexdigest()
    user = users[(users["username"] == username) & (users["password"] == hashed)]
    if not user.empty:
        return user.iloc[0]["user_id"], user.iloc[0]["role"]
    return None, None

def get_all_topologies():
    return pd.read_csv(os.path.join(DATA_DIR, "topologies.csv"))

def create_topology(name, username, switch_count=2):
    topologies = get_all_topologies()
    new_id = topologies["topology_id"].max() + 1 if not topologies.empty else 1
    
    new_topology = pd.DataFrame([{
        "topology_id": new_id,
        "topology_name": name,
        "created_by": username,
        "switch_count": switch_count,
        "vlan_count": 0,
        "rule_count": 0,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }])
    
    topologies = pd.concat([topologies, new_topology], ignore_index=True)
    topologies.to_csv(os.path.join(DATA_DIR, "topologies.csv"), index=False)
    return new_id

def update_topology_counts(topology_id, vlan_increment=0, rule_increment=0):
    topologies = get_all_topologies()
    idx = topologies[topologies["topology_id"] == topology_id].index
    if len(idx) > 0:
        topologies.loc[idx, "vlan_count"] += vlan_increment
        topologies.loc[idx, "rule_count"] += rule_increment
        topologies.to_csv(os.path.join(DATA_DIR, "topologies.csv"), index=False)

def get_all_vlans():
    return pd.read_csv(os.path.join(DATA_DIR, "vlans.csv"))

def get_vlans_by_topology(topology_id):
    vlans = get_all_vlans()
    return vlans[vlans["topology_id"] == topology_id]

def create_vlan(vlan_id, vlan_name, topology_id, subnet, gateway):
    vlans = get_all_vlans()
    
    existing = vlans[(vlans["topology_id"] == topology_id) & (vlans["vlan_id"] == vlan_id)]
    if not existing.empty:
        return False, f"VLAN ID {vlan_id} already exists"
    
    new_vlan = pd.DataFrame([{
        "vlan_id": vlan_id,
        "vlan_name": vlan_name,
        "topology_id": topology_id,
        "subnet": subnet,
        "gateway": gateway,
        "is_active": True,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }])
    
    vlans = pd.concat([vlans, new_vlan], ignore_index=True)
    vlans.to_csv(os.path.join(DATA_DIR, "vlans.csv"), index=False)
    update_topology_counts(topology_id, vlan_increment=1)
    return True, "VLAN created successfully"

def get_vlan_members(vlan_id):
    members = pd.read_csv(os.path.join(DATA_DIR, "vlan_members.csv"))
    return members[members["vlan_id"] == vlan_id]

def add_vlan_member(vlan_id, device_name, mac_address, ip_address, port_number):
    members = pd.read_csv(os.path.join(DATA_DIR, "vlan_members.csv"))
    new_id = members["member_id"].max() + 1 if not members.empty else 1
    
    new_member = pd.DataFrame([{
        "member_id": new_id,
        "vlan_id": vlan_id,
        "device_name": device_name,
        "mac_address": mac_address,
        "ip_address": ip_address,
        "port_number": port_number,
        "status": "active",
        "assigned_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }])
    
    members = pd.concat([members, new_member], ignore_index=True)
    members.to_csv(os.path.join(DATA_DIR, "vlan_members.csv"), index=False)
    return new_id

def get_all_firewall_rules():
    return pd.read_csv(os.path.join(DATA_DIR, "firewall_rules.csv"))

def get_rules_by_topology(topology_id):
    rules = get_all_firewall_rules()
    return rules[rules["topology_id"] == topology_id]

def create_firewall_rule(topology_id, source_vlan, dest_vlan, protocol, dest_port, action, priority):
    rules = get_all_firewall_rules()
    new_id = rules["rule_id"].max() + 1 if not rules.empty else 1
    
    new_rule = pd.DataFrame([{
        "rule_id": new_id,
        "topology_id": topology_id,
        "source_vlan": source_vlan,
        "destination_vlan": dest_vlan,
        "protocol": protocol,
        "source_port": 0,
        "destination_port": dest_port,
        "action": action,
        "priority": priority,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }])
    
    rules = pd.concat([rules, new_rule], ignore_index=True)
    rules.to_csv(os.path.join(DATA_DIR, "firewall_rules.csv"), index=False)
    
    add_rule_sequence(new_id, priority, f"Rule {action} from {source_vlan} to {dest_vlan}")
    update_topology_counts(topology_id, rule_increment=1)
    return new_id

def get_rule_sequence():
    return pd.read_csv(os.path.join(DATA_DIR, "rule_sequence.csv"))

def add_rule_sequence(rule_id, priority, description):
    sequences = get_rule_sequence()
    new_id = sequences["sequence_id"].max() + 1 if not sequences.empty else 1
    
    new_sequence = pd.DataFrame([{
        "sequence_id": new_id,
        "rule_id": rule_id,
        "priority_order": priority,
        "description": description,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }])
    
    sequences = pd.concat([sequences, new_sequence], ignore_index=True)
    sequences.to_csv(os.path.join(DATA_DIR, "rule_sequence.csv"), index=False)

def get_all_packet_logs():
    return pd.read_csv(os.path.join(DATA_DIR, "packet_logs.csv"))

def log_packet(session_id, source_vlan, dest_vlan, packet_size, vlan_tag, action, protocol, port):
    logs = get_all_packet_logs()
    new_id = logs["log_id"].max() + 1 if not logs.empty else 1
    
    new_log = pd.DataFrame([{
        "log_id": new_id,
        "session_id": session_id,
        "source_vlan": source_vlan,
        "destination_vlan": dest_vlan,
        "packet_size": packet_size,
        "vlan_tag": vlan_tag,
        "action": action,
        "protocol": protocol,
        "port": port,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }])
    
    logs = pd.concat([logs, new_log], ignore_index=True)
    logs.to_csv(os.path.join(DATA_DIR, "packet_logs.csv"), index=False)

def get_all_scenarios():
    return pd.read_csv(os.path.join(DATA_DIR, "scenarios.csv"))

def save_assessment(user_id, scenario_id, score):
    assessments = pd.read_csv(os.path.join(DATA_DIR, "assessments.csv"))
    new_id = assessments["assessment_id"].max() + 1 if not assessments.empty else 1
    
    new_assessment = pd.DataFrame([{
        "assessment_id": new_id,
        "user_id": user_id,
        "scenario_id": scenario_id,
        "score": score,
        "completed_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }])
    
    assessments = pd.concat([assessments, new_assessment], ignore_index=True)
    assessments.to_csv(os.path.join(DATA_DIR, "assessments.csv"), index=False)


# ============================================================================
# NETWORK SIMULATION ENGINE
# ============================================================================
class NetworkSimulationEngine:
    @staticmethod
    def simulate_packet(source_vlan, dest_vlan, protocol, port, firewall_rules):
        if firewall_rules.empty:
            return "DENY", None
        
        sorted_rules = firewall_rules.sort_values("priority")
        
        for _, rule in sorted_rules.iterrows():
            source_match = (str(rule["source_vlan"]).upper() == source_vlan.upper() or 
                           str(rule["source_vlan"]).upper() == "ANY")
            dest_match = (str(rule["destination_vlan"]).upper() == dest_vlan.upper() or 
                         str(rule["destination_vlan"]).upper() == "ANY")
            proto_match = (rule["protocol"].upper() == protocol.upper() or 
                          rule["protocol"].upper() == "ANY")
            port_match = (rule["destination_port"] == port or rule["destination_port"] == 0)
            
            if source_match and dest_match and proto_match and port_match:
                return rule["action"], rule["rule_id"]
        
        return "DENY", None
    
    @staticmethod
    def add_vlan_tag(packet_id, vlan_id):
        return {
            "packet_id": packet_id,
            "original_frame": "Ethernet Frame (untagged)",
            "vlan_tag": f"802.1Q VLAN {vlan_id} Tag Inserted",
            "priority_code_point": random.randint(0, 7),
            "tagged_frame": f"Ethernet Frame + VLAN {vlan_id} Tag (4 bytes)"
        }
    
    @staticmethod
    def simulate_inter_vlan_routing(source_vlan_data, dest_vlan_data):
        return [
            f"[1] Packet arrives at default gateway ({source_vlan_data['gateway']})",
            f"[2] Router strips source VLAN tag (VID: {source_vlan_data['vlan_id']})",
            "[3] Router checks routing table for destination subnet",
            f"[4] Destination network {dest_vlan_data['subnet']} found",
            f"[5] Router adds destination VLAN tag (VID: {dest_vlan_data['vlan_id']})",
            f"[6] Packet forwarded to {dest_vlan_data['gateway']}"
        ]


# ============================================================================
# SESSION STATE
# ============================================================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_id" not in st.session_state:
    st.session_state.user_id = None
if "user_role" not in st.session_state:
    st.session_state.user_role = None
if "current_topology" not in st.session_state:
    st.session_state.current_topology = None
if "simulation_active" not in st.session_state:
    st.session_state.simulation_active = False
if "session_id" not in st.session_state:
    st.session_state.session_id = f"SES_{datetime.now().strftime('%Y%m%d%H%M%S')}_{random.randint(1000, 9999)}"

# ============================================================================
# LOGIN FORM
# ============================================================================
if not st.session_state.logged_in:
    st.markdown("### 🔐 Login to Secure LAN System")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            
            if submitted:
                user_id, role = authenticate_user(username, password)
                if user_id:
                    st.session_state.logged_in = True
                    st.session_state.user_id = user_id
                    st.session_state.user_role = role
                    st.success(f"✅ Welcome, {username}!")
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password")
    
    st.markdown("---")
    st.markdown("**Demo Credentials:** Username: `admin`, Password: `admin123`")
    st.stop()

# ============================================================================
# SIDEBAR NAVIGATION - WITH WHITE FONT
# ============================================================================
with st.sidebar:
    st.markdown(f"### 👤 {st.session_state.user_role}")
    st.markdown(f"User ID: {st.session_state.user_id}")
    st.markdown("---")
    
    menu = st.radio("📋 MENU", [
        "📊 Dashboard",
        "🏗️ Topology Builder",
        "🔧 VLAN Configuration",
        "👥 VLAN Members",
        "🔥 Firewall Rules",
        "📋 Rule Sequence",
        "📡 Packet Simulation",
        "📊 Policy Comparison",
        "📜 Packet Logs",
        "🔍 Troubleshooting",
        "📝 Assessments",
        "🗄️ Database Tables",
        "ℹ️ System Info"
    ])
    
    st.markdown("---")
    st.markdown("### 📊 System Status")
    st.markdown("🟢 Engine: Active")
    st.markdown(f"📅 {datetime.now().strftime('%Y-%m-%d')}")
    st.markdown(f"⏰ {datetime.now().strftime('%H:%M:%S')}")
    
    st.markdown("---")
    st.markdown("### 📚 IEEE 802.1Q")
    st.markdown("VLAN Tagging Standard")
    st.markdown("4-byte Tag inserted")
    st.markdown("12-bit VLAN ID (4096 VLANs)")
    
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.session_state.user_role = None
        st.rerun()

# Clean menu name for display
menu_clean = menu.replace("📊 ", "").replace("🏗️ ", "").replace("🔧 ", "").replace("👥 ", "").replace("🔥 ", "").replace("📋 ", "").replace("📡 ", "").replace("🔍 ", "").replace("📝 ", "").replace("🗄️ ", "").replace("ℹ️ ", "")

# ============================================================================
# PAGE 1: DASHBOARD
# ============================================================================
if menu_clean == "Dashboard":
    st.markdown("# 📊 System Dashboard")
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        topologies = get_all_topologies()
        st.metric("🌐 Topologies", len(topologies))
    
    with col2:
        vlans = get_all_vlans()
        st.metric("🔧 VLANs", len(vlans))
    
    with col3:
        rules = get_all_firewall_rules()
        st.metric("🔥 Firewall Rules", len(rules))
    
    with col4:
        logs = get_all_packet_logs()
        st.metric("📦 Total Packets", len(logs))
    
    st.markdown("---")
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.markdown("### 📊 VLAN Distribution")
        if not vlans.empty:
            vlan_counts = vlans["vlan_id"].value_counts().reset_index()
            vlan_counts.columns = ["VLAN ID", "Count"]
            fig = px.bar(vlan_counts.head(10), x="VLAN ID", y="Count", 
                         title="Configured VLANs", color_discrete_sequence=["#d4a017"])
            fig.update_layout(
                paper_bgcolor="#3e2723", 
                plot_bgcolor="#3e2723", 
                font_color="#ffffff",
                title_font_color="#f5d060"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("ℹ️ No VLANs configured yet.")
    
    with col_chart2:
        st.markdown("### 📊 Firewall Actions")
        if not logs.empty:
            action_counts = logs["action"].value_counts().reset_index()
            action_counts.columns = ["Action", "Count"]
            fig = px.pie(action_counts, values="Count", names="Action", 
                         title="Packet Allow/Block", color_discrete_sequence=["#d4a017", "#b8860b"])
            fig.update_layout(
                paper_bgcolor="#3e2723", 
                plot_bgcolor="#3e2723", 
                font_color="#ffffff",
                title_font_color="#f5d060"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("ℹ️ No packet data available.")

# ============================================================================
# PAGE 2: TOPOLOGY BUILDER
# ============================================================================
elif menu_clean == "Topology Builder":
    st.markdown("# 🏗️ Network Topology Builder")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### ✨ Create New Topology")
        with st.form("create_topology_form"):
            name = st.text_input("Topology Name", placeholder="e.g., Corporate Network")
            switches = st.number_input("Number of Switches", min_value=1, max_value=10, value=2)
            submitted = st.form_submit_button("🚀 Create Topology")
            
            if submitted and name:
                new_id = create_topology(name, st.session_state.user_role, switches)
                st.success(f"✅ Topology '{name}' created! ID: {new_id}")
                st.balloons()
                st.session_state.current_topology = new_id
    
    with col2:
        st.markdown("### 📋 Existing Topologies")
        topologies = get_all_topologies()
        if not topologies.empty:
            selected = st.selectbox("Select Topology", topologies["topology_name"].tolist())
            top_data = topologies[topologies["topology_name"] == selected].iloc[0]
            st.info(f"""
            **Topology Details:**
            - **ID:** {top_data['topology_id']}
            - **Name:** {top_data['topology_name']}
            - **Switches:** {top_data['switch_count']}
            - **VLANs:** {top_data['vlan_count']}
            - **Rules:** {top_data['rule_count']}
            """)
            st.session_state.current_topology = top_data["topology_id"]
        else:
            st.info("ℹ️ No topologies created yet.")

# ============================================================================
# PAGE 3: VLAN CONFIGURATION
# ============================================================================
elif menu_clean == "VLAN Configuration":
    st.markdown("# 🔧 VLAN Configuration (IEEE 802.1Q)")
    st.markdown("---")
    
    topologies = get_all_topologies()
    if topologies.empty:
        st.warning("⚠️ Please create a topology first!")
    else:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### ➕ Create New VLAN")
            with st.form("create_vlan_form"):
                selected_top = st.selectbox("Select Topology", topologies["topology_name"].tolist())
                top_id = topologies[topologies["topology_name"] == selected_top]["topology_id"].iloc[0]
                
                vlan_id = st.number_input("VLAN ID (1-4094)", min_value=1, max_value=4094, value=10)
                vlan_name = st.text_input("VLAN Name", placeholder="e.g., Sales, Engineering, HR")
                subnet = st.text_input("IP Subnet", placeholder="e.g., 192.168.10.0/24")
                gateway = st.text_input("Gateway IP", placeholder="e.g., 192.168.10.1")
                
                submitted = st.form_submit_button("✅ Create VLAN")
                
                if submitted and vlan_name and subnet and gateway:
                    success, msg = create_vlan(vlan_id, vlan_name, top_id, subnet, gateway)
                    if success:
                        st.success(msg)
                        st.balloons()
                    else:
                        st.error(msg)
        
        with col2:
            st.markdown("### 📋 Existing VLANs")
            vlans = get_all_vlans()
            if not vlans.empty:
                st.dataframe(vlans[["vlan_id", "vlan_name", "subnet", "gateway", "is_active"]], use_container_width=True)
            else:
                st.info("ℹ️ No VLANs configured.")

# ============================================================================
# PAGE 4: VLAN MEMBERS
# ============================================================================
elif menu_clean == "VLAN Members":
    st.markdown("# 👥 VLAN Member Management")
    st.markdown("---")
    
    vlans = get_all_vlans()
    if vlans.empty:
        st.warning("⚠️ Please create VLANs first!")
    else:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### ➕ Add Device to VLAN")
            with st.form("add_member_form"):
                selected_vlan = st.selectbox("Select VLAN", vlans["vlan_name"].tolist())
                vlan_id = vlans[vlans["vlan_name"] == selected_vlan]["vlan_id"].iloc[0]
                
                device_name = st.text_input("Device Name", placeholder="e.g., PC-Sales-01")
                mac_address = st.text_input("MAC Address", placeholder="AA:BB:CC:DD:EE:FF")
                ip_address = st.text_input("IP Address", placeholder="192.168.10.50")
                port_number = st.text_input("Switch Port", placeholder="Gi1/0/1")
                
                submitted = st.form_submit_button("➕ Add Device")
                
                if submitted and device_name:
                    add_vlan_member(vlan_id, device_name, mac_address, ip_address, port_number)
                    st.success(f"✅ Device '{device_name}' added to VLAN {selected_vlan}")
        
        with col2:
            st.markdown("### 📋 VLAN Members List")
            selected_vlan_view = st.selectbox("View VLAN", vlans["vlan_name"].tolist(), key="view_vlan")
            vlan_id_view = vlans[vlans["vlan_name"] == selected_vlan_view]["vlan_id"].iloc[0]
            members = get_vlan_members(vlan_id_view)
            
            if not members.empty:
                st.dataframe(members[["device_name", "mac_address", "ip_address", "port_number", "status"]], use_container_width=True)
            else:
                st.info(f"ℹ️ No devices assigned to VLAN {selected_vlan_view}")

# ============================================================================
# PAGE 5: FIREWALL RULES
# ============================================================================
elif menu_clean == "Firewall Rules":
    st.markdown("# 🔥 Firewall Policy Configuration")
    st.markdown("---")
    
    topologies = get_all_topologies()
    if topologies.empty:
        st.warning("⚠️ Please create a topology first!")
    else:
        vlans = get_all_vlans()
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### ➕ Add Firewall Rule")
            with st.form("add_rule_form"):
                selected_top = st.selectbox("Select Topology", topologies["topology_name"].tolist())
                top_id = topologies[topologies["topology_name"] == selected_top]["topology_id"].iloc[0]
                
                top_vlans = vlans[vlans["topology_id"] == top_id]
                vlan_options = top_vlans["vlan_name"].tolist() if not top_vlans.empty else []
                vlan_options.append("ANY")
                
                source_vlan = st.selectbox("Source VLAN", vlan_options)
                dest_vlan = st.selectbox("Destination VLAN", vlan_options)
                protocol = st.selectbox("Protocol", ["TCP", "UDP", "ICMP", "ANY"])
                dest_port = st.number_input("Destination Port", min_value=1, max_value=65535, value=80)
                action = st.selectbox("Action", ["ALLOW", "DENY"])
                priority = st.number_input("Priority (1=highest)", min_value=1, max_value=1000, value=100)
                
                submitted = st.form_submit_button("➕ Add Rule")
                
                if submitted:
                    create_firewall_rule(top_id, source_vlan, dest_vlan, protocol, dest_port, action, priority)
                    st.success(f"✅ Rule added: {action} {source_vlan} → {dest_vlan}")
        
        with col2:
            st.markdown("### 📋 Firewall Rules")
            rules = get_all_firewall_rules()
            if not rules.empty:
                display = rules[["priority", "source_vlan", "destination_vlan", "protocol", "destination_port", "action"]]
                st.dataframe(display.sort_values("priority"), use_container_width=True)
            else:
                st.info("ℹ️ No firewall rules configured.")

# ============================================================================
# PAGE 6: RULE SEQUENCE
# ============================================================================
elif menu_clean == "Rule Sequence":
    st.markdown("# 📋 Firewall Rule Sequence")
    st.markdown("---")
    
    sequences = get_rule_sequence()
    rules = get_all_firewall_rules()
    
    if sequences.empty:
        st.info("ℹ️ No rule sequences configured. Add firewall rules first!")
    else:
        merged = pd.merge(sequences, rules, left_on="rule_id", right_on="rule_id", how="left")
        merged = merged[["priority_order", "source_vlan", "destination_vlan", "protocol", "destination_port", "action", "description"]]
        merged = merged.sort_values("priority_order")
        
        st.markdown("### 📊 Rule Processing Order (Higher Priority First)")
        st.dataframe(merged, use_container_width=True)
        
        # Visual representation
        st.markdown("### 🎯 Rule Sequence Visualization")
        for idx, row in merged.iterrows():
            color = "#10b981" if row["action"] == "ALLOW" else "#ef4444"
            st.markdown(f"""
            <div style="background: #4a2c1a; border-radius: 10px; padding: 10px; margin: 8px 0; border-left: 4px solid {color};">
                <span style="color: #f5d060; font-weight: bold;">Priority {row['priority_order']}</span>
                <span style="color: #ffffff; margin-left: 15px;">{row['source_vlan']} → {row['destination_vlan']}</span>
                <span style="color: #e8d5a5; margin-left: 15px;">{row['protocol']}:{row['destination_port']}</span>
                <span style="color: {color}; margin-left: 15px; font-weight: bold;">{row['action']}</span>
            </div>
            """, unsafe_allow_html=True)

# ============================================================================
# PAGE 7: PACKET SIMULATION
# ============================================================================
elif menu_clean == "Packet Simulation":
    st.markdown("# 📡 Packet Flow Simulation")
    st.markdown("---")
    
    topologies = get_all_topologies()
    vlans = get_all_vlans()
    
    if topologies.empty or vlans.empty:
        st.warning("⚠️ Please create a topology and configure VLANs first!")
    else:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 🎮 Simulation Controls")
            selected_top = st.selectbox("Select Topology", topologies["topology_name"].tolist())
            top_id = topologies[topologies["topology_name"] == selected_top]["topology_id"].iloc[0]
            
            top_vlans = vlans[vlans["topology_id"] == top_id]
            vlan_options = top_vlans["vlan_name"].tolist()
            
            if len(vlan_options) >= 2:
                source_vlan = st.selectbox("Source VLAN", vlan_options)
                dest_vlan = st.selectbox("Destination VLAN", [v for v in vlan_options if v != source_vlan])
                protocol = st.selectbox("Protocol", ["TCP", "UDP", "ICMP"])
                dest_port = st.number_input("Destination Port", min_value=1, max_value=65535, value=80)
                packet_size = st.slider("Packet Size (bytes)", 64, 1500, 512)
                
                if st.button("🚀 Send Packet", use_container_width=True):
                    st.session_state.simulation_active = True
                    
                    with st.spinner("🔐 Simulating packet flow..."):
                        time.sleep(0.5)
                        
                        source_data = top_vlans[top_vlans["vlan_name"] == source_vlan].iloc[0]
                        dest_data = top_vlans[top_vlans["vlan_name"] == dest_vlan].iloc[0]
                        
                        rules = get_rules_by_topology(top_id)
                        action, rule_id = NetworkSimulationEngine.simulate_packet(
                            source_vlan, dest_vlan, protocol, dest_port, rules
                        )
                        
                        log_packet(st.session_state.session_id, source_vlan, dest_vlan, packet_size,
                                  f"VID: {source_data['vlan_id']}",
                                  "ALLOWED" if action == "ALLOW" else "BLOCKED", protocol, dest_port)
                        
                        if action == "ALLOW":
                            st.success(f"✅ Packet ALLOWED: {source_vlan} → {dest_vlan}")
                            
                            st.markdown("### 🏷️ 802.1Q VLAN Tagging")
                            tagging = NetworkSimulationEngine.add_vlan_tag(1, source_data["vlan_id"])
                            st.code(f"""
Packet ID: {tagging['packet_id']}
Original: {tagging['original_frame']}
Tag Added: {tagging['vlan_tag']}
Priority: {tagging['priority_code_point']}
Result: {tagging['tagged_frame']}
                            """)
                            
                            if source_vlan != dest_vlan:
                                st.markdown("### 🔄 Inter-VLAN Routing (Router-on-a-Stick)")
                                steps = NetworkSimulationEngine.simulate_inter_vlan_routing(source_data, dest_data)
                                for step in steps:
                                    st.info(step)
                            
                            st.balloons()
                        else:
                            st.error(f"❌ Packet BLOCKED: {source_vlan} → {dest_vlan}")
                            st.markdown("**Reason:** No matching ALLOW rule found (implicit deny)")
            else:
                st.warning("⚠️ Need at least 2 VLANs in this topology to simulate traffic")
        
        with col2:
            st.markdown("### 📋 Active Firewall Rules")
            top_rules = get_rules_by_topology(top_id)
            if not top_rules.empty:
                st.dataframe(top_rules[["priority", "source_vlan", "destination_vlan", "protocol", "destination_port", "action"]]
                            .sort_values("priority"), use_container_width=True)
            else:
                st.info("ℹ️ No firewall rules for this topology.")

# ============================================================================
# PAGE 8: POLICY COMPARISON
# ============================================================================
elif menu_clean == "Policy Comparison":
    st.markdown("# 📊 Firewall Policy Comparison")
    st.markdown("---")
    
    rules = get_all_firewall_rules()
    
    if rules.empty:
        st.info("ℹ️ No firewall rules to compare.")
    else:
        col1, col2 = st.columns(2)
        
        with col1:
            action_counts = rules["action"].value_counts().reset_index()
            action_counts.columns = ["Action", "Count"]
            fig = px.pie(action_counts, values="Count", names="Action", title="Allow vs Deny",
                         color_discrete_sequence=["#d4a017", "#b8860b"])
            fig.update_layout(paper_bgcolor="#3e2723", plot_bgcolor="#3e2723", font_color="#ffffff", title_font_color="#f5d060")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            proto_counts = rules["protocol"].value_counts().reset_index()
            proto_counts.columns = ["Protocol", "Count"]
            fig = px.bar(proto_counts, x="Protocol", y="Count", title="Rules by Protocol",
                         color="Count", color_continuous_scale="Oranges")
            fig.update_layout(paper_bgcolor="#3e2723", plot_bgcolor="#3e2723", font_color="#ffffff", title_font_color="#f5d060")
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        st.markdown("### 📋 Complete Rule Set (Priority Order)")
        st.dataframe(rules[["priority", "source_vlan", "destination_vlan", "protocol", "destination_port", "action"]]
                    .sort_values("priority"), use_container_width=True)

# ============================================================================
# PAGE 9: PACKET LOGS
# ============================================================================
elif menu_clean == "Packet Logs":
    st.markdown("# 📜 Packet Audit Logs")
    st.markdown("---")
    
    logs = get_all_packet_logs()
    
    if not logs.empty:
        st.dataframe(logs, use_container_width=True)
        
        csv = logs.to_csv(index=False)
        st.download_button("💾 Download Logs as CSV", csv, "packet_logs.csv", "text/csv")
    else:
        st.info("ℹ️ No packet logs yet. Run a packet simulation to see logs here.")

# ============================================================================
# PAGE 10: TROUBLESHOOTING
# ============================================================================
elif menu_clean == "Troubleshooting":
    st.markdown("# 🔍 Network Troubleshooting Scenarios")
    st.markdown("---")
    
    scenarios = get_all_scenarios()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        selected = st.selectbox("Select Scenario", scenarios["name"].tolist())
        scenario = scenarios[scenarios["name"] == selected].iloc[0]
        
        st.markdown(f"**📊 Difficulty:** {scenario['difficulty']}")
        st.markdown(f"**📝 Description:** {scenario['description']}")
        
        solution = st.text_area("Your Solution", height=150, placeholder="Describe how you would troubleshoot and resolve this issue...")
        
        if st.button("🔍 Check Solution", use_container_width=True):
            if solution.lower().find(scenario["solution_hint"].lower()) != -1:
                st.success("✅ Correct approach! You've identified the right solution.")
                st.balloons()
            else:
                st.warning(f"💡 Hint: {scenario['solution_hint']}")
    
    with col2:
        st.markdown("### 🔧 Common VLAN Issues")
        
        with st.expander("❌ VLAN Mismatch"):
            st.markdown("**Symptoms:** Devices on same VLAN cannot communicate")
            st.markdown("**Fix:** Verify port assignments and VLAN existence across all switches")
        
        with st.expander("❌ Trunking Failure"):
            st.markdown("**Symptoms:** Inter-switch VLAN connectivity fails")
            st.markdown("**Fix:** Check trunk configuration and allowed VLAN lists")
        
        with st.expander("❌ Inter-VLAN Routing"):
            st.markdown("**Symptoms:** Cannot communicate between different VLANs")
            st.markdown("**Fix:** Verify router sub-interfaces and default gateway configurations")
        
        with st.expander("❌ Firewall Blocking"):
            st.markdown("**Symptoms:** Legitimate traffic is being blocked")
            st.markdown("**Fix:** Check rule ordering and create explicit ALLOW rules")

# ============================================================================
# PAGE 11: ASSESSMENTS
# ============================================================================
elif menu_clean == "Assessments":
    st.markdown("# 📝 Knowledge Assessment Quiz")
    st.markdown("---")
    
    questions = [
        {"q": "Maximum number of VLANs supported by IEEE 802.1Q standard?", "opt": ["256", "512", "1024", "4094"], "ans": "4094", 
         "exp": "IEEE 802.1Q supports up to 4094 VLAN IDs (1-4094)."},
        {"q": "Which network device is required for inter-VLAN routing?", "opt": ["Layer 2 Switch", "Hub", "Router/Layer 3 Switch", "Bridge"], "ans": "Router/Layer 3 Switch", 
         "exp": "A router or Layer 3 switch is required to route traffic between different VLANs."},
        {"q": "What is the default action of a firewall when no rule matches a packet?", "opt": ["ALLOW", "FORWARD", "LOG", "DENY"], "ans": "DENY", 
         "exp": "Firewalls use an implicit deny rule at the end of the policy - deny all traffic not explicitly allowed."},
        {"q": "Which protocol is used for VLAN tagging on Ethernet frames?", "opt": ["IEEE 802.3", "IEEE 802.11", "IEEE 802.1Q", "IEEE 802.1X"], "ans": "IEEE 802.1Q", 
         "exp": "IEEE 802.1Q is the standard that defines VLAN tagging for Ethernet frames."},
        {"q": "What type of switch port carries traffic for multiple VLANs?", "opt": ["Access Port", "Trunk Port", "Console Port", "PoE Port"], "ans": "Trunk Port", 
         "exp": "Trunk ports carry traffic for multiple VLANs between switches."},
        {"q": "What does ACL stand for in network security?", "opt": ["Access Control List", "Advanced Circuit Link", "Automatic Configuration Layer", "Address Connection List"], "ans": "Access Control List", 
         "exp": "ACL stands for Access Control List, used to filter network traffic."},
        {"q": "Which firewall rule placement is considered a security best practice?", "opt": ["Most specific rules last", "Most specific rules first", "Random order", "Alphabetical order"], "ans": "Most specific rules first", 
         "exp": "Place specific rules before general rules to ensure proper traffic handling."}
    ]
    
    if "quiz_score" not in st.session_state:
        st.session_state.quiz_score = 0
    if "quiz_answered" not in st.session_state:
        st.session_state.quiz_answered = {}
    
    for i, q in enumerate(questions):
        st.markdown(f"**Q{i+1}: {q['q']}**")
        answer = st.radio("Select your answer:", q["opt"], key=f"q{i}", index=None, label_visibility="collapsed")
        
        if answer:
            if answer == q["ans"]:
                if f"q{i}" not in st.session_state.quiz_answered:
                    st.session_state.quiz_score += 1
                    st.session_state.quiz_answered[f"q{i}"] = True
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Incorrect. {q['exp']}")
        st.markdown("---")
    
    if st.button("📊 Submit Assessment", use_container_width=True):
        final = (st.session_state.quiz_score / len(questions)) * 100
        st.markdown(f"### 🎯 Your Score: {final:.1f}% ({st.session_state.quiz_score}/{len(questions)})")
        
        save_assessment(st.session_state.user_id, 1, final)
        
        if final >= 80:
            st.success("🎉 Excellent! You have strong network security knowledge!")
            st.balloons()
        elif final >= 60:
            st.warning("📚 Good effort! Review the materials to improve your score.")
        else:
            st.error("📖 Please review the VLAN and firewall concepts and try again.")

# ============================================================================
# PAGE 12: DATABASE TABLES
# ============================================================================
elif menu_clean == "Database Tables":
    st.markdown("# 🗄️ Database Tables Viewer")
    st.markdown("---")
    
    tables = {
        "👤 USERS": "users.csv",
        "🌐 TOPOLOGIES": "topologies.csv",
        "🔧 VLANS": "vlans.csv",
        "👥 VLAN MEMBERS": "vlan_members.csv",
        "🔥 FIREWALL RULES": "firewall_rules.csv",
        "📋 RULE SEQUENCE": "rule_sequence.csv",
        "📦 PACKET LOGS": "packet_logs.csv",
        "📚 SCENARIOS": "scenarios.csv",
        "📝 ASSESSMENTS": "assessments.csv"
    }
    
    selected_table = st.selectbox("Select Table to View", list(tables.keys()))
    
    if selected_table:
        df = pd.read_csv(os.path.join(DATA_DIR, tables[selected_table]))
        st.dataframe(df, use_container_width=True)
        st.caption(f"📊 Total records: {len(df)}")

# ============================================================================
# PAGE 13: SYSTEM INFO
# ============================================================================
elif menu_clean == "System Info":
    st.markdown("# ℹ️ System Information")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🔒 Design and Implementation of a Secure LAN
        
        **Using VLANs and Firewalls | IEEE 802.1Q Compliant**
        
        This system provides an interactive simulation environment for learning network security concepts:
        
        - **VLAN Configuration (IEEE 802.1Q)** - Create and manage Virtual Local Area Networks
        - **Firewall Policy Management** - Implement security rules with priority-based processing
        - **Inter-VLAN Routing** - Router-on-a-stick simulation for routing between VLANs
        - **Packet Flow Analysis** - Real-time traffic visualization with 802.1Q tagging
        
        ### 🗄️ Database Schema
        
        | Table | Purpose |
        |-------|---------|
        | USERS | User accounts and authentication |
        | TOPOLOGIES | Network topology configurations |
        | VLANS | IEEE 802.1Q VLAN configurations |
        | VLAN MEMBERS | Devices assigned to VLANs |
        | FIREWALL RULES | Security policy rules |
        | RULE SEQUENCE | Rule priority ordering |
        | PACKET LOGS | Simulation audit trail |
        | SCENARIOS | Training scenarios |
        | ASSESSMENTS | Quiz results |
        """)
    
    with col2:
        st.markdown("""
        ### 📊 System Statistics
        
        | Metric | Value |
        |--------|-------|
        | Version | 3.0 Enterprise |
        | Database Tables | 9 |
        | Max VLANs | 4094 |
        | Supported Protocols | TCP, UDP, ICMP |
        | System Status | 🟢 Active |
        
        ### 🔐 Standards Compliance
        
        - IEEE 802.1Q VLAN Tagging
        - Enterprise Firewall Best Practices
        - Implicit Deny Security Model
        - Least Privilege Principle
        
        ### 📁 Database Files
        
        All data stored in CSV format in the `secure_lan_data/` folder.
        """)
    
    st.markdown("---")
    st.markdown("""
    <div class="footer">
        <p><strong>Design and Implementation of a Secure LAN using VLANs and Firewalls</strong></p>
        <p>IEEE 802.1Q Compliant | Complete Database Integration | Enterprise-Grade Training Platform</p>
        <p>© 2024 Network Security Training System | All Rights Reserved</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# AUTO-REFRESH
# ============================================================================
if st.session_state.simulation_active:
    time.sleep(0.5)
    st.session_state.simulation_active = False
    st.rerun()