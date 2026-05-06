func hasDuplicate(nums []int) bool {
    seen := make(map[int]bool)

    for _, x := range nums{
        if seen[x] {
            return true
        }
        seen[x] = true
    }
    return false
}
