from parsel import Selector 

with open('./data/scifi.html') as f: 
    html_file = f.read()
selector = Selector(text=html_file)
all_items_on_page = selector.css('li.product.item').getall()
print(len(all_items_on_page))
for item in all_items_on_page: 
    item_selector = Selector(str(item).strip())
    print(item_selector.css('h3.product.name > a::text').get().strip())
