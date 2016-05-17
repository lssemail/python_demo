# coding:utf8

class HtmlOutputer(object):

    def __init__(self):
        self.dates = []

    def collect_data(self,data):
        if data is None:
            return
        self.dates.append(data)

    def output_html(self):
        fout = open('output.html','w')

        fout.write("<html>")
        fout.write("<head>")
        fout.write('<meta charset="utf-8"></meta>')
        fout.write("<title>百度百科Python页面爬取相关数据</title>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.dates:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()
