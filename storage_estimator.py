storage_mb = float(input("Enter storage in MB: "))
storage_kb = storage_mb * 1024
storage_gb = storage_mb / 1024
print(f"Storage in KB: {storage_kb:.2f}")
print(f"Storage in GB: {storage_gb:.2f}")
