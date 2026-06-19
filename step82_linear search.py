def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return None

server_ports = [22, 80, 443, 8080, 3306]
print(linear_search(server_ports, 443))
print(linear_search(server_ports, 9999))