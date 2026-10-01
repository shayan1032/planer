#import
import streamlit as st
import json
import datetime
import jdatetime

#var
now = jdatetime.datetime.now()
days = ["شنبه", "یک شنبه", "دو شنبه", "سه شنبه", "چهار شنبه", "پنج شنبه", "جمعه"]
to_day = days[now.weekday()]
hour = now.hour
if "page" not in st.session_state:
    st.session_state.page = 0
password = ("1032")
input_password = ()
col1, col2, col3 = st.columns([1, 4, 1])
habit = {"1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":"","10":"","11":"","12":"","13":"","14":"","15":""}
habit_score_ne = {"1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":"","10":"","11":"","12":"","13":"","14":"","15":""}
habit_score_pl = {"1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":"","10":"","11":"","12":"","13":"","14":"","15":""}
habit_abu = {"1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":"","10":"","11":"","12":"","13":"","14":"","15":""}
habit_do = {"1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":"","10":"","11":"","12":"","13":"","14":"","15":""}
y_day = ()
score_habit = 0
rerun = {"1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":"","10":"","11":"","12":"","13":"","14":"","15":"","16":"","17":"","18":"","19":"","20":"","21":"","22":"","23":"","24":""}
rerun_day = {"1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":"","10":"","11":"","12":"","13":"","14":"","15":"","16":"","17":"","18":"","19":"","20":"","21":"","22":"","23":"","24":""}
rerun_st_time = {"1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":"","10":"","11":"","12":"","13":"","14":"","15":"","16":"","17":"","18":"","19":"","20":"","21":"","22":"","23":"","24":""}
rerun_en_time = {"1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":"","10":"","11":"","12":"","13":"","14":"","15":"","16":"","17":"","18":"","19":"","20":"","21":"","22":"","23":"","24":""}
reruns = [rerun,rerun_st_time,rerun_en_time,rerun_day]
saver = {
    "rerun" : rerun ,
    "rerun_day" : rerun_day ,
    "rerun_st_time" : rerun_st_time  ,
    "rerun_en_time" : rerun_en_time ,
    "habit": habit,
    "habit_score_ne": habit_score_ne,
    "habit_score_pl": habit_score_pl,
    "habit_abu": habit_abu,
    "y_day" : y_day,
    "habit_do" : habit_do,
    "score_habit" : score_habit
}
one_tow = []

#cod
st.set_page_config(
    page_title="my planer",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #B7E4C7;
}

h1, h2, h3, p, label,h4,h5,h6 {
    text-align: center !important;
    color: #263238 !important;
}

.stButton > button {
    background-color: #A8C7E8;
    color: #263238;
    font-size: 25px !important;
}

.stButton > button p {
    font-size: 25px !important;
    color: #263238 !important;
}
[data-testid="stHeader"] {
    display: none;
}
[data-testid="stAppViewContainer"] {
    padding-top: 50px;
    padding-bottom: 50px;
.stTextInput input,
.stNumberInput input }
{
    background-color: #A8C7E8 !important;
    color: #263238 !important;
}
p{
    font-size: 25px !important;
}

</style>
""", unsafe_allow_html=True)


if st.session_state.page == 0:
    st.session_state.page = 0
    with col2:
        st.title("سلام خوش اومدی")
        input_password = st.number_input("رمز ورود را وارد کنید",min_value=0 )
        if st.button ("ورود",use_container_width=True):    
            if str(input_password) == password:
                st.session_state.page = 1
                st.rerun()

                
if st.session_state.page == 1:
    st.session_state.page = 1
    
    with col2:
        st.title("سلام شایان خوش اومدی")
        if st.button("کار های امروزم",use_container_width=True):
            st.session_state.page = 2
            st.rerun()

        if st.button("نگاهی به برنامه روز های دیگه",use_container_width=True):
            st.session_state.page = 3
            st.rerun()

        if st.button ("ثبت برنامه جدید",use_container_width=True):
            st.session_state.page = 4
            st.rerun()

        if st.button ("حذف برنامه قدیمی",use_container_width=True):
            st.session_state.page = 5
            st.rerun()

        if st.button("ثبت عادت جدید",use_container_width=True):
            st.session_state.page = 6
            st.rerun()

        if st.button("حذف عادت قدیمی",use_container_width=True):
            st.session_state.page = 7
            st.rerun()

        if st.button("کارنامه عادات",use_container_width=True):
            st.session_state.page = 8
            st.rerun()

        if st.button("تنظیمات",use_container_width=True):
            st.session_state.page = 9
            st.rerun()
if st.session_state.page == 2:
    with col2:
        with open("data.json", "r", encoding="utf-8") as file:
            saver = json.load(file) 
        rerun = saver["rerun"]
        rerun_day = saver["rerun_day"]
        rerun_en_time = saver["rerun_en_time"]
        rerun_st_time = saver["rerun_st_time"]
        habit = saver["habit"]
        habit_score_ne = saver["habit_score_ne"]
        habit_score_pl = saver["habit_score_pl"]
        habit_abu = saver["habit_abu"]
        habit_do = saver ["habit_do"]
        y_day = saver ["y_day"]
        score_habit = saver ["score_habit"]

        st.title("برنامه های امروزت")
        st.markdown("<hr style='border: 3px solid #E89B5F;'>", unsafe_allow_html=True)
        x = dict(sorted(rerun_st_time.items(),key=lambda x: x[1]))
        one_tow = list(x.keys())
        one_tow = [int(x) for x in one_tow]
        for i in one_tow:
            i = str(i)
            if rerun[i] != "" :
                x = rerun_st_time[i]
                x = int(x[:2])
                if hour+1 <= x :
                    if to_day in rerun_day[i]:
                        st.write(f"***{rerun[i]}***")
                        st.markdown(
                        f"از ساعت <span style='color:#D95D6A'>{rerun_st_time[i]}</span> تا ساعت <span style='color:#D95D6A'>{rerun_en_time[i]}</span>",
                        unsafe_allow_html=True
                        )
                        st.markdown("<hr style='border: 2px solid #E89B5F;'>", unsafe_allow_html=True)
        if hour > 1 :
            if to_day != y_day :
                score_habit = 0
                for i in habit:
                    if habit[i] != "":
                        if habit_do[i] == "":
                            (score_habit) -= int(habit_score_ne[i] or 0)
                        else:
                            (score_habit) += int(habit_score_pl[i] or 0)
                for i in habit_do:
                    habit_do[i] = ""
                y_day = to_day
                saver["habit_do"] = habit_do
                saver["y_day"] = y_day
                saver["score_habit"] = score_habit
                with open("data.json", "w", encoding="utf-8") as file:
                    json.dump(saver, file, ensure_ascii=False)
        for i in habit:
            if habit[i] != "":
                if habit_do[i] == "":
                    st.write(habit[f"{i}"])
                    st.write(f"امتیاز انجام ندادن {habit_score_ne[f"{i}"]}")
                    st.write(f"امتیاز انجام دادن {habit_score_pl[f"{i}"]}")
                    st.write(f" در باره عادت : {habit_abu [f"{i}"]}")
                    if st.button("انجام شد 🫡" , use_container_width=True):
                        with open("data.json", "r", encoding="utf-8") as file:
                            saver = json.load(file) 
                        score_habit = saver ["score_habit"]
                        habit_do = saver ["habit_do"]
                        habit_do.update({f"{i}" : "1" })
                        score_habit = score_habit + int(habit_score_pl[i])
                        print (score_habit)
                        print (habit_score_pl[i])
                        saver["habit_do"] = habit_do 
                        saver["score_habit"] = score_habit
                        with open("data.json", "w", encoding="utf-8") as file:
                            json.dump(saver, file, ensure_ascii=False)
                        st.rerun()

if st.session_state.page == 3:
    with col2:
        with open("data.json", "r", encoding="utf-8") as file:
            saver = json.load(file) 
        rerun = saver["rerun"]
        rerun_day = saver["rerun_day"]
        rerun_en_time = saver["rerun_en_time"]
        rerun_st_time = saver["rerun_st_time"]
        habit = saver["habit"]
        habit_score_ne = saver["habit_score_ne"]
        habit_score_pl = saver["habit_score_pl"]
        habit_abu = saver["habit_abu"]

        for j in days:
            st.title(f"برنامه روز{j}")
            st.markdown("<hr style='border: 3px solid #E89B5F;'>", unsafe_allow_html=True)
            x = dict(sorted(rerun_st_time.items(),key=lambda x: x[1]))
            one_tow = list(x.keys())
            one_tow = [int(x) for x in one_tow]
            print (one_tow)
            for i in one_tow:
                i = str(i)
                if rerun[i] != "" :
                    x = rerun_st_time[i]
                    x = int(x[:2])
                    if j in rerun_day[i]:
                        st.write(f"***{rerun[i]}***")
                        st.markdown(
                        f"از ساعت <span style='color:#D95D6A'>{rerun_st_time[i]}</span> تا ساعت <span style='color:#D95D6A'>{rerun_en_time[i]}</span>",
                        unsafe_allow_html=True
                        )
                        st.markdown("<hr style='border: 2px solid #E89B5F;'>", unsafe_allow_html=True)



if st.session_state.page == 4:
    with col2:   
        st.title("اطلاعات رو وارد کن")
        x2 = st.text_input("چه برنامه ای داری؟")
        x3 = st.multiselect("چه روز هایی؟",["شنبه","یک شنبه","دو شنبه","سه شنبه","چهار شنبه","پنج شنبه","جمعه"])
        x4 = st.time_input("از چه ساعتی کارت شروع میشه؟",value = datetime.time(0, 0))
        x5 = st.time_input("تا چه ساعتی در گیری؟" , value = datetime.time(0, 0))
        if st.button("ثبت نهایی" , use_container_width=True):
            with open("data.json", "r", encoding="utf-8") as file:
                saver = json.load(file) 
            rerun = saver["rerun"]
            rerun_day = saver["rerun_day"]
            rerun_en_time = saver["rerun_en_time"]
            rerun_st_time = saver["rerun_st_time"]

            i = 1
            for i in rerun:
                if rerun[i] == "":
                    rerun.update({f"{i}" : f"{x2}"})
                    rerun_day.update({f"{i}" : x3 })
                    rerun_en_time.update({f"{i}" : f"{x5.strftime("%H:%M")}"})
                    rerun_st_time.update({f"{i}" : f"{x4.strftime("%H:%M")}"})
                    break
            
            rerun = saver["rerun"]
            rerun_day = saver["rerun_day"]
            rerun_en_time = saver["rerun_en_time"]
            rerun_st_time = saver["rerun_st_time"]
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(saver, file, ensure_ascii=False)
            x2 = x3 = x4 = x5 = x6 = ()
            st.session_state.page = 1
            st.rerun()

if st.session_state.page == 5:
    with col2: 
        with open("data.json", "r", encoding="utf-8") as file:
            saver = json.load(file) 
        rerun = saver["rerun"]
        rerun_day = saver["rerun_day"]
        rerun_en_time = saver["rerun_en_time"]
        rerun_st_time = saver["rerun_st_time"]
        i = 1
        st.title("برنامه های موجود")
        for i in rerun :
            if rerun[i] != "":
                st.write (rerun[i])
                st.write (f"از ساعت {rerun_st_time[i]} تا ساعت {rerun_en_time[i]}")
                for j in rerun_day[i]:
                    rer = " , ".join(rerun_day[i])
                st.write (f"روز های {rer}")
                if st.button("حذف برنامه",key = f"del{i}", use_container_width=True):
                    rerun.update({f"{i}" : ""})
                    rerun_day.update({f"{i}" : ""})
                    rerun_en_time.update({f"{i}" : ""})
                    rerun_st_time.update({f"{i}" : ""})
                    rerun = saver["rerun"]
                    erun_day = saver["rerun_day"]
                    rerun_en_time = saver["rerun_en_time"]
                    rerun_st_time = saver["rerun_st_time"]
                    with open("data.json", "w", encoding="utf-8") as file:
                        json.dump(saver, file, ensure_ascii=False)
                    st.rerun ()

if st.session_state.page == 6:
    with col2:
        st.title("اطلاعات رو وارد کن")
        x2 = st.text_input("عادت جدیدت چیه؟")
        x3 = st.number_input("چقدر امتیاز مثبت داره؟" , min_value=0 , max_value= 7)
        x4 = st.number_input("چقدر امتیاز منفی داره؟" , min_value=0 , max_value=20)
        x5 = st.text_area("یک مقدار توضیح بده")
        if st.button("ثبت نهایی" , use_container_width=True):
            with open("data.json", "r", encoding="utf-8") as file:
                saver = json.load(file)

            habit = saver["habit"]
            habit_score_ne = saver["habit_score_ne"]
            habit_score_pl = saver["habit_score_pl"]
            habit_abu = saver["habit_abu"]

            i = 1
            while i <= 15:
                if habit.get(f"{i}", "") == "":
                    break
                i += 1
            
            if i <= 15:
                print('ok')
                habit.update({f"{i}" : f"{x2}"})
                habit_score_ne.update({f"{i}" : f"{x4}"})
                habit_score_pl.update({f"{i}" : f"{x3}"})
                habit_abu.update({f"{i}" : f"{x5}"})

                habit = saver["habit"]
                habit_score_ne = saver["habit_score_ne"]
                habit_score_pl = saver["habit_score_pl"]
                habit_abu = saver["habit_abu"]
        
                with open("data.json", "w", encoding="utf-8") as file:
                    json.dump(saver, file, ensure_ascii=False)
                st.session_state.page = 1
                st.rerun()
                i = 0
            else:
                st.title("جا برای عادت جدید نداری")
                st.session_state.page = 9
                st.rerun
                i = 0
if st.session_state.page == 7:
    with col2: 
        st.title("عادت های موجود")

        with open("data.json", "r", encoding="utf-8") as file:
            saver = json.load(file)

        habit = saver["habit"]
        habit_score_ne = saver["habit_score_ne"]
        habit_score_pl = saver["habit_score_pl"]
        habit_abu = saver["habit_abu"]

        for i in habit:
            if habit[f"{i}"] != "" :
                st.write(habit[f"{i}"])
                st.write(f"امتیاز انجام ندادن {habit_score_ne[f"{i}"]} ")
                st.write(f"امتیاز انجام دادن {habit_score_pl[f"{i}"]}")
                st.write(f" در باره عادت : {habit_abu [f"{i}"]}")
                with col2:
                    if st.button("حذف عادت",key = f"del{i}", use_container_width=True):
                        habit.update({f"{i}" : ""})
                        habit_score_ne.update({f"{i}" : ""})
                        habit_score_pl.update({f"{i}" : ""})
                        habit_abu.update({f"{i}" : ""})

                        habit = saver["habit"]
                        habit_score_ne = saver["habit_score_ne"]
                        habit_score_pl = saver["habit_score_pl"]
                        habit_abu = saver["habit_abu"]

                        with open("data.json", "w", encoding="utf-8") as file:
                            json.dump(saver, file, ensure_ascii=False)
                        st.rerun()

if st.session_state.page == 8:
    with col2: 
        with open("data.json", "r", encoding="utf-8") as file:
            saver = json.load(file) 
        habit_do = saver ["habit_do"]
        y_day = saver ["y_day"]
        score_habit = saver ["score_habit"]
        st.title("کارنامه عادات")
        if hour > 1 :
            if to_day != y_day :
                for i in habit:
                    if habit[i] != "":
                        if habit_do[i] == "":
                            (score_habit) -= int(habit_score_ne[i] or 0)
                        else:
                            (score_habit) += int(habit_score_pl[i] or 0)
                for i in habit_do:
                    habit_do[i] = ""
                y_day = to_day
                saver["habit_do"] = habit_do
                saver["y_day"] = y_day
                saver["score_habit"] = score_habit
                with open("data.json", "w", encoding="utf-8") as file:
                    json.dump(saver, file, ensure_ascii=False)
        st.write(f"امتیاز هایی جمع کردی{score_habit}")
        st.markdown("<hr style='border: 3px solid #E89B5F;'>", unsafe_allow_html=True)
        st.write("کتاب جدید")
        st.write("هزینه 150 امتیاز")
        if st.button("پرداخت 150 امتیاز" , use_container_width=True):
            with open("data.json", "r", encoding="utf-8") as file:
                saver = json.load(file) 
            score_habit = saver ["score_habit"]
            if score_habit >= 150 :
                st.write("با موفقیت از امتیاز ها کم شد")
                score_habit = score_habit - 150
            else:
                st.write("موجودی ناکافی")
            saver["score_habit"] = score_habit
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(saver, file, ensure_ascii=False)
            st.markdown("<hr style='border: 3px solid #E89B5F;'>", unsafe_allow_html=True)
        st.write("صد تومن خرید از کتاب شهر")
        st.write("هزینه 200 امتیاز")
        if st.button("پرداخت 200 امتیاز" , use_container_width=True):
            with open("data.json", "r", encoding="utf-8") as file:
                saver = json.load(file) 
            score_habit = saver ["score_habit"]
            if score_habit >= 200 :
                st.write("با موفقیت از امتیاز ها کم شد")
                score_habit = score_habit - 200
            else:
                st.write("موجودی ناکافی")
            saver["score_habit"] = score_habit
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(saver, file, ensure_ascii=False)
            st.markdown("<hr style='border: 3px solid #E89B5F;'>", unsafe_allow_html=True)
        st.write("پنج دقیقه ازاد شدن تایم موبایل")
        st.write("هزینه 50 امتیاز")
        if st.button("پرداخت 50 امتیاز" , use_container_width=True ):
            with open("data.json", "r", encoding="utf-8") as file:
                saver = json.load(file) 
            score_habit = saver ["score_habit"]
            if score_habit >= 50 :
                st.write("با موفقیت از امتیاز ها کم شد")
                score_habit = score_habit - 50
            else:
                st.write("موجودی ناکافی")
            saver["score_habit"] = score_habit
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(saver, file, ensure_ascii=False)
            st.markdown("<hr style='border: 3px solid #E89B5F;'>", unsafe_allow_html=True)
        st.write("صد مگ نت برای دانلود بازی")
        st.write("هزینه 75 امتیاز")
        if st.button("پرداخت 75 امتیاز" , use_container_width=True):
            with open("data.json", "r", encoding="utf-8") as file:
                saver = json.load(file) 
            score_habit = saver ["score_habit"]
            if score_habit >= 75 :
                st.write("با موفقیت از امتیاز ها کم شد")
                score_habit = score_habit - 75
            else:
                st.write("موجودی ناکافی")
            saver["score_habit"] = score_habit
            with open("data.json", "w", encoding="utf-8") as file:
                json.dump(saver, file, ensure_ascii=False)

if st.session_state.page == 9:
    with col2:
        file =  st.file_uploader("فایل بکاپ رو وارد کن",type='json')
        if st.button("آپلود", use_container_width=True):
            if file is not None:
                data = json.load(file)
                with open("data.json", "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False,indent=4)
                    st.write("جای گذاری شد")
            
        st.download_button(
    "دانلود بکاپ",
    data=open("data.json","rb"),
    file_name="data2.json" ,
    mime="application/json",
    use_container_width=True)
       

        

if st.session_state.page != 0 and st.session_state.page != 1:
    with col2:
        if st.button("بازگشت" , use_container_width=True):
            st.session_state.page = 1
            st.rerun()





