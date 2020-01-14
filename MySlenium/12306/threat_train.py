import train
import inputdata
import multiprocessing
# 告知数据源的路径
path = "C://Users//86176//Desktop//inputData.xlsx"
# 实例化对象
inputData =inputdata.ReadExcel(path)

ListNum = inputData.dict_data()
intList1 = int(ListNum[0][8])
# 对象实例化
ticket12306 = train.buy_tickets()
if __name__ == '__main__':
    if ListNum[1][8] != '':
        intList2 = int(ListNum[1][8])
        intPool = intList2 - intList1
        # 开连接线程池的个数
        p = multiprocessing.Pool(5)
        p.map(ticket12306.buy_tickets, [int(intList1)-1, intList2-1])
    else:
        ticket12306.buy_tickets(int(intList1)-1)
