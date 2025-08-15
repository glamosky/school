using System;

namespace GaussianElimination
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== Gaussian Elimination Calculator ===");
            Console.WriteLine("This program solves systems of linear equations");
            
            // get the size of the system (number of equations)
            Console.Write("Enter number of equations (2 or 3): ");
            string sizeInput = Console.ReadLine();
            int size = 0;
            
            // convert input to number
            if (sizeInput == "2")
                size = 2;
            else if (sizeInput == "3")
                size = 3;
            else
            {
                Console.WriteLine("Only 2x2 and 3x3 systems supported!");
                return;
            }
            
            // create arrays to store the augmented matrix
            double[,] matrix = new double[size, size + 1];
            
            // get coefficients from user
            Console.WriteLine("\nEnter the coefficients:");
            for (int i = 0; i < size; i++)
            {
                Console.WriteLine($"\nEquation {i + 1}:");
                for (int j = 0; j < size; j++)
                {
                    Console.Write($"Coefficient of x{j + 1}: ");
                    string input = Console.ReadLine();
                    matrix[i, j] = ConvertToDouble(input);
                }
                Console.Write("Constant term: ");
                string constInput = Console.ReadLine();
                matrix[i, size] = ConvertToDouble(constInput);
            }
            
            // display the original system
            Console.WriteLine("\n=== Original System ===");
            DisplaySystem(matrix, size);
            
            // perform Gaussian elimination
            bool success = GaussianEliminate(matrix, size);
            
            if (success)
            {
                // back substitution to find solutions
                double[] solutions = BackSubstitute(matrix, size);
                
                // display results
                Console.WriteLine("\n=== Solution ===");
                for (int i = 0; i < size; i++)
                {
                    Console.WriteLine($"x{i + 1} = {solutions[i]:F2}");
                }
            }
            else
            {
                Console.WriteLine("\nNo unique solution exists!");
            }
        }
        
        // convert string input to double
        static double ConvertToDouble(string input)
        {
            double result = 0;
            if (input == "")
                result = 0;
            else
            {
                // simple conversion - in real programs you'd use double.TryParse()
                if (input.Contains("."))
                {
                    // handle decimal numbers
                    string[] parts = input.Split('.');
                    int whole = 0;
                    int decimal_part = 0;
                    
                    if (parts[0] != "")
                        whole = Convert.ToInt32(parts[0]);
                    if (parts.Length > 1 && parts[1] != "")
                        decimal_part = Convert.ToInt32(parts[1]);
                    
                    result = whole + (decimal_part / 100.0);
                }
                else
                {
                    result = Convert.ToInt32(input);
                }
            }
            return result;
        }
        
        // display the system of equations
        static void DisplaySystem(double[,] matrix, int size)
        {
            for (int i = 0; i < size; i++)
            {
                Console.Write("Equation " + (i + 1) + ": ");
                for (int j = 0; j < size; j++)
                {
                    if (j > 0 && matrix[i, j] >= 0)
                        Console.Write("+ ");
                    Console.Write(matrix[i, j] + "x" + (j + 1) + " ");
                }
                Console.WriteLine("= " + matrix[i, size]);
            }
        }
        
        // perform Gaussian elimination
        static bool GaussianEliminate(double[,] matrix, int size)
        {
            // Forward elimination
            for (int i = 0; i < size; i++)
            {
                // find pivot (largest element in current column)
                int maxRow = i;
                for (int k = i + 1; k < size; k++)
                {
                    if (Math.Abs(matrix[k, i]) > Math.Abs(matrix[maxRow, i]))
                    {
                        maxRow = k;
                    }
                }
                
                // swap rows if necessary
                if (maxRow != i)
                {
                    for (int j = 0; j <= size; j++)
                    {
                        double temp = matrix[i, j];
                        matrix[i, j] = matrix[maxRow, j];
                        matrix[maxRow, j] = temp;
                    }
                }
                
                // check if pivot is zero (singular matrix)
                if (Math.Abs(matrix[i, i]) < 0.0001)
                {
                    return false; // No unique solution
                }
                
                // eliminate column below pivot
                for (int k = i + 1; k < size; k++)
                {
                    double factor = matrix[k, i] / matrix[i, i];
                    for (int j = i; j <= size; j++)
                    {
                        matrix[k, j] = matrix[k, j] - factor * matrix[i, j];
                    }
                }
            }
            
            return true;
        }
        
        // back substitution to find solutions
        static double[] BackSubstitute(double[,] matrix, int size)
        {
            double[] solutions = new double[size];
            
            // start from the last equation
            for (int i = size - 1; i >= 0; i--)
            {
                double sum = 0;
                for (int j = i + 1; j < size; j++)
                {
                    sum = sum + matrix[i, j] * solutions[j];
                }
                solutions[i] = (matrix[i, size] - sum) / matrix[i, i];
            }
            
            return solutions;
        }
        
        // method to check if a number is close to zero
        static bool IsZero(double number)
        {
            return Math.Abs(number) < 0.0001;
        }
        
        // method to display the matrix (for debugging)
        static void DisplayMatrix(double[,] matrix, int size)
        {
            Console.WriteLine("\n=== Matrix ===");
            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j <= size; j++)
                {
                    Console.Write(matrix[i, j] + " ");
                }
                Console.WriteLine();

                
                /* THIS IS SO DIFFICULT */
            }
        }
    }
}
