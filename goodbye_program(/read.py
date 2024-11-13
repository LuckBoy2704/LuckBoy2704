def reading_txt_file(name):
    with open('text', 'r', encoding='utf8') as file:
        for good in file:
            item_name, url = good.strip().split(',')
            if item_name == name:
                return url
    return None
