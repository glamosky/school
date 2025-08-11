using System;

namespace PalindromeChecker
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("«Palindrome Checker»");
            Console.WriteLine("Enter a word to check if it's a palindrome:");
            
            while (true)
            {
                Console.Write("\nEnter word (or 'quit' to exit): ");
                string input = Console.ReadLine();
                
                // check if user wants to quit
                if (input == "quit" || input == "QUIT")
                {
                    Console.WriteLine("Goodbye!");
                    break;
                }
                
                // check if input is empty
                if (input == "" || input == null)
                {
                    Console.WriteLine("Please enter a valid word!");
                    continue;
                }
                
                // check if it's a palindrome
                bool isPalindrome = CheckPalindrome(input);
                
                if (isPalindrome)
                {
                    Console.WriteLine("YES! '" + input + "' is a palindrome!");
                }
                else
                {
                    Console.WriteLine("NO! '" + input + "' is NOT a palindrome.");
                }
                
                // show the reversed word
                string reversed = ReverseWord(input);
                Console.WriteLine("Reversed: '" + reversed + "'");
            }
        }
        
        // check if a word is a palindrome
        static bool CheckPalindrome(string word)
        {
            // convert to lowercase for comparison
            string lowerWord = word.ToLower();
            
            // get the length of the word
            int length = lowerWord.Length;
            
            // check each character from start and end
            for (int i = 0; i < length / 2; i++)
            {
                // compare characters from start and end
                if (lowerWord[i] != lowerWord[length - 1 - i])
                {
                    return false;
                }
            }
            
            return true;
        }
        
        // reverse a word using arrays
        static string ReverseWord(string word)
        {
            // convert string to character array
            char[] charArray = new char[word.Length];
            
            // copy characters to array
            for (int i = 0; i < word.Length; i++)
            {
                charArray[i] = word[i];
            }
            
            // reverse the array
            for (int i = 0; i < charArray.Length / 2; i++)
            {
                // swap characters
                char temp = charArray[i];
                charArray[i] = charArray[charArray.Length - 1 - i];
                charArray[charArray.Length - 1 - i] = temp;
            }
            
            // convert back to string
            string reversed = "";
            for (int i = 0; i < charArray.Length; i++)
            {
                reversed = reversed + charArray[i];
            }
            
            return reversed;
        }
        
        // alternative method using while loop
        static bool CheckPalindromeWhile(string word)
        {
            string lowerWord = word.ToLower();
            int left = 0;
            int right = lowerWord.Length - 1;
            
            while (left < right)
            {
                if (lowerWord[left] != lowerWord[right])
                {
                    return false;
                }
                left++;
                right--;
            }
            
            return true;
        }
        
        // count vowels in a word 
        static int CountVowels(string word)
        {
            int count = 0;
            string lowerWord = word.ToLower();
            
            for (int i = 0; i < lowerWord.Length; i++)
            {
                char c = lowerWord[i];
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
                {
                    count++;
                }
            }
            
            return count;
        }
    }
}
