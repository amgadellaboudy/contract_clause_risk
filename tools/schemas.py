from typing import List, Optional
from pydantic import BaseModel, Field, RootModel
import pandas as pd


class ClauseRisk(BaseModel):
    clause_excerpt: str
    risk_score: int = Field(..., ge=1, le=10)
    why_risky: str
    suggested_change: Optional[str] = ""


class ClauseRiskList(BaseModel):
    items: List[ClauseRisk] = Field(..., description="List of risky clauses.")

    def to_list(self) -> List[ClauseRisk]:
        return self.items

    def to_pandas(self) -> pd.DataFrame:
        return pd.DataFrame([item.model_dump() for item in self.items])
