let secretMessage = ['Learning','is','not','about','what','you','get','easily','the','first','time,','it','is','about','what','you','can','figure','out.', '-2015','Chris','Pine','learn','JavaScript'];

// Step 1: Use an array method to remove the last string of the array secretMessage
secretMessage.pop();

// Step 2: Use an array method to add words to and Program as separate strings to the end of the secretMessage array
secretMessage.push('to');
secretMessage.push('Program');

// Step 3: Change the word easily to the word right by accessing the index and replacing it.
secretMessage[7] = 'right';

// Step 4: Use an array method to remove the first string of the array.
secretMessage.shift();

// Use an array method to add the string Programming to the beginning of the array.
secretMessage.unshift('Programming');

// Step 6: Use an array method to remove the strings get, right, the, first, time, , and replace them with the single string know,.
// First, find the indices of the words to remove
let startIndex = secretMessage.indexOf('get');
let endIndex = secretMessage.indexOf('time,') + 1;
secretMessage.splice(startIndex, endIndex - startIndex, 'know,');

// Step 7: On one line, use console.log() and join() to print the secret message as a sentence.
console.log(secretMessage.join(' '));

