
import logging

def get_logger(name):
    log=logging.getLogger(name)
    if not log.handlers:
        h=logging.StreamHandler()
        h.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
        log.addHandler(h)
    log.setLevel(logging.INFO)
    return log
