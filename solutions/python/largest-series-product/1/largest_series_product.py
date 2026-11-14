def largest_product(series, size):
    """series: a full number
    size: gap to test"""
    if size < 0:
        raise ValueError("span must not be negative")

    if size > len(series):
        raise ValueError("span must not exceed string length")

    if not series.isdigit():
        raise ValueError("digits input must only contain digits")

    if size == 0:
        return 1

    products = []

    for i in range(len(series) - size + 1):
        window = series[i:i + size]

        product = 1
        for digit in window:
            product *= int(digit)

        products.append(product)

    return max(products)