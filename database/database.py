import sqlite3
from datetime import datetime
import os

def init_db(db_path="db/wellness.db"):
  # Ensure the parent directory exists
  os.makedirs(os.path.dirname(db_path), exist_ok=True)

  conn = sqlite3.connect(db_path)
  c = conn.cursor()

  # Create user_profile table
  c.execute("""
    CREATE TABLE IF NOT EXISTS user_profile (
      user_id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      age INTEGER,
      gender TEXT,
      height_cm REAL,
      weight_kg REAL,
      fitness_goal TEXT,
      activity_level TEXT,
      dietary_preferences TEXT,
      mental_health_background TEXT,
      daily_schedule TEXT,
      medical_conditions TEXT
    )
  """)

  # Create mental_health_logs table
  c.execute("""
    CREATE TABLE IF NOT EXISTS mental_health_logs (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INTEGER,
      user_input TEXT,
      llm_response TEXT,
      emotion TEXT,
      timestamp TEXT
    )
  """)

  conn.commit()
  conn.close()

def save_memory_entry(user_id, user_input, llm_response, emotion=None, db_path="db/wellness.db"):
  conn = sqlite3.connect(db_path)
  c = conn.cursor()
  c.execute("""
    INSERT INTO mental_health_logs (user_id, user_input, llm_response, emotion, timestamp)
    VALUES (?, ?, ?, ?, ?)
  """, (user_id, user_input, llm_response, emotion, datetime.now()))
  conn.commit()
  conn.close()

def save_user_profile(profile, db_path="db/wellness.db"):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""
        INSERT INTO user_profile (
            name, age, gender, height_cm, weight_kg,
            fitness_goal, activity_level, dietary_preferences,
            mental_health_background, daily_schedule, medical_conditions
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        profile["name"], profile["age"], profile["gender"],
        profile["height"], profile["weight"], profile["fitness_goal"],
        profile["activity_level"], profile["dietary_preferences"],
        profile["mental_health_background"], profile["daily_schedule"],
        profile["medical_conditions"]
    ))
    conn.commit()
    user_id = c.lastrowid
    conn.close()
    return user_id

def get_user_profile(user_id, db_path="db/wellness.db"):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM user_profile WHERE user_id = ?", (user_id,))
    row = c.fetchone()
    conn.close()
    return row
