import logging

logging.basicConfig(filename='test_result.log', filemode='w',
                    format='%(asctime)s, %(levelname)s %(message)s',
                    datefmt='%H:%M:%S', level=logging.INFO)


def logger(msg="", error=False):
    if error:
        logging.error(msg)
    else:
        logging.info(msg)
