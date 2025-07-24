CREATE TABLE IF NOT EXISTS users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL UNIQUE,
  password_hash TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS mental_health_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    user_input TEXT,
    llm_response TEXT,
    emotion TEXT,
    timestamp TEXT
);


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
);
