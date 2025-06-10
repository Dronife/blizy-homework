def extract_brand_name(product_name):
    if 'iphone' in product_name:
        return 'apple'
    elif product_name.startswith('2nd-'):
        return product_name.split('-')[-1]
    else:
        return product_name