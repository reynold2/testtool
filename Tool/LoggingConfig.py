import logging
import logging.config

CONF_LOG = "config/logging_console.ini"
logging.config.fileConfig(CONF_LOG)
logger = logging.getLogger(__name__)