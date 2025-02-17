import logging
from fastapi import HTTPException

# Configuração do Logger
logger = logging.getLogger("cria_chave")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Função para registrar logs apenas (melhorada)
def log_only(message, status_code: int = 200, level: str = "info"):
    """
    Registra mensagens no log sem retornar uma resposta.

    :param message: Mensagem a ser registrada no log
    :param status_code: Código de status HTTP relacionado ao evento (padrão: 200)
    :param level: Nível do log ('info', 'warning', 'error', etc.)
    """
    log_message = f"{message} (Status code: {status_code})"
    
    if level.lower() == "info":
        logger.info(log_message)
    elif level.lower() == "warning":
        logger.warning(log_message)
    elif level.lower() == "error":
        logger.error(log_message)
    else:
        logger.debug(log_message)  # Default to debug if an unknown level is passed

# Função para resposta de sucesso
def success(message, data=None, status_code: int = 200):
    """
    Retorna uma resposta padronizada de sucesso.

    :param message: Mensagem descritiva da resposta
    :param data: Dados opcionais a serem incluídos na resposta
    :param status_code: Código de status HTTP (padrão: 200)
    :return: Dicionário contendo a resposta formatada
    """
    log_only(message, status_code)
    response = {"message": message, "status": status_code}
    if data is not None:
        response["data"] = data
    return response

# Função para resposta de erro
def error(message, status_code, exception=None):
    """
    Retorna uma resposta padronizada de erro e registra o evento nos logs.

    :param message: Mensagem descritiva do erro
    :param status_code: Código de status HTTP correspondente ao erro
    :param exception: Exceção opcional para fornecer mais detalhes
    :raise: HTTPException para interromper a execução e retornar o erro
    """
    log_only(message, status_code, level="error")
    raise HTTPException(status_code=status_code, detail=message)