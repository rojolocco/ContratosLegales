# Imports
from fastapi import APIRouter

from models.front import ContractF01012023, ContractF01022023
from compile.front import FrontLatex

# Router
router = APIRouter(prefix="/contracts", tags=["Contract"])


# Frontend F_01_01_2023 Endpoint
@router.post("/front/F_01_01_2023")
async def create_frontend_contract(cdata: ContractF01012023):
    frontlatex = FrontLatex()
    latex_path, latex_file = frontlatex.create_F01012023("F_01_01_2023.tex",cdata.source)
    print(latex_path)
    print(latex_file)
    return {"message": f"Frontend contract of type F_01_01_2023 created!"}


# Frontend F_01_02_2023 Endpoint
@router.post("/front/F_01_02_2023")
async def create_frontend_contract(cdata: ContractF01022023):
    return {"message": f"Frontend contract of type F_01_01_2023 created!"}