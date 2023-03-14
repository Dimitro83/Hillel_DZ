values = [1, 2, '3', 'forth', 'end', 99, True, None]

new_values = list(map(lambda i: str(i) if type(i) == int else i, values))
print('values: ', values, '\nnew_values: ', new_values)
