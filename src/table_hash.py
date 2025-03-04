dict = {}
dict['john'] = True

def verify(dict, name):
    if dict.get(name):
        print(f'{name} voted!')
    else:
        dict[name] = True
        print(f'{name} need to vote.')

verify(dict,'john')
verify(dict,'raul')

