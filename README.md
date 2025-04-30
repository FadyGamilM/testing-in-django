# To run a tests file
```shell
╰─ python -m unittest [filename].py
```

# Example to a unit test using `unittest` pkg:
- app.py file 

```python
class Character():
    def __init__(self, name:str, superpower:str, health:int):
        self.name = name
        self.superpower = superpower
        self.health = health
        
    def is_powerful(self, other: 'Character') -> bool:
        return self.health > other.health
    
    def __str__(self) -> str:
        return f"{self.name}".upper() 
```

- tests.py file 

```python
import unittest

from app import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character("Superman", "Flying", 100)
        self.character2 = Character("Batman", "Gadgets", 80)
        self.character3 = Character("spiderman", "Web-slinging", 100)
    
    def test_class_str(self):
        self.assertEqual(str(self.character), "SUPERMAN")
    
    def test_is_powerful(self):
        self.assertTrue( self.character.is_powerful(self.character2))
        self.assertFalse(self.character2.is_powerful(self.character))
        self.assertFalse(self.character.is_powerful(self.character3))    
```