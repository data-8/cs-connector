def bday(n):
    """Return the probability that 2 of n people have the same birthday."""
    if (n >= 365): return 1.0
    p_of_notwo = 1.0
    for i in range(n-1):
        p_of_notwo = p_of_notwo * (364-i)/365.0
    return 1-p_of_notwo



