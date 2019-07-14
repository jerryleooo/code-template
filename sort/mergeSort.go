package main

import "fmt"

func mergeSort(A []int, left int, right int, tmp []int) {
    if right - left <= 0 {
        return
    } else {
        mid := (right - left) / 2 + left
        mergeSort(A, left, mid, tmp)
        mergeSort(A, mid + 1, right, tmp)
        merge(A, left, mid, right, tmp)
    }
}

func merge(A []int, left, mid, right int, tmp []int) int {
    sum := 0
    i, j, k := left, mid + 1, 0
    
    for i <= mid && j <= right {
        if A[i] < A[j] {
            tmp[k] = A[i]
            i += 1
        } else {
            sum += mid - i + 1
            tmp[k] = A[j]
            j += 1
        }
        k ++
    }
    
    for i <= mid {
        tmp[k] = A[i]
        k ++
        i ++
    }
    
    for j <= right {
        tmp[k] = A[j]
        k ++
        j ++
    }
    
    for i := 0; left + i <= right; i ++ {
        A[left + i] = tmp[i]
    }
    
    return sum
}

func main() {
	A := []int{1, 3, 5, 2, 4, 6, 7}
	tmp := make([]int, len(A)) // NOTE: use only one tmp array to save memory
	mergeSort(A, 0, len(A) - 1, tmp)
	fmt.Println(A)
}