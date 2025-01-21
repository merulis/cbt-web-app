from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Path, HTTPException, status

from app.db import database
from app.activity.schemas.activity import Activity
from app.activity.service import activity as service

from app.db.exceptions import Missing


async def get_activity_by_id(
    activity_id: Annotated[int, Path],
    session: AsyncSession = Depends(database.scoped_session_dependency),
) -> Activity:
    try:
        await service.get_one(session, activity_id)

    except Missing as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.msg,
        )
