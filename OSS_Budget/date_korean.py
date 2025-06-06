
import datetime

def get_korean_day():
    days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    today = datetime.date.today()
    weekday = today.weekday()  # 월: 0 ~ 일: 6
    return f"오늘은 {today.year}년 {today.month}월 {today.day}일 {days[weekday]}입니다."

    if __name__ == "__main__":
    print(get_korean_day())