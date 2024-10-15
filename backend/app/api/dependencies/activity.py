from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, Path, HTTPException, status

from app.core.db import database
from app.exeptions.data import Missing
from app.schemas.activity import Activity
from app.service import activity as service


async def get_activity_by_id(
    activity_id: Annotated[int, Path],
    session: AsyncSession = Depends(database.scoped_session_dependency),
) -> Activity:
    try:
        return await service.get_one(session, activity_id)

    except Missing as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.msg,
        )
