using System;
using System.Collections.Generic;
using System.Linq;


namespace CodingTest
{
    public class UnionFind
    {
        private List<int> parent= new List<int>();
        private List<int> rank = new List<int>();

        public UnionFind(int n)
        {
            for (int i = 0; i < n; ++i)
            {
                parent.Add(i);
                rank.Add(0);
            }
        }

        // 경로 압축을 통해서 최상위 부모 원소 찾기
        public int Find(int node)
        {
            // 경로 압축
            if (parent[node] != node)
            {
                parent[node] = Find(parent[node]);
            }

            return parent[node];
        }
        
        // 합집합 연산 : 두 집합을 합치기
        public void Union(int node_1, int node_2)
        {
            int rootX = Find(node_1);
            int rootY = Find(node_2);

            if (rootX != rootY)
            {
                // 두 집합 중에서 더 높이가 낮은 쪽을 높은 트리의 아래에 붙임
                if (rank[rootX] > rank[rootY])
                {
                    parent[rootY] = rootX;
                }
                else if (rank[rootX] < rank[rootY])
                {
                    parent[rootX] = rootY;
                }
                else
                {
                    parent[rootY] = rootX;
                    rank[rootX]++;
                }
            }
        }

        public bool IsConnected(int node_1, int node_2)
        {
            // 두 집합의 부모 원소가 동일한지 == 서로 연결되어 있는지를 확인함.
            return Find(node_1) == Find(node_2);
        }
    }

    class Edge
    {
        private int u = -1;
        private int v = -1;
        private int cost = -1;

        public int U
        {
            get
            {
                return u;
            }
        }

        public int V
        {
            get
            {
                return v;
            }
        }

        public int Cost
        {
            get
            {
                return cost;
            }
        }
        
        
        public Edge(int u, int v, int cost)
        {
            this.u = u;
            this.v = v;
            this.cost = cost;
        }
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            StreamReader input = new StreamReader(Console.OpenStandardInput());

            int N = 0;
            int K = 0;

            string[] line = new string[3];
            line = input.ReadLine().Split(" ");

            N = int.Parse(line[0]);
            K = int.Parse(line[1]);

            UnionFind unionFind = new UnionFind(N);
            
            // 인접 그래프 생성
            List<Edge> graph = new List<Edge>(N);
            
            for (int i = 0; i < K; ++i)
            {
                line = input.ReadLine().Split(" ");
                
                int u, v, cost;
                u = int.Parse(line[0]);
                v = int.Parse(line[1]);
                cost = int.Parse(line[2]);

                graph.Add(new Edge(u, v, cost));
            }
            
            // 크루스칼 알고리즘 사용을 위한 사전 준비 작업
            graph.Sort(delegate(Edge e1, Edge e2)
            {
                if (e1.Cost < e2.Cost)
                {
                    return -1;
                }
                else if (e1.Cost == e2.Cost)
                {
                    return 0;
                }
                else
                {
                    return 1;
                }
            });

            List<Edge> MST = new List<Edge>();
            
            // 크루스칼 알고리즘 구현
            for (int edge_index = 0; edge_index < K; ++edge_index)
            {
                if (MST.Count == N - 1)
                {
                    break;
                }
                
                if (!unionFind.IsConnected(graph[edge_index].U, graph[edge_index].V))
                {
                    MST.Add(graph[edge_index]);
                    unionFind.Union(graph[edge_index].U, graph[edge_index].V);
                }
            }

            long sum = MST.Sum(delegate(Edge e)
            {
                return e.Cost;
            });
            
            Console.WriteLine(sum);

            // 가장 멀리 떨어져있는 노드 탐색
            Dictionary<int, bool> visited = new Dictionary<int, bool>();
            for (int i = 0; i < N; ++i)
            {
                visited.Add(i, false);
            }

            int far_node = -1;
            far_node = DFS(MST, 0, -1, ref visited, 0).Item1;
            
            // 가장 멀리 떨어져 있는 노드로부터 최대 거리 탐색
            for (int i = 0; i < N; ++i)
            {
                visited[i] = false;
            }

            long max_distance = -1;
            max_distance = DFS(MST, far_node, -1, ref visited, 0).Item2;

            Console.WriteLine(max_distance);
        }

        private static Tuple<int, int> DFS(List<Edge> graph, int current, int parent, ref Dictionary<int, bool> visited, int current_cost)
        {
            visited[current] = true;
            int max_distance = current_cost;
            int far_node = current;

            foreach (var edge in graph)
            {
                int next = -1;
                if (edge.U == current && !visited[edge.V])
                {
                    next = edge.V;
                }
                else if (edge.V == current && !visited[edge.U])
                {
                    next = edge.U;
                }

                if (next != -1 && next != parent)
                {
                    Tuple<int, int> node_and_dist = DFS(graph, next, current, ref visited, current_cost + edge.Cost);

                    if (node_and_dist.Item2 > max_distance)
                    {
                        max_distance = node_and_dist.Item2;
                        far_node = node_and_dist.Item1;
                    }
                }
            }
            
            return new Tuple<int, int>(far_node, max_distance);
        }
    }
}
