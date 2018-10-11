from datetime import datetime
import uuid

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(now)
print(len('05d209b5-ee28-4b39-8907-9aa25d098fcd'))
print(uuid.uuid4())
print(uuid.uuid1())