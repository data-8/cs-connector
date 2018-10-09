"""
Key-Value Abstract Data Type

Using an internal representation of a dict
"""

# Constructors

def kv_empty():
    """Create and return an empty KV
    """
    return {}

def kv_add(kv, key, value):
    """Create a new KV with an addition (key,value) binding
    """
    assert type(key) == str  # the key should be a string
    nkv = kv.copy()
    nkv[key] = value
    return nkv

def kv_create(kv_pairs):
    """Create and return a KV initialized to list of kvpairs.
    
    A KV is a collection of key-value pairs such that kv_get(kv, key) returns the value
    bound to key
    """
    
    # Internal representation of a KV is a pair of lists: keys and values
    for kv in kv_pairs:   # Verify that initialization is valid
        assert len(kv)==2      # Each should be a key, value pair
    kv = kv_empty()
    for (k,v) in kv_pairs:
        kv = kv_add(kv, k, v)
    return kv       # 

# Selectors 

def kv_get(kv, key):
    """Return the value bound to key in kv, or None if not present
    
    >>> kv = kv_create([('a', 1), ('frog', 'croak')])
    >>> kv_get(kv, 'frog')
    'croak'
    >>> kv_get(kv, 'baba')
    """
    if key in kv:
        return kv[key]
    else:
        return None

def kv_items(kv):
    """Return a list of the (key, value) pairs in kv
    
    >>> kv = kv_create([('a', 1), ('frog', 'croak')])
    >>> ('a', 1) in kv_items(kv)
    True
    >>> ('b', 1) in kv_items(kv)
    False
    """
    return list(kv.items())

def kv_keys(kv):
    """Return a list of the keys in kv
    
    >>> kv = kv_create([('a', 1), ('frog', 'croak')])
    >>> 'a' in kv_keys(kv)
    True
    >>> 'b' in kv_items(kv)
    False
    """
    return list(kv.keys())

def kv_values(kv):
    """Return a list of the values in kv
    
    >>> kv = kv_create([('a', 1), ('frog', 'croak')])
    >>> 1 in kv_values(kv)
    True
    >>> 2 in kv_values(kv)
    False
    """
    return list(kv.values())

# Operations - built on constructors and selectors

def kv_in(kv, key):
    """Determine whether key is present in kv
    """
    return key in kv

def kv_delete(kv, key):
    """Return a KV based in kv having removed any binding for key
    """
    return kv_create([(k, v) for (k, v) in kv_items(kv) if not k == key])

def kv_print(kv):
    pairs = sorted(kv_items(kv))
    dsp = "{"
    for (key, val) in pairs[:-1]:
        dsp = dsp + "'" + key + "':" + str(val) + ",\n"
    if pairs:
        key, val = pairs[-1]
        dsp = dsp + "'" + key + "':" + str(val)
    dsp = dsp + "}"
    print(dsp)
