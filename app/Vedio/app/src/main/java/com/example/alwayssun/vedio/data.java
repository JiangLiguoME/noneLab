package com.example.alwayssun.vedio;

/**
 * Created by Administrator on 2018\4\12 0012.
 */

public class data{
    private static Boolean state =true;

    public static Boolean getState() {
        return state;
    }

    public static void setState(Boolean a) {
        data.state = a;
    }
}