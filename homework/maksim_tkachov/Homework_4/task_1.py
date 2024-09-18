my_dict = {}
my_dict['tuple'] = ('hostname', 'location', 'vendor', 'model', 'ios', 'ip')
my_dict['list'] = [1, 20, 4.0, 'word', 'minsk']
my_dict['dict'] = {'city': 'London', 'club': "Tottenham", 'year_of_origin': 1882,
                   'stadium': 'Tottenham Hotspur Stadium', 'nick_name': "The lilywhites"}
my_dict['set'] = {10, 20, 30, 40, 100}
last_element_of_the_tuple = my_dict['tuple'][-1]
print('Last element of the tupple key of the dictionary: '
      + last_element_of_the_tuple)
my_dict['list'].append('gomel')
my_dict['list'].pop(1)
my_dict['dict'][('i am a tuple',)] = 'some value'
del my_dict['dict']['club']
my_dict['set'].add(1000)
my_dict['set'].discard(30)
print('Updated final view of "my_dict" dictionary after all changes: ', my_dict)
