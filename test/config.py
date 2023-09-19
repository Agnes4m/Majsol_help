from pydantic import BaseModel

from typing import Optional, List


class AllConfig(BaseModel):
    """整体配置"""

    mode: int
    """当前状态,0是他人回合,1是自身回合(摸到牌)"""
    special: Optional[str] = None
    """特殊牌型，包括【七对子】【国士无双】"""


class HandCard(BaseModel):
    """手牌内容"""

    wan: List[str]
    """万字牌"""
    tiao: List[str]
    """条子"""
    tong: List[str]
    """筒子"""
    zi: List[str]
    """字牌,顺序发白中"""
