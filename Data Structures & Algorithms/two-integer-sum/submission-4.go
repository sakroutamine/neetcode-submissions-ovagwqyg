func twoSum(nums []int, target int) []int {
    dic := make(map[int]int)

    for i,x := range nums{
        if _, ok := dic[target-x]; ok {
            return []int{dic[target-x], i}
        }
        dic[x] = i
    }
    return []int{}
}