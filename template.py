
class StringSeparator:
    def get_string(string):
        """Returns string with separator"""
        
        numbers = ['1','2','3','4','5','6','7','8','9','0']
        result_string = ''
        
        # Loop to check if character is number
        for char in string:            
            if not char in numbers: # Check if character is valailable in the list of numbers
                result_string += char # if not available then  add character to result_string
        
        return result_string

    def get_number(string):
        """
        uyuyg iuygy uy  7f y7f7ftyft7ftyfijio 
        """
        pass

number = "123tyrty4567wer89asdvvs"

print(StringSeparator.get_string(number))
   

