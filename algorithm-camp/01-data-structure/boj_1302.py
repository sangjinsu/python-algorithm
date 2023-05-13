import sys
from collections import defaultdict

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    book_sale = defaultdict(int)
    for _ in range(n):
        book_title = sys.stdin.readline().strip()
        book_sale[book_title] += 1

    result = ''
    most_sale = 0

    titles = sorted(book_sale.keys())
    for title in titles:
        sale = book_sale[title]
        if sale > most_sale:
            result = title
            most_sale = sale

    sys.stdout.write(result)
