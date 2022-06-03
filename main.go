package main

import (
	"fmt"
	"strconv"
)

func task() string {
	var n int
	fmt.Scanln(&n)
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}
	if n == 1 {
		return "0"
	}
	var counter int
	k := 0
	offset := 0
	for true {
		for arr[k] == arr[0] {
			k += 1
			if k == n {
				return strconv.Itoa(counter)
			}
			if arr[k] < arr[k-1] {
				return "-1"
			}
		}
		counter += arr[k] - arr[k-1]
		for i := offset; i < k; i++ {
			arr[i] = arr[k]
		}
		offset = k - 1
	}
	return ""
}

func main() {
	fmt.Println(task())
}
