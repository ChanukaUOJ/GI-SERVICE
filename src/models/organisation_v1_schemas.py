from pydantic import BaseModel
<<<<<<< HEAD
<<<<<<< HEAD
from typing import Optional
=======
>>>>>>> e4e8c9f (Closes: #27: Active portfolio list API implementation (#28))
=======
from typing import Optional
>>>>>>> adf920a (fixed conflict)

class Date(BaseModel):
    date: str

<<<<<<< HEAD
<<<<<<< HEAD
class PersonsByPortfolioRquest(BaseModel):
    activeDate: Date
    president_id: str
=======
>>>>>>> e4e8c9f (Closes: #27: Active portfolio list API implementation (#28))
=======
class PersonsByPortfolioRquest(BaseModel):
    activeDate: Date
    president_id: str
>>>>>>> adf920a (fixed conflict)
