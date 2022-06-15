import logging

logging.basicConfig(filename='test_run.log', filemode='a+', format='%(created)f - %(levelname)s - %(message)s',
                    datefmt='%H:%M:%S', level=logging.INFO)


def logger(msg="", error=False):
    if error:
        logging.error(msg)
    else:
        logging.info(msg)
