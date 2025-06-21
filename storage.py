import sqlite3
from datetime import datetime
from typing import List, Dict

DB_FILE = "analises.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            emotion TEXT NOT NULL,
            confidence REAL NOT NULL,
            explanation TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def save_analysis(text: str, emotion: str, confidence: float, explanation: str):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        "INSERT INTO analyses (text, emotion, confidence, explanation, timestamp) VALUES (?, ?, ?, ?, ?)",
        (text, emotion, confidence, explanation, datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()

def get_all_analyses() -> List[Dict]:
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT text, emotion, confidence, explanation, timestamp FROM analyses ORDER BY timestamp DESC")
    rows = c.fetchall()
    conn.close()
    return [
        {
            "text": row[0],
            "emotion": row[1],
            "confidence": row[2],
            "explanation": row[3],
            "timestamp": row[4]
        }
        for row in rows
    ]

def get_emotion_distribution():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT emotion, COUNT(*) FROM analyses GROUP BY emotion")
    rows = c.fetchall()
    conn.close()
    total = sum(row[1] for row in rows)
    if total == 0:
        return {}
    return {row[0]: row[1] / total * 100 for row in rows}
