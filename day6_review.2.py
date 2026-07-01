cloudshield = {"10.0.0.1", "192.168.1.5", "172.16.0.9", "8.8.8.8"}
autopilot = {"192.168.1.5", "10.0.0.99"}
whitelist = {"8.8.8.8"}

result = (cloudshield - autopilot) - whitelist
print(result)

def has_duplicates(lst):
    return len(lst) != len(set(lst))

print(has_duplicates([1, 2, 3, 4]))      
print(has_duplicates([1, 2, 3, 2]))      