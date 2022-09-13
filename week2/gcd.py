import gc


def naive_gcd(a, b):
    gcd_val = 0
    for i in range(1, a+b):
        if a%i == 0 and b%i == 0:
            gcd_val = i
    return gcd_val 

def opti_gcd(a, b):
    if b == 0:
        return a
    else:
        return opti_gcd(b, a%b) 
    
if __name__ == "__main__":
    input_string = input()
    a = int(input_string.split()[0])
    b = int(input_string.split()[1])
    if b < a: a, b = b, a  
    #print(naive_gcd(a,b), opti_gcd(a,b))
    print(opti_gcd(a,b))