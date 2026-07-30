# app.py (Part 1: Foundation)

import streamlit as st
import pandas as pd
import sqlite3
import datetime
import logging
import os

# --- Logging Setup ---
LOG_FILE = "app.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# --- Database Setup ---
DB_FILE = "projects.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Table for indices
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS indices (
        material TEXT,
        date TEXT,
        value REAL
    )
    """)
    # Table for project history
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        created_at TEXT,
        annex_factor REAL
    )
    """)
    conn.commit()
    conn.close()

def save_index(material, value):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    today = datetime.date.today().isoformat()
    cursor.execute("INSERT INTO indices VALUES (?, ?, ?)", (material, today, value))
    conn.commit()
    conn.close()
    logging.info(f"Saved index for {material}: {value}")

def get_latest_index(material):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM indices WHERE material=? ORDER BY date DESC LIMIT 1", (material,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# --- Settings Page ---
def settings_page():
    st.title("⚙️ Settings")
    st.write("Configure your AI Price Adjustment System")

    # Dark mode toggle
    dark_mode = st.checkbox("Enable Dark Mode")
    if dark_mode:
        st.markdown(
            """
            <style>
            body { background-color: #121212; color: #e0e0e0; }
            </style>
            """,
            unsafe_allow_html=True,
        )

    # Threshold for alerts
    threshold = st.number_input("Escalation Alert Threshold (Pn)", value=1.10)
    st.write(f"Current threshold: {threshold}")

    # Email settings (placeholder)
    email = st.text_input("Notification Email", value="your_email@example.com")
    st.write(f"Alerts will be sent to: {email}")

    st.success("Settings saved (session only).")

# app.py (Part 1: Foundation)

import streamlit as st
import pandas as pd
import sqlite3
import datetime
import logging
import os

# --- Logging Setup ---
LOG_FILE = "app.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# --- Database Setup ---
DB_FILE = "projects.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Table for indices
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS indices (
        material TEXT,
        date TEXT,
        value REAL
    )
    """)
    # Table for project history
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        created_at TEXT,
        annex_factor REAL
    )
    """)
    conn.commit()
    conn.close()

def save_index(material, value):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    today = datetime.date.today().isoformat()
    cursor.execute("INSERT INTO indices VALUES (?, ?, ?)", (material, today, value))
    conn.commit()
    conn.close()
    logging.info(f"Saved index for {material}: {value}")

def get_latest_index(material):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM indices WHERE material=? ORDER BY date DESC LIMIT 1", (material,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# --- Settings Page ---
def settings_page():
    st.title("⚙️ Settings")
    st.write("Configure your AI Price Adjustment System")

    # Dark mode toggle
    dark_mode = st.checkbox("Enable Dark Mode")
    if dark_mode:
        st.markdown(
            """
            <style>
            body { background-color: #121212; color: #e0e0e0; }
            </style>
            """,
            unsafe_allow_html=True,
        )

    # Threshold for alerts
    threshold = st.number_input("Escalation Alert Threshold (Pn)", value=1.10)
    st.write(f"Current threshold: {threshold}")

    # Email settings (placeholder)
    email = st.text_input("Notification Email", value="your_email@example.com")
    st.write(f"Alerts will be sent to: {email}")

    st.success("Settings saved (session only).")

# app.py (Part 1: Foundation)

import streamlit as st
import pandas as pd
import sqlite3
import datetime
import logging
import os

# --- Logging Setup ---
LOG_FILE = "app.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# --- Database Setup ---
DB_FILE = "projects.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Table for indices
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS indices (
        material TEXT,
        date TEXT,
        value REAL
    )
    """)
    # Table for project history
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        created_at TEXT,
        annex_factor REAL
    )
    """)
    conn.commit()
    conn.close()

def save_index(material, value):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    today = datetime.date.today().isoformat()
    cursor.execute("INSERT INTO indices VALUES (?, ?, ?)", (material, today, value))
    conn.commit()
    conn.close()
    logging.info(f"Saved index for {material}: {value}")

def get_latest_index(material):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM indices WHERE material=? ORDER BY date DESC LIMIT 1", (material,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# --- Settings Page ---
def settings_page():
    st.title("⚙️ Settings")
    st.write("Configure your AI Price Adjustment System")

    # Dark mode toggle
    dark_mode = st.checkbox("Enable Dark Mode")
    if dark_mode:
        st.markdown(
            """
            <style>
            body { background-color: #121212; color: #e0e0e0; }
            </style>
            """,
            unsafe_allow_html=True,
        )

    # Threshold for alerts
    threshold = st.number_input("Escalation Alert Threshold (Pn)", value=1.10)
    st.write(f"Current threshold: {threshold}")

    # Email settings (placeholder)
    email = st.text_input("Notification Email", value="your_email@example.com")
    st.write(f"Alerts will be sent to: {email}")

    st.success("Settings saved (session only).")

# app.py (Part 1: Foundation)

import streamlit as st
import pandas as pd
import sqlite3
import datetime
import logging
import os

# --- Logging Setup ---
LOG_FILE = "app.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# --- Database Setup ---
DB_FILE = "projects.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Table for indices
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS indices (
        material TEXT,
        date TEXT,
        value REAL
    )
    """)
    # Table for project history
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        created_at TEXT,
        annex_factor REAL
    )
    """)
    conn.commit()
    conn.close()

def save_index(material, value):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    today = datetime.date.today().isoformat()
    cursor.execute("INSERT INTO indices VALUES (?, ?, ?)", (material, today, value))
    conn.commit()
    conn.close()
    logging.info(f"Saved index for {material}: {value}")

def get_latest_index(material):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM indices WHERE material=? ORDER BY date DESC LIMIT 1", (material,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# --- Settings Page ---
def settings_page():
    st.title("⚙️ Settings")
    st.write("Configure your AI Price Adjustment System")

    # Dark mode toggle
    dark_mode = st.checkbox("Enable Dark Mode")
    if dark_mode:
        st.markdown(
            """
            <style>
            body { background-color: #121212; color: #e0e0e0; }
            </style>
            """,
            unsafe_allow_html=True,
        )

    # Threshold for alerts
    threshold = st.number_input("Escalation Alert Threshold (Pn)", value=1.10)
    st.write(f"Current threshold: {threshold}")

    # Email settings (placeholder)
    email = st.text_input("Notification Email", value="your_email@example.com")
    st.write(f"Alerts will be sent to: {email}")

    st.success("Settings saved (session only).")
