using System;
using System.Collections.Generic;
using System.IO;

class Program
{
    static void Main()
    {
        StreamReader reader = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
        StreamWriter writer = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
        string[] input = reader.ReadLine().Split(' ');
        long v = long.Parse(input[0]);
        long k = long.Parse(input[1]);

        List<long> votes = new List<long>();
        long currentVote = v;

        while (currentVote > 0)
        {
            // Add k values
            for (long i = 0; i < k; i++)
            {
                if (currentVote > 0)
                {
                    votes.Add(currentVote);
                    currentVote -= 1;
                }
            }

            // Skip next k values
            currentVote -= k;
        }

        writer.WriteLine(votes.Count.ToString());
        foreach (long vote in votes)
        {
            writer.WriteLine(vote.ToString());
        }

        reader.Close();
        writer.Close();
    }
}