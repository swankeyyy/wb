from pydantic import BaseModel, Field

class Item(BaseModel):
    id: int = Field(alias="nm_id")
    name: str = Field(alias="imt_name")
    category: str = Field(alias="subj_root_name")
    description: str
    
    class Config:
        populate_by_name = True