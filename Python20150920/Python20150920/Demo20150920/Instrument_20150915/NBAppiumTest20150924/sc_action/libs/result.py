# -*- coding:utf-8 -*-
import path
import exe_status
case_res = {}
failed_path = {}
case_pic = {}
case_purpose = {}


def res_save(res_dic):
    """
    输出测试报表
    @type res_dic:dict
    """
    PATH = path.get_multi_platform(path.PATH + '/result/result.txt')
    res = ""
    # res = res + "成功用例数:" + str(res_dic["p_count"]) + "  失败用例数:" + str(res_dic["f_count"]) + '\n' + '\n'
    # res += "失败用例列表: "

    f = open(PATH, 'w')

    for key in res_dic:

        if failed_path.has_key(key.encode('utf8')) is False:
            failed_path[key.encode('utf8')] = "无"
            t_path = failed_path[key.encode('utf8')]
        else:
            t_path = failed_path[key.encode('utf8')].encode('utf8')
            t_path = t_path[:-1]

        if case_pic.has_key(key.encode('utf8')) is False:
            case_pic[key.encode('utf8')] = ""
            t_pic = case_pic[key.encode('utf8')]
        else:
            t_pic = case_pic[key.encode('utf8')].encode('utf8')
            t_pic = t_pic[:-1]

        if case_purpose.has_key(key.encode('utf8')) is False:
            case_purpose[key.encode('utf8')] = "无"
            t_purpose = case_purpose[key.encode('utf8')]
        else:
            t_purpose = case_purpose[key.encode('utf8')].encode('utf8')

        res = res + str(key)
        res = res + ";" + t_purpose
        res = res + ";" + res_dic[key.encode('utf8')].encode('utf8')
        res = res + ";" + t_pic
        res = res + ";" + t_path + '\n'
    res = res[:-1]
    f.write(res)

    print res
    f.close()

def set_pass_result(case_title):
    if failed_path.has_key(case_title):
        print "pass"
    else:
        case_res[case_title] = "pass"

def set_check_result(check_title):

    """
    设置检查点返回结果
    @type check_title:str
    """
    case_name = exe_status.exe_case_title
    if failed_path.has_key(case_name):
        failed_path[case_name] += check_title + "|"
    else:
        failed_path[case_name] = check_title + "|"
        case_res[case_name] = "failed"





