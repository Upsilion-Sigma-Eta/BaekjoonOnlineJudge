using System;
using System.Collections.Generic;
using System.Linq;

namespace CodingTest
{
    public class Shape
    {
        private List<string> shapeGrid;
        private int shape_type = -1;

        public int Height { get; private set; }

        public int Width { get; private set; }

        public List<string> ShapeGrid
        {
            get
            {
                return shapeGrid;
            }
        }

        public int ShapeType
        {
            get
            {
                return shape_type;
            }
        }

        public int[] BoxOffset { get; private set; }

        public int[] BoxTop { get; private set; }

        public Shape(List<string> shapeLines, int type)
        {
            this.shapeGrid = shapeLines;
            this.shape_type = type;
            this.Height = shapeGrid.Count;
            this.Width = shapeGrid[0].Length;

            CalculateOffsets();
        }

        private void CalculateOffsets()
        {
            int w = this.Width;
            int h = this.Height;
            BoxOffset = new int[w];
            BoxTop = new int[w];

            for (int k = 0; k < w; k++)
            {
                // BoxOffset 계산: 각 열에서 아래부터 첫 번째 'X'까지의 빈 공간
                BoxOffset[k] = 0;
                for (int j = 0; j < h; j++)
                {
                    if (shapeGrid[j][k] == 'X')
                    {
                        break;
                    }
                    BoxOffset[k]++;
                }

                // BoxTop 계산: 각 열에서 위부터 첫 번째 'X'까지의 높이
                BoxTop[k] = h;
                for (int j = h - 1; j >= 0; j--)
                {
                    if (shapeGrid[j][k] == 'X')
                    {
                        break;
                    }
                    BoxTop[k]--;
                }
            }
        }
    }

    public class Box
    {
        private int width;
        private int height;
        private List<Shape> shapes;
        private int[] cols; // 각 열의 현재 높이

        public Box(int width, int height)
        {
            this.width = width;
            this.height = height;
            shapes = new List<Shape>();
            cols = new int[width];
        }

        public int CurrentHeight { get; private set; }

        public bool InsertShape(Shape shape)
        {
            int[] newCols = new int[width];
            int max = 0;

            for (int k = 0; k < width; k++)
            {
                newCols[k] = cols[k] + shape.BoxTop[k];
                if (newCols[k] > max)
                {
                    max = newCols[k];
                }
            }

            if (max > height)
            {
                return false; // 박스에 도형을 넣을 수 없음
            }
            else
            {
                // cols 업데이트
                for (int k = 0; k < width; k++)
                {
                    cols[k] = max - shape.BoxOffset[k];
                }
                shapes.Add(shape);
                CurrentHeight = max;
                return true;
            }
        }
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            int n, w, b;

            string[] tokens = Console.ReadLine().Split();
            n = int.Parse(tokens[0]);
            w = int.Parse(tokens[1]);
            b = int.Parse(tokens[2]);

            List<Shape> shapes = new List<Shape>();

            for (int i = 0; i < n; ++i)
            {
                int h = int.Parse(Console.ReadLine());

                List<string> shapeLines = new List<string>();
                for (int j = 0; j < h; ++j)
                {
                    shapeLines.Add(Console.ReadLine());
                }

                shapes.Add(new Shape(shapeLines, i));
            }

            List<Box> boxes = new List<Box>();
            boxes.Add(new Box(w, b));

            foreach (Shape shape in shapes)
            {
                if (!boxes.Last().InsertShape(shape))
                {
                    boxes.Add(new Box(w, b));
                    boxes.Last().InsertShape(shape);
                }
            }

            foreach (Box box in boxes)
            {
                Console.Write(box.CurrentHeight.ToString() + " ");
            }
        }
    }
}
