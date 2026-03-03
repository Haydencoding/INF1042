from datetime import datetime, timedelta
now = datetime.now()
future = now + timedelta(hours=100)
print(future)
