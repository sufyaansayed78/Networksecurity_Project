import sys 
class NetwrorkSecurityException(Exception):
    def __init__(self, error_message,error_details : sys ):
        #super().__init__(error_message)
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        self.line_no = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
    

    def __str__(self):
        return f"Error occured in line number : [{self.line_no}] , in file name : {self.file_name} , error message = {self.error_message}"
    


if __name__=="__main__":
    try : 
        a=1/0
        print("This will be not be printed " , a)

    except Exception as e :
        raise NetwrorkSecurityException(e,sys)
    
