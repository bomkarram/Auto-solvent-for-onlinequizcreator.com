from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time

#def storeQA(driver):    #this function will return a 2d list of every quastion and its true answer that I will select manually by hovering over a link
#   quastionAnswer = [["x","x"]]
#    while len(quastionAnswer) <= 17:    #^ 17 .. is actully total of 15 quations but 1 for ["x","x"] another for mistake page hovering.
#        
#        soup = BeautifulSoup(driver.page_source, "html.parser")
#
#        quastion = soup.find_all("h1")
#        quastion = quastion[0].text
#        
#        removeFirstSpace = quastion.index(" ")
#        finalquastion = quastion[removeFirstSpace:]
#        finalquastion = finalquastion.strip()
#        
#        answer = soup.find_all("li",{"class":"hover"})
#        for ele in answer:
#            x = ele.find_all("span")
#            for y in x:
#                finalAnswer = y.text
#                finalAnswer = finalAnswer.strip()
#
#                if [finalquastion,finalAnswer] != quastionAnswer[-1] and finalAnswer != "":
#                    quastionAnswer.append([finalquastion,finalAnswer])
#                    print(finalquastion)
#                    print(finalAnswer,"\n")
#                    print(len(quastionAnswer))
#
#                break
#        
#    return quastionAnswer

def main():
    try:
        driver = webdriver.Firefox()
        driver.get("https://www.onlinequizcreator.com/hum-2610-movie-quiz/quiz-183621")
        driver.get("https://www.onlinequizcreator.com/current/site/index.php?r=quiz/start&id=183621&language=en")
        time.sleep(5)
        driver.find_element_by_class_name("button").click()
        log = driver.find_element_by_name("LoginFormModel[email]")
        log.send_keys("****@****.com")
        log = driver.find_element_by_name("LoginFormModel[password]")
        log.send_keys("*****")
        log.send_keys(Keys.RETURN)
        time.sleep(7)

        #quastionAnswer = storeQA(driver)

        quastionAnswer = [['Where did Florentino work when he first daw Femina?', 'The telegram office'], ['In the enemy Adam Bell is a professor of', 'History'], ['How do the other characters know Susanita on Midaq Alley?', 'She is the landlord, owns the building'], ["Salma Hayek's character loves", 'Money'], ["Where does Don Ru's son find him with his boyfriend?", 'In a bath house shower'], ['What is the setting of the play that Melanie acts in?', 'A beauty salon'], ["Salma Hayek's character becomes a", 'Prostitute'], ['In Disgrace, David Lurie is a professor of', 'Romantic poetry'], ['When the men set David on fire one of them appears to be eating', "Mac's Cheese"], ['Which movie used a doppelganger?', 'The Enemy'], ['What does David say about the "trial" experience when asked by a reporter?', '"It was enriching"'], ['How does the doctor die in Love in the Time of Cholera?', 'Falls off a ladder getting a parrot'], ['The first movie we watched from in class was', 'Disgrace'], ['Which movie was set in Columbia?', 'Love in the time of cholera'], ['When David returns back to the city he:', 'Picks up a prostitute']]
        #^^^ The result of calling the upper 2d list


        while True:
            try:
                soup = BeautifulSoup(driver.page_source, "html.parser")
                ul = soup.find_all("ul",{"class":"answers"})
                for li in ul[0]:    # according to html source:
                                    # there are 4 li in the selected ul
                    for qa in quastionAnswer:
                        if qa[1] in str(li) and qa[0] in str(driver.page_source):
                            trueChoice = ul[0].index(li) + 1
                            driver.find_element_by_xpath("//ul[@class='answers']/li[{}]/label/span".format(trueChoice)).click()
                            quastionAnswer.remove(qa)
                            #time.sleep(.3)
            except:
                pass
    except:
        driver.close()
        None
main()
