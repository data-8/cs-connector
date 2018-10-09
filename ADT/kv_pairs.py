# KV using list of (k, v) pairs as internal representation

# Constructors
def kv_empty():
    """Create and return an empty KV
    A KV is a collection of key-value pairs such that kv_get(kv, key) returns the value
    """
    return []

def kv_add(kv, key, value):
    """Create a new KV with an additional (key,value) binding
    """
    assert type(key) == str  # the key should be a string
    return [(key, value)] + kv

def kv_create(kv_pairs):
    """Create and return a KV initialized to list of kvpairs.
    """
    nkv = kv_empty()
    for pair in kv_pairs:   # Verify that initialization is valid
        assert len(pair)==2      # Each should be a (key, value) pair
        key, val = pair
        nkv = kv_add(nkv, key, val)
    return nkv

# Selectors

def kv_get(kv, key):
    """Return the value bound to key in kv, or None if not present
    
    >>> kv = kv_create([('a', 1), ('frog', 'croak')])
    >>> kv_get(kv, 'frog')
    'croak'
    >>> kv_get(kv, 'baba')
    """
    for k, v in kv:
        if k == key:
            return v
    return None

def kv_items(kv):
    """Return a list of the (key, value) pairs in kv
    
    >>> kv = kv_create([('a', 1), ('frog', 'croak')])
    >>> ('a', 1) in kv_items(kv)
    True
    >>> ('b', 1) in kv_items(kv)
    False
    """
    return kv

def kv_keys(kv):
    """Return a list of the keys in kv
    
    >>> kv = kv_create([('a', 1), ('frog', 'croak')])
    >>> 'a' in kv_keys(kv)
    True
    >>> 'b' in kv_items(kv)
    False
    """
    return [key for (key, val) in kv]

def kv_values(kv):
    """Return a list of the values in kv
    
    >>> kv = kv_create([('a', 1), ('frog', 'croak')])
    >>> 1 in kv_values(kv)
    True
    >>> 2 in kv_values(kv)
    False
    """
    return [val for (key, val) in kv]

# Operators

def kv_in(kv, key):
    """Determine whether key is present in kv
    """
    return key in kv_keys(kv)

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

