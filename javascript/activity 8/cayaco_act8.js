// Whale Talk - Loops Activity
// Rules:
// 1. Only vowels (a, e, i, o, u) are kept (excluding 'y')
// 2. The letters 'u' and 'e' are doubled in the output
// 3. The result should be in uppercase

// Test phrase
const input = 'turpentine and turtles';
let whaleTalk = '';

// Loop through each character in the phrase
for (let i = 0; i < input.length; i++) {
    const char = input[i];
    
    // Check if the character is a vowel (excluding 'y')
    if (char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u') {
        // Double 'u' and 'e' as per whale talk rules
        if (char === 'u' || char === 'e') {
            whaleTalk += char.toUpperCase() + char.toUpperCase();
        } else {
            whaleTalk += char.toUpperCase();
        }
    }
}

// Display the result
console.log('Input:', input);
console.log('Whale talk:', whaleTalk);
