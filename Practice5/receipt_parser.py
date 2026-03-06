import re
import json
with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()
pp = re.findall(
    r"\d+\.\s*\n(.+?)\n([\d,]+)\s*x\s*([\d\s,]+)\n([\d\s,]+)",
    text
)
products = []
for name, qty, price, total in pp:
    products.append({
        "name": name.strip(),
        "quantity": float(qty.replace(",", ".")),
        "unit_price": float(price.replace(" ", "").replace(",", ".")),
        "total_price": float(total.replace(" ", "").replace(",", "."))
    })
totalm = re.search(r"ИТОГО:\s*\n?([\d\s,]+)", text)
totala = None
if totalm:
    totala = float(totalm.group(1).replace(" ", "").replace(",", "."))
pmatch = re.search(r"(Банковская карта|Наличные)", text)
pmethod = pmatch.group(1) if pmatch else "Unknown"
dtmatch = re.search(r"(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})", text)
date, time = (dtmatch.groups() if dtmatch else (None, None))
data = {
    "date": date,
    "time": time,
    "pmethod": pmethod,
    "totala": totala,
    "products": products
}
print(json.dumps(data, indent=4, ensure_ascii=False))