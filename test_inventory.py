from inventory_manager import InventoryManager

def test_add_product():
    manager = InventoryManager()
    manager.add_product("Laptop", 5)
    assert manager.get_stock("Laptop") == 5
