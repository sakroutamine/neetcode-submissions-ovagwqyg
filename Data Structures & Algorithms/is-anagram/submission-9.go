func isAnagram(s string, t string) bool {
    if len(s) != len(t){
        return false
    }
    s1 := make(map[rune]int)
    t1 := make(map[rune]int)

    for _, c := range s {
        s1[c]++
    }

    for _, c := range t {
        t1[c]++
    }

    for t, _ := range s1 {
        if s1[t] != t1[t]{
            return false
        }
    }

    return true

}
