from pydantic import BaseModel


class Pages(BaseModel):
	title: str
	body: str
	published: bool 
