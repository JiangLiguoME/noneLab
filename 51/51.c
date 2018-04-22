#include<reg52.h>  
#define uchar unsigned char  
#define uint  unsigned int  
sbit p20=P2^3;
uchar buf,buf2,buf3;  
uchar receive[2],num=0;
void main(void)  
{  
    SCON=0x50;//????????0101 0000  
    PCON=0x00;  
    TMOD=0x20;  
    EA=1;  
    ES=1;  
    TL1=0xfd;//???9600  
    TH1=0xfd;  
    TR1=1;  
    while(1)
    {
	    P1 = receive[0];
	    if(receive[1]=='0')
        {
    		p20 = 0;
    	}
        else
        {
		    p20 = 1;
	    }
    }  
}  
  
//????????  
void serial() interrupt 4  
 {  
	 if(RI)                        
     {
        RI=0;
        ES=0;
        receive[num]=SBUF;
        num++;
        if(num==2)num=0;
        ES=1;
				
		       //????????    
    /*buf=SBUF;   //???????SBUF??buf??  
		if(buf=='#'){
			buf2 = SBUF;
			P1 = buf2;
			buf3 = SBUF;
			p20 = buf3;
		}*/
    
           //????????  
					 
    }
    if(TI)                        
    {
        TI=0;
        TI = 0;

     }

 }  

