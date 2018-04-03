public class PalinPerm{
	public static boolean PalinPermSort(String str){
		if(str.length() == 0 || str.length() ==1)
			return true;
		
		s = str.toCharArray();
		s = Array.sort(s);
		
		int currCount = 0;
		boolean oddCount = 0;
		
		for(int i = 1; i < str.length(); i++){
			
			while(s[i-1] == s[i] && i < str.length()){
				currCount++;
				i++;
			}
			
			if(currCount % 2 == 0){}
			
			else{
				if(str.length() % 2 != 0 && oddCount == 0){
					oddCount = 1
				}
				else if(str.length() % 2 == 0 || (str.length() % 2 != 0 && oddCount == 1)){
					return false;
				}
			}
			currCount = 0;
		}
		return true;
	}
	
	public static boolean PalinPermVector(String str){
		if(str.length() == 0 || str.length() == 1)
			return true;
		
		int[] alphabet = new int[128];
		
		for(int i = 0; i < str.length(); i++){
			alphabet[(int)str.charAt(i)]++;
		}
		
		boolean oddFlag = 0;
		
		for(int i: alphabet){
			if(i % 2 == 0){}
			
			else{
				
				if(str.length() % 2 == 0 || (str.length() % 2 != 0 && oddFlag ==1))
					return false;
				else if((str.length() % 2 != 0 && oddFlag =0) )
					oddFlag = 1;
			}
			
		}
		return true;
	}
}