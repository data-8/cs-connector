import kv_pairs as kv
#import kv_lists as kv
#import kv_dict as kv

print(kv)

phone_book_data = [
    ("Christine Strauch", "510-842-9235"),
    ("Frances Catal Buloan", "932-567-3241"),
    ("Jack Chow", "617-547-0923"),
    ("Joy De Rosario", "310-912-6483"),
    ("Casey Casem", "415-432-9292"),
    ("Lydia Lu", "707-341-1254")]

phone_book = kv.kv_create(phone_book_data)
print("Jack Chows's Number: ", kv.kv_get(phone_book, "Jack Chow"))

print("Area codes")
area_codes = list(map(lambda x:x[0:3], kv.kv_values(phone_book)))
print(area_codes)
