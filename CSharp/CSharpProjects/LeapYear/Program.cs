using System;

namespace MyApp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter year here: ");
            string inputline = Console.ReadLine();
            int myVar = int.Parse(inputline);
            Console.WriteLine("User has entered year " + inputline);

            if (myVar % 4 == 0 && myVar % 100 == 0 && myVar % 400 == 0)
            {
                Console.WriteLine("The year you entered IS A LEAP YEAR");
            }

            else if (myVar % 4 == 0 && myVar % 100 == 0)
            {
                Console.WriteLine("NOT A LEAP YEAR");
            }
            else if (myVar % 4 == 0)
            {
                Console.WriteLine("The year you entered IS A LEAP YEAR");
            }

            else
            {
                Console.WriteLine("NOT A LEAP YEAR");
            }
        }
    }
}