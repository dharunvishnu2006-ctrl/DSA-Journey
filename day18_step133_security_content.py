from collections import defaultdict, deque
import heapq

class NetworkGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def shortest_path(self, start, target):
        visited = {start}
        queue = deque([(start, [start])])

        while queue:
            node, path = queue.popleft()

            if node == target:
                return path

            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, path + [neighbour]))
        return None

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class DomainTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, domain):
        node = self.root

        for ch in domain:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_end = True

    def is_malicious(self, domain):
        node = self.root

        for ch in domain:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

class IOCBlacklist:
    def __init__(self):
        self.blacklist = set()

    def add_ioc(self, ip):
        self.blacklist.add(ip)

    def is_blacklisted(self, ip):
        return ip in self.blacklist

class ThreatPriorityQueue:
    def __init__(self):
        self.heap = []

    def add_threat(self, severity, description):
        heapq.heappush(self.heap, (-severity, description))

    def get_top_threat(self):
        if self.heap:
            severity, description = heapq.heappop(self.heap)
            return (-severity, description)
        return None

print("----- Task 1: NetworkGraph -----")

graph = NetworkGraph()
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("A", "D")
graph.add_edge("D", "C")

print("Shortest path from A to C:")
print(graph.shortest_path("A", "C"))
print("\n----- Task 2: DomainTrie -----")

trie = DomainTrie()
trie.insert("malicious.com")
trie.insert("bad.net")

print("malicious.com:", trie.is_malicious("malicious.com"))
print("safe.com:", trie.is_malicious("safe.com"))
print("\n----- Task 3: IOCBlacklist -----")

blacklist = IOCBlacklist()
blacklist.add_ioc("192.168.1.1")

print("192.168.1.1:", blacklist.is_blacklisted("192.168.1.1"))
print("10.0.0.1:", blacklist.is_blacklisted("10.0.0.1"))
print("\n----- Task 4: ThreatPriorityQueue -----")

pq = ThreatPriorityQueue()
pq.add_threat(5, "Critical Ransomware")
pq.add_threat(2, "Spam Email")
pq.add_threat(4, "SQL Injection")

print("Highest Priority Threat:")
print(pq.get_top_threat())
print("Next Highest Threat:")
print(pq.get_top_threat())

class MiniThreatAnalyzer:
    def __init__(self):
        self.network = NetworkGraph()
        self.domain_trie = DomainTrie()
        self.ioc_blacklist = IOCBlacklist()
        self.threat_queue = ThreatPriorityQueue()

    def add_connection(self, host_a, host_b):
        self.network.add_edge(host_a, host_b)

    def register_malicious_domain(self, domain):
        self.domain_trie.insert(domain)

    def register_ioc(self, ip):
        self.ioc_blacklist.add_ioc(ip)

    def report_threat(self, severity, description):
        self.threat_queue.add_threat(severity, description)

    def analyze(self, entry_host, target_host, domain_to_check, ip_to_check):
        report = {}
        report['attack_path'] = self.network.shortest_path(entry_host, target_host)
        report['domain_flagged'] = self.domain_trie.is_malicious(domain_to_check)
        report['ip_flagged'] = self.ioc_blacklist.is_blacklisted(ip_to_check)
        report['top_threat'] = self.threat_queue.get_top_threat()
        return report

analyzer = MiniThreatAnalyzer()

analyzer.add_connection("Gateway", "Server1")
analyzer.add_connection("Server1", "Database")
analyzer.register_malicious_domain("evil-hacker.com")
analyzer.register_ioc("45.33.12.99")
analyzer.report_threat(9, "Active Data Exfiltration")
analyzer.report_threat(3, "Failed Login Attempt")

report = analyzer.analyze("Gateway", "Database", "evil-hacker.com", "45.33.12.99")
print(report)    