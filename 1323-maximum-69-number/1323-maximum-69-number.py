class Solution:
    def maximum69Number (self, num: int) -> int:
            result = num
            array = list(str(num))

            if '6' in array:
                index = array.index('6')
                array[index] = '9'
            mx_num = int(''.join(array))
            result = max(result, mx_num)

            return result