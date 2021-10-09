/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package codechef;

/**
 *
 * @author kumar
 */
import java.util.*;
public class Diagonal_move {
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int T=sc.nextInt();
        while(T>0){
            int a=0;
            int b=0;
            int x=sc.nextInt();
            int y=sc.nextInt();
            for(int i=0;i<=1;i++){
            if((a+i==x)&&(b+i==y)||(a+i==x)&&(b-i=='y')||(a-i==x)&&(b+i==y)||(a-i==x)&&(b-i==y)){
                 System.out.println("yes");
            }
                   
            
                
            else
            {
                            System.out.println("no");
                            }
                T--;
            }
        }
        }
    }

