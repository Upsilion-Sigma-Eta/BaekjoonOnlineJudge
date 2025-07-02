def Main():
    vertical_count, edge_count = map(int, input().split(' '));

    vertical_edge_count_list = list(0 for i in range(vertical_count));

    parent = list(range(vertical_count))

    def Find(x):
        if parent[x] != x:
            parent[x] = Find(parent[x]);
        return parent[x]

    def Union(a, b):
        parent_of_a, parent_of_b = Find(a), Find(b);
        if parent_of_a != parent_of_b:
            parent[parent_of_b] = parent_of_a;
    
    for i in range(edge_count):
        vertical_1, vertical_2 = map(int, input().split(' '));

        vertical_edge_count_list[vertical_1 - 1] += 1;
        vertical_edge_count_list[vertical_2 - 1] += 1;
    
        Union(vertical_1 - 1, vertical_2 - 1);

    odd_count = sum(1 for cnt in vertical_edge_count_list if cnt % 2 != 0);

    start = next(i for i, cnt in enumerate(vertical_edge_count_list))
    root = Find(start)
    for i, cnt in enumerate(vertical_edge_count_list):
        if cnt > 0 and Find(i) != root:
            print("NO")
            return;

    if (odd_count == 0 or odd_count == 2):
        print("YES");
    else:
        print("NO");

Main();