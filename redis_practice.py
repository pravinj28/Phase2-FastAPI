from upstash_redis import Redis
import json
import time

#BASIC SET AND GET 
r = Redis(url="https://live-treefrog-179617.upstash.io", token="gQAAAAAAAr2hAAIgcDE1YWM2ODI4ZDE4OTM0MDVmOWE2Njk0ODBjYzdiOWMxYw",)


r.set("name", "Pravin") #this sets the value
print(r.get("name")) #this gives the value back 

#SET with expiry- expires after 60 seconds

r.set("temp_key", "I will disappear", ex=60)
print(r.get("temp_key")) #i will disappear
print(r.ttl("temp_key")) #shows seconds remaining

#Caching JSON responses (most important for AI):

def get_user_data(username):
    cache_key = f"github_user:{username}" # This Check cache first
    cached = r.get(cache_key)

    if cached:
        print(f"Cache HIT for {username}")
        return json.loads(cached)
    
    # Simulate expensive API call (pretend this is calling GitHub API)
    print(f"Cache MISS for {username} - calling API...")
    time.sleep(2)  # simulate 2 second API call

    user_data = {
        "username": username,
        "repos": 25,
        "followers": 100,
        "language": "Python"
    }

    r.set(cache_key, json.dumps(user_data), ex=300)

    return user_data

print(get_user_data("pravinj28")) # First call — cache miss, takes 2 seconds


print(get_user_data("pravinj28")) # Second call — cache hit, instant


#Hashes (storing structured data):

r.hset("session:user123", "user_id", "123")
r.hset("session:user123", "model", "claude-sonnet")
r.hset("session:user123", "tokens_used", "1500")
r.hset("session:user123", "last_active", "2026-07-21")

# Get all session data

session = r.hgetall("session:user123")
print("Complete Session:")
print(session)

# Get one field

print("\nModel:")
print(r.hget("session:user123", "model"))

# Update one field

r.hset("session:user123", "tokens_used", "2000")

print("\nUpdated Tokens Used:")
print(r.hget("session:user123", "tokens_used"))

# Set expiry (1 hour)

r.expire("session:user123", 3600)

print("\nExpiry set for 1 hour.")

# Add tasks to a queue
r.rpush("task_queue", "summarise document 1")
r.rpush("task_queue", "summarise document 2")
r.rpush("task_queue", "summarise document 3")

# Check queue length
print(r.llen("task_queue"))  # 3

# Process tasks one by one
while r.llen("task_queue") > 0:
    task = r.lpop("task_queue")
    print(f"Processing: {task}")

print(r.llen("task_queue"))  # 0

# Track which users have used the AI today
r.sadd("active_users:2026-07-21", "user123")
r.sadd("active_users:2026-07-21", "user456")
r.sadd("active_users:2026-07-21", "user123")  # duplicate — ignored

# Count unique users
print(r.scard("active_users:2026-07-21"))  # 2 not 3

# Check if user is active
print(r.sismember("active_users:2026-07-21", "user123"))  # True
print(r.sismember("active_users:2026-07-21", "user999"))  # False

pipe = r.pipeline()
pipe.set("key1", "value1")
pipe.set("key2", "value2")
pipe.get("key1")
pipe.execute()  # all 3 commands sent at once