// Activity 3

const userName = "Frank";
const userQuestion = "Why do I always feel so sleepy?";

if (userName) {
  console.log(`Hello, ${userName}!`)    // name exists
} else {
 console.log("Hello!");     // no name entered
}

console.log(`${userName} asks, "${userQuestion}"`);

const random = Math.floor(Math.random() * 8);

switch (random) { 
  case 0:
    console.log("The eight ball says: You debug more than you code.");
    break;
  case 1:
    console.log("The eight ball says: You're the reason linters cry.");
    break;
  case 2:
    console.log("The eight ball says: You commit to main like you commit to bad decisions.");
    break;
  case 3:
    console.log("The eight ball says: Your logic is as broken as your sleep schedule.");
    break;
  case 4:
    console.log("The eight ball says: Stack Overflow can’t save you now.");
    break;
  case 5:
    console.log("The eight ball says: You write spaghetti code... and forget the sauce.");
    break;
  case 6:
    console.log("The eight ball says: Recruiters read your resume for comic relief.");
    break;
  case 7:
    console.log("The eight ball says: You might be jobless, but at least you're self-aware.");
    break;
}
