
from typing import List, Dict, Any, Optional, Tuple
from app.database import get_conn

def list_orders(limit: int = 50, offset: int = 0) -> List[Dict[str, Any]]:
    sql = """
        SELECT OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate,
               ShipVia, Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry
        FROM Orders
        ORDER BY OrderDate DESC
        LIMIT ? OFFSET ?;
    """
    with get_conn() as conn:
        cur = conn.execute(sql, (limit, offset))
        return [dict(row) for row in cur.fetchall()]

def get_order_by_id(order_id: int) -> Optional[Dict[str, Any]]:
    sql = """
        SELECT OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate,
               ShipVia, Freight, ShipName, ShipAddress, ShipCity, ShipRegion, ShipPostalCode, ShipCountry
        FROM Orders
        WHERE OrderID = ?;
    """
    with get_conn() as conn:
        cur = conn.execute(sql, (order_id,))
        row = cur.fetchone()
        return dict(row) if row else None
