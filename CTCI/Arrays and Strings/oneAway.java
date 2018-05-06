public class oneAway{
	
	public static boolean oneAway(String str1, String str2){
		if(str1.length() != str2.length() && str1.length()-1 != str2.length() && str1.length()+1 != str2.length())
			return false;
		if(str1.length() <= str2.length())
			return compare(str1,str2);
		else
			return compare(str2,str1);
	}
	
	public static boolean compare(String small, String large){
		boolean difference = false;
		
		for(int smallCount = 0, largeCount = 0; smallCount < small.length() && largeCount < large.length(); smallCount++, largeCount++){
			
			if(!(small.charAt(smallCount) == large.charAt(largeCount))){				
				if(difference == true)
					return false;
				else{
					difference = true;
					if(small.length() < large.length())
						smallCount--;
				}
			}
		}
	
		return true;
	}

	public static void main(String[] args){
		System.out.println(oneAway("back","pale"));
	}
}
