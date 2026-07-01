cloudshield_ips = {"10.0.0.1", "192.168.1.5", "172.16.0.9"}
autopilot_ips = {"192.168.1.5", "10.0.0.99", "172.16.0.9"}

common_ips = cloudshield_ips & autopilot_ips
all_ips = cloudshield_ips | autopilot_ips
only_cloudshield = cloudshield_ips - autopilot_ips

print("Common IPs:", common_ips)
print("All IPs:", all_ips)
print("Only in CloudShield:", only_cloudshield)

raw_events = ["login", "login", "logout", "error", "error", "error"]
unique_events = set(raw_events)
print("Unique events:", unique_events)

frozen = frozenset(unique_events)
print("Frozen:", frozen)

def find_unique(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums = [4, 1, 2, 1, 2]
print("Unique element:", find_unique(nums))