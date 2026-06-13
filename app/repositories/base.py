from typing import Generic, TypeVar, Type, List, Optional, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import select, and_, or_
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(self, db: AsyncSession, obj_in: dict, user_id:UUID):
        obj = self.model(**obj_in)
        if user_id:
            obj.created_by = user_id

        db.add(obj)

        await db.flush()
        await db.refresh(obj)

        return obj

    def bulk_create(self, db: Session, objs: List[dict]) -> List[ModelType]:
        objects = [self.model(**obj) for obj in objs]
        db.add_all(objects)
        db.commit()
        for obj in objects:
            db.refresh(obj)
        return objects

    async def get(self, db, id: Any):
        stmt = select(self.model).where(
            self.model.id == id,
            self.model.is_deleted == False
        )

        result = await db.execute(stmt)
        return result.scalars().first()

    def get_by_ids(self, db: Session, ids: List[Any]) -> List[ModelType]:
        return db.query(self.model).filter(
            self.model.id.in_(ids),
            self.model.is_deleted == False
        ).all()

    def get_one_by_filters(self, db: Session, filters: Dict) -> Optional[ModelType]:
        query = db.query(self.model).filter(self.model.is_deleted == False)
        for k, v in filters.items():
            query = query.filter(getattr(self.model, k) == v)
        return query.first()

    def exists(self, db: Session, filters: Dict) -> bool:
        query = db.query(self.model).filter(self.model.is_deleted == False)
        for k, v in filters.items():
            query = query.filter(getattr(self.model, k) == v)
        return db.query(query.exists()).scalar()

    async def get_multi(
        self,
        db: AsyncSession,
        filters: dict | None = None,
        search: str | None = None,
        search_fields: list[str] | None = None,
        order_by=None
    ):
        stmt = select(self.model).where(self.model.is_deleted == False)

        if filters:
            for key, value in filters.items():
                if hasattr(self.model, key):
                    stmt = stmt.where(getattr(self.model, key) == value)

        if search and search_fields:
            conditions = []
            for field in search_fields:
                if hasattr(self.model, field):
                    col = getattr(self.model, field)
                    conditions.append(col.ilike(f"%{search}%"))

            if conditions:
                stmt = stmt.where(or_(*conditions))

        if order_by is not None:
            stmt = stmt.order_by(order_by)

        result = await db.execute(stmt)

        return result.scalars().all()
    
    def paginate(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 10,
        filters: Optional[Dict] = None
    ) -> Dict:

        query = db.query(self.model).filter(self.model.is_deleted == False)

        if filters:
            for k, v in filters.items():
                query = query.filter(getattr(self.model, k) == v)

        total = query.count()
        items = query.offset(skip).limit(limit).all()

        return {
            "total": total,
            "skip": skip,
            "limit": limit,
            "items": items
        }

    async def update(self, db: AsyncSession, id: Any, obj_in: dict, user_id: UUID):
        obj = await self.get(db, id)

        if not obj:
            return None

        for key, value in obj_in.items():
            setattr(obj, key, value)

        if user_id:
            obj.updated_by = user_id

        await db.commit()
        await db.refresh(obj)
        return obj

    def bulk_update(self, db: Session, updates: List[Dict]) -> bool:
        for item in updates:
            obj = self.get(db, item["id"])
            if obj:
                for k, v in item.items():
                    if k != "id":
                        setattr(obj, k, v)

        db.commit()
        return True

    def partial_update(self, db: Session, id: Any, obj_in: dict) -> Optional[ModelType]:
        return self.update(db, id, obj_in)

    async def delete(self, db: AsyncSession, id: Any, user_id: UUID):
        obj = await self.get(db, id)

        if not obj:
            return False

        if user_id:
            obj.updated_by = user_id

        obj.is_deleted = True

        await db.commit()
        await db.refresh(obj)

        return obj

    def hard_delete(self, db: Session, id: Any) -> bool:
        obj = db.query(self.model).filter(self.model.id == id).first()
        if not obj:
            return False

        db.delete(obj)
        db.commit()
        return True

    def restore(self, db: Session, id: Any) -> bool:
        obj = db.query(self.model).filter(self.model.id == id).first()
        if not obj:
            return False

        obj.is_deleted = False
        db.commit()
        return True

    def search(self, db: Session, field: str, value: str) -> List[ModelType]:
        query = db.query(self.model).filter(self.model.is_deleted == False)
        column = getattr(self.model, field)
        return query.filter(column.ilike(f"%{value}%")).all()

    def filter_in(self, db: Session, field: str, values: List[Any]) -> List[ModelType]:
        column = getattr(self.model, field)
        return db.query(self.model).filter(
            column.in_(values),
            self.model.is_deleted == False
        ).all()

    def filter_like(self, db: Session, field: str, value: str) -> List[ModelType]:
        column = getattr(self.model, field)
        return db.query(self.model).filter(
            column.like(f"%{value}%"),
            self.model.is_deleted == False
        ).all()

    def count(self, db: Session, filters: Optional[Dict] = None) -> int:
        query = db.query(func.count(self.model.id)).filter(
            self.model.is_deleted == False
        )

        if filters:
            for key, value in filters.items():
                query = query.filter(getattr(self.model, key) == value)

        return query.scalar()

    def distinct(self, db: Session, field: str) -> List[Any]:
        column = getattr(self.model, field)
        return db.query(column).distinct().all()