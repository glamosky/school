// Import built-in libraries
using System;
using System.Globalization; // For CultureInfo

// Namespace groups related classes
namespace FrankFirstProject
{
    // PascalCase for class names
    class Program
    {
        // Entry point — program starts here
        static void Main()
        {
            Console.WriteLine("👋 Welcome to Frank's C# Demo!");
            Console.WriteLine("-------------------------------");

            // camelCase for variables
            string userName = GetUserName();
            int userAge = GetUserAge();

            Console.WriteLine($"\nHello {userName}! You are {userAge} years old.");

            // Example of arithmetic + relational + conditional
            int yearsUntilRetirement = 60 - userAge;

            string message = (userAge < 60) 
                ? $"⏳ You have {yearsUntilRetirement} years left until retirement." 
                : "🎉 You're already at retirement age or beyond!";
            Console.WriteLine(message);

            // Logical operator example
            if (userAge >= 18 && userAge < 60)
            {
                Console.WriteLine("✅ You're an adult and not yet retired.");
            }

            // Convert.ToInt32 vs int.Parse
            Console.Write("\nEnter your favorite number: ");
            string favoriteInput = Console.ReadLine();

            int favoriteNumber = Convert.ToInt32(favoriteInput); // Safer than int.Parse
            Console.WriteLine($"Your favorite number multiplied by 5 is: {favoriteNumber * 5}");

            // Formatting with CultureInfo.InvariantCulture
            double pi = 3.14159;
            string formattedPi = pi.ToString(CultureInfo.InvariantCulture);
            Console.WriteLine($"Formatted Pi (InvariantCulture): {formattedPi}");

            Console.WriteLine("\n🎉 Thanks for trying out C#! See ya!");
        }

        // A reusable method (PascalCase name)
        static string GetUserName()
        {
            Console.Write("What's your name? ");
            return Console.ReadLine();
        }

        // Another reusable method
        static int GetUserAge()
        {
            Console.Write("How old are you? ");
            // int.Parse will crash on invalid input, Convert is safer
            return Convert.ToInt32(Console.ReadLine());
        }
    }
}
