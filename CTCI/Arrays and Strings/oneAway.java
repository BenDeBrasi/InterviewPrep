public class oneAway{
	public static boolean oneAway(String str1, String str2){
		if(str1.length() != str2.length() && str1.length()-1 != str2.length() && str1.length()+1 != str2.length())
			return false;
		if(str1.length() <= str2.length())
			return compare(str1,str2);
		else
			return compare(str2,str1);
	}
	
	public static boolean compare(small, large){
		
		int smallCount = 0;
		boolean difference = 0;
		
		for(int largeCount = 0; largeCount < large.length(); largeCount++){
			
			if(small.getChar(smallCount) == large.getChar(largeCount))
				smallCount = largeCount + 1;
			
			else{
				
				if(difference == 1)
					return false
				
				else{
					
					if(small.length() == large.length())
						smallCount = largeCount + 1;
					
					else{
						smallCount = largeCount;
					}
					difference = 1;
				}
			}
		}
		
		return true;
	}
}