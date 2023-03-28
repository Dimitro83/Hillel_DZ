dz_15 = b'r\xc3\xa9sum\xc3\xa9'
print('initial: ', dz_15)
step_1 = dz_15.decode()
print('step_1 (decode) :', step_1)
step_2 = step_1.encode('Latin1')
print('step_2 (‘Latin1’): ', step_2)
step_3 = step_2.decode('Latin1')
print('step_3 (decode) :', step_3)
