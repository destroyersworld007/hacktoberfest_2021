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
public class RCB_playoffs {
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int T=sc.nextInt();
        while(T>0){
            int x=sc.nextInt();
            int y=sc.nextInt();
            int z=sc.nextInt();
            if((x+2*z>=y)||(x+z>=y)){
                System.out.println("yes");
            }
            else{
                System.out.println("no");
            }
            T--;
        }
    }
}
