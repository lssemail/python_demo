# coding:utf8
from bs4 import BeautifulSoup
html_doc = """
   <div id="login-area">
            <ul class="clearfix logined">
                <li class="header-app">
                    <a href="/mobile/app" >
                        <span class="icon-appdownload"></span>
                    </a>
                    <div class="QR-download">
                        <p id="app-text">慕课网APP下载</p>
                        <p id="app-type">iPhone / Android / iPad</p>
                        <img src="/static/img/index/QR-code.jpg">
                    </div>
                </li>
                <li class='remind_warp'>
                    <i class="msg_remind"></i>
                    <a target="_blank" href='/u/1297104/notices'><i class='icon-notifi'></i></a>
                </li>
        	    <li class="my_message">
                    <a href="/u/1297104/messages" title="我的消息" target="_blank">
                        <span class="msg_icon" style="display: none;"></span>
                        <i class="icon-mail"></i>
                        <span style="display: none;">我的消息</span>
                    </a>
                </li>
                <li class="set_btn user-card-box">
                    <a id="header-avator" class="user-card-item" action-type="my_menu"  href="/u/1297104/courses" target="_self"><img src='http://img.mukewang.com/user/533e4caf0001fac402000200-40-40.jpg' width='40' height='40' />
                        <i class="myspace_remind" style="display: none;"></i>
                        <span style="display: none;">动态提醒</span>
                    </a>
                    <div class="g-user-card">
                        <div class="card-inner">
                            <div class="card-top">
                                <a href='/u/1297104/courses'><img src="http://img.mukewang.com/533e4caf0001fac402000200-100-100.jpg" alt="lius" class="l"></a>
                                <a href='/u/1297104/courses'><span class="name text-ellipsis">lius</span></a>
                                <p class="meta">
					<a href="/u/1297104/experience">经验<b id="js-user-mp">2442</b></a>
					<a href="/u/1297104/credit">积分<b id="js-user-credit">0</b></a>            </p>

                                <a href='/user/setprofile' class='icon-set setup'></a>
                            </div>
                            <!--
                            <div class="card-links">
                                <a href="/space/index" class="my-mooc l">我的慕课<i class="dot-update"></i></a>
                                <span class="split l"></span>
                                <a href="/myclub/myquestion/t/ques" class="my-sns l">我的社区</a>
                            </div>
                            -->
                                                        <div class="card-history">
                                <span class="history-item">
                                    <span class="tit text-ellipsis">Python开发简单爬虫</span>
                                    <span class="media-name text-ellipsis">4-2 URL管理器的实现方式</span>
                                    <i class="icon-clock"></i>
                                                                            <a href="/video/10680" class="continue">继续</a>
                                                                    </span>
                            </div>
                                                        <div class="card-sets clearfix">
                                <a href="/wenda/save" target="_blank" class="l mr30">发问题</a>
                                <a href="/article/publish" target="_blank" class="l">写文章</a>
                                <a href="/passport/user/logout?referer=http://www.imooc.com" class="r">退出</a>
                            </div>
                        </div>
                        <i class="card-arr"></i>
                    </div>
                </li>
            </ul>
        </div>
"""
soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
print ('连接数')
links = soup.find_all('a')
for link in links:
    print (link.name,':',link['href'],':',link.get_text())
print ('特定的url')
link_node = soup.find('a',href='/video/10680')
print (link_node)