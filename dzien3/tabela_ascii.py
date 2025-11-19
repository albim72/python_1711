def read_table(path):
    with open(path, 'r',encoding='utf-8') as f:
        rows = [line.strip().split(",") for line in f]
    return rows


def print_table(table):
    #obliczamy szrokości kolumn
    col_widths = [max(len(row[i]) for row in table) for i in range(len(table[0]))]

    #funclja pomocnicza do formatu wiersza
    def format_row(row):
        return " | ".join(row[i].ljust(col_widths[i]) for i in range(len(row)))

    #rysowanie
    header = format_row(table[0])
    print(header)
    print("-" * len(header))
    for row in table[1:]:
        print(format_row(row))


table = read_table("dane/users.txt")
print_table(table)
