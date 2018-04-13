public class StringCompression{
	public static String Compress(String str){
		
		char[] arr = new char[str.length()];
		char currLetter = ' ';
		int currCount = 1;
		int arrSpot = 0;
		
		for(int i; i < str.length(); i++){
			currLetter = str.getChar(i);
			
			while(currLetter == str.getChar(i) && i < str.length()){
				currCount++;
				i++;
			}
			
			if(arrCount + 1 >= arr.length()){
				return str;
			}
			else{
				arr[arrSpot] = currLetter;
				arr[++arrSpot] = currCount;
			}
			currCount = 1;
			currLetter = ' ';
		}
		
		if(arr.length() <= str.length())
			return str;
		else
			return new String(arr);
	}
}