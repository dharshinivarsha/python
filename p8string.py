def snake_to_camel(Word):
        import re
        return ''.join(X.capitalize() or '_' for X in Word.split('_'))

print(snake_to_camel('python'))
