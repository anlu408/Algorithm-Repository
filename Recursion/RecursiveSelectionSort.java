public class(RecursiveSelectionSort)
{
  public static void sort(double[] list)
{
  //Invokes method sort and passes a list, the first character and last character
  sort(list, 0, list.length - 1);
}
}

//Method to recursively selection sort the passed list
private static void sort(double[] list, int low, int high)
{
  //Comares low index to high index.
  if (low < high)
  {
    //indexofMin set to low
    int indexofMin = low;
    //Sets min ( a key) to the low element in the list
    double min = list[low];

    //For loop traverses the list
    for (int i = low + 1; i <= high; i++)
    {
      if (list[i] < min)
      {
        min = list [i];
        indexOfMin = i;
      }
    }

    list[indexOfMin] = list[low];
    list[low] = min;
    sort(list, low + 1, high);
  }
}

/*
 Let's say that the list we have is [2,1,7,4,11]
Going through the code:
list, 0, list.length -1 is passed where list.length -1 is 4.

indexofMin set to low which is 0
min = list[low] which is 0th element of list which is 2

moving onto for loop:
i = low -> 0
high = 4 so the for loop will run until i = 4.

list[0] <  min if statement but they are equal so the if statement does not run.
i ++ -> i now equals to 1

list[i] = 1 which is less than 2.
min is now set to list[i]
and indexOfMin is set to 1.

i is now equal to 2
list[2] = 7 which is greater than the min -> not executed

i is now equal to 3
list[3] = 4 which is greater than the min -> not executed

i is now equal to 4.
list[4] = 11 which is greater than the min -> not executed

list[1] = 1 -> set equal to list[low] which means our new list is
[1,2,7,4,11]
and list[low] which is the 0th element is set equal to min which as it current stands is 1.

the recursive function call moves onto the next element -> low is now equal to 1.
This will continue until we run through each element in the list.
*/
