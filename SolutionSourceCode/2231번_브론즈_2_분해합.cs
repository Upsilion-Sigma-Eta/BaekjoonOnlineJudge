using System;
using System.Collections.Generic;

namespace CodingTest
{
    public class Program
    {
        public static void Main()
        {
            int N = int.Parse(Console.ReadLine());

            int result = 0;
            for (int i = 0; i < N; ++i)
            {
                string number = i.ToString();

                int generator = i;

                foreach (char c in number)
                {
                    generator += int.Parse(c.ToString());
                }

                if (generator == N)
                {
                    result = i;
                    break;
                }
            }
            
            Console.WriteLine(result.ToString());
        }
    }
}
