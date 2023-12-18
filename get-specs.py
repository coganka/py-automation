import psutil

print(psutil.cpu_count())
print(psutil.cpu_percent(interval=1))
print(psutil.cpu_stats())
print(psutil.cpu_freq())

print(psutil.virtual_memory())

print(psutil.disk_usage('/'))