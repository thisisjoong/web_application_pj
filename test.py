from datetime import date, timedelta
import mosquito_data


now= date.today()
now_str = str(now)
#print(now_str)

#오늘날짜로 요청
real_data = mosquito_data.get_mosquito_data(now_str)
print(real_data)
#없으면 어제 날짜로 요청
if not real_data['RESULT']['MESSAGE'][0] ==  '해당하는 데이터가 없습니다.':
     yesterday = now - timedelta(days=1)
     yesterday_str = str(yesterday)
     print(yesterday_str)

     real_data = mosquito_data.get_mosquito_data(yesterday_str)
     print(real_data)

