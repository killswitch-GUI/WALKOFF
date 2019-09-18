import json
import logging
from http import HTTPStatus
from typing import List

from fastapi import APIRouter, Depends
from pydantic import ValidationError
from motor.motor_asyncio import AsyncIOMotorCollection

from api.server.db import get_mongo_c
from api.server.db.appapi import AppApiModel

from common.helpers import validate_uuid
from common.config import static

router = APIRouter()
logger = logging.getLogger(__name__)


async def app_api_getter(app_api_col: AsyncIOMotorCollection, app_api: str):
    if validate_uuid(app_api):
        return await app_api_col.find_one({"id_": app_api}, projection={'_id': False})
    else:
        return await app_api_col.find_one({"name": app_api}, projection={'_id': False})


@router.get("/")
async def read_all_app_names(app_api_col: AsyncIOMotorCollection = Depends(get_mongo_c)):
    return await app_api_col.distinct("name")


@router.get("/apis/")
async def read_all_app_apis(app_api_col: AsyncIOMotorCollection = Depends(get_mongo_c)):
    ret = []
    for app_api in (await app_api_col.find().to_list(None)):
        ret.append(AppApiModel(**app_api))
    return ret


@router.post("/apis/", status_code=HTTPStatus.CREATED)
async def create_app_api(*, app_api_col: AsyncIOMotorCollection = Depends(get_mongo_c), new_api: AppApiModel):
    r = await app_api_col.insert_one(dict(new_api))
    if r.acknowledged:
        result = await app_api_getter(app_api_col, new_api.id_)
        logger.info(f"Updated Workflow {result.name} ({result.id_})")
        return result


@router.get("/apis/{app_name}")
async def read_app_api(*, app_api_col: AsyncIOMotorCollection = Depends(get_mongo_c), app_name: str):
    app = await app_api_getter(app_api_col, app_name)
    return app


@router.put("/apis/{app_name}")
async def update_app_api(*, app_api_col: AsyncIOMotorCollection = Depends(get_mongo_c), app_name: str, new_api: AppApiModel):
    app = await app_api_getter(app_api_col, app_name)
    r = await app_api_col.replace_one(dict(app), dict(new_api))
    return r.acknowledged


@router.delete("/apis/{app_name}")
async def delete_app_api(*, app_api_col: AsyncIOMotorCollection = Depends(get_mongo_c), app_name: str):
    app = await app_api_getter(app_api_col, app_name)
    r = await app_api_col.delete_one(dict(app))
    return r.acknowledged
