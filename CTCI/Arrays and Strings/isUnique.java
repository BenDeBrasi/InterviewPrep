import java.util.BitSet;
import java.util.Arrays;

public class isUnique{
	
	//Array for ascii value approach. Time: O(n) Space: 0(n)
	static boolean isUnique1(String str){
		BitSet alphabet = new BitSet(128);
		for(int i = 0; i < str.length(); i++){
			if(alphabet.get(str.charAt(i)) == true)
				return false;
			alphabet.flip(str.charAt(i));
		}
		return true;
	}

	//Sort String then compare neighboring letters.
	static boolean isUnique2(String str){
		char[] sorted = str.toCharArray();
		Arrays.sort(sorted);
		for(int i = 1; i < sorted.length; i++){
			if(sorted[i] == sorted[i-1])
				return false;
		}
		return true;
	}

	public static void main(String[] args){
		System.out.println(isUnique2("Helo"));
		return;
	}
}
