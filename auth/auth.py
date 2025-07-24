import sqlite3
import bcrypt

DB_PATH = "db/wellness.db"

def hash_password(password):
  return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def check_password(password, hashed):
  return bcrypt.checkpw(password.encode(), hashed.encode())

def register_user(username, email, password):
  conn = sqlite3.connect(DB_PATH)
  c = conn.cursor()
  try:
    c.execute("""
      INSERT INTO users (username, email, password_hash)
      VALUES (?, ?, ?)
    """, (username, email, hash_password(password)))
    conn.commit()
    return True, "Registration successful!"
  except sqlite3.IntegrityError:
    return False, "Username or email already exists."
  finally:
    conn.close()

def authenticate_user(username, password):
  conn = sqlite3.connect(DB_PATH)
  c = conn.cursor()
  c.execute("SELECT user_id, password_hash FROM users WHERE username = ?", (username,))
  user = c.fetchone()
  conn.close()
  if user and check_password(password, user[1]):
    return True, user[0]
  return False, None
