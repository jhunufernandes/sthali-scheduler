from sthali_crud import SthaliCRUD


async def get_schedules(sthali_crud: SthaliCRUD) -> list:
    return await sthali_crud.db.read_all()
