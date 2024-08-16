<!-- Basic Type -->
first_name :str
age: int
item_c: float
item_d: bool
item_e: bytes
<!-- Generaic Data Type -->
items: list[str]                  -> [2,3,4,5,6]  array
items_t: tuple[int, int, str]     -> order = ( 2, 15, "French Fry")
set[bytes]
prices: dict[str, float]          -> object  

enum type

<!-- Function -->
def NAME():
  // WORK HERE
    return name_with_age


<!-- Smart way -->
name: Optional[str] = None
if name is not None: