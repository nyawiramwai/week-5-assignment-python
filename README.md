 Python OOP Assignments – Week 5

This repository contains my **Object-Oriented Programming (OOP)** assignments for Week 5.  
The tasks involve creating classes, constructors, inheritance, and demonstrating polymorphism in Python.  

---

 Files Included
- `inheritance.py` → A class design for a **Smartphone** with attributes, methods, and inheritance (`SmartphonePro`).
- `polymorphism.py` → A **Polymorphism Challenge** where different vehicle classes (`Car`, `Plane`, `Boat`, `Train`) share the same `move()` method but behave differently.

---

 Assignment Details
 1. Smartphone Class
- Created a `Smartphone` class with attributes:
  - Brand, Model, Storage, Battery
- Methods:
  - `call()` → Simulates calling a number   
  - `charge()` → Increases battery level   
- Added `SmartphonePro` class (inherits from `Smartphone`):
  - Extra attribute: `camera_quality`  
  - Extra method: `take_photo()` 
  - Demonstrated **polymorphism** by redefining `call()` to simulate video calling  

2. Polymorphism Challenge
- Designed a base class `Vehicle` with a method `move()`.
- Created subclasses:
  - `Car` → " Driving on the road!"
  - `Plane` → " Flying in the sky!"
  - `Boat` → " Sailing on the water!"
  - `Train` → " Running on the tracks!"
- Demonstrated **polymorphism**: same method name, different behaviors.


