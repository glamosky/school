using System;

class Program
{
    static void Main()
    {
        // I will *NEVER* conform to American Imperialist MM-DD.
        Console.Write("Enter your birthday date STRICTLY in (dd-mm) format: ");
        string input = Console.ReadLine();

        // Parse the input string into a DateTime object using the dd-MM format for strict validation
        DateTime BirthdayDate = DateTime.ParseExact(input, "dd-MM", null);

        // Get today's date (without time component) for comparison
        DateTime today = DateTime.Today;

        // Calculate the difference between birthday and today
        // Positive days = birthday is in the future
        // Negative days = birthday has already passed
        // Zero days = birthday is today
        TimeSpan difference = BirthdayDate - today;

        // Decision logic based on the calculated difference:
        // Check if birthday is more than 1 day in the future
        if (difference.Days > 1)
        {
            Console.WriteLine($"Your birthday is yet to come. It's {difference.Days} days to go until your birthday.");
        }
        // Check if birthday is exactly 1 day away (tomorrow)
        else if (difference.Days == 1)
        {
            Console.WriteLine("Tomorrow's your birthday! Don't you remember?");
        }
        // Check if birthday is today (difference is exactly 0 days)
        else if (difference.Days == 0)
        {
            Console.WriteLine("Today is your birthday. Happy Birthday! 🥳");
        }
        // If none of the above, birthday has already passed (negative difference)
        // Use Math.Abs() to convert negative days to positive for display
        else
        {
            Console.WriteLine($"Your birthday has already passed. It has been {Math.Abs(difference.Days)} days since your birthday.");
        }
        // Provide audio feedback to signal the program has completed its calculation
        Console.Beep(800, 500);
    }
}