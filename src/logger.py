from loguru import logger
import watchtower

# Save logs locally
logger.add("output/pipeline.log", rotation="1 MB")

def get_logger():
    return logger
