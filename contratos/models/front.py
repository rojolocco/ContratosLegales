# Import
from pydantic import BaseModel


# Base Contract
class BaseContract(BaseModel):
    pass


# Back Contract
class FrontContract(BaseContract):
    source: str = "back"


# ________________________________________________________________________________________________________________________________
# Contract: F_01_01_2023 - Contrato de Arriendo(01) tipo 01
class ContractF01012023(FrontContract):
    code: str = "F_01_01_2023"


# ________________________________________________________________________________________________________________________________
# Contract: F_01_02_2023 - Contrato de Arriendo(01) tipo 02
class ContractF01022023(FrontContract):
    code: str = "F_01_02_2023"
