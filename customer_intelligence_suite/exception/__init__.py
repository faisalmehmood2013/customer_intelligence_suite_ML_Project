"""
exception/__init__.py
------------------------
Custom Exception class - jab error aaye, normal Python error ke
bajaye yeh batayega EXACT FILE NAME aur LINE NUMBER jahan error hui.

Yeh debugging ko BOHOT asaan banata hai. Aap ke template
mein bhi yehi pattern tha. Standard implementation:

    import sys

    class CustomException(Exception):
        def __init__(self, error_message, error_detail: sys):
            self.error_message = error_message
            _, _, exc_tb = error_detail.exc_info()
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename

        def __str__(self):
            return (f"Error in [{self.file_name}] at line [{self.lineno}]: "
                    f"{self.error_message}")

Usage: har function mein try/except ke andar
    raise CustomException(str(e), sys) from e
"""
