from fastapi import FastAPI,Depends,HTTPException
from typing import Optional, Union
import schemas,models
from database import engine,SessionLocal
from sqlalchemy.orm import Session


models.Base.metadata.create_all(engine)

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()



app = FastAPI()

@app.get('/pages')
def get_pages(db:Session = Depends(get_db)):
	pages = db.query(models.Pages).all()
	return pages
	
@app.post('/pages', status_code=201)
def get_pages(pages: schemas.Pages, db:Session = Depends(get_db)):
	new_page = models.Pages(title = pages.title, body = pages.body, published = pages.published)
	db.add(new_page)
	db.commit()
	db.refresh(new_page)
	return new_page
@app.delete('/pages/{id}')
def destroy(id:int,db:Session = Depends(get_db)):
	page = db.query(models.Pages).filter(models.Pages.id == id).first()
	if not page:
		raise HTTPException(status_code = 404, detail = f"The page with th give id of {id} is not found or missing")
	else:	
		db.delete(page)
		db.commit()
		return "sucessfully removed from DB"
@app.put('/pages/{id}')
def update_page(id:int,pages: schemas.Pages, db:Session = Depends(get_db)):
	page = db.query(models.Pages).filter(models.Pages.id == id).first()
	if not page:
		raise HTTPException(status_code = 404, detail = f"The page with th give id of {id} is not found or missing")
	else:	
		#db.update(page)
		db.query(models.Pages).filter(models.Pages.id == id).update({"title":pages.title, "body": pages.body, "published": pages.published })
		db.commit()
		return "sucessfully updated from DB"

	
