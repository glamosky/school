// Activity 4

// change values of age and isEarlyRegistered for testing
const age = 19;             // could be any number
const isEarlyRegistered = true;   // true or false
let raceNumber = Math.floor(Math.random() * 1000);
const youthRaceNumber = Math.abs(raceNumber - 1000);

if (age > 18 && isEarlyRegistered) {
    console.log(`Runner ${raceNumber += 1000}, your race will start at 9:30 AM.`); 
} 
else if (age > 18 && !isEarlyRegistered) {
    console.log(`Runner ${raceNumber += 1000}, your race will start at 11:00 AM. Late adults run at 11:00 AM.`);
}
else if (age < 18) {
    console.log(`Runner ${youthRaceNumber}, your race will start at 12:30 PM. Youth runners start at 12:30 PM (regardless of registration).`);
}
else if (age === 18) {
    console.log("Please see the registration desk.");
}

//alternate
// const adult = age > 18;
// const youth = age <= 18;

// if (adult) {
//     if (isEarlyRegistered) {
//         console.log(`Runner ${raceNumber += 1000}, your race will start at 9:30 AM.`);
//     }
//     else if (!isEarlyRegistered) {
//         console.log(`Runner ${raceNumber += 1000}, your race will start at 11:00 AM. Late adults run at 11:00 AM.`);
//     }
// }
// else if (youth) {
//     if (age < 18) {
//         console.log(`Runner ${youthRaceNumber}, your race will start at 12:30 PM. Youth runners start at 12:30 PM (regardless of registration).`);
//     }
//     else if (age === 18) {
//         console.log("Please see the registration desk.");
//     }
// }