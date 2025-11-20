# -*- coding: utf-8 -*-
"""
XML users demo with xml.dom.minidom:
- create users.xml
- parse with minidom
- validate & analyze with pandas
- save CSVs and plot a simple chart
"""

from xml.dom import minidom
from pathlib import Path
import pandas as pd
import re
import matplotlib.pyplot as plt


# ---------- 1) Create sample XML ----------
def make_sample_xml(path: Path) -> None:
    doc = minidom.Document()
    users_el = doc.createElement("users")
    doc.appendChild(users_el)

    sample_users = [
        ("U001", "Anna Kowalska", "anna.kowalska@example.com", "Warszawa", "admin", 34),
        ("U002", "Jan Nowak", "jan.nowak@example.com", "Kraków", "user", 29),
        ("U003", "Ewa Zielińska", "ewa.zielinska@example.com", "Gdańsk", "manager", 41),
        ("U004", "Piotr Wiśniewski", "piotr.wisniewski@example.com", "Wrocław", "user", 24),
        ("U005", "Marta Lewandowska", "marta.lewandowska@example.com", "Poznań", "user", 31),
        ("U006", "Tomasz Wójcik", "tomasz.wojcik@example.com", "Warszawa", "user", 27),
        ("U007", "Karolina Jankowska", "karolina.jankowska@example.com", "Kraków", "admin", 38),
        ("U008", "Paweł Kamiński", "pawel.kaminski@example.com", "Warszawa", "user", 22),
        ("U009", "Magdalena Woźniak", "magda.wozniak@example.com", "Łódź", "manager", 45),
        ("U010", "Krzysztof Kaczmarek", "krzysztof.kaczmarek@example.com", "Gdynia", "user", 26),
        ("U011", "Agnieszka Piotrowska", "agnieszka.piotrowska@example.com", "Szczecin", "user", 33),
        ("U012", "Michał Grabowski", "michal.grabowski@example.com", "Wrocław", "user", 28),
        ("U013", "Joanna Zając", "joanna.zajac@example.com", "Katowice", "manager", 39),
        ("U014", "Rafał Pawlak", "rafal.pawlak@example.com", "Poznań", "user", 23),
        ("U015", "Dominika Sokołowska", "dominika.sokolowska@example.com", "Warszawa", "user", 36),
        ("U016", "Łukasz Dudek", "lukasz.dudek@example.com", "Kraków", "user", 32),
        ("U017", "Natalia Bąk", "natalia.bak@example.com", "Gdańsk", "user", 21),
        ("U018", "Sebastian Król", "sebastian.krol@example.com", "Warszawa", "manager", 44),
        ("U019", "Aleksandra Baran", "aleksandra.baran@example.com", "Rzeszów", "user", 25),
        ("U020", "Marcin Albiniak", "marcin.albiniak@example.com", "Warszawa", "user", 53),
    ]

    def child(tag: str, text: str) -> minidom.Element:
        el = doc.createElement(tag)
        el.appendChild(doc.createTextNode(text))
        return el

    for uid, name, email, city, role, age in sample_users:
        user_el = doc.createElement("user")
        user_el.setAttribute("id", uid)
        user_el.appendChild(child("name", name))
        user_el.appendChild(child("email", email))
        user_el.appendChild(child("city", city))
        user_el.appendChild(child("role", role))
        user_el.appendChild(child("age", str(age)))
        users_el.appendChild(user_el)

    with open(path, "w", encoding="utf-8") as f:
        f.write(doc.toprettyxml(indent="  ", encoding=None))


# ---------- 2) Parse with minidom ----------
def text_or_none(node_list):
    """Return text content of first element in node_list, or None."""
    if not node_list:
        return None
    node = node_list[0]
    # concatenate all text nodes inside (handles mixed content)
    texts = []
    for child in node.childNodes:
        if child.nodeType == child.TEXT_NODE:
            texts.append(child.data)
    return "".join(texts).strip() if texts else None


def parse_users_minidom(path: Path) -> pd.DataFrame:
    doc = minidom.parse(str(path))
    users = doc.getElementsByTagName("user")

    rows = []
    for u in users:
        uid = u.getAttribute("id")
        name = text_or_none(u.getElementsByTagName("name"))
        email = text_or_none(u.getElementsByTagName("email"))
        city = text_or_none(u.getElementsByTagName("city"))
        role = text_or_none(u.getElementsByTagName("role"))
        age_txt = text_or_none(u.getElementsByTagName("age"))
        try:
            age = int(age_txt) if age_txt is not None else None
        except ValueError:
            age = None

        rows.append(
            {"id": uid, "name": name, "email": email, "city": city, "role": role, "age": age}
        )

    return pd.DataFrame(rows)


# ---------- 3) Validate & analyze ----------
def enrich_and_summarize(df: pd.DataFrame):
    df = df.copy()
    email_re = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    df["email_valid"] = df["email"].apply(lambda x: bool(email_re.match(x)) if isinstance(x, str) else False)
    df["email_is_duplicate"] = df["email"].duplicated(keep=False)

    by_city = df.groupby("city").size().reset_index(name="user_count").sort_values("user_count", ascending=False)
    by_role = (
        df.groupby("role")
          .agg(user_count=("id", "count"), avg_age=("age", "mean"))
          .reset_index()
          .sort_values("user_count", ascending=False)
    )
    return df, by_city, by_role


# ---------- 4) Main ----------
if __name__ == "__main__":
    out_xml = Path("users_minidom.xml")
    out_parsed = Path("users_minidom_parsed.csv")
    out_summary = Path("users_minidom_summary.csv")

    # create example xml
    make_sample_xml(out_xml)

    # parse & analyze
    df = parse_users_minidom(out_xml)
    df_enriched, by_city, by_role = enrich_and_summarize(df)

    # save
    df_enriched.to_csv(out_parsed, index=False, encoding="utf-8")
    (by_city.merge(by_role, how="cross")).to_csv(out_summary, index=False, encoding="utf-8")

    # quick console
    print("Total users:", len(df_enriched))
    print("\nUsers by city:\n", by_city.to_string(index=False))
    print("\nUsers by role (avg age):\n", by_role.to_string(index=False))

    # plot
    plt.figure()
    plt.bar(by_city["city"], by_city["user_count"])
    plt.title("Users per City")
    plt.xlabel("City")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
