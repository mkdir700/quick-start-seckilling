"""
数据库模型
"""
from typing import Optional

import sqlmodel as sm
import sqlalchemy as sa


class OrderHistory(sm.SQLModel, table=True):
    __tablename__ = "order_history"
    id: Optional[int] = sm.Field(
        default=None,
        primary_key=True,
        sa_column=sa.Column(
            sa.Integer, autoincrement=True, primary_key=True, comment="id"
        ),
    )
    goods_id: str = sm.Field(nullable=False, description="商品id")
    user_id: str = sm.Field(nullable=False, description="用户id")
    order_id: str = sm.Field(nullable=False, description="订单id")
    status: str = sm.Field(
        nullable=False,
        default="0",
        description="订单状态, -1: 超时, 0: 未支付, 1: 已支付",
        sa_column=sa.Column(sa.String(1), default="0"),
    )
