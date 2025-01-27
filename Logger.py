import logging
from colorama import Fore, Style


# Colors for each type of Log
LOG_COLORS = {
    "DEBUG": Fore.CYAN,
    "INFO": "\033[97m",
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "CRITICAL": Fore.MAGENTA,
}


class CustomFormatter(logging.Formatter):
    """Custom formatter to add colors e formats"""

    def __init__(self):
        super().__init__()
        # Formato per i messaggi
        self.formats = {
            logging.DEBUG: self._format(logging.DEBUG),
            logging.INFO: self._format(logging.INFO),
            logging.WARNING: self._format(logging.WARNING),
            logging.ERROR: self._format(logging.ERROR),
            logging.CRITICAL: self._format(logging.CRITICAL),
        }

    def _format(self, level):
        """Returns a colored format for each level"""
        color = LOG_COLORS.get(logging.getLevelName(level), "")
        return f"{color}%(asctime)s - %(name)s - %(levelname)s - %(message)s{Style.RESET_ALL}"

    def format(self, record):
        """Formatta il messaggio in base al livello."""
        log_fmt = self.formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)


# Logger Configurator
def get_logger():
    """Returns a universal logger that accept all levels"""
    logger = logging.getLogger("CommonLogger")
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)  # Allows every log level

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(CustomFormatter())

        # Handler for log files
        file_handler = logging.FileHandler("shared_log.log")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger