from xml.dom import minidom
import pandas as pd

def text_or_none(nodes):
    if not nodes:
        return None
    texts = [c.data for c in nodes[0].childNodes if c.nodeType == c.TEXT_NODE]
    return "".join(texts).strip() if texts else None

doc = minidom.parse("users.xml")  # <-- twój plik
rows = []
for u in doc.getElementsByTagName("user"):
    rows.append({
        "id": u.getAttribute("id"),
        "name": text_or_none(u.getElementsByTagName("name")),
        "email": text_or_none(u.getElementsByTagName("email")),
        "city": text_or_none(u.getElementsByTagName("city")),
        "role": text_or_none(u.getElementsByTagName("role")),
        "age": int(text_or_none(u.getElementsByTagName("age")) or 0) or None,
    })
df = pd.DataFrame(rows)
print(df.head())
