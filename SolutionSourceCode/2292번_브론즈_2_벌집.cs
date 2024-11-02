using System;
using System.Collections.Generic;

namespace CodingTest
{
    public class Program
    {
        public static void Main()
        {
            int N = int.Parse(Console.ReadLine());

            if (N == 1)
            {
                Console.WriteLine("1");
                return;
            }

            int room_outside_count = 6;
            int max_room_number = 2;
            int passing_room_counter = 1;
            while (max_room_number <= N)
            {
                max_room_number += room_outside_count * passing_room_counter;
                passing_room_counter++;
            }

            Console.WriteLine(passing_room_counter);
        }
    }
}
