from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import time
import os
from datetime import date

classes_with_number_prefix = {
"Spanish 1 A" : "011 Spanish 1 A" ,
"Spanish 1 B" : "011 Spanish 1 B" ,
"Spanish 2 A" : "012 Spanish 2 A" ,
"Spanish 2 B" : "012 Spanish 2 B" ,
"Spanish 2 Honors A" : "012H Spanish 2 Honors A" ,
"Spanish 2 Honors B" : "012H Spanish 2 Honors B" ,
"Spanish 3 A" : "013 Spanish 3 A" ,
"Spanish 3 B" : "013 Spanish 3 B" ,
"Spanish 3 Honors A" : "013H Spanish 3 Honors A" ,
"Spanish 3 Honors B" : "013H Spanish 3 Honors B" ,
"Spanish 4 A" : "014 Spanish 4 A" ,
"Spanish 4 B" : "014 Spanish 4 B" ,
"Spanish 4 Honors A" : "014H Spanish 4 Honors A" ,
"Spanish 4 Honors B" : "014H Spanish 4 Honors B" ,
"Spanish 5 A" : "015 Spanish 5 A" ,
"Spanish 5 Honors A" : "015H Spanish 5 Honors A" ,
"French 1 A" : "021 French 1 A" ,
"French 1 B" : "021 French 1 B" ,
"French 2 A" : "022 French 2 A" ,
"French 2 B" : "022 French 2 B" ,
"French 2 Honors A" : "022H French 2 Honors A" ,
"French 2 Honors B" : "022H French 2 Honors B" ,
"French 3 A" : "023 French 3 A" ,
"French 3 B" : "023 French 3 B" ,
"French 4 A": "024 French 4 A",
"French 4 B": "024 French 4 B",
"French 5 A": "025 French 5 A",
"French 5 B": "025 French 5 B",
"Japanese 1 A" : "031 Japanese 1 A" ,
"Japanese 1 B" : "031 Japanese 1 B" ,
"Japanese 1 Honors A" : "031H Japanese 1 Honors A" ,
"Japanese 1 Honors B" : "031H Japanese 1 Honors B" ,
"Japanese 2 A" : "032 Japanese 2 A" ,
"Japanese 2 B" : "032 Japanese 2 B" ,
"Japanese 2 Honors A" : "032H Japanese 2 Honors A" ,
"Japanese 2 Honors B" : "032H Japanese 2 Honors B" ,
"Japanese 3 A" : "033 Japanese 3 A" ,
"Japanese 3 B" : "033 Japanese 3 B" ,
"MS Japanese A" : "036 MS Japanese A" ,
"MS Japanese B" : "036 MS Japanese B" ,
"ASL 1 A" : "041 ASL 1 A" ,
"ASL 1 B" : "041 ASL 1 B" ,
"ASL 1 Honors A" : "041H ASL 1 Honors A" ,
"ASL 1 Honors B" : "041H ASL 1 Honors B" ,
"ASL 2 A" : "042 ASL 2 A" ,
"ASL 2 B" : "042 ASL 2 B" ,
"ASL 2 Honors A" : "042H ASL 2 Honors A" ,
"ASL 2 Honors B" : "042H ASL 2 Honors B" ,
"ASL 3 A" : "043 ASL 3 A" ,
"ASL 3 B" : "043 ASL 3 B" ,
"ASL 3 Honors A" : "043H ASL 3 Honors A" ,
"ASL 3 Honors A" : "043H ASL 3 Honors A" ,
"Italian 1 A" : "051 Italian 1 A" ,
"Italian 1 B" : "051 Italian 1 B" ,
"Italian 2 A" : "052 Italian 2 A" ,
"German 1 A" : "061 German 1 A" ,
"German 1 B" : "061 German 1 B" ,
"German 2 A" : "062 German 2 A" ,
"German 2 B" : "062 German 2 B" ,
"Hebrew 1 A" : "071 Hebrew 1 A" ,
"Hebrew 1 B" : "071 Hebrew 1 B" ,
"Mandarin 1 A" : "081 Mandarin 1 A" ,
"Mandarin 1 B" : "081 Mandarin 1 B" ,
"Mandarin 2 A" : "082 Mandarin 2 A" ,
"Mandarin 2 B" : "082 Mandarin 2 B" ,
"Mandarin 3 A" : "083 Mandarin 3 A" ,
"Mandarin 3 B" : "083 Mandarin 3 B" ,
"MS Latin 1 A" : "090 MS Latin 1 A" ,
"MS Latin 1 B" : "090 MS Latin 1 B" ,
"Latin 1 A" : "091 Latin 1 A" ,
"Latin 1 B" : "091 Latin 1 B" ,
"Latin 2 A" : "092 Latin 2 A" ,
"Latin 2 B" : "092 Latin 2 B" ,
"Latin 3 A" : "093 Latin 3 A" ,
"Latin 3 B" : "093 Latin 3 B" ,
"Latin 4 A" : "094 Latin 4 A" ,
"Latin 4 B" : "094 Latin 4 B" ,
"Latin 4 Honors A" : "094H Latin 4 Honors A" ,
"World Language Conversation A" : "098 World Language Conversation A" ,
"World Language Conversation A" : "098 World Language Conversation A" ,
"Independent PE 6 A" : "1000: Independent PE 6 A" ,
"Independent PE 7 A" : "1001: Independent PE 7 A" ,
"Independent PE 8 A" : "1002: Independent PE 8 A" ,
"MS Health" : "1010 MS Health" ,
"Group PE 3 A" : "1013 Group PE 3 A" ,
"Foundations of Personal Fitness 1 A" : "1015 Foundations of Personal Fitness 1 A" ,
"Foundations of Personal Fitness 1 B" : "1015 Foundations of Personal Fitness 1 B" ,
"Foundations of Personal Fitness 2 A" : "1016 Foundations of Personal Fitness 2 A" ,
"Foundations of Personal Fitness 2 B" : "1016 Foundations of Personal Fitness 2 B" ,
"Foundations of Personal Fitness 3 A" : "1017 Foundations of Personal Fitness 3 A" ,
"Foundations of Personal Fitness 3 B" : "1017 Foundations of Personal Fitness 3 B" ,
"Foundations of Personal Fitness 4 A" : "1018 Foundations of Personal Fitness 4 A" ,
"Foundations of Personal Fitness 4 B" : "1018 Foundations of Personal Fitness 4 B" ,
"Yoga A" : "1021 Yoga A" ,
"Yoga B" : "1021 Yoga B" ,
"Yoga 2 A" : "1022 Yoga 2 A" ,
"Yoga 2 B" : "1022 Yoga 2 B" ,
"Yoga 3 A" : "1023 Yoga 3 A" ,
"Yoga 3 B Accelerated" : "1023 Yoga 3 B Accelerated" ,
"MS Foundations of Personal Fitness 6 A" : "1041 MS Foundations of Personal Fitness 6 A" ,
"MS Foundations of Personal Fitness 6 B" : "1041 MS Foundations of Personal Fitness 6 B" ,
"MS Foundations of Personal Fitness 7 A" : "1042 MS Foundations of Personal Fitness 7 A" ,
"MS Foundations of Personal Fitness 7 B" : "1042 MS Foundations of Personal Fitness 7 B" ,
"MS Foundations of Personal Fitness 8 A" : "1043 MS Foundations of Personal Fitness 8 A" ,
"MS Foundations of Personal Fitness 8 B" : "1043 MS Foundations of Personal Fitness 8 B" ,
"HS Physical Education-Blended B" : "1050 HS Physical Education-Blended B" ,
"MS Physical Education-Blended B" : "1060 MS Physical Education-Blended B" ,
"Pre-Algebra A" : "109 Pre-Algebra A" ,
"Pre-Algebra B" : "109 Pre-Algebra B" ,
"MS Algebra 1 A" : "110 MS Algebra 1 A" ,
"MS Algebra 1 B" : "110 MS Algebra 1 B" ,
"Algebra 1 A" : "111 Algebra 1 A" ,
"Algebra 1 B" : "111 Algebra 1 B" ,
"Independent PE 1 A" : "1111: Independent PE 1 A" ,
"Independent PE 1 B" : "1111: Independent PE 1 B" ,
"Independent PE 2 A" : "1112: Independent PE 2 A" ,
"Independent PE 2 B" : "1112: Independent PE 2 B" ,
"Independent PE 3 A" : "1113: Independent PE 3 A" ,
"Independent PE 3 B" : "1113: Independent PE 3 B" ,
"Independent PE 4 A" : "1114: Independent PE 4 A" ,
"Independent PE 4 B" : "1114: Independent PE 4 B" ,
"Algebra 1 Honors A" : "111H Algebra 1 Honors A" ,
"Algebra 1 Honors B" : "111H Algebra 1 Honors B" ,
"Algebra 2 A" : "112 Algebra 2 A" ,
"Algebra 2 with Trigonometry A" : "112 Algebra 2 with Trigonometry A" ,
"Algebra 2 with Trigonometry B" : "112 Algebra 2 with Trigonometry B" ,
"Algebra 2 with Trigonometry Honors A" : "112H Algebra 2 with Trigonometry Honors A" ,
"Algebra 2 with Trigonometry Honors B" : "112H Algebra 2 with Trigonometry Honors B" ,
"Algebra 1A A" : "114 Algebra 1A A" ,
"Algebra 1A B" : "114 Algebra 1A B" ,
"Algebra 1B A" : "115 Algebra 1B A" ,
"Algebra 1B B" : "115 Algebra 1B B" ,
"Geometry A" : "121 Geometry A" ,
"Geometry B" : "121 Geometry B" ,
"Geometry Honors A" : "121H Geometry Honors A" ,
"Geometry Honors B" : "121H Geometry Honors B" ,
"Pre-Calculus A" : "141 Pre-Calculus A" ,
"Pre-Calculus B": "141 Pre-Calculus B",
"Pre-Calculus Honors A" : "141H Pre-Calculus Honors A" ,
"Pre-Calculus Honors B" : "141H Pre-Calculus Honors B" ,
"Calculus A" : "142 Calculus A" ,
"Calculus B" : "142 Calculus B" ,
"Calculus Honors A" : "142H Calculus Honors A" ,
"Calculus Honors B" : "142H Calculus Honors B" ,
"Statistics A" : "151 Statistics A" ,
"Statistics B" : "151 Statistics B" ,
"Statistics Honors A" : "151H Statistics Honors A" ,
"Statistics Honors B" : "151H Statistics Honors B" ,
"Business Math 1 A" : "161 Business Math 1 A" ,
"Business Math 1 B" : "161 Business Math 1 B" ,
"Business Math A" : "161 Business Math A" ,
"Business Math B" : "161 Business Math B" ,
"Consumer Math 1 A" : "162 Consumer Math 1 A" ,
"Consumer Math 1 B" : "162 Consumer Math 1 B" ,
"Consumer Math A" : "162 Consumer Math A" ,
"Consumer Math B" : "162 Consumer Math B" ,
"Trigonometry A" : "171 Trigonometry A" ,
"Personal Finance" : "172 Personal Finance" ,
"Personal Finance A" : "172 Personal Finance A" ,
"Integrated Math 1 A" : "181 Integrated Math 1 A" ,
"Integrated Math 1 B" : "181 Integrated Math 1 B" ,
"Integrated Math 2 A" : "182 Integrated Math 2 A" ,
"Integrated Math 2 B" : "182 Integrated Math 2 B" ,
"Integrated Math 3 A" : "183 Integrated Math 3 A" ,
"Integrated Math 3 B" : "183 Integrated Math 3 B" ,
"MS Earth Science A" : "206 MS Earth Science A" ,
"MS Earth Science B" : "206 MS Earth Science B" ,
"Life Science 7 A" : "207 Life Science 7 A" ,
"Life Science 7 B" : "207 Life Science 7 B" ,
"MS Life Science A" : "207 MS Life Science A" ,
"MS Life Science B" : "207 MS Life Science B" ,
"MS Physical Science A" : "208 MS Physical Science A" ,
"MS Physical Science B" : "208 MS Physical Science B" ,
"Physical Science 8 A" : "208 Physical Science 8 A" ,
"Physical Science 8 B" : "208 Physical Science 8 B" ,
"Earth Space Science A" : "211 Earth Space Science A" ,
"Earth Space Science B" : "211 Earth Space Science B" ,
"Conceptual Physics A" : "215 Conceptual Physics A" ,
"Conceptual Physics B" : "215 Conceptual Physics B" ,
"MS Integrated Science 1 A" : "216 MS Integrated Science 1 A" ,
"MS Integrated Science 1 B" : "216 MS Integrated Science 1 B" ,
"MS Integrated Science 2 A" : "217 MS Integrated Science 2 A" ,
"MS Integrated Science 2 B" : "217 MS Integrated Science 2 B" ,
"MS Integrated Science 3 A" : "218 MS Integrated Science 3 A" ,
"MS Integrated Science 3 B" : "218 MS Integrated Science 3 B" ,
"Biology A" : "221 Biology A" ,
"Biology B" : "221 Biology B" ,
"Biology Honors A" : "221H Biology Honors A" ,
"Biology Honors B" : "221H Biology Honors B" ,
"Marine Biology A" : "222 Marine Biology A" ,
"Marine Biology B" : "222 Marine Biology B" ,
"Forensic Science A" : "225 Forensic Science A" ,
"Forensic Science B" : "225 Forensic Science B" ,
"Physics A" : "231 Physics A" ,
"Physics B" : "231 Physics B" ,
"Physics Honors A" : "231H Physics Honors A" ,
"Physics Honors B" : "231H Physics Honors B" ,
"Chemistry A" : "241 Chemistry A" ,
"Chemistry B" : "241 Chemistry B" ,
"Chemistry Honors A" : "241H Chemistry Honors A" ,
"Chemistry Honors B" : "241H Chemistry Honors B" ,
"Integrated Science Physics and Chemistry A" : "242 Integrated Science Physics and Chemistry A" ,
"Integrated Science Physics and Chemistry B" : "242 Integrated Science Physics and Chemistry B" ,
"Conceptual Chemistry A" : "243 Conceptual Chemistry A" ,
"Conceptual Chemistry B" : "243 Conceptual Chemistry B" ,
"Organic Chemistry A" : "244 Organic Chemistry A" ,
"Organic Chemistry B" : "244 Organic Chemistry B" ,
"Environmental Science A" : "251 Environmental Science A" ,
"Environmental Science B" : "251 Environmental Science B" ,
"Anatomy and Physiology A" : "261 Anatomy and Physiology A" ,
"Anatomy and Physiology B" : "261 Anatomy and Physiology B" ,
"Anatomy and Physiology Honors A" : "261H Anatomy and Physiology Honors A" ,
"Anatomy and Physiology Honors B" : "261H Anatomy and Physiology Honors B" ,
"Astronomy A" : "271 Astronomy A" ,
"Astronomy B" : "271 Astronomy B" ,
"Astronomy Honors A" : "271H Astronomy Honors A" ,
"Astronomy Honors B" : "271H Astronomy Honors B" ,
"Robotics A" : "275 Robotics A" ,
"Robotics B" : "275 Robotics B" ,
"Integrated Science 1 A" : "291 Integrated Science 1 A" ,
"Integrated Science 1 B" : "291 Integrated Science 1 B" ,
"Integrated Science 2 A" : "292 Integrated Science 2 A" ,
"Integrated Science 2 B" : "292 Integrated Science 2 B" ,
"Integrated Science 3 A" : "293 Integrated Science 3 A" ,
"Integrated Science 3 B" : "293 Integrated Science 3 B" ,
"English 6 A" : "306 English 6 A" ,
"English 6 B" : "306 English 6 B" ,
"Language Arts 6 A" : "306 Language Arts 6 A" ,
"Language Arts 6 B" : "306 Language Arts 6 B" ,
"English 7 A" : "307 English 7 A" ,
"English 7 B" : "307 English 7 B" ,
"Language Arts 7 A" : "307 Language Arts 7 A" ,
"Language Arts 7 B" : "307 Language Arts 7 B" ,
"English 8 A" : "308 English 8 A" ,
"English 8 B" : "308 English 8 B" ,
"Language Arts 8 A" : "308 Language Arts 8 A" ,
"Language Arts 8 B" : "308 Language Arts 8 B" ,
"English 9 A" : "311 English 9 A" ,
"English 9 B" : "311 English 9 B" ,
"English 9 Honors A" : "311H English 9 Honors A" ,
"English 9 Honors B" : "311H English 9 Honors B" ,
"English 10 A" : "312 English 10 A" ,
"English 10 B" : "312 English 10 B" ,
"English 10 Honors A" : "312H English 10 Honors A" ,
"English 10 Honors B" : "312H English 10 Honors B" ,
"English 11 A" : "313 English 11 A" ,
"English 11 B" : "313 English 11 B" ,
"English 11 Honors A" : "313H English 11 Honors A" ,
"English 11 Honors B" : "313H English 11 Honors B" ,
"English 12 A" : "314 English 12 A" ,
"English 12 B" : "314 English 12 B" ,
"English 12 Honors A" : "314H English 12 Honors A" ,
"English 12 Honors B" : "314H English 12 Honors B" ,
"Research & Technical Writing A" : "322 Research & Technical Writing A" ,
"Research & Technical Writing B" : "322 Research & Technical Writing B" ,
"Poetry A" : "323 Poetry A" ,
"Poetry B" : "323 Poetry B" ,
"Creative Writing A" : "324 Creative Writing A" ,
"Creative Writing B" : "324 Creative Writing B" ,
"Ancient Civilizations A" : "410 Ancient Civilizations A" ,
"Ancient Civilizations B" : "410 Ancient Civilizations B" ,
"Ancient Civilizations Honors A" : "410 Ancient Civilizations Honors A" ,
"Ancient Civilizations Honors B" : "410 Ancient Civilizations Honors B" ,
"US History A" : "411 US History A" ,
"US History B" : "411 US History B" ,
"US History Honors A" : "411H US History Honors A" ,
"US History Honors B" : "411H US History Honors B" ,
"World History A" : "421 World History A" ,
"World History B" : "421 World History B" ,
"World History Honors A" : "421H World History Honors A" ,
"World History Honors B" : "421H World History Honors B" ,
"Economics" : "431 Economics" ,
"Economics Accelerated" : "431 Economics Accelerated" ,
"Economics Honors" : "431H Economics Honors" ,
"Government" : "432 Government" ,
"Government Honors" : "432H Government Honors" ,
"Controversies in American Politics A" : "433 Controversies in American Politics A" ,
"Controversies in American Politics B" : "433 Controversies in American Politics B" ,
"Cultural Geography A" : "441 Cultural Geography A" ,
"Big History A" : "451 Big History A" ,
"Big History B" : "451 Big History B" ,
"Life Skills A" : "510 Life Skills A" ,
"Life Skills B" : "510 Life Skills B" ,
"Study Skills" : "511 Study Skills" ,
"Study Skills B" : "512 Study Skills B" ,
"Roadtrip Nation" : "517 Roadtrip Nation" ,
"Health" : "520 Health" ,
"Humanities A" : "541 Humanities A" ,
"Philosophy A" : "545 Philosophy A" ,
"Philosophy B" : "545 Philosophy B" ,
"Wellness" : "560 Wellness" ,
"Leadership" : "565 Leadership" ,
"Community Minds A" : "566 Community Minds A" ,
"Community Minds B" : "566 Community Minds B" ,
"Work Experience" : "570 Work Experience" ,
"Business Entrepreneurship" : "572 Business Entrepreneurship" ,
"Social Entrepreneurship" : "574 Social Entrepreneurship" ,
"The Science and Practice of Mindfulness A" : "575 The Science and Practice of Mindfulness A" ,
"Portfolio Development" : "579 Portfolio Development" ,
"Computer Science A" : "611 Computer Science A" ,
"Computer Programming 1 A" : "621 Computer Programming 1 A" ,
"Computer Programming 1 B" : "621 Computer Programming 1 B" ,
"Computer Programming 2 A" : "622 Computer Programming 2 A" ,
"Computer Programming 2 B" : "622 Computer Programming 2 B" ,
"Animation Production A" : "631 Animation Production A" ,
"Animation Production B" : "631 Animation Production B" ,
"MS Digital Photography A" : "703 MS Digital Photography A" ,
"Art 6 A" : "706 Art 6 A" ,
"Art 6 B" : "706 Art 6 B" ,
"Art 7 A" : "707 Art 7 A" ,
"Art 7 B" : "707 Art 7 B" ,
"Art 8 A" : "708 Art 8 A" ,
"Art 8 B" : "708 Art 8 B" ,
"MS Study Skills" : "709 MS Study Skills" ,
"MS Community Minds A" : "710 MS Community Minds A" ,
"MS Community Minds A Accelerated" : "710 MS Community Minds A Accelerated" ,
"Intro to Film and Media A" : "711 Intro to Film and Media A" ,
"Intro to Film and Media B" : "711 Intro to Film and Media B" ,
"Film Studies A" : "715 Film Studies A" ,
"Film Studies B" : "715 Film Studies B" ,
"Graphic Design A" : "731 Graphic Design A" ,
"Graphic Design B" : "731 Graphic Design B" ,
"Digital Photography A" : "741 Digital Photography A" ,
"Digital Photography B" : "741 Digital Photography B" ,
"Digital Photography 2 A" : "742 Digital Photography 2 A" ,
"Advanced Digital Photography A" : "745 Advanced Digital Photography A" ,
"Advanced Digital Photography B" : "745 Advanced Digital Photography B" ,
"Studio Arts A" : "751 Studio Arts A" ,
"Studio Arts B" : "751 Studio Arts B" ,
"Studio Arts 2 A" : "752 Studio Arts 2 A" ,
"Studio Arts 2 B" : "752 Studio Arts 2 B" ,
"Studio Arts 3 A" : "753 Studio Arts 3 A" ,
"Form and Space A" : "757 Form and Space A" ,
"Form and Space B" : "757 Form and Space B" ,
"Advanced Studio Art A" : "758 Advanced Studio Art A" ,
"Advanced Studio Art B" : "758 Advanced Studio Art B" ,
"Sociology A" : "760 Sociology A" ,
"Psychology A" : "761 Psychology A" ,
"Psychology A" : "761 Psychology A" ,
"Psychology B" : "761 Psychology B" ,
"Art History A" : "762 Art History A" ,
"Art History B" : "762 Art History B" ,
"Positive Psychology A" : "763 Positive Psychology A" ,
"Positive Psychology B" : "763 Positive Psychology B" ,
"Acting A" : "771 Acting A" ,
"Social Justice A" : "776 Social Justice A" ,
"Social Justice B" : "776 Social Justice B" ,
"Screenwriting A" : "781 Screenwriting A" ,
"Screenwriting B" : "781 Screenwriting B" ,
"Theatre Appreciation A" : "790 Theatre Appreciation A" ,
"Theatre Appreciation B" : "790 Theatre Appreciation B" ,
"Middle School Elective Course A" : "8888 Middle School Elective Course A" ,
"Middle School Elective Course B" : "8888 Middle School Elective Course B" ,
"Guitar 1 A" : "911 Guitar 1 A" ,
"Guitar 1 B" : "911 Guitar 1 B" ,
"Guitar 2 A" : "912 Guitar 2 A" ,
"Guitar 2 B" : "912 Guitar 2 B" ,
"Recording Arts A" : "922 Recording Arts A" ,
"Recording Arts B" : "922 Recording Arts B" ,
"Recording Arts 2 A" : "923 Recording Arts 2 A" ,
"Recording Arts 2 B" : "923 Recording Arts 2 B" ,
"Advanced Recording Arts B" : "926 Advanced Recording Arts B" ,
"Advanced Recording Arts B" : "926 Advanced Recording Arts B" ,
"Music Theory A" : "933 Music Theory A" ,
"Music Theory B" : "933 Music Theory B" ,
"Music Theory 2 A" : "934 Music Theory 2 A" ,
"Music Theory 2 B" : "934 Music Theory 2 B" ,
"Drums A" : "941 Drums A" ,
"Drums B" : "941 Drums B" ,
"Drums 2 A" : "942 Drums 2 A" ,
"Drums 2 B" : "942 Drums 2 B" ,
"Piano A" : "945 Piano A" ,
"Piano B" : "945 Piano B" ,
"Vocal Fundamentals A" : "954 Vocal Fundamentals A" ,
"Vocal Fundamentals B" : "954 Vocal Fundamentals B" ,
"Vocal Fundamentals 2 A" : "955 Vocal Fundamentals 2 A" ,
"Vocal Fundamentals 2 B" : "955 Vocal Fundamentals 2 B" ,
"DJ Performing Arts A" : "970 DJ Performing Arts A" ,
"DJ Performing Arts B" : "970 DJ Performing Arts B" ,
"Music Appreciation B" : "980 Music Appreciation B" ,
}

def get_full_class_name(plain_class_name):
    try:
        return classes_with_number_prefix[plain_class_name]
    except:
        return plain_class_name

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# # To print Console.log Messages
# d = DesiredCapabilities.CHROME
# d['goog:loggingPrefs'] = { 'browser':'ALL' }
# # print messages
# for entry in browser.get_log('browser'):
#     print(entry)
# browser = webdriver.Chrome(executable_path='C:\\Users\\Andrew\\Documents\\automatic-enrollment-project\\chromedriver.exe',options=options, desired_capabilities=d)

url = 'https://fusion.geniussis.com/PublicWelcome.aspx'
browser = webdriver.Chrome(executable_path='C:\\Users\\Andrew\\Documents\\automatic-enrollment-project\\chromedriver.exe',options=options)
# browser = webdriver.Chrome(executable_path='/home/drew/automatic-enrollment-project/chromedriver.exe')
browser.get(url)

username = browser.find_element_by_id("ctl00_centerLoginContent_tbLogin")
password = browser.find_element_by_id("ctl00_centerLoginContent_tbPassword")

username.send_keys(os.getenv('username_mat'))
password.send_keys(os.getenv('pw_mat'))

browser.find_element_by_id("ctl00_centerLoginContent_btnSignMeIn").click()


browser.find_element_by_id("ctl00_ddChangeRole_chosen").click() # Roles Dropdown
browser.find_element_by_xpath('//*[@id="ctl00_ddChangeRole_chosen"]/div/ul/li[1]').click() # Super User Role
browser.get("https://fusion.geniussis.com/ActiveStudents.aspx") # Students Page
browser.find_element_by_link_text('Practice, Student').click() # Desired Student
browser.find_element_by_link_text('Enroll in Section').click() # Enroll in Section Page


browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddTerm_chosen"]/a/span').click()
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddTerm_chosen"]/div/ul/li[2]').click()
time.sleep(1)




browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbCourse"]').click()
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbCourse"]').send_keys( get_full_class_name("US History A") ) # 

time.sleep(1)
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbCourse"]').send_keys(Keys.DOWN) # down
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbCourse"]').send_keys(Keys.TAB) # enter

browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddSectionType_chosen"]').click() # tab
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddSectionType_chosen"]/div/div/input').click() # tab
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddSectionType_chosen"]/div/div/input').send_keys("FT") # FT 
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddSectionType_chosen"]/div/div/input').send_keys(Keys.ENTER) # enter

browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddTeacher_chosen"]').click() # tab
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddTeacher_chosen"]/div/div/input').click() # tab
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddTeacher_chosen"]/div/div/input').send_keys("Lee") # FT 
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddTeacher_chosen"]/div/div/input').send_keys(Keys.ENTER) # enter

browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddWeeks_chosen"]').click() # tab
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddWeeks_chosen"]/div/div/input').click() # tab
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddWeeks_chosen"]/div/div/input').send_keys("25") # FT 
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_ddWeeks_chosen"]/div/div/input').send_keys(Keys.ENTER) # enter

today_date = date.today().strftime("%m/%d/%Y")
today_date_plus_one_year = today_date[:-1] + str(int(today_date[-1:]) + 1)

browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbSD"]').click() 
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbSD"]').send_keys(today_date) #  
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbSD"]').send_keys(Keys.TAB) # 

browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbED"]').click() 
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbED"]').send_keys(today_date_plus_one_year) #  
browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbSD"]').send_keys(Keys.TAB) # 

browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbSecondaryName"]').click() 
# browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_btnEnroll"]').click() 


# browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbCourse"]').send_keys(Keys.DOWN) # down //*[@id="ctl00_ContentPlaceHolder1_ddTeacher_chosen"]/a/span
# browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbCourse"]').send_keys(Keys.ENTER) # enter
# browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbCourse"]').send_keys(Keys.TAB) # tab
# browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_tbCourse"]').send_keys(Keys.TAB) # tab