import multiprocessing

def calc_square(numbers, result):
    for idx, n in enumerate(numbers):
        result[idx] = n*n

if __name__ == "__main__":
    numbers = [2,3,5]
    result = multiprocessing.Array('i',3)
    p = multiprocessing.Process(target = calc_square, args=(numbers, result))
    p.start()
    p.join()
    print(result[:])
