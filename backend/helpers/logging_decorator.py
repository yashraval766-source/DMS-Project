import functools
import logging
import os
import time

logger = logging.getLogger("dms_project")
if not logger.handlers:
    handler = logging.FileHandler(os.path.join(os.getcwd(), "project.log"), encoding="utf-8")
    fmt = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    handler.setFormatter(logging.Formatter(fmt))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

def log_method(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cls_name = args[0].__class__.__name__ if args else ""
        logger.info("Calling: %s.%s args=%s kwargs=%s",
                    cls_name, func.__name__, args[1:] if len(args) > 1 else (), kwargs)
        start = time.time()
        try:
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            logger.info("Finished: %s.%s result=%s elapsed=%.4fs",
                        cls_name, func.__name__, repr(result), elapsed)
            return result
        except Exception:
            logger.exception("Exception in %s.%s", cls_name, func.__name__)
            raise
    return wrapper
