def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[1])

    count_removed = 0
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start < prev_end:   
            count_removed += 1
        else:                    
            prev_end = end
    return count_removed

print(erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]))
print(erase_overlap_intervals([[1,2],[1,2],[1,2]]))
print(erase_overlap_intervals([[1,2],[2,3]]))