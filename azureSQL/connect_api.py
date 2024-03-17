from fastapi import APIRouter, HTTPException, Body
from .connect_logic import azure_con

router = APIRouter()

# Assuming your data model here; you might need to adjust it
from pydantic import BaseModel
class InsertRowSchema(BaseModel):
    CONDITION_A: str
    CONDITION_B: str
    GRAPH: str
    timeTaken: int
    Error: int
    controlCondition: int
    timePer: int

@router.post("/insertRows")
async def post_insertRow(data: InsertRowSchema):
    try:
        result = azure_con().insertRow(**data.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



@router.get("/Allrows")
async def get_Allrows():
    result = azure_con().getTable()
    return {'result:': result}