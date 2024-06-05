import unittest
from unittest import TestCase
from src.zoo import Zoo,ZooKeeper,Fence,Animal

class TestZoo(TestCase):

    def setUp(self) -> None:
        pass
    def test_animal_dimension(self):
        # Nome : Marim Arafa questo test controlla che i animali troppo grandi non vengono aggiunti al recinto
        zoo :Zoo = Zoo()
        animal1 = Animal(name="Scoiattolo", species="Canide", height=250.8, width =10.8, age=10, preferred_habitat="Continent")
        fence1 = Fence(area=100, temperature=25, habitat="Continent")
        zoo_keeper1 = ZooKeeper(name="Lorenzo", surname="Maggi", id=1234)
        zoo_keeper1.add_animal(animal1,fence1)
        result = len(fence1.animals)
        message :str = "Error. The function add animal should not add animal1 in fence1"

        self.assertEqual(result,0,message)

    def test_animal_habitat(self):
        #Nome : Marim Arafa questo test controlla che i animali con habitat diversi non vengono aggiunti al recinto
        zoo :Zoo = Zoo()
        animal1 = Animal(name="Scoiattolo", species="Canide", height=20.8, width =10.8, age=10, preferred_habitat="Sea")
        fence1 = Fence(area=100, temperature=25, habitat="Continent")
        zoo_keeper1 = ZooKeeper(name="Lorenzo", surname="Maggi", id=1234)
        zoo_keeper1.add_animal(animal1,fence1)
        result = len(fence1.animals)
        message :str = "Error. The function add animal should not add animal1 in fence1"

        self.assertEqual(result,0,message)
    
    def test_add_animal(self):
        #Nome : Marim Arafa questo test controlla che i animali vengono aggiunti al recinto
        zoo :Zoo = Zoo()
        animal1 = Animal(name="Scoiattolo", species="Canide", height=2.8, width =10.8, age=10, preferred_habitat="Continent")
        fence1 = Fence(area=100, temperature=25, habitat="Continent")
        zoo_keeper1 = ZooKeeper(name="Lorenzo", surname="Maggi", id=1234)
        zoo_keeper1.add_animal(animal1,fence1)
        result = len(fence1.animals)
        message :str = "Error. The function add animal should add animal1 in fence1"

        self.assertEqual(result,1,message)

    def test_remove_animal(self):
        #Nome : Marim Arafa questo test controlla se un animale è dentro il recinto 
        zoo :Zoo = Zoo()
        animal1 = Animal(name="Scoiattolo", species="Canide", height=2.8, width =10.8, age=10, preferred_habitat="Continent")
        fence1 = Fence(area=100, temperature=25, habitat="Continent")
        zoo_keeper1 = ZooKeeper(name="Lorenzo", surname="Maggi", id=1234)
        zoo_keeper1.remove_animal(animal1,fence1)
        result1 :bool = (animal1 in fence1.animals)
        message1 :str = "Error. The fence1 does not have animal1"

        self.assertEqual(result1,False,message1)

        #Nome : Marim Arafa questo test controlla se un animale dentro il recintro e stato eliminato
        zoo_keeper1.add_animal(animal1,fence1)
        zoo_keeper1.remove_animal(animal1,fence1)
        result2:int = (len(fence1.animals))
        message2 :str = "Error. The function should remove animal1 from fence1"

        self.assertEqual(result2,0,message2)

    def test_animal_demension_after_feeding(self):
        #Nome : Marim Arafa questo test controlla se i animali sono piu grandi del area del recinto 
        zoo :Zoo = Zoo()
        animal1 = Animal(name="Scoiattolo", species="Canide", height=100.0, width =1.0, age=10, preferred_habitat="Continent")
        fence1 = Fence(area=100, temperature=25, habitat="Continent")
        zoo_keeper1 = ZooKeeper(name="Lorenzo", surname="Maggi", id=1234)
        zoo_keeper1.feed(animal1,fence1)
        result = (len(fence1.animals))
        message :str = "Error. The animal1 should not be feeded"
        self.assertEqual(result,0,message)


    







    





    
    
    





if __name__ == "__main__":
    unittest.main()

#sul terminale : python3 -m unittest -v