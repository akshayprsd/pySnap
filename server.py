from flask import Flask,render_template,request,redirect,url_for,flash
from edit import add_new,edit_entry,delete_entry,session
from database import Base,articlecontent,articletag,recent,tag,unmissable,trending,engine


# if len(videos)%6==0:
#   con=len(videos)/6
# else:
#   con=len(videos)/6+1

#con is the total number of pages

#have to add exceptions and 404 pages and form filling left

app=Flask(__name__)

@app.route("/")
@app.route('/home/')
@app.route('/page/1')
def homepage():
    articlecontentrec=session.query(articlecontent).all()
    l1=articlecontentrec[0:len(articlecontentrec)-1:1]
    recentrec=session.query(recent).all()
    unmissablerec=session.query(unmissable).all()
    trendingrec=session.query(trending).all()
    return render_template('homepagetemp.html',recent=recentrec,unmissable=unmissablerec,trending=trendingrec,list=l1)


@app.route('/contact')
def contactpage():
    recentrec=session.query(recent).all()
    unmissablerec=session.query(unmissable).all()
    trendingrec=session.query(trending).all()
    return render_template('contactus.html',recent=recentrec,unmissable=unmissablerec,trending=trendingrec)
    

#about page has 6 videos

@app.route('/about')
def aboutpage():
    recentrec=session.query(recent).all()
    unmissablerec=session.query(unmissable).all()
    trendingrec=session.query(trending).all()
    return render_template('about.html',recent=recentrec,unmissable=unmissablerec,trending=trendingrec)


#temp has one main video which is vid and 10 random videos
@app.route('/article/<int:id_num>')
def articlepage(id_num):
    articlecontentrec=session.query(articlecontent).filter_by(id_num=id_num).first()
    recentrec=session.query(recent).all()
    unmissablerec=session.query(unmissable).all()
    trendingrec=session.query(trending).all()
    return render_template('posttemp.html',recent=recentrec,unmissable=unmissablerec,trending=trendingrec,articlecontent=articlecontentrec)
#use vid to get the video and randvid to get the 10 videos


'''   
@app.route('/page/<int:page_no>')
def diffpage(page_no):
    videos=session.query(YTLink1).all()
    if page_no>len(videos)//6+1:
        return render_template('404.html'),404
    elif page_no<len(videos)//6:
        l1=videos[len(videos)-1*page_no:len(videos)-1*page_no-7:-1]
        randvid=sample(list(set(videos)^set(l1)),7)
        return render_template('hometemp.html',links=l1,rlinks=randvid)
    elif page_no==len(videos)//6 and len(videos)%6==0:
        l1=videos[:6]
        randvid=sample(list(set(videos)^set(l1)),7)
        return render_template('hometemp.html',links=l1,rlinks=randvid)
    elif page_no==len(videos)//6 +1 and len(videos)%6!=0:
        l1=videos[:len(videos)%6]
        randvid=sample(list(set(videos)^set(l1)),7)
        return render_template('hometemp.html',links=l1,rlinks=randvid)
    else:
        return redirect(url_for('homepage'))



@app.route('/admin/form',methods=['GET','POST'])
def formfill():
    videos=session.query(YTLink1).all()
    if request.method=='POST':
        newvideo=YTLink1(id_num=len(videos)+1,title=request.form['nameofvid'],description=request.form['description'],embed_url='http://www.youtube.com/embed/'+request.form['urllink'][27:],thumbnail_url='https://i.ytimg.com/vi/'+request.form['urllink']+'/hqdefault.jpg')
        session.add(newvideo)
        session.commit()
        return redirect(url_for('formfill'))
    else:
        return render_template('form.html')
'''

if __name__ == '__main__':
    app.debug=True
    app.run()
