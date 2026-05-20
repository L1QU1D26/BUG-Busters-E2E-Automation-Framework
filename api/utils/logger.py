import logging
import os


# Create logs folder if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")


# Logger configuration
logging.basicConfig(
    filename="logs/api_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_logger():
    return logging.getLogger()