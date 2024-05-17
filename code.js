let letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

function generateCoprimes(n) {
    let coprimes = [];
    for (let i = 2; i < n; i++) {
        if (gcd(i, n) === 1) {
            coprimes.push(i);
        }
    }
    return coprimes;
}

function gcd(a, b) {
    while (b !== 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

function affineEncrypt(message) {
    let n = letters.length; // number of letters in the alphabet (both capital and small)
    let coprimes = generateCoprimes(n);
    let a = coprimes[Math.floor(Math.random() * coprimes.length)];
    let b = Math.floor(Math.random() * (n - 1)) + 1;

    let encryptedNumbers = [];
    for (let char of message) {
        if (letters.includes(char)) {
            let x = letters.indexOf(char);
            let y = (a * x + b) % n;
            encryptedNumbers.push(y);
        } else {
            encryptedNumbers.push(char);
        }
    }

    return [encryptedNumbers, [a, b]];
}

function modInverse(a, n) {
    for (let x = 1; x < n; x++) {
        if ((a * x) % n === 1) {
            return x;
        }
    }
    return 1;
}

function affineDecrypt(encryptedNumbers, coprimePair) {
    let a = coprimePair[0];
    let b = coprimePair[1];
    let n = letters.length; // number of letters in the alphabet (both capital and small)
    let aInv = modInverse(a, n);

    let decryptedMessage = "";
    for (let y of encryptedNumbers) {
        if (typeof y === 'number') {
            let x = (aInv * (y - b)) % n;
            if (x < 0) {
                x += n;
            }
            decryptedMessage += letters[x];
        } else {
            decryptedMessage += y;
        }
    }

    return decryptedMessage;
}

// Example usage:
let message = "Hello, World abc!";
let [encryptedNumbers, coprimePair] = affineEncrypt(message);
console.log("Encrypted numbers:", encryptedNumbers);
console.log("Co-prime pair:", coprimePair);

let decryptedMessage = affineDecrypt(encryptedNumbers, coprimePair);
console.log("Decrypted message:", decryptedMessage);