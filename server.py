from flask import Flask,render_template,request,redirect,url_for,flash
from edit import add_new,edit_entry,delete_entry,session
from random import randint,sample
from database import YTLink1



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
    recent=session.query(recent).all()
    unmissable=session.query(unmissable).all()
    trending=session.query(trending).all()
    return render_template('homepagetemp.html',recent=recent,unmissable=unmissable,trending=trending)

    
@app.route('/contact')
def contactpage():
    videos=session.query(YTLink1).all()
    rand4=sample(videos,4)
    return render_template('contact.html',rand4=rand4)
    

#about page has 6 videos

@app.route('/about')
def aboutpage():
    videos=session.query(YTLink1).all()
    rand6=sample(videos,6)
    return render_template('about.html',rand6=rand6)

#temp has one main video which is vid and 10 random videos
@app.route('/video/<int:id_num>')
def videopage(id_num):
    videos=session.query(YTLink1).all()
    vid=session.query(YTLink1).filter_by(id_num=id_num).first()
    random10=sample(videos,10)
    return render_template('temp.html',vid=vid,randvid=random10)
#use vid to get the video and randvid to get the 10 videos



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

if __name__ == '__main__':
    app.debug=True
    app.run()
