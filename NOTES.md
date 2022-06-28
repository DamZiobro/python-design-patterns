Singleton pattern
=====

* useful when we have object which should have one global instance ex. logger


Prototype pattern
=====

* useful when we need to create lots of the same or almost the same objects (ex. warriors in the RTS game)
* it is more optimal to read the properties of the object from the DB/file once and clone the objects than..
* ... create each object by reading it's properties from the DB/file straight away 
 
 
Factory pattern
=====

* we want to be able to create objects throught a common interface rather than spreading the creation code throughout the system
