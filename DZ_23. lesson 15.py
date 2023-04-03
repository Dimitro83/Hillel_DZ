class String(str):

    def __add__(self, other):
        return String(str(self) + str(other))

    def __sub__(self, other):
        if str(other) in str(self):
            return String(self.replace(str(other), "", 1))
        else:
            return self


print(String('New') + String(890))
print(String(1234) + 5678)
print(String('New') + 'castle')
print(String('New') + 77)
print(String('New') + True)
print(String('New') + ['s', ' ', 23])
print(String('New') + None)
print(String('New bala7nce') - 7)
print(String('New balance') - 'bal')
print(String('New balance') - 'Bal')
print(String('pineapple apple pine') - 'apple')
print(String('New balance') - 'apple')
print(String('NoneType') - None)
print(String(55678345672) - 7)

# result checking
# String('New') + String(890)    ->    'New890'
# String(1234) + 5678            ->    12345678
# String('New') + 'castle'       ->    'Newcastle'
# String('New') + 77             ->    'New77'
# String('New') + True           ->    'NewTrue'
# String('New') + ['s', ' ', 23] ->    "New['s', ' ', 23]"
# String('New') + None           ->    'NewNone'
# String('New bala7nce') - 7               ->    'New balance'
# String('New balance') - 'bal'            ->    'New ance'
# String('New balance') - 'Bal'            ->    'New balance'
# String('pineapple apple pine') - 'apple' ->    'pine apple pine'
# String('New balance') - 'apple'          ->    'New balance'
# String('NoneType') - None                ->    'Type'
# String(55678345672) - 7                  ->    '5568345672'
