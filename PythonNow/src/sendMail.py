#!/usr/bin/python
#coding=utf-8

from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEMultipart import MIMEMultipart
import mimetypes,smtplib



class getData:
    def __init__(self,**mesgCon):
        ###邮件附件
        self.messageFilie=mesgCon["MAIL_ATTCH"]
        ###邮件标题
        self.message=mesgCon["MAIL_TITLE"]
        ###邮件发送列表
        self.MAIL_LIST = []
        self.MAIL_LIST = mesgCon["MAIL_LIST"].split(",")
        ###邮件发送服务器
        self.MAIL_HOST = str.replace((mesgCon["MAIL_HOST"]),"'","")
        ###邮件发送人
        self.MAIL_USER = str.replace((mesgCon["MAIL_USER"]),"'","")
        ###邮件发送密码
        self.MAIL_PASS = str.replace((mesgCon["MAIL_PASS"]),"'","")
        ###邮件接收服务器
        self.MAIL_POSTFIX = str.replace((mesgCon["MAIL_POSTFIX"]),"'","")
        ###邮件发送人
        self.MAIL_FROM = r"<" + self.MAIL_USER + ">" 
        ###邮件正文
        self.MAIL_CON = mesgCon["MAIL_CON"]
        ###邮件标题
        self.MAIL_SUB = mesgCon["MAIL_SUB"]
        
        ###邮件内嵌对象.初始增加六个
        self.MAIL_IMG1=mesgCon["MAIL_IMG1"]
        self.MAIL_IMG2=mesgCon["MAIL_IMG2"]
        self.MAIL_IMG3=mesgCon["MAIL_IMG3"]
        self.MAIL_IMG4=mesgCon["MAIL_IMG4"]
        self.MAIL_IMG5=mesgCon["MAIL_IMG5"]
        self.MAIL_IMG6=mesgCon["MAIL_IMG6"]
        

    
    def __addimg__(self,src,imgid):
        fp = open(src,'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', imgid)   
        return msgImage
             
    def __sendmail__(self): 
        try:
            message = MIMEMultipart('related')
            text_msg = MIMEText(self.MAIL_CON,_subtype='html',_charset="utf-8")
            message.attach(text_msg)
            message["Subject"] = self.MAIL_SUB
            message["From"] = self.MAIL_FROM
            message["To"] = ";".join(self.MAIL_LIST)
            
            ###如果没有附件,则直接发送邮件正文.
            if self.messageFilie == None:
                ctype = 'application/octet-stream' 
                maintype, subtype = ctype.split("/", 1)
                
                ###需要判断下是否有内嵌对象.
                ###添加邮件正文内嵌对象
                if self.MAIL_IMG1 != None:
                    message.attach(self.__addimg__(self.MAIL_IMG1,'img1'))
                
                if self.MAIL_IMG2 != None:
                    message.attach(self.__addimg__(self.MAIL_IMG2,'img2'))
                    
                if self.MAIL_IMG3 != None:
                    message.attach(self.__addimg__(self.MAIL_IMG3,'img3'))
                    
                if self.MAIL_IMG4 != None:
                    message.attach(self.__addimg__(self.MAIL_IMG4,'img4'))
                    
                if self.MAIL_IMG5 != None:
                    message.attach(self.__addimg__(self.MAIL_IMG5,'img5'))
                    
                if self.MAIL_IMG6 != None:
                    message.attach(self.__addimg__(self.MAIL_IMG6,'img6'))
                ###添加邮件正文内嵌对象
                smtp = smtplib.SMTP()
                smtp.set_debuglevel(0)
                smtp.connect(self.MAIL_HOST)
                smtp.login(self.MAIL_USER, self.MAIL_PASS)
                smtp.sendmail(self.MAIL_FROM, self.MAIL_LIST, message.as_string())
                smtp.quit()
                
            else:
                ctype, encoding = mimetypes.guess_type(self.messageFilie)
                ctype=None
                #print 'ctype[%s], encoding[%s],self.MAIL_USER[%s], self.MAIL_PASS[%s]'%(ctype, encoding,self.MAIL_USER, self.MAIL_PASS)
                if ctype is None or encoding is not None:
                    ctype = 'application/octet-stream' 
                    maintype, subtype = ctype.split("/", 1)
                    
                    ###添加邮件附件
                    attachment = MIMEImage((lambda f: (f.read(), f.close()))(open(self.messageFilie, "rb"))[0], _subtype = subtype)
                    attachment.add_header("Content-Disposition", "attachment", filename = self.messageFilie.split("\\")[-1])
                    message.attach(attachment)
                    ###添加邮件附件
                    
                    ###需要判断下是否有内嵌对象.
                    ###添加邮件正文内嵌对象
                    if self.MAIL_IMG1 != None:
                        message.attach(self.__addimg__(self.MAIL_IMG1,'img1'))
                
                    if self.MAIL_IMG2 != None:
                        message.attach(self.__addimg__(self.MAIL_IMG2,'img2'))
                        
                    if self.MAIL_IMG3 != None:
                        message.attach(self.__addimg__(self.MAIL_IMG3,'img3'))
                        
                    if self.MAIL_IMG4 != None:
                        message.attach(self.__addimg__(self.MAIL_IMG4,'img4'))
                        
                    if self.MAIL_IMG5 != None:
                        message.attach(self.__addimg__(self.MAIL_IMG5,'img5'))
                        
                    if self.MAIL_IMG6 != None:
                        message.attach(self.__addimg__(self.MAIL_IMG6,'img6'))
                    ###添加邮件正文内嵌对象
                    
                    smtp = smtplib.SMTP()
                    ###邮件调试信息,值越大,打印信息越详细.为0则不打印.
                    smtp.set_debuglevel(0)
                    smtp.connect(self.MAIL_HOST)
                    smtp.login(self.MAIL_USER, self.MAIL_PASS)
                    smtp.sendmail(self.MAIL_FROM, self.MAIL_LIST, message.as_string())
                    smtp.quit()
        except Exception, errmsg: 
            print "Send mail failed to: %s" % errmsg



if __name__ == "__main__":
    mydict={}
    ###邮件附件路径.为空时给None即可.
    mydict["MAIL_ATTCH"]="02h_o.png"
    ###邮件收件人列表
    mydict["MAIL_LIST"]="收件人邮件列表,以逗号分隔"
    ###邮箱服务器地址
    mydict["MAIL_HOST"]="172.16.9.127"
    ###邮件发送人邮箱
    mydict["MAIL_USER"]="发件人邮件"
    ###邮件发送人密码
    mydict["MAIL_PASS"]="发件人邮箱密码"
    ###邮箱服务器地址
    mydict["MAIL_POSTFIX"]="172.16.9.185"
    ###邮件正文
    mydict["MAIL_CON"]=""" <style> .table_border{     border: solid 1px #B4B4B4;     border-collapse: collapse; --折叠样式. } .table_border tr th{     background:url("../../images/gray/bg_table_th.gif") repeat;     padding-left:4px;     height:27px;     border: solid 1px #B4B4B4; } .table_border tr td{     height:25px;     padding:4px;     border: solid 1px #B4B4B4; } th { text-align:left; } td { border: 1px solid #C1DAD7; background: #fff; font-size:11px; padding: 6px 6px 6px 12px; color: #4f6b72; } td.alt { background: #F5FAFA; color: #797268; } </style> <table width="100%" border="0" align="center" class="table_border"> <tr>这个就是本次的示例,附件可以为任何格式的附件,本样例中的附件为图片;正文中的文件为html样式,可以引入图片</tr></br></br><tr><img src="cid:img1" height:50% width:50%></tr></table><br><br> """
    ###邮件标题
    mydict["MAIL_SUB"]=u"中文测试"
    ###图片附件为空时给None即可.
    mydict["MAIL_IMG1"]="ph1.png"
    mydict["MAIL_IMG2"]=None
    mydict["MAIL_IMG3"]=None
    mydict["MAIL_IMG4"]=None
    mydict["MAIL_IMG5"]=None
    mydict["MAIL_IMG6"]=None
    #print mydict
    
    getData(**mydict).__sendmail__()
    
    
    
    
    
    
    
    
