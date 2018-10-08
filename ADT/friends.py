import kv_pairs as kv
#import kv_lists as kv
#import kv_dict as kv

print(kv)

# A Database of friend pairs
friend_data = [
    ("Christine Strauch", "Jack Chow"),
    ("Christine Strauch", "Lydia Lu"),
    ("Jack Chow", "Christine Strauch"),
    ("Casey Casem", "Christine Strauch"),
    ("Casey Casem", "Jack Chow"),
    ("Casey Casem", "Frances Catal Buloan"),
    ("Casey Casem", "Joy De Rosario"),
    ("Casey Casem", "Casey Casem"),
    ("Frances Catal Buloan", "Jack Chow"),
    ("Jack Chow", "Frances Catal Buloan"),
    ("Joy De Rosario", "Lydia Lu"),
    ("Joy De Lydia", "Jack Chow")
    ]

def make_friends(friendships):
    friends = kv.kv_empty()
    for (der, dee) in friendships:
        if not kv.kv_in(friends, der):
            friends = kv.kv_add(friends, der, [dee])
        else:
            der_friends = kv.kv_get(friends, der)
            friends = kv.kv_add(kv.kv_delete(friends, der), 
                                der, [dee] + der_friends)
    return friends

kv.kv_print(make_friends(friend_data))

