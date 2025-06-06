my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def print_recursively(seq, idx=0):
  
    if idx == len(seq):           
        print("Конец списка")
        return
    print(seq[idx])                
    print_recursively(seq, idx+1)  

if __name__ == '__main__':
    print_recursively(my_list)
