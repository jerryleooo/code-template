func find(x int, parent []int) int {
    // fmt.Println(parent[x], x)
    if parent[x] != x {
        parent[x] = find(parent[x], parent)
    }
    return parent[x]
}

func union(x, y int, parent []int, rank []int) {
    x, y = find(x, parent), find(y, parent)
    if rank[x] < rank[y] {
        parent[x] = y
    } else {
        parent[y] = x
        if rank[x] == rank[y] {
            rank[x] += 1
        }
    }
}

func findCircleNum(M [][]int) int {
    if len(M) == 0 {
        return 0
    }
    parent := []int{}
    rank := []int{}
    for i := 0; i < len(M); i ++ {
        parent = append(parent, i)
        rank = append(rank, 0)
    }

    for i := 0; i < len(M); i++ {
        for j := 0; j < i; j++ {
            if M[i][j] == 1 {
                union(i, j, parent, rank)
            }
        }
    }

    m := make(map[int]bool)
    count := 0

    for _, v := range parent {
        r := find(v, parent)
        if m[r] == false {
            count += 1
        }
        m[r] = true
    }

    return count
}
