import os
import sys


def error_message_detail(error, error_detail: sys) -> str:
    """
    Builds a detailed error message - not just "what went wrong",
    but also "where it went wrong" (file name, line number).

    Parameters
    ----------
    error : Exception
        The actual exception object that was raised.
    error_detail : sys
        The sys module - used to extract traceback information
        (file name, line number) of the current exception.

    Returns
    -------
    str
        A formatted error message containing the file name,
        line number, and the original error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomerIntelligenceException(Exception):
    """
    Project-wide custom exception class.

    Used across every tier (CLV, Churn, Segmentation, Demand Forecast,
    Recommendation) and every component (data_ingestion, model_trainer,
    etc.) so that every raised error consistently includes the
    file name and line number where it occurred, making debugging
    significantly faster.

    Usage (inside any component file):

        import sys
        from customer_intelligence_suite.exception.exception import CustomerIntelligenceException

        try:
            df = pd.read_csv(path)
        except Exception as e:
            raise CustomerIntelligenceException(e, sys) from e
    """

    def __init__(self, error_message, error_detail: sys):
        """
        :param error_message: error message in string format
        :param error_detail: sys module, used to extract the traceback
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message