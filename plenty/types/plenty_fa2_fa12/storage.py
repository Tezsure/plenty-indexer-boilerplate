# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from pydantic import BaseModel, Extra


class PlentyFa2Fa12Storage(BaseModel):
    class Config:
        extra = Extra.forbid

    admin: str
    lpFee: str
    lpTokenAddress: str
    maxSwapLimit: str
    paused: bool
    systemFee: str
    token1Address: str
    token1Check: bool
    token1Id: str
    token1_Fee: str
    token1_pool: str
    token2Address: str
    token2Check: bool
    token2Id: str
    token2_Fee: str
    token2_pool: str
    totalSupply: str