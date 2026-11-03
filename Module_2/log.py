import logging
import os

logging.basicConfig(
    filename="a1.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Hy")
logging.warning("Alert your data us hack")


print(os.path.abspath("a1.log"))
print(os.path.exists("a1.log"))
