from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainigPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainigPipeline
from textSummarizer.logging import logger



STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainigPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n x==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Validation Stage'
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainigPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\n x==========x")
except Exception as e:
    logger.exception(e)
    raise e