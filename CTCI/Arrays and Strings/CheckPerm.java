public class CheckPerm{
	public static boolean CheckPermArray(String str1, String str2){
		if(str1.length() != str2.length())
			return false;
		
		//Array alphabet approach. (need to know size of alphabet) Assume 128 for ascii
		
		int[] alphabet = new int[128];
		//In Java must turn String to Char Array first. Strings immutable EL o EL.
		char[] s = str1.toCharArray();
		
		for(Char c: s){
			alphebet[c]++;
		}
		
		
		//Look for ways to avoid toCharArray operation cost.
		for(int i; i < str2.length(); i++){
			
			alphabet[(int) str2.charAt(i)]--;
			
			if(alphabet[i] != 0)
				return false;
		}
		
		return true;
	}
	
	public static boolean CheckPermSort(String str1, String str2){
		if(str1.length() != str2.length())
			return false;
		
		//Sort and compare index by index 
		char[] s1 = str1.toCharArray();
		char[] s2 = str2.toCharArray();
		
		//Sort str1
		Array.sort(str1);
		//Sort str2
		Array.sort(str2)
		
		return str1.equals(str2);
	}
}

//.toCharArray(), Array.sort(), .equals(). Remember to use these!

//Hints 1, 84, 122, 131