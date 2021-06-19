public class RecursiveBinarySearch
{
  public static int recursiveBinarySearch (int[] list, int key)
  {
    int low = 0;
    int high = list.length - 1;
    return recursiveBinarySearch(list, key, low, high)
  }

  private static int recursiveBinarySearch(int[] list, int key, int low, int high)
  {
    if (low > high)
    {
      return -low - 1;

      int mid = (low+high)/2;
      if (key < list[mid])
      {
        return recursiveBinarySearch(list,key,low, mid - 1);
      }

      else if (key == list[mid])
      {
        return mid;
      }

      else
      return recursiveBinarySearch(list, key, mid + 1, high);
    }
  }
}

/*
Analysis

Let's say the list is [1,2,3,4]

recursiveBinarySearch passes a list and a key where low = 0 and
high = the element number of the last element in the list

Helper Function recursiveBinarySearch takes in list, key and low and high.
If low > high -> there was no match. this is a stopping case.

mid is then set to the average of low and high which should be the average

if key is smaller than the average, the method searches the first half of the list
If the key is equal to the middle element, that value is returned
Lastly, if the key is larger, the method searches the 2nd half.

This is repeated on the half of the array that key falls
into (first half if lower and second half if higher)
*/
