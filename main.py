import datetime
import multiprocessing

def SumOfMilions(unit):
    sum = 0
    rangeLimit = unit * 1000000
    for index in range(rangeLimit):
        if index % 17 == 0:
            sum += index
    print("Suma numerelor divizibile cu 17 mai mici decat " + str(rangeLimit)\
          + " este: " + str(sum))

if __name__ == "__main__":
        start = datetime.datetime.now()

        SumOfMilions(210)
        SumOfMilions(119)

        stop = datetime.datetime.now()

        print("Timp scurs in modul liniar: " + str(stop - start))
        del start, stop

        start = datetime.datetime.now()

        process1 = multiprocessing.Process(target=SumOfMilions, args=[210])
        process2 = multiprocessing.Process(target=SumOfMilions, args=[119])
        process1.start()
        process2.start()
        process1.join()
        process2.join()

        stop = datetime.datetime.now()

        print("Timp scurs in modul paralel: " + str(stop - start))