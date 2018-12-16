#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import datetime 
get_ipython().run_line_magic('matplotlib', 'inline')

def opener(url):
    with open(url, 'r', encoding = 'utf-8') as file:
        data = pd.read_json(file, orient = 'records')

    data_date = data.dropna(how = 'any')

    def converter(d) :
        if type(d) == int:
            return d
        elif type(d) == str:

            r = d.replace(',','')
            if r != '':
                return int(r)
            else :
                return 0

    data_date['reply_count'] = data_date['reply_count'].apply(lambda d : converter(d))
    data_date['play_count'] = data_date['play_count'].apply(lambda d : converter(d))
    data_date['heart_count'] = data_date['heart_count'].apply(lambda d : converter(d))

    data_reflist = []
    for date,rows in data_date.groupby("date"):
        data_ref = {}
        data_ref['date'] = date
        data_ref['heart_count_mean'] = rows.heart_count.mean()
        data_ref['play_count_mean'] = rows.play_count.mean()
        data_ref['reply_count_mean'] = rows.reply_count.mean()
        data_reflist.append(data_ref)

    pand = pd.DataFrame.from_records(data_reflist)

    pand['qt1'] = pand.date.apply(lambda e: datetime.datetime(2015,1,1) <= e < datetime.datetime(2015,4,1))
    pand['qt2'] = pand.date.apply(lambda e: datetime.datetime(2015,4,1) <= e < datetime.datetime(2015,7,1))
    pand['qt3'] = pand.date.apply(lambda e: datetime.datetime(2015,7,1) <= e < datetime.datetime(2015,10,1))
    pand['qt4'] = pand.date.apply(lambda e: datetime.datetime(2015,10,1) <= e < datetime.datetime(2016,1,1))

    return pand


#open files
mudo = opener(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\navertv_json_data\2015\mudo_2015.json")
# mudo = mudo.iloc[1:]   #무도는 2009년 데이터가 하나 포함되어 있어서 그 데이터 제거해줌.
nahonja = opener(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\navertv_json_data\2015\nahonja_2015.json")
bokga = opener(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\navertv_json_data\2015\bokga_2015.json")
radio = opener(r"C:\Users\bumso\datajournalism-2018\datajournalism-team-1\Beomsoo\navertv_json_data\2015\radio_2015.json")
data_list = [(mudo,'mudo'), (nahonja,'nahonja'), (bokga,'bokga'), (radio,'radio')]
radio

#%%
'''
시계열 그래프 그리기!
'''

def time_graph(data_list, category):

    #2017/1/1 ~ 2018/1/1 까지의 날짜 list 생성
    # start_day = datetime.datetime(2015,1,1)   
    # one_day = datetime.timedelta(days = 1)    
    # end_day = datetime.datetime(2015,12,28) # 2017 연예대상 시상식 날짜 기준

    # date_list = []
    
    # while start_day < end_day:
    #     date_list.append(start_day)
    #     start_day = start_day + one_day
        
    plt.figure(num = None, figsize = (18,9))
    if category == 'play_count_mean':
        plt.ylim(0,1500000)
    if category == 'reply_count_mean' :
        plt.ylim(0,900)
    if category == 'heart_count_mean':
        plt.ylim(0,7000)
    x1 = data_list[0][0]['date']
    y1 = data_list[0][0][category]
    x2 = data_list[1][0]['date']
    y2 = data_list[1][0][category]
    x3 = data_list[2][0]['date']
    y3 = data_list[2][0][category]
    x4 = data_list[3][0]['date']
    y4 = data_list[3][0][category]
    plt.plot(x1, y1, label = data_list[0][1], color = 'r')
    plt.plot(x2, y2, label = data_list[1][1], color = 'y')
    plt.plot(x3, y3, label = data_list[2][1], color = 'g')
    plt.plot(x4, y4, label = data_list[3][1], color = 'b')   
    plt.legend()
    plt.title(category + "2015")
    plt.xticks(rotation=90)
    plt.savefig(category + "2015")
    return
    plt.show()

# time_graph(data_list, 'heart_count_mean')
# time_graph(data_list, 'reply_count_mean')
# time_graph(data_list, 'play_count_mean')



'''
분기별 평균 그래프 그리기!
'''

def histo_graph(data_list, category):
    

histo_graph(data_list, "heart_count")
data_list[0][0]

# histo_graph(data_list, "heart_count_mean")

#%%
import datetime
data["2015.04.01." <= data.date < "2015.07.01"]