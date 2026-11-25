#basic network sniffer: prints src/dst IP, protocol, ports, payload (run as admin/sudo)
from scapy.all import sniff, IP, TCP, UDP, Raw

def show(p):
    if IP in p:
        l4 = p[TCP] if TCP in p else p[UDP] if UDP in p else None
        print(p[IP].src, "->", p[IP].dst, "| proto", p[IP].proto, "| ports", (l4.sport, l4.dport) if l4 else "-", "| payload", bytes(p[Raw].load)[:50] if Raw in p else "-")

sniff(prn=show, count=20, store=False)
