package com.example.alwayssun.vedio;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;

/**
 * Created by Administrator on 2018\3\22 0022.
 */

public class StreamTool {

    public static byte[] readInputStream(InputStream inputStream) throws IOException {
        byte[] buffer = new byte[7200000];
        int len = 0;
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        while((len = inputStream.read(buffer)) != -1) {
            bos.write(buffer, 0, len);
            }
        bos.close();
        return bos.toByteArray();
    }
}
