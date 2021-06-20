import java.util.Scanner; //Used to take user input for number of disks

public class towerOfHanoi
{
  //Main method

  public static void main(String[] args)
  {
    Scanner input = new scanner(System.in);
    System.out.println("Enter number of disks");
    int n = input.nextInt();

    //Recursive method invokation
    System.out.println("The moves are: ")
    moveDisks(n, 'A', 'B', 'C')
  }

  public static void moveDisks(int n, char fromTower, char toTower, char auxTower)
  {
    if (n == 1) //Stopping Condition
    {
      System.out.println("Move disk " + n + "from " + fromTower + " to " + toTower);
    }
      else
      {
        moveDisks (n-1, fromTower, auxTower, toTower);
        System.out.println("Move disk " + n + "from " + fromTower + " to " + toTower);
        moveDisks (n-1, auxTower, toTower, fromTower)
      }
    }
  }
}

/*
Analysis
Let's say that n = 4.
A is passed to fromTower, B to toTower and C to auxTower

n != 1 -> stopping condition is not ran.
movedisks invoked with 4-1 = 3 -> recursively invoked with 2 and 1 as well

Function passes
n=4
fromTower = a
toTower = b
auxTower = c

First recursive method invoked
n = 4
fromTower = a
toTower = b
auxTower = c

moveDisks invoked with n = 3
fromTower = a
toTower = c
auxTower = b

which invokes the method again with n= 2
fromTower = a
toTower = b
auxTower = c

which invokes the method again with n = 1
fromTower = a
toTower = c
auxTower = b
first if loop is satisfied so system prnts
Move disk 1 from A to C. This loop is now satisfied now move back to n=2

n=2
fromTower = a
toTower = b
auxtower = c
system prints Move disk 2 from A to B

2nd moveDisk in function 2 is now called with n = 1
moveDisk (1, A, B, C)
auxTower = A
toTower = B
fromTower = C
-> if n ==1 satisfied
Move disk 1 from fromTower(C) to toTower (B)
then System prints Move disk 1 from fromTower(C) to toTower(B)
*/
