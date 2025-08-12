using System;

namespace MyApp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter year here: ");
            string inputLine = Console.ReadLine();
            
            if (int.TryParse(inputLine, out int year))
            {
                Console.WriteLine($"User has entered year {year}");
                
                if (IsLeapYear(year))
                {
                    Console.WriteLine("The year you entered IS A LEAP YEAR");
                }
                else
                {
                    Console.WriteLine("NOT A LEAP YEAR");
                }
            }
            else
            {
                Console.WriteLine("Invalid input. Please enter a valid year.");
            }
        }
        
        static bool IsLeapYear(int year)
        {
            // Leap year rules:
            // 1. If divisible by 400, it's a leap year
            // 2. If divisible by 100 but not 400, it's NOT a leap year
            // 3. If divisible by 4 but not 100, it's a leap year
            // 4. Otherwise, it's NOT a leap year
            
            if (year % 400 == 0)
                return true;
            if (year % 100 == 0)
                return false;
            if (year % 4 == 0)
                return true;
            return false;
        }
    }
}