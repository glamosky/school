// Test version of Color Mixer Program
// Simulates prompt inputs to test the logic

// Function to validate if a color is valid (red, green, or blue)
function isValidColor(color) {
    const validColors = ['red', 'green', 'blue'];
    return validColors.includes(color.toLowerCase());
}

// Function to mix two colors
function mixColors(color1, color2) {
    // Convert colors to lowercase for case-insensitive comparison
    const c1 = color1.toLowerCase();
    const c2 = color2.toLowerCase();
    
    // Check if both colors are valid
    if (!isValidColor(c1) || !isValidColor(c2)) {
        return 'No Data';
    }
    
    // Color mixing logic based on RGB theory
    if (c1 === c2) {
        // Same colors result in the same color
        return c1.charAt(0).toUpperCase() + c1.slice(1); // Capitalize first letter
    }
    
    // Different color combinations
    if ((c1 === 'red' && c2 === 'blue') || (c1 === 'blue' && c2 === 'red')) {
        return 'Magenta';
    }
    if ((c1 === 'blue' && c2 === 'green') || (c1 === 'green' && c2 === 'blue')) {
        return 'Cyan';
    }
    if ((c1 === 'green' && c2 === 'red') || (c1 === 'red' && c2 === 'green')) {
        return 'Yellow';
    }
    
    return 'No Data'; // Fallback
}

// Test function that simulates the main program
function testColorMixer(color1, color2) {
    console.log(`Input: color1 = "${color1}", color2 = "${color2}"`);
    
    // Mix the colors
    const result = mixColors(color1, color2);
    
    // Display result
    if (result === 'No Data') {
        console.log(`${color1.toLowerCase()} + ${color2.toLowerCase()} = ${result}`);
    } else {
        // Format output for valid combinations
        const formattedColor1 = color1.toUpperCase();
        const formattedColor2 = color2.toUpperCase();
        console.log(`${formattedColor1} + ${formattedColor2} = ${result}`);
    }
    console.log('---');
}

// Test cases
console.log('=== COLOR MIXER TEST CASES ===\n');

// Valid combinations
testColorMixer('red', 'red');
testColorMixer('blue', 'blue');
testColorMixer('green', 'green');
testColorMixer('red', 'blue');
testColorMixer('blue', 'green');
testColorMixer('green', 'red');

// Case insensitive tests
testColorMixer('RED', 'blue');
testColorMixer('Green', 'RED');

// Invalid combinations
testColorMixer('Pink', 'Red');
testColorMixer('red', 'yellow');
testColorMixer('purple', 'orange');
