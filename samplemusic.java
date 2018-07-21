
public class samplemusic{
  public static void main(String[] args)throws Exception{
    String m1 = "🌟";
    String m2  ="▲";
    String m3 = "⭕️";
    String a = "hello";
    char [] b  =a.toCharArray();
    for(char c : b){
      if(c==b[b.length-1]){
      System.out.println(" "+c);
    }
    System.out.print(" "+c);
  }
    System.out.println("would u wanna hear some music❓");
    String input = new java.util.Scanner(System.in).nextLine();
    if(input.equals( "yes")){
for(int i=0; i<40; i++){
  System.out.println(m2);
  System.out.println(m3);
  Thread.sleep(300);
  if(10 <= i && i<=20){
    System.out.println(m1);
    System.out.println(m2);
    Thread.sleep(300);
  }else {


  }
  }
}

  }
  }
