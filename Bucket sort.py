def bucket_sort(arr):
    # Find the maximum value in the array
    max_value = max(arr)
    
    # Create empty buckets
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]
    
    # Assign elements to the appropriate bucket
    for num in arr:
        index = int(num * num_buckets / (max_value + 1))
        buckets[index].append(num)
    
    # Sort each bucket individually
    for bucket in buckets:
        bucket.sort()
    
    # Concatenate the sorted buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    
    return sorted_arr

# Example usage
arr = [0.42, 0.32, 0.67, 0.89, 0.11, 0.55, 0.23, 0.78, 0.99, 0.01]
sorted_arr = bucket_sort(arr)
print(sorted_arr)