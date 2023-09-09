from Class_utils import utils

if __name__ == "__main__":
    utils.reversed(1234)
    utils.reversed(-5678)
    utils.reversed(1)
    utils.reversed(10)
    utils.reversed(0.01) #Should fail
    utils.reversed("String 1") #Should fail
    
    utils.formatter(1)
    utils.formatter(10)
    utils.formatter(4567)
    utils.formatter(-100)
    utils.formatter(0.02) #Should fail
    utils.formatter("String 2") #Should fail