using System.Drawing;

public partial class Program
{
    public static double GetDistance(Point a, Point b)
    {
        return (Math.Sqrt(Math.Pow(Math.Abs(a.X - b.X), 2) + Math.Pow(Math.Abs(a.Y - b.Y), 2)));
    }

    public static string ActualProcess()
    {
        Point yumiPoint = new Point(0, 0);
        List<Point> points = new List<Point>();

        string? yumiPointStr = Console.ReadLine();

        if (yumiPointStr != null)
        {
            yumiPoint = new Point(int.Parse(yumiPointStr.Split(' ')[0]), int.Parse(yumiPointStr.Split(' ')[1]));
        }

        for (int i = 0; i < 3; ++i)
        {
            string? pointStr = Console.ReadLine();

            if (pointStr != null)
            {
                points.Add(new Point(int.Parse(pointStr.Split(' ')[0]), int.Parse(pointStr.Split(' ')[1])));
            }
        }

        List<int> distances = new List<int>();

        int[][] testIndex = new int[6][];
        
        testIndex[0] = new int[] { 0, 1, 2 };
        testIndex[1] = new int[] { 0, 2, 1 };
        testIndex[2] = new int[] { 1, 0, 2 };
        testIndex[3] = new int[] { 1, 2, 0 };
        testIndex[4] = new int[] { 2, 0, 1 };
        testIndex[5] = new int[] { 2, 1, 0 };

        foreach (int[] testCase in testIndex)
        {
            Point yumiPointTemp = new Point(yumiPoint.X, yumiPoint.Y);
            double totalDistance = 0;

            totalDistance += GetDistance(yumiPointTemp, points[testCase[0]]);
            yumiPointTemp = points[testCase[0]];

            totalDistance += GetDistance(yumiPointTemp, points[testCase[1]]);
            yumiPointTemp = points[testCase[1]];

            totalDistance += GetDistance(yumiPointTemp, points[testCase[2]]);
            yumiPointTemp = points[testCase[2]];

            distances.Add((int)Math.Floor(totalDistance));
        }

        distances.Sort();

        Console.WriteLine(distances[0].ToString());

        return distances[0].ToString();
    }

    public static void Main()
    {
        ActualProcess();
    }
}
