# python3
# Mareks Siņica-Siņavskis 221RDB430

def parallel_processing(n, m, data):
    output = []
    queue = list(range(n))
    time = [0] * n

    for i in range(m):
        if not queue:
            min_start_time = min(time)
            for j in range(n):
                if time[j] == min_start_time:
                    index = j
                    break
        else:
            index = queue.pop(0)

        start_time = time[index]
        output.append((index, start_time))

        time[index] += data[i]

        if time[index] != 0:
            queue.append(index)
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for index, start_time in result:
        print(index, start_time)

if __name__ == "__main__":
    main()
