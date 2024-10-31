using System;
using System.Collections.Generic;

namespace CodingTest
{
    public enum Color
    {
        White = 0,
        Red = 1,
        Blue = 2,
    }

    public enum Direction
    {
        Right = 1,
        Left = 2,
        Up = 3,
        Down = 4,
    }

    public class Piece
    {
        public int X { get; set; }
        public int Y { get; set; }
        public Direction Dir { get; set; }

        public Piece(int x, int y, Direction dir)
        {
            X = x;
            Y = y;
            Dir = dir;
        }
    }

    public class Cell
    {
        public Color CellColor { get; set; }
        public List<int> PieceIndices { get; set; } = new List<int>();
    }

    public class Board
    {
        public Cell[][] Grid { get; set; }
        public int Width { get; set; }
        public int Height { get; set; }

        public Board(int width, int height)
        {
            Width = width;
            Height = height;
            Grid = new Cell[width][];
            for (int i = 0; i < width; i++)
            {
                Grid[i] = new Cell[height];
                for (int j = 0; j < height; j++)
                {
                    Grid[i][j] = new Cell();
                }
            }
        }
    }

    public class Program
    {
        static readonly Dictionary<Direction, (int dx, int dy)> directions = new()
        {
            { Direction.Right, (0, 1) },
            { Direction.Left, (0, -1) },
            { Direction.Up, (-1, 0) },
            { Direction.Down, (1, 0) }
        };

        public static void Main()
        {
            var input = Console.ReadLine().Split();
            int N = int.Parse(input[0]);
            int K = int.Parse(input[1]);

            Board board = new Board(N, N);
            List<Piece> pieces = new List<Piece>();

            for (int i = 0; i < N; i++)
            {
                input = Console.ReadLine().Split();
                for (int j = 0; j < N; j++)
                {
                    board.Grid[i][j].CellColor = (Color)int.Parse(input[j]);
                }
            }

            for (int i = 0; i < K; i++)
            {
                input = Console.ReadLine().Split();
                int x = int.Parse(input[0]) - 1;
                int y = int.Parse(input[1]) - 1;
                Direction dir = (Direction)int.Parse(input[2]);

                Piece piece = new Piece(x, y, dir);
                pieces.Add(piece);
                board.Grid[x][y].PieceIndices.Add(i);
            }

            int turn = 0;
            while (turn <= 1000)
            {
                turn++;
                for (int i = 0; i < K; i++)
                {
                    if (IsBottomPiece(pieces[i], board, pieces) && MovePiece(pieces, i, board, N))
                    {
                        Console.WriteLine(turn);
                        return;
                    }
                }
            }

            Console.WriteLine(-1);
        }

        public static bool MovePiece(List<Piece> pieces, int pieceIndex, Board board, int N)
        {
            Piece piece = pieces[pieceIndex];
            List<int> currentStack = board.Grid[piece.X][piece.Y].PieceIndices;
            int stackIndex = currentStack.IndexOf(pieceIndex);

            // 현재 위치의 위에 있는 모든 말들을 이동 대상으로 추적
            List<int> movingPieces = currentStack.GetRange(stackIndex, currentStack.Count - stackIndex);
            currentStack.RemoveRange(stackIndex, currentStack.Count - stackIndex);

            // 이동할 위치 결정
            var (dx, dy) = directions[piece.Dir];
            int nx = piece.X + dx;
            int ny = piece.Y + dy;

            // 파란색이거나 범위 밖인 경우 방향 반대
            if (!IsInBounds(nx, ny, N) || board.Grid[nx][ny].CellColor == Color.Blue)
            {
                piece.Dir = ReverseDirection(piece.Dir);
                (dx, dy) = directions[piece.Dir];
                nx = piece.X + dx;
                ny = piece.Y + dy;
                if (!IsInBounds(nx, ny, N) || board.Grid[nx][ny].CellColor == Color.Blue)
                {
                    // 파란색 방향을 반대로 바꿔도 파란색이거나 경계 밖이라면 이동하지 않음
                    board.Grid[piece.X][piece.Y].PieceIndices.AddRange(movingPieces);
                    return false;
                }
            }

            // 빨간색 칸인 경우 이동하는 말의 순서 뒤집기
            if (board.Grid[nx][ny].CellColor == Color.Red)
            {
                movingPieces.Reverse();
            }

            // 이동 및 위치 갱신
            foreach (int movingPieceIndex in movingPieces)
            {
                pieces[movingPieceIndex].X = nx;
                pieces[movingPieceIndex].Y = ny;
                board.Grid[nx][ny].PieceIndices.Add(movingPieceIndex);
            }

            // 종료 조건: 말이 4개 이상 쌓이면 종료
            return board.Grid[nx][ny].PieceIndices.Count >= 4;
        }

        // 해당 말이 맨 아래에 있는지 확인
        public static bool IsBottomPiece(Piece piece, Board board, List<Piece> pieces)
        {
            return board.Grid[piece.X][piece.Y].PieceIndices[0] == pieces.IndexOf(piece);
        }

        public static bool IsInBounds(int x, int y, int N)
        {
            return x >= 0 && x < N && y >= 0 && y < N;
        }

        public static Direction ReverseDirection(Direction dir)
        {
            return dir switch
            {
                Direction.Right => Direction.Left,
                Direction.Left => Direction.Right,
                Direction.Up => Direction.Down,
                Direction.Down => Direction.Up,
                _ => dir
            };
        }
    }
}
