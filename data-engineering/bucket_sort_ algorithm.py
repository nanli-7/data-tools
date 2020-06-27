def bucket_sort(input_list):
    # Find maximum value in the list and use length of the list to 
    # determine which value in the list goes into which bucket 
    max_value = max(input_list)
    size = max_value / len(input_list)

    # Create n empty buckets where n is equal to the length of the input list
    bucket_list = []
    for i in range(len(input_list)):
        bucket_list.append([])

    # Put list elements into different buckets based on the size
    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            bucket_list[j].append(input_list[i])
        else:
            bucket_list[len(input_list)-1].append(input_list[i])
    
    # Sort elements within the buckets using Insertion Sort
    for i in range(len(input_list)):
        insertion_sort(bucket_list[i])
    
    # Concatenate buckets with sorted elements into a single list
    result_list = []
    for i in range(len(input_list)):
        result_list = result_list + bucket_list[i]
    
    return result_list

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        var = bucket[i]
        j = i - 1
        while(j>=0 and var<bucket[j]):
            bucket[j+1] = bucket[j]
            j = j-1
        bucket[j+1] = var


if __name__ == "__main__":
    input_list = [1.20, 0.22, 0.43, 0.36,0.39,0.27]
    print('ORIGINAL LIST:')
    print(input_list)
    sorted_list = bucket_sort(input_list)
    print('SORTED LIST:')
    print(sorted_list)
