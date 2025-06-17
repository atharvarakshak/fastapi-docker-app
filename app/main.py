import fastapi as _fastapi
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, List
from . import schemas as _schemas
import sqlalchemy.orm as _orm
from . import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


@asynccontextmanager
async def lifespan(app: _fastapi.FastAPI):
    _services._add_tables()
    yield


app = _fastapi.FastAPI(lifespan=lifespan)


@app.post("/api/contacts/", response_model=_schemas.Contact)
async def create_contact(
    contact: _schemas.CreateContact,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.create_contact(contact=contact, db=db)


@app.get("/api/contacts/", response_model=List[_schemas.Contact])
async def get_contacts(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_contacts(db=db)


@app.get("/api/contacts/{contact_id}/", response_model=_schemas.Contact)
async def get_contact(
    contact_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    contact = await _services.get_contact(contact_id=contact_id, db=db)
    if contact is None:
        raise _fastapi.HTTPException(status_code=404, detail="contact does not exist!")
    return await _services.get_contact(contact_id=contact_id, db=db)


@app.delete("/api/delete/{contact_id}/")
async def delete_contact(
    contact_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    contact = await _services.get_contact(contact_id=contact_id, db=db)
    if contact is None:
        raise _fastapi.HTTPException(status_code=404, detail="contact does not exist!")

    await _services.delete_contact(contact=contact, db=db)

    return "Successfully deleted the contact!"


@app.put("/api/update/{contact_id}/", response_model=_schemas.Contact)
async def update_contact(
    contact_id: int,
    contact_data: _schemas.CreateContact,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    contact = await _services.get_contact(contact_id=contact_id, db=db)
    if contact is None:
        raise _fastapi.HTTPException(status_code=404, detail="contact does not exist!")

    return await _services.update_contact(contact_data=contact_data, contact=contact, db=db)

     
