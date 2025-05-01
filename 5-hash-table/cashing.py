cache = {}

def get_page(url):
  if cache.get(url):
    return cache(url)
  else:
    data_page = get_data_page_from_server(url)
    cache[url] = data_page
    return data_page