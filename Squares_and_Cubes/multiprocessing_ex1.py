import time
import multiprocessing

def calc_square(numbers):
    for n in numbers:
        print('square' + str(n*n*n))

def calc_cube(numbers):
    for n in numbers:
        print('cube' + str(n*n*n))

if __name__ == "__main__":
    t = time.time()
    arr = [2999999999999,999999999399,9999999999999,99999,19999999992,39994,39994,9923,1992,9923,999912,99923,1992,99912,9934,945,923,1992,234,9912,23,34,12,34,234,235,2663,2333,19999999992,19999999992,19999999992,19999999992,19999999992,19999999992,19999999992,19999999992,19999999992,19999999992,19999999992,19999999992,19999999992,19999999992,19999999992]
    p1 = multiprocessing.Process(target=calc_square,args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube,args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("time taken : ", time.time()-t)
    print("done!!")
