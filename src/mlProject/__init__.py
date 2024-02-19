import os
import sys
import logging

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# log folder
log_dir="logs"

# log file
log_filepath=os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath), # With the help of this we can save the log in the file name running_log.log
        logging.StreamHandler(sys.stdout) # With the help of this we can see the log on the terminal
    ]
)

logger=logging.getLogger("mlProjectLogger")
