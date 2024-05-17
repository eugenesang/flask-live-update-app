#include <iostream>
#include <string>
#include <vector>

class BigNumber {
private:
    std::vector<int> digits;

public:
    BigNumber() {}

    BigNumber(const std::string& number) {
        for (int i = number.size() - 1; i >= 0; --i) {
            digits.push_back(number[i] - '0');
        }
    }

    BigNumber(int number) {
        while (number > 0) {
            digits.push_back(number % 10);
            number /= 10;
        }
    }

    std::string toString() const {
        std::string result;
        for (int i = digits.size() - 1; i >= 0; --i) {
            result += std::to_string(digits[i]);
        }
        return result;
    }

    BigNumber operator+(const BigNumber& other) const {
        BigNumber result;
        int carry = 0;
        int maxLength = std::max(digits.size(), other.digits.size());

        for (int i = 0; i < maxLength; ++i) {
            int sum = carry;
            if (i < digits.size()) {
                sum += digits[i];
            }
            if (i < other.digits.size()) {
                sum += other.digits[i];
            }

            result.digits.push_back(sum % 10);
            carry = sum / 10;
        }

        if (carry > 0) {
            result.digits.push_back(carry);
        }

        return result;
    }

    BigNumber operator*(const BigNumber& other) const {
        BigNumber result;
        for (int i = 0; i < digits.size(); ++i) {
            BigNumber partialProduct;
            int carry = 0;
            for (int j = 0; j < other.digits.size(); ++j) {
                int product = digits[i] * other.digits[j] + carry;
                partialProduct.digits.push_back(product % 10);
                carry = product / 10;
            }
            if (carry > 0) {
                partialProduct.digits.push_back(carry);
            }
            partialProduct.digits.insert(partialProduct.digits.begin(), i, 0);
            result = result + partialProduct;
        }
        return result;
    }
};

int main() {
    BigNumber num1("12345678901234567890");
    BigNumber num2("98765432109876543210");

    BigNumber sum = num1 + num2;
    BigNumber product = num1 * num2;

    std::cout << "Sum: " << sum.toString() << std::endl;
    std::cout << "Product: " << product.toString() << std::endl;

    return 0;
}