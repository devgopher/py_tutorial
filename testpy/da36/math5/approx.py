class Result:
    def __init__(self):
        self.returned = 0.0
        self.function = "none"
    

def sqrt_approx(x,  cycles_cnt):
    ret = x / 2;
    for z in range(0, cycles_cnt):
        ret = (x + ret * ret)/(2*ret);
    
    result = Result();
    result.returned = ret;
    result.function = "sqrt_approx";
    
    return result;
