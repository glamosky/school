// Euclidean Distance Calculator using Closures
function getDistanceCalculator(x1, y1) {
    // This closure remembers the coordinates of point A (x1, y1). It makes sure that the coordinates of point A are not changed.
    return function(x2, y2) {
        // Calculate Euclidean distance using Pythagoras's theorem
        const deltaX = x2 - x1;
        const deltaY = y2 - y1;
        const distance = Math.sqrt(deltaX ** 2 + deltaY ** 2);
        
        // Return as stringified number rounded to 1 decimal place
        return distance.toFixed(1);
    };
}

// Create distance calculator from origin (0,0)
const distanceFromOrigin = getDistanceCalculator(0, 0);

// Create distance calculator from point (5,5)
const distanceFromPoint = getDistanceCalculator(5, 5);

// Calculate distances from origin
console.log(`From (0,0) to (30,5): ${distanceFromOrigin(30, 5)}`);
console.log(`From (0,0) to (8,8): ${distanceFromOrigin(8, 8)}`);
console.log(`From (0,0) to (-5,-10): ${distanceFromOrigin(-5, -10)}`);

// Calculate distances from point (5,5)
console.log(`From (5,5) to (10,2): ${distanceFromPoint(10, 2)}`);
console.log(`From (5,5) to (0,1): ${distanceFromPoint(0, 1)}`);                                                                         
console.log(`From (5,5) to (-90,-1): ${distanceFromPoint(-90, -1)}`);
