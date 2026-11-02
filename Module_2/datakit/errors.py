

class DataKitError(Exception):
    """"Base class for all exceptions raised by datakit"""
    pass

class InvalidFileError(DataKitError):
    """Raised when the file is not valid"""
    pass

class EmptyDatasetError(DataKitError):
    """Raised when the dataset is empty"""
    pass

