class BigNumber:
    def __init__(self, value=0):
        if isinstance(value, int):
            self.digits = [int(d) for d in str(value)]
        elif isinstance(value, str):
            self.digits = [int(d) for d in value]
        else:
            raise ValueError("Invalid input type")

    def __str__(self):
        return ''.join(map(str, self.digits))

    def __add__(self, other):
        result = []
        carry = 0
        for i in range(max(len(self.digits), len(other.digits))):
            sum_ = carry
            if i < len(self.digits):
                sum_ += self.digits[-1 - i]
            if i < len(other.digits):
                sum_ += other.digits[-1 - i]
            carry, digit = divmod(sum_, 10)
            result.append(digit)
        if carry:
            result.append(carry)
        return BigNumber(''.join(map(str, reversed(result))))

    def __mul__(self, other):
        result = BigNumber(0)
        for i in range(len(other.digits)):
            partial_product = BigNumber(0)
            carry = 0
            for j in range(len(self.digits)):
                product = self.digits[-1 - j] * other.digits[-1 - i] + carry
                carry, digit = divmod(product, 10)
                partial_product.digits.insert(0, digit)
            if carry:
                partial_product.digits.insert(0, carry)
            partial_product.digits.extend([0] * i)
            result += partial_product
        return result
    
    def __truediv__(self, other):
        # Normalize the dividend and divisor
        dividend = self
        divisor = other
        while len(dividend.digits) < len(divisor.digits):
            dividend.digits.insert(0, 0)

        # Initialize the quotient and remainder
        quotient = BigNumber(0)
        remainder = BigNumber(0)

        # Calculate the partial quotient
        for i in range(len(dividend.digits) - len(divisor.digits) + 1):
            partial_quotient = 0
            temp = BigNumber(0)
            for j in range(len(divisor.digits)):
                temp.digits.append(dividend.digits[i + j])
            while temp >= divisor:
                temp -= divisor
                partial_quotient += 1
            quotient.digits.append(partial_quotient)
            remainder = temp

        # Remove leading zeros from the quotient
        while quotient.digits[0] == 0:
            quotient.digits.pop(0)

        return quotient, remainder



# Example usage
num1 = BigNumber("1234567899876543219284924092840280495809238409")
num2 = BigNumber("2345")
print(num2)
print(f'num: {num1}')
sum_ = num1 + num2
print(f"Sum: {sum_}")

product = num1 * num2
print(f"Product: {product}")