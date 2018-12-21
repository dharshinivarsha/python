class py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val
        for x in range(len(s)):
            if x > 0 and rom_val[s[x]] > rom_val[s[x - 1]]:
                int_val += rom_val[s[x]] - 2 * rom_val[s[x - 1]]
            else:
                int_val += rom_val[s[x]]
        return int_val

print(py_solution().roman_to_int('MMCMLXVI'))
print(py_solution().roman_to_int('MM'))
print(py_solution().roman_to_int('C'))
