import pyaudio,wave
import time,datetime

def getSound():
    WIDTH = 2
    CHANNELS = 2
    RATE = 44100
    
    now = datetime.datetime.now()
    a = now.second//3
    p = pyaudio.PyAudio()
    print('-----prepare to get sound  '+str(a)+'-----')

    def callback(in_data, frame_count, time_info, status):
        #in_data = stream.read(1024)
        return (in_data, pyaudio.paContinue)

    stream = p.open(format=p.get_format_from_width(WIDTH),
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    output=True,
                    frames_per_buffer=1024
                    )

    #stream_callback=callback
    #frames_per_buffer=1024,

    stream.start_stream()
    frames=[]
    '''while stream.is_active():
        time.sleep(0.1)
        #data = stream.read(1024)
        #frames.append(data)
        #print(data)'''
    #f = open('sound.wav','wb')



    for i in range(0, int(RATE / 1024 * 3)):
        data = stream.read(1024)
        frames.append(data)
        #print(data)
        #print('\n')
        #stream.write(data, 1024)
        #f.write(data)
    #f.close()


    stream.stop_stream()
    stream.close()
    p.terminate()


    
    print('get sound    '+str(a))
    wf = wave.open("D:\django_web\server\sound\\"+str(a)+'.wav', "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print('-----save sound '+str(a)+'-----')
def getSound_s():
    while True:
        getSound()
if __name__=="__main__":
    getSound_s()
