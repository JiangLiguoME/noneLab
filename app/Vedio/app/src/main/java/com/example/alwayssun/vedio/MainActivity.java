package com.example.alwayssun.vedio;

import android.app.DownloadManager;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.media.MediaPlayer;
import android.provider.ContactsContract;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import org.w3c.dom.Text;
import org.xutils.http.annotation.HttpResponse;
import org.xutils.http.body.RequestBody;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.security.spec.ECField;
import java.text.SimpleDateFormat;
import java.util.Date;

import okhttp3.FormBody;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {
    private String myURL;
    private EditText myEditText;
    private ImageView myImage;
    private TextView myText;
    private CheckBox LED1;
    private CheckBox LED2;
    private CheckBox LED3;
    private CheckBox LED4;
    private CheckBox LED5;
    private CheckBox LED6;
    private CheckBox LED7;
    private CheckBox LED8;

    private CheckBox jidianqi;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        LED1=(CheckBox)findViewById(R.id.LED1);
        LED2=(CheckBox)findViewById(R.id.LED2);
        LED3=(CheckBox)findViewById(R.id.LED3);
        LED4=(CheckBox)findViewById(R.id.LED4);
        LED5=(CheckBox)findViewById(R.id.LED5);
        LED6=(CheckBox)findViewById(R.id.LED6);
        LED7=(CheckBox)findViewById(R.id.LED7);
        LED8=(CheckBox)findViewById(R.id.LED8);
        jidianqi = (CheckBox)findViewById(R.id.jidianqi);
        myImage = (ImageView)findViewById(R.id.image);
        myImage.setImageResource(R.mipmap.my);
        myEditText = (EditText)findViewById(R.id.urlText);
        myText = (TextView)findViewById(R.id.text);
        Button myGetBtn = (Button)findViewById(R.id.getBtn);
        LEDChecked ledChecked = new LEDChecked();

        final Button myStopBtn = (Button)findViewById(R.id.stopBtn);
        myStopBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Log.d("mianii",data.getState().toString());
                data.setState(!data.getState());


            }
        });
        jidianqi.setOnCheckedChangeListener(ledChecked);
        LED1.setOnCheckedChangeListener(ledChecked);
        LED2.setOnCheckedChangeListener(ledChecked);
        LED3.setOnCheckedChangeListener(ledChecked);
        LED4.setOnCheckedChangeListener(ledChecked);
        LED5.setOnCheckedChangeListener(ledChecked);
        LED6.setOnCheckedChangeListener(ledChecked);
        LED7.setOnCheckedChangeListener(ledChecked);
        LED8.setOnCheckedChangeListener(ledChecked);
        myGetBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                data.setState(true);
                Runnable myRunable = new myVedioThread("sound");
                Runnable myRunable_s = new myVedioThread("image");
                Thread thread1 = new Thread(myRunable);
                Thread thread2_s = new Thread(myRunable_s);
                //thread1.setDaemon(true);
                //thread2_s.setDaemon(true);
                thread2_s.start();
                thread1.start();
            }
        });

    }

    public void myToast(final String myNote){
        runOnUiThread(new Runnable() {
            @Override
            public void run() {
                Toast.makeText(MainActivity.this,myNote,Toast.LENGTH_SHORT).show();
            }
        });
    }

    public int getChe(CheckBox checkB){
        return checkB.isChecked()?1:0;
    }

    public class LEDChecked implements CompoundButton.OnCheckedChangeListener {

        @Override
        public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
            new Thread(new Runnable() {
                @Override
                public void run() {
                    int a = getChe(LED8)*128+getChe(LED7)*64+getChe(LED6)*32+getChe(LED5)*16+getChe(LED4)*8+getChe(LED3)*4+getChe(LED2)*2+getChe(LED1);
                    String b = String.valueOf(a);
                    String c = jidianqi.isChecked()?"1":"0";
                    Log.d("fasonf",String.valueOf(b));
                    okhttp3.RequestBody requestBody = new FormBody.Builder()
                            .add("command",b)
                            .add("jidianqi",c)
                            .build();
                    Request request = new Request.Builder()
                            .url("http://49.140.219.113/blog/index/")
                            .post(requestBody)
                            .build();
                    //http://49.140.231.111:8080/command
                    try{
                        OkHttpClient client = new OkHttpClient();
                        Response response = client.newCall(request).execute();
                        String responseData = response.body().string();
                        Log.d("return",responseData);
                    }catch (Exception e){
                        e.printStackTrace();
                    }

                }
            }).start();
        }
    }

    public class myVedioThread implements Runnable {

        private String type = "sound";

        public myVedioThread(String type){
            this.type = type;
        }
        public void myRun(String urlPathContent,final int i){
            try {
                byte[] data = ImageService.getImage(urlPathContent);
                final Bitmap bitmap = BitmapFactory.decodeByteArray(data, 0, data.length); //生成位图
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        myImage.setImageBitmap(bitmap);//显示图片
                        //myText.setText("已获得"+i);
                        myText.setText("");
                    }
                });

            } catch (IOException e) {
                //myToast("连接超时");
                Log.i("Maib", e.toString());
            }

        }
        public void playSound(String urlPathContent, Context context,int pre){
            try{
                MediaPlayer myMedia = new MediaPlayer();
                byte[] data = ImageService.getImage(urlPathContent);
                File temp = File.createTempFile("KenTo", "wav", context.getCacheDir()); //生成临时文件
                temp.deleteOnExit();
                FileOutputStream fos = new FileOutputStream(temp);
                fos.write(data);
                fos.close();
                //播放音频文件
                FileInputStream fis = new FileInputStream(temp);
                myMedia.setDataSource(fis.getFD());
                myMedia.prepare();
                myMedia.start();
                Log.d("Main","start");
                try{
                    Thread.currentThread().sleep(3000);
                }catch(InterruptedException e){
                    Log.d("Main","chucuo");
                    e.printStackTrace();
                }
                Log.d("Main","stop");
                myMedia.stop();
                myMedia.release();
            }catch (Exception e){
                e.printStackTrace();
            }

        }

        @Override
        public void run() {
            String urlPathContent = myEditText.getText().toString();
            String urlPathContent1=urlPathContent;
            int j=0;
            int pre = 1;
            //Thread.currentThread().setDaemon(true);
            while(data.getState()){
                if(this.type.equals("image")){
                    urlPathContent1 = urlPathContent+"image";
                    Log.d("Main",urlPathContent1);
                    myRun(urlPathContent1,0);
                }
                SimpleDateFormat formatter   =   new SimpleDateFormat("ss");
                Date curDate =  new Date(System.currentTimeMillis());
                String   str   =   formatter.format(curDate);
                int i = Integer.valueOf(str);
                if(i==0) i=60;
                //urlPathContent1 =urlPathContent+"/"+(i-1)+"/";
                if(j==i){

                }else{
                    System.out.print(this.type);
                    if(this.type.equals("sound")){
                        urlPathContent1 = urlPathContent+"sound/"+((i/3)-1)+"/";
                        Log.d("Main",urlPathContent1);
                        playSound(urlPathContent1,MainActivity.this,pre);
                        j=i;
                        try{
                            Thread.currentThread().sleep(900);
                        }catch(InterruptedException e){
                            e.printStackTrace();
                        }

                    }
                    /*else{
                        urlPathContent1 = urlPathContent+"image";
                        Log.d("Main",urlPathContent1);
                        myRun(urlPathContent1,i-1);
                        j=i;
                    }*/
                }
                pre = pre+1;
            }



            /*for(int i=1;i<61;i++){
                urlPathContent1 =urlPathContent+"/"+i+"/";
                Log.d("Main",urlPathContent1);
                myRun(urlPathContent1,i);
                try {
                    Thread.currentThread().sleep(0);//阻断2秒
                    SimpleDateFormat formatter   =   new SimpleDateFormat("ss");
                    Date curDate =  new Date(System.currentTimeMillis());
                    String   str   =   formatter.format(curDate);
                    Log.d("Main",str);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }*/
        }
    }

    @Override
    protected void onStop() {
        super.onStop();
        data.setState(false);
    }
}


