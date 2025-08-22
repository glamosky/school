// ========================================
// COMPREHENSIVE JAVASCRIPT CONCEPTS GUIDE
// ========================================

// ========================================
// 1. VARIABLES AND DATA TYPES
// ========================================

// var - function-scoped variable (older way, avoid in modern JS)
var oldWay = "I'm function-scoped";

// let - block-scoped variable (preferred for variables that change)
let modernVariable = "I'm block-scoped and can be reassigned";
modernVariable = "I can be changed!";

// const - block-scoped constant (preferred for values that don't change)
const constantValue = "I cannot be reassigned";
// constantValue = "This would cause an error!"; // Uncomment to see error

// Primitive Data Types
const stringExample = "Hello, World!"; // Text data
const numberExample = 42; // Numbers (both integer and float)
const booleanExample = true; // true or false
const nullExample = null; // Intentional absence of value
const undefinedExample = undefined; // Variable declared but not assigned
const symbolExample = Symbol("unique"); // Unique identifier
const bigIntExample = 9007199254740991n; // Large integers

// Reference Data Types
const objectExample = { name: "John", age: 30 }; // Object literal
const arrayExample = [1, 2, 3, 4, 5]; // Array
const functionExample = function() { return "I'm a function!"; }; // Function

// ========================================
// 2. OPERATORS
// ========================================

// Arithmetic Operators
let a = 10, b = 3;
console.log("Addition:", a + b); // 13
console.log("Subtraction:", a - b); // 7
console.log("Multiplication:", a * b); // 30
console.log("Division:", a / b); // 3.333...
console.log("Modulus:", a % b); // 1 (remainder)
console.log("Exponentiation:", a ** b); // 1000
console.log("Increment:", ++a); // 11 (pre-increment)
console.log("Decrement:", b--); // 3 (post-decrement)

// Assignment Operators
let x = 5;
x += 3; // Same as x = x + 3
x -= 2; // Same as x = x - 2
x *= 4; // Same as x = x * 4
x /= 2; // Same as x = x / 2
x %= 3; // Same as x = x % 3

// Comparison Operators
console.log("Equal (value):", 5 == "5"); // true (type coercion)
console.log("Strict Equal:", 5 === "5"); // false (no type coercion)
console.log("Not Equal:", 5 != "6"); // true
console.log("Strict Not Equal:", 5 !== "5"); // true
console.log("Greater Than:", 10 > 5); // true
console.log("Less Than:", 3 < 7); // true
console.log("Greater or Equal:", 5 >= 5); // true
console.log("Less or Equal:", 4 <= 4); // true

// Logical Operators
console.log("AND:", true && false); // false
console.log("OR:", true || false); // true
console.log("NOT:", !true); // false

// ========================================
// 3. CONTROL STRUCTURES
// ========================================

// If-Else Statements
let userAge = 18;
if (userAge >= 18) {
    console.log("You are an adult");
} else if (userAge >= 13) {
    console.log("You are a teenager");
} else {
    console.log("You are a child");
}

// Switch Statement
let weekDay = "Monday";
switch (weekDay) {
    case "Monday":
        console.log("Start of work week");
        break; // Prevents fall-through
    case "Friday":
        console.log("TGIF!");
        break;
    default:
        console.log("Regular day");
}

// Loops
// For Loop
for (let i = 0; i < 3; i++) {
    console.log(`For loop iteration ${i}`);
}

// While Loop
let count = 0;
while (count < 3) {
    console.log(`While loop iteration ${count}`);
    count++;
}

// Do-While Loop (executes at least once)
let num = 0;
do {
    console.log(`Do-while iteration ${num}`);
    num++;
} while (num < 3);

// For...of Loop (iterates over iterable values)
const colors = ["red", "green", "blue"];
for (const color of colors) {
    console.log(`Color: ${color}`);
}

// For...in Loop (iterates over object properties)
const person = { name: "Alice", age: 25 };
for (const key in person) {
    console.log(`${key}: ${person[key]}`);
}

// ========================================
// 4. FUNCTIONS
// ========================================

// Function Declaration
function greet(name) {
    return `Hello, ${name}!`;
}

// Function Expression
const greetExpression = function(name) {
    return `Hello, ${name}!`;
};

// Arrow Function (ES6+)
const greetArrow = (name) => `Hello, ${name}!`;

// Arrow Function with multiple parameters and body
const add = (a, b) => {
    const result = a + b;
    return result;
};

// Default Parameters
function greetWithDefault(name = "Guest") {
    return `Hello, ${name}!`;
}

// Rest Parameters (collects multiple arguments into array)
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}

// Higher-Order Functions
function createMultiplier(factor) {
    return function(number) {
        return number * factor;
    };
}
const double = createMultiplier(2);
const triple = createMultiplier(3);

// Immediately Invoked Function Expression (IIFE)
(function() {
    console.log("I run immediately!");
})();

// ========================================
// 5. ARRAYS AND ARRAY METHODS
// ========================================

const fruits = ["apple", "banana", "orange"];

// Array Methods
// push() - adds element to end
fruits.push("grape");

// pop() - removes and returns last element
const lastFruit = fruits.pop();

// unshift() - adds element to beginning
fruits.unshift("strawberry");

// shift() - removes and returns first element
const firstFruit = fruits.shift();

// splice() - adds/removes elements at specific index
fruits.splice(1, 1, "mango"); // Remove 1 element at index 1, add "mango"

// slice() - extracts portion of array
const citrus = fruits.slice(1, 3);

// indexOf() - finds index of element
const bananaIndex = fruits.indexOf("banana");

// includes() - checks if element exists
const hasApple = fruits.includes("apple");

// Array Iteration Methods
const numbers = [1, 2, 3, 4, 5];

// map() - transforms each element
const doubled = numbers.map(num => num * 2);

// filter() - creates new array with elements that pass test
const evenNumbers = numbers.filter(num => num % 2 === 0);

// reduce() - reduces array to single value
const sum = numbers.reduce((total, num) => total + num, 0);

// forEach() - executes function for each element
numbers.forEach(num => console.log(`Number: ${num}`));

// find() - returns first element that passes test
const firstEven = numbers.find(num => num % 2 === 0);

// some() - checks if at least one element passes test
const hasEven = numbers.some(num => num % 2 === 0);

// every() - checks if all elements pass test
const allPositive = numbers.every(num => num > 0);

// ========================================
// 6. OBJECTS AND OBJECT METHODS
// ========================================

// Object Literal
const user = {
    name: "John",
    age: 30,
    email: "john@example.com",
    
    // Method (function as property)
    greet() {
        return `Hello, I'm ${this.name}`;
    },
    
    // Arrow function (doesn't bind 'this')
    greetArrow: () => {
        return "Hello from arrow function";
    }
};

// Object Destructuring
const { name, age } = user;
const { name: userName, age: userAge2 } = user; // Renaming

// Object Spread Operator
const userCopy = { ...user };
const userWithRole = { ...user, role: "admin" };

// Object Methods
// Object.keys() - returns array of property names
const keys = Object.keys(user);

// Object.values() - returns array of property values
const values = Object.values(user);

// Object.entries() - returns array of [key, value] pairs
const entries = Object.entries(user);

// Object.assign() - copies properties from one object to another
const targetObj = {};
Object.assign(targetObj, user);

// ========================================
// 7. CLASSES (ES6+)
// ========================================

class Animal {
    constructor(name, species) {
        this.name = name;
        this.species = species;
    }
    
    // Instance method
    speak() {
        return `${this.name} makes a sound`;
    }
    
    // Static method (called on class, not instance)
    static create(name, species) {
        return new Animal(name, species);
    }
}

class Dog extends Animal {
    constructor(name, breed) {
        super(name, "Dog"); // Call parent constructor
        this.breed = breed;
    }
    
    // Override parent method
    speak() {
        return `${this.name} barks!`;
    }
    
    // Getter
    get description() {
        return `${this.name} is a ${this.breed} ${this.species}`;
    }
    
    // Setter
    set age(value) {
        if (value >= 0) {
            this._age = value;
        }
    }
}

// ========================================
// 8. PROMISES AND ASYNCHRONOUS PROGRAMMING
// ========================================

// Promise - represents eventual completion of async operation
const myPromise = new Promise((resolve, reject) => {
    // Simulate async operation
    setTimeout(() => {
        const random = Math.random();
        if (random > 0.5) {
            resolve("Success!");
        } else {
            reject("Failed!");
        }
    }, 1000);
});

// Promise handling
myPromise
    .then(result => console.log("Promise resolved:", result))
    .catch(error => console.log("Promise rejected:", error))
    .finally(() => console.log("Promise completed"));

// Promise.all() - waits for all promises to resolve
const promise1 = Promise.resolve(3);
const promise2 = new Promise(resolve => setTimeout(() => resolve("foo"), 2000));
const promise3 = Promise.resolve(42);

Promise.all([promise1, promise2, promise3])
    .then(values => console.log("All resolved:", values));

// Promise.race() - returns first promise to resolve/reject
Promise.race([promise1, promise2, promise3])
    .then(value => console.log("First resolved:", value));

// Async/Await (ES2017+) - cleaner way to handle promises
async function fetchUserData() {
    try {
        const response = await fetch('https://api.example.com/user');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Error fetching user data:", error);
        throw error;
    }
}

// ========================================
// 9. MODULES (ES6+)
// ========================================

// Exporting from module (would be in separate file)
export const PI = 3.14159;
export function square(x) {
    return x * x;
}
export default class Calculator {
    add(a, b) { return a + b; }
    subtract(a, b) { return a - b; }
}

// Importing modules (would be in separate file)
import Calculator, { PI, square } from './math.js';
import * as MathUtils from './math.js';

// ========================================
// 10. TEMPLATE LITERALS (ES6+)
// ========================================

const firstName = "John";
const lastName = "Doe";
const age2 = 30;

// Template literal with interpolation
const fullName = `${firstName} ${lastName}`;
const message = `Hello, my name is ${fullName} and I am ${age2} years old.`;

// Multi-line template literal
const html = `
    <div class="user">
        <h1>${fullName}</h1>
        <p>Age: ${age2}</p>
    </div>
`;

// Template literal with expressions
const price = 19.99;
const quantity = 3;
const total = `Total: $${(price * quantity).toFixed(2)}`;

// ========================================
// 11. DESTRUCTURING ASSIGNMENT
// ========================================

// Array Destructuring
const [first, second, ...rest] = [1, 2, 3, 4, 5];
const [a1, b1, c1 = "default"] = [1, 2]; // c1 will be "default"

// Object Destructuring
const { title, author, year = 2023 } = { title: "Book", author: "Author" };

// Nested Destructuring
const { user: { name: userName2, preferences: { theme } } } = {
    user: { name: "Alice", preferences: { theme: "dark" } }
};

// ========================================
// 12. SPREAD AND REST OPERATORS
// ========================================

// Spread Operator (...)
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5]; // [1, 2, 3, 4, 5]

const obj1 = { a: 1, b: 2 };
const obj2 = { ...obj1, c: 3 }; // { a: 1, b: 2, c: 3 }

// Rest Operator (collects remaining elements)
function sumRest(...args) {
    return args.reduce((total, num) => total + num, 0);
}

// ========================================
// 13. ERROR HANDLING
// ========================================

// Try-Catch-Finally
try {
    // Code that might throw an error
    throw new Error("Something went wrong!");
} catch (error) {
    console.error("Caught error:", error.message);
} finally {
    console.log("This always runs");
}

// Custom Error Class
class CustomError extends Error {
    constructor(message, code) {
        super(message);
        this.name = "CustomError";
        this.code = code;
    }
}

// ========================================
// 14. REGULAR EXPRESSIONS
// ========================================

// Creating RegExp
const regex1 = /pattern/;
const regex2 = new RegExp("pattern");

// Common patterns
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const phoneRegex = /^\d{3}-\d{3}-\d{4}$/;

// RegExp methods
const text = "Hello World";
const match = text.match(/world/i); // Case-insensitive match
const replaced = text.replace(/world/i, "JavaScript");

// ========================================
// 15. LOCAL STORAGE AND SESSION STORAGE
// ========================================

// Local Storage (persists until cleared)
localStorage.setItem("username", "john_doe");
const username = localStorage.getItem("username");
localStorage.removeItem("username");
localStorage.clear(); // Clear all

// Session Storage (persists only for session)
sessionStorage.setItem("sessionId", "abc123");
const sessionId = sessionStorage.getItem("sessionId");

// ========================================
// 16. DATE AND TIME
// ========================================

// Creating Date objects
const now = new Date();
const specificDate = new Date("2023-12-25");
const timestamp = new Date(1703520000000);

// Date methods
const currentYear = now.getFullYear();
const currentMonth = now.getMonth(); // 0-11
const currentDay = now.getDate();
const currentHours = now.getHours();
const currentMinutes = now.getMinutes();
const currentSeconds = now.getSeconds();

// Date formatting
const formattedDate = now.toLocaleDateString();
const formattedTime = now.toLocaleTimeString();
const isoString = now.toISOString();

// ========================================
// 17. JSON (JavaScript Object Notation)
// ========================================

const jsonString = '{"name": "John", "age": 30, "city": "New York"}';

// Parsing JSON string to object
const parsedObject = JSON.parse(jsonString);

// Converting object to JSON string
const objectToJson = JSON.stringify(parsedObject);

// Pretty-printed JSON
const prettyJson = JSON.stringify(parsedObject, null, 2);

// ========================================
// 18. CLOSURES
// ========================================

function createCounter() {
    let count = 0; // Private variable
    
    return {
        increment() {
            return ++count;
        },
        decrement() {
            return --count;
        },
        getCount() {
            return count;
        }
    };
}

const counter = createCounter();
counter.increment(); // 1
counter.increment(); // 2
counter.decrement(); // 1

// ========================================
// 19. EVENT HANDLING
// ========================================

// Adding event listener
function handleClick(event) {
    console.log("Button clicked!", event);
}

// In a real DOM environment:
// document.getElementById("myButton").addEventListener("click", handleClick);

// Event delegation
function handleDelegatedClick(event) {
    if (event.target.matches(".item")) {
        console.log("Item clicked:", event.target.textContent);
    }
}

// ========================================
// 20. CALLBACKS AND HIGHER-ORDER FUNCTIONS
// ========================================

// Callback function
function processData(data, callback) {
    const processed = data.toUpperCase();
    callback(processed);
}

processData("hello world", (result) => {
    console.log("Processed:", result);
});

// Higher-order function that returns a function
function multiplyBy(factor) {
    return function(number) {
        return number * factor;
    };
}

const multiplyByTwo = multiplyBy(2);
const multiplyByTen = multiplyBy(10);

// ========================================
// 21. ITERATORS AND GENERATORS
// ========================================

// Iterator
const iterable = {
    [Symbol.iterator]() {
        let step = 0;
        return {
            next() {
                step++;
                if (step <= 3) {
                    return { value: step, done: false };
                }
                return { done: true };
            }
        };
    }
};

for (const value of iterable) {
    console.log("Iterator value:", value);
}

// Generator function
function* numberGenerator() {
    yield 1;
    yield 2;
    yield 3;
}

const generator = numberGenerator();
console.log(generator.next().value); // 1
console.log(generator.next().value); // 2
console.log(generator.next().value); // 3

// ========================================
// 22. PROXY AND REFLECT
// ========================================

// Proxy - intercepts and customizes operations on objects
const target = { name: "John" };
const handler = {
    get(target, property) {
        console.log(`Getting property: ${property}`);
        return target[property];
    },
    set(target, property, value) {
        console.log(`Setting property: ${property} to ${value}`);
        target[property] = value;
        return true;
    }
};

const proxy = new Proxy(target, handler);
proxy.name; // Logs: Getting property: name
proxy.age = 30; // Logs: Setting property: age to 30

// Reflect - provides methods for interceptable JavaScript operations
const obj = { x: 1, y: 2 };
Reflect.set(obj, 'z', 3);
const hasZ = Reflect.has(obj, 'z');

// ========================================
// 23. MAPS AND SETS
// ========================================

// Map - key-value pairs with any type as key
const map = new Map();
map.set("key1", "value1");
map.set(42, "value2");
map.set({}, "value3");

console.log(map.get("key1")); // "value1"
console.log(map.has(42)); // true
console.log(map.size); // 3

// Set - collection of unique values
const set = new Set([1, 2, 2, 3, 3, 4]);
console.log(set.size); // 4 (duplicates removed)
set.add(5);
set.delete(1);
console.log(set.has(2)); // true

// ========================================
// 24. WEAKMAP AND WEAKSET
// ========================================

// WeakMap - Map with weak references (keys must be objects)
const weakMap = new WeakMap();
const weakMapObj = {};
weakMap.set(weakMapObj, "value");
console.log(weakMap.get(weakMapObj)); // "value"

// WeakSet - Set with weak references (values must be objects)
const weakSet = new WeakSet();
const weakSetObj = {};
weakSet.add(weakSetObj);
console.log(weakSet.has(weakSetObj)); // true

// ========================================
// 25. TYPED ARRAYS
// ========================================

// Typed arrays for handling binary data
const int8Array = new Int8Array(4);
const uint8Array = new Uint8Array(4);
const float32Array = new Float32Array(4);

// ArrayBuffer - raw binary data
const buffer = new ArrayBuffer(16);
const view = new DataView(buffer);

// ========================================
// 26. INTERNATIONALIZATION (i18n)
// ========================================

// Number formatting
const number = 1234567.89;
const formatter = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD'
});
console.log(formatter.format(number)); // "$1,234,567.89"

// Date formatting
const date = new Date();
const dateFormatter = new Intl.DateTimeFormat('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
});
console.log(dateFormatter.format(date)); // "December 25, 2023"

// ========================================
// 27. WEB APIs
// ========================================

// Fetch API (for HTTP requests)
async function fetchData() {
    try {
        const response = await fetch('https://api.example.com/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Fetch error:', error);
    }
}

// Geolocation API
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
        (position) => {
            console.log('Latitude:', position.coords.latitude);
            console.log('Longitude:', position.coords.longitude);
        },
        (error) => {
            console.error('Geolocation error:', error);
        }
    );
}

// ========================================
// 28. WORKERS (Web Workers)
// ========================================

// Main thread
// const worker = new Worker('worker.js');
// worker.postMessage({ data: 'Hello from main thread' });
// worker.onmessage = (event) => {
//     console.log('Message from worker:', event.data);
// };

// Worker thread (worker.js)
// self.onmessage = (event) => {
//     const result = processData(event.data);
//     self.postMessage(result);
// };

// ========================================
// 29. SERVICE WORKERS
// ========================================

// Service Worker registration
// if ('serviceWorker' in navigator) {
//     navigator.serviceWorker.register('/sw.js')
//         .then(registration => {
//             console.log('SW registered:', registration);
//         })
//         .catch(error => {
//             console.log('SW registration failed:', error);
//         });
// }

// ========================================
// 30. MODERN JAVASCRIPT FEATURES
// ========================================

// Optional Chaining (?.)
const user2 = { profile: { name: "John" } };
const userName3 = user2?.profile?.name; // "John"
const userAge3 = user2?.profile?.age; // undefined (no error)

// Nullish Coalescing (??)
const nullishValue = null ?? "default"; // "default"
const nullishValue2 = 0 ?? "default"; // 0 (only null/undefined trigger default)

// Logical Assignment Operators
let x2 = 1;
x2 ||= 2; // x2 = x2 || 2
x2 &&= 3; // x2 = x2 && 3
x2 ??= 4; // x2 = x2 ?? 4

// Top-level await (ES2022)
// const data = await fetchData(); // Can be used at module top level

// ========================================
// DEMONSTRATION OF CONCEPTS
// ========================================

console.log("=== JavaScript Concepts Demonstration ===");

// Test function calls
console.log("Function call:", greet("World"));
console.log("Arrow function:", greetArrow("Arrow"));
console.log("Default parameter:", greetWithDefault());
console.log("Rest parameters sum:", sum(1, 2, 3, 4, 5));

// Test array methods
console.log("Doubled numbers:", doubled);
console.log("Even numbers:", evenNumbers);
console.log("Sum of numbers:", sum);

// Test object methods
console.log("User greeting:", user.greet());
console.log("Object keys:", keys);
console.log("Object values:", values);

// Test classes
const dog = new Dog("Buddy", "Golden Retriever");
console.log("Dog speaks:", dog.speak());
console.log("Dog description:", dog.description);

// Test template literals
console.log("Template literal:", message);
console.log("Total calculation:", total);

// Test destructuring
console.log("Destructured name:", userName);
console.log("Array destructuring:", first, second, rest);

// Test closures
console.log("Counter count:", counter.getCount());

// Test Map and Set
console.log("Map size:", map.size);
console.log("Set size:", set.size);

console.log("=== All JavaScript concepts demonstrated! ===");
