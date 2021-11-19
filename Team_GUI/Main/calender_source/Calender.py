from google_auth_oauthlib.flow import InstalledAppFlow #앱 인증을 위한 라이브러리
from google.auth.transport.requests import Request
from google_auth_oauthlib.helpers import credentials_from_session
from googleapiclient.discovery import build
import pickle
import os.path



#----------------------------------------------- 사용자 인증------------------------------------------------------------

#클라이언트 ID Json 파일명
creds_filename = 'calender_source/client.json'
#범위 지정
SCOPES = ['https://www.googleapis.com/auth/calendar']

creds = None


#token.pickle은 유저의 접근 정보를 저장하고 토큰을 refresh한다 
#또한 token.pickle은 유저가 인증 flow를 완료하면 자동적으로 만들어진다
if os.path.exists('calender_source/token.pickle'):
    with open('calender_source/token.pickle','rb') as token:
        creds = pickle.load(token)

#token.pickle이 존재하지 않거나 타당하지 않으면 유저가 로그인하게 한다
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token: #creds가 존재하지만 만료된 상태면
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(creds_filename, SCOPES) 
        creds = flow.run_local_server(port=0)
        with open('calender_source/token.pickle','wb') as token:
            pickle.dump(creds,token)


#----------------------------------------------- 서비스 사용------------------------------------------------------------
import datetime
from dateutil import relativedelta
import dateutil.parser




def GetEvents(month): #0: 11월 ,1: 12월
    Calender = []
    Events_List = []
    today = datetime.date.today()
    end_day=0
    #11월의 첫번째 날
    November_first = datetime.datetime(today.year,11,1,)
    #12월의 첫번째 날
    December_first = datetime.datetime(today.year,12,1,)
    #1월의 첫번째 날
    January_first = datetime.datetime(today.year+1,1,1,)

    Time_min = November_first.isoformat() + 'z'
    Time_max = December_first.isoformat() + 'z'


    if month == 0: #11월이라면
        end_day = 30
    elif month == 1: #12월이라면
        end_day = 31
        Time_min = December_first.isoformat() + 'z'
        Time_max = January_first.isoformat() + 'z'
  
    #다음달의 마지막날
    #December_last_day = ( December_first - datetime.timedelta(seconds=1)).isoformat() + 'z'

    service = build('calendar', 'v3', credentials=creds) #Api에 대한 서비스 객체 생성
    print('Show today s schedule.')

    #이벤트 추출
    events_result = service.events().list(calendarId='primary',singleEvents=True,timeMin=Time_min,timeMax=Time_max,maxResults=10,orderBy='startTime').execute()
    events = events_result.get('items')


    for event in events: #events 1차 정제
            start = event['start'].get('dateTime',event['start'].get('date'))
            end = event['end'].get('dateTime',event['end'].get('date'))
            parsedDate_Start = dateutil.parser.parse(start) #이벤트의 문자열화된 시간정보를 다시 dateTime으로 바꿔준다
            parsedDate_End = dateutil.parser.parse(end)
            t = (event['summary'],parsedDate_Start,parsedDate_End)
            Events_List.append(t)


    #1일부터 마지막까지 순회
    for day_i in range(0,end_day+1) :
        if day_i == 0 :
            Calender.append('빈 자료형')
            continue

        Day_list = []
        Event_list = []
        events_count = 0

        for event in Events_List:
            if day_i == event[1].day:
                Event_list.append(event)
                events_count += 1

        Day_list.append(events_count)
        for event in Event_list:
            Day_list.append(event)
        
        
        Calender.append(Day_list)

    
        
    return Calender