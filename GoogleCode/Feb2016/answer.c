#include<stdio.h>

#define true 1
#define false 0

int solution(int X){ 
   int max=1,val=X; 
   while(val/10!=0){ 
     max*=10; 
     val/=10; 
   } 
   int del=true; 
   int pos=-1,cur=-1,rep=0,max1=max; 
   val=X; 
   while(del && max!=0){ 
     int new_cur=val/max; 
     if(rep==1 && new_cur > cur){ 
       pos=max*10; 
       del=false; 
     } 
     else if(new_cur==cur){ 
       pos=max; 
     } 
     if(new_cur==cur) 
       rep = 1; 
     else 
       rep = 0; 
     val=val%max; 
     max=max/10; 
     cur=new_cur; 
   } 
   int new_num=0,max_new=max1/10; 
   val=X; 
   while(max1!=0){ 
     if(max1==pos){ 
       max1/=10; 
       continue; 
     } 
     int num=(val/max1)%10; 
     new_num+=max_new*num; 
     max_new/=10; 
     max1/=10; 
   } 
   return new_num; 
}

int main(){
	int n;
	scanf("%d",&n);
	printf("%d\n",solution(n));
	return 0;
}
