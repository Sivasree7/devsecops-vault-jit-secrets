# Test pipeline trigger
import os
import sys
secret =os.getenv("DB_PASSWORD")
if not secret:
    print("secret not found")
    sys.exit(1)
print("secret received securely")
print("App executed successfully")
