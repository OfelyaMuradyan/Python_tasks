def create_counter(count = 0):
    counter = count
    def inc(amount = 1):
        nonlocal counter;
        counter += amount

    def dec(amount = 1):
        nonlocal counter;
        counter -= amount

    def get_counter_value():
        return counter
    
    return inc, dec, get_counter_value

inc, dec, get = create_counter(5)
print(get())
inc(2)
print(get())
dec(10)
print(get())

