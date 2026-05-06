func hasDuplicate(nums []int) bool {
    dic := make(map[int]bool)

    for _, x := range nums {
        // fmt.Println(x)
        if dic[x] {
            return true
        }
        dic[x] = true
    }

    return false
}
