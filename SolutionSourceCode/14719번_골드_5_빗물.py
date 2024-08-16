import sys

def Solution():
    H, W = map(int, sys.stdin.readline().strip().split())
    block_height_map = list(map(int, sys.stdin.readline().strip().split()))

    grid_map = [[0] * W for _ in range(H)]
    for i in range(W - 1, -1, -1):
        for j in range(block_height_map[i]):
            grid_map[j][i] = 1

    water_block_count = 0
    for i in range(H):
        string_height_info = "".join(map(str, grid_map[i]))
        left_index = string_height_info.find("1")
        right_index = string_height_info.rfind("1")

        if (left_index != -1) and (right_index != -1):
            water_block_count += right_index - left_index + 1
            water_block_count -= string_height_info.count("1")

    print(water_block_count)


if __name__ == "__main__":
    Solution()