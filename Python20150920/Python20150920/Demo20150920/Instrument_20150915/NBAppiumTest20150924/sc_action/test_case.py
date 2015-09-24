# -*- coding:utf-8 -*-

import path
import xmind
import logging
import logging.config
from xmind.core.topic import TopicElement
# PATH = os.path.dirname(__file__)

# print xmind_file

LSubTopics = []  #终点节点
getParentTopicByID_Dic = {}
getTopicByID_Dic = {}

logger = logging.getLogger("log_NB")

def get_LSubTopics(topic):
    #初始化主题关系链
    if topic.getSubTopics() == None:
        LSubTopics.append(topic)

    else:
        for subtopic in topic.getSubTopics():
            get_LSubTopics(subtopic)
            getParentTopicByID_Dic[subtopic.getID()] = topic
            getTopicByID_Dic[subtopic.getID()] = subtopic

def testcase_list_init(topic,testcase_list):

    if topic.getType() == "root":
        testcase_list.append(topic)
        return
    else:
        testcase_list.append(topic)
        testcase_list_init(getParentTopicByID_Dic[topic.getID()] ,testcase_list)

def get_testcase_list(topic):
    testcase_list = []
    testcase_list_init(topic ,testcase_list)

    return testcase_list


class Tcase():

    caseCheckPoint = []
    caseList = []
    caseCount = 0
    def __init__(self,ui_case = 0):
        if ui_case == 0:
            test_file = path.get_multi_platform(path.PATH + r'/conf/release.xmind')
        else:
            test_file = path.get_multi_platform(path.PATH + r'/conf/test.xmind')

        logger.info('test_file:'+test_file)
        w = xmind.load(test_file)
        s1=w.getPrimarySheet() # get the first sheet

        r1=s1.getRootTopic() # get the root topic of this sheet

        r1.getSubTopics()

        get_LSubTopics(r1)

        Tcase.caseCheckPoint = LSubTopics
        Tcase.caseCount = LSubTopics.__len__()

    def getCaseList(self,i):
        """:rtype: list of TopicElement """

        return get_testcase_list(Tcase.caseCheckPoint[i-1])

if __name__ == "__main__":
    myclass = Tcase()

