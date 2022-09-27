import json
import numbers

json_str = """{
"title": "python",
"price": 0,
"location": {
    "address": "город Москва",
    "metro_stations": ["Люблино"]
    }
}
"""


class ColorizeMixin:
    def __init__(self, repr_color):
        self.repr_color = repr_color


class MyClass(ColorizeMixin):
    repr_color = 35

    def __init__(self, data, check_price=True):
        if isinstance(data, str):
            json_obj = json.loads(json_str)
        elif isinstance(data, dict):
            json_obj = data
        else:
            raise ValueError("Invalid data for initialization. Should be json-string or dictionary")
        self.json_obj = json_obj

        if check_price:
            if 'price' not in self.json_obj:
                self.json_obj['price'] = 0
            elif not (
                    isinstance((self.json_obj['price']), numbers.Number)
                    and self.json_obj['price'] >= 0
            ):
                raise ValueError("Price must be a number >= 0")

    def __getattr__(self, field):
        if field in self.json_obj:
            if isinstance(self.json_obj[field], dict):
                return MyClass(data=self.json_obj[field], check_price=False)
            else:
                return self.json_obj[field]
        else:
            raise ValueError("Unknown attribute")

    def repr(self):
        return f"\33[{self.repr_color}m{self.title} | {self.price} ₽"


a = MyClass(json_str)
print(a.title)
print(a.location.address)

iphone_ad = MyClass('iPhone X', 100)
print(iphone_ad.repr())
