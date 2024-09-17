
import logging

from pydantic import BaseModel
from opentelemetry.instrumentation.logging import LoggingInstrumentor

class LoggerFields(BaseModel):
    user_id: int | None
    order_id: str | None
    extra: dict | None

class Logger:
    def __init__(self, level: str):

        logging.basicConfig(
            level=logging.getLevelName(level),
            format='[%(asctime)s - %(name)s - %(levelname)s] - [trace_id=%(otelTraceID)s span_id=%(otelSpanID)s resource.service.name=%(otelServiceName)s trace_sampled=%(otelTraceSampled)s] - %(message)s',
            handlers=[logging.StreamHandler()]
        )
        # LoggingInstrumentor().instrument(set_logging_format=True)


        self.__logger = logging.getLogger("client")
        
    
    def log(self, level: int, user_id: int, order_id: int, extra: dict, message: str):
        
        fields = LoggerFields(user_id=user_id, order_id=order_id, extra=extra)
        fields_json = fields.model_dump()
        match level:
            case logging.DEBUG:
                self.__logger.debug(msg=f"{fields_json} - {message}")
            case logging.INFO:
                self.__logger.info(msg=f"{fields_json} - {message}")
            case logging.WARNING:
                self.__logger.warning(msg=f"{fields_json} - {message}")
            case logging.ERROR:
                self.__logger.error(msg=f"{fields_json} - {message}")
            case logging.CRITICAL:
                self.__logger.critical(msg=f"{fields_json} - {message}")
            case _:
                raise ValueError(f"Invalid log level: {level}")
            
                