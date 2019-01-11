import base64,os

#with open('/home/crh/uuspace/voice-ops/resource/Chicks come from eggs..wav','rb') as f:
with open('/home/crh/uuspace/voice-ops/resource/is.wav','rb') as f:
    b64_str = base64.b64encode(f.read())
    #print(b64_str)
    with open('/home/crh/uuspace/voice-ops/resource/is.txt','w') as w:
        w.write(str(b64_str))

