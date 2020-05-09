class RomanNumerals:
        def to_roman(number):
        num = [1, 4, 5, 9, 10, 40, 50, 90,  
           100, 400, 500, 900, 1000] 
        sym = ["I", "IV", "V", "IX", "X", "XL",  
           "L", "XC", "C", "CD", "D", "CM", "M"] 
        i = 12
        ret = ""
        while num:
            div = number // num[i]
            number %= num[i]
            while div:
                ret += sym[i]
                div -= 1
            i -= 1
        return ret

        def from_roman(romanNumber):
            value = { 
                'M': 1000, 
                'D': 500, 
                'C': 100, 
                'L': 50, 
                'X': 10, 
                'V': 5, 
                'I': 1
            } 
            ret = 0
            previous = 0
            l = len(romanNumber)
            for i in range(l-1,-1,-1):
                if value[romanNumber[i]] >= previous:
                    ret += value[romanNumber[i]]
                else:
                    ret -= value[romanNumber[i]]
                previous = value[romanNumber[i]]
            return ret
                    