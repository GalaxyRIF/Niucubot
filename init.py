from math import sin,pi

def get_token():
    mode=int(input("Mode:"))
    key=int(input("Key:"))
    fac=(1/mode+1/(key**2+pi))+mode/1.3
    content="wAbYW'LkMfhTjeAh4TzMVUkTXhAyfzN.rwTjEErykHMoqSzPKUW3oGhbNzsuEYCFS5MCMLjyIyvcwzOlMQzm.QGgKG4PCSydKr5ysIXWq.IHCJUKhz5VCjDBciMVailCxrIfO1W7GoGYb8ixTtkPTSB5YBVljlVuMdrTNNKc.FbKe4jSDDY4Kwe3vM1sjRTHGhAkzVyNTw6LzFVRdjcF5ZkVZehuYsv'A"
    sequence=[]
    fac=(1/mode+1/(key**2+pi))+mode/1.3
    len1=len(content)
    len2=int(len(content)/ mode)
    for n in range(0,len1):
        preout=int(n*fac+fac/(n+1)+n**2+sin(n))   
        out=preout%mode
        sequence.append(out)
    cftable="0"*len2
    cftable1=list(cftable)
    for i in range(0,len2):
        x=i*mode+int(sequence[i])
        cftable1[i]=content[x]
    content="".join(cftable1)
    return content[2:-1]


access=("members", # bot可以访问群员列表和进行相关操作
"messages", # bot可以发送接收消息
"message_content", #bot可以查看消息
"voice_states",)