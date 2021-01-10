from merry import Merry

merry = Merry()

class A():
    def __init__(self) :
        merry.setObject(self)

    @merry._try
    def func(self):
        raise IOError()
        # raise Exception('1')

    @merry._except(IOError)
    def ioerror(self):
        print("Error: can't write to file")

    @merry._except(Exception)
    def catch_all(self,e):
        print('Unexpected error: ' + str(e))

class B(A):
    def __init__(self) -> None:
        super().__init__()
        self.value = 'test'


    @merry._try
    def funcB(self,string:str):
        print('23',string)
        raise IOError()
    
    #Rewrite the Exception handler and read the obj. 
    @merry._except(Exception)
    def getObjet(self,e):
        print(self.value,str(e))
        
    @merry._try
    def testKeyErro(self):
        raise KeyboardInterrupt('exit')
        
    @merry._except(KeyboardInterrupt)
    def catch_KeyboardInterrupt(self,e):
        print('KeyboardInterrupt ')
        print(str(e))
        
    #Reuse the @merry._except(IOError)  
    
A().func()
B().funcB('testB')
B().testKeyErro()

