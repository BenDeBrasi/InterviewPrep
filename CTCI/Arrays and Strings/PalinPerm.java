import java.util.Arrays;
import java.util.BitSet;

public class PalinPerm{
	public static boolean PalinPermSort(String str){
		if(str.length() >= 0 && str.length() <= 2)
			return true;
		
		char[] s = str.toCharArray();
		Arrays.sort(s);
		
		int currMatches = 0;
		boolean oddFlag = false;
		int i = 0;
		char currChar = 'a';

		while(i < str.length()){
			
			currChar = s[i];
			currMatches = 0;

			while(i < str.length() && s[i] == currChar){
				currMatches++;
				i++;
			}
			
			if(str.length() % 2 == 0){
				if(currMatches % 2 != 0)
					return false;
			}

			else{
				if(oddFlag == false && currMatches % 2 != 0)
					oddFlag = true;
				else if(oddFlag == true && currMatches % 2 != 0)
					return false;
			}
			
			currMatches = 0;

		}
		return true;
	}
	
	public static boolean PalinPermVector(String str){
		if(str.length() >= 0 && str.length() <= 2)
			return true;
		
		BitSet alphabet = new BitSet(128);
		boolean oddFlag = false;

		for(int i = 0; i < str.length(); i++){
			alphabet.flip(Character.getNumericValue(str.charAt(i)));
		}
		
		for(int i = 0; i < alphabet.length(); i++){	
			if(alphabet.get(i) == false){
				if(str.length() % 2 == 0){
					return false;
				}
				else{
					if(oddFlag == false)
						oddFlag = true;
					else
						return false;
				}
			}
		}
		return true;
	}

	public static void main(String[] args){
		System.out.println(PalinPermVector("aabbcd"));
	}
}
