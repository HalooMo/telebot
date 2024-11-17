import multiprocessing as mp
from datetime import datetime



class NameSpace1:

    def f1(self, p1, l):
        print(datetime.now())
        print(f"Namespace1 ")
        print(f"Это  p1 - {p1}")

class NameSpace2:

    def f2(self,p2, l):
        print(datetime.now())
        name = NameSpace1()
        print(f"Namespace2 ")
        name.f1(p2,l)
        print(f"Это  p2 - {p2}")


def f3(p3, l):
    name1 = NameSpace1()
    name2 = NameSpace2()
    name1.f1(p3, l)
    name2.f2(p3, l)


if __name__ == "__main__":
    with mp.Manager() as manager:
        
        dict3 = manager.dict({"p3":"p3"})
        list = manager.list(range(10))

        #process1 = mp.Process(target=namespace.f1, args=(dict1, list))
        #process2 = mp.Process(target=namespace2.f2, args=(dict2, list))
        process3 = mp.Process(target=f3, args=(dict3, list))

        #process1.start()
        #process2.start()
        process3.start()

        #process1.join()
        #process2.join()
        process3.join()
