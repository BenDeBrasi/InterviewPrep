public class StringCompression{
	public static String Compress(String str){
		if(str.length() >= 0 && str.length() <= 2)
			return str;

		char[] arr = new char[str.length()];
		char currLetter = ' ';
		int currCount = 0;
		int arrSpot = 0;
		int i = 0;

		while (i < str.length()){
			currLetter = str.charAt(i);
			currCount = 0;

			while(i < str.length() && currLetter == str.charAt(i)){
				currCount++;
				i++;
			}
			
			if(currCount > 2){
				arr[arrSpot] = currLetter;
				arr[++arrSpot] = (char)(currCount + '0');
			}
			else{
				if(currCount == 2){
					arr[arrSpot] = currLetter;
					arr[++arrSpot] = currLetter;
				}
				else{
					arr[arrSpot] = currLetter;
				}
			}
			
			arrSpot++;
		}
		
		String s = new String(arr);
		System.out.println(s);
		
		if(s.length() > str.length())
			return str;
		else
			return s;
	}

	public static void main(String[] args){
		System.out.println(Compress("helllllo"));
	}
}
