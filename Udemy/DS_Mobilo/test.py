from datetime import  datetime

birthday = datetime(1984, 5, 18, 0, 0, 0)
diff = datetime.today() - birthday

print(diff)