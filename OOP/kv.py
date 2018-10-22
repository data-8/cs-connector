class KV:
    """Key-Value container abstraction
    a collection of key-value pairs such that kv_get(kv, key) returns the value
    """
    def __init__(self, kv_pairs=[]):
        self._kv = []
        for (key, val) in kv_pairs:   # Verify and initialize
            assert (type(key) == str) # the key should be a string
            self._kv.append((key, val))
        
    @classmethod
    def create(cls, kv_pairs=[]):
        return cls(kv_pairs)

    def items(self):
        """Return a list of the (key, value) pairs in kv
    
        >>> kv = KV([('a', 1), ('frog', 'croak')])
        >>> ('a', 1) in kv.items()
        True
        >>> ('b', 1) in kv.items()
        False
        """
        return self._kv
            
    def get(self, key):
        """Return the value bound to key in kv, or None if not present
    
        >>> kv = KV([('a', 1), ('frog', 'croak')])
        >>> kv.get('frog')
        'croak'
        >>> kv.get('baba')
        """
        for k, v in self.items():
            if k == key:
                return v
        return None

    def keys(self):
        """Return a list of the keys in kv
    
        >>> kv = KV([('a', 1), ('frog', 'croak')])
        >>> 'a' in kv.keys()
        True
        >>> 'b' in kv.keys()
        False
        """
        return [key for (key, val) in self.items()]

    def values(self):
        """Return a list of the values in kv
    
        >>> kv = KV([('a', 1), ('frog', 'croak')])
        >>> kv.values()
        [1, 'croak']
        """
        return [val for (key, val) in self.items()]

    def add(self, key, value):
        """Return a new KV adding binding (key, value)"""
        return type(self)([(key, value)] + self.items())
        
    def delete(self, key):
        """Return a new KV having removed any binding for key"""
        return type(self)([(k, v) for (k, v) in self.items() if not k == key])

    def __str__(self):
        pairs = sorted(self.items())
        dsp = "{"
        for (key, val) in pairs[:-1]:
            dsp = dsp + "'" + key + "':" + str(val) + ",\n"
        if pairs:
            key, val = pairs[-1]
            dsp = dsp + "'" + key + "':" + str(val)
        dsp = dsp + "}"
        return dsp
    
    def __repr__(self):
        return self.__str__()
    
    def __contains__(self, key):
        """Determine whether key is present in kv"""
        return key in self.keys()
