
from pydantic import BaseModel, Field
from typing import Optional

class Order(BaseModel):
    OrderID: int = Field(..., description="Unique order ID")
    CustomerID: Optional[str] = None
    EmployeeID: Optional[int] = None
    OrderDate: Optional[str] = None
    RequiredDate: Optional[str] = None
    ShippedDate: Optional[str] = None
    ShipVia: Optional[int] = None
    Freight: Optional[float] = None
    ShipName: Optional[str] = None
    ShipAddress: Optional[str] = None
    ShipCity: Optional[str] = None
    ShipRegion: Optional[str] = None
    ShipPostalCode: Optional[str] = None
    ShipCountry: Optional[str] = None
