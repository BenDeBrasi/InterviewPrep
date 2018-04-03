class URLify{
	public static String URLify(string){
		
		int space_count = 0;
		
		for(int i; i < string.length(); i++){
			if(string.charAt(i).equals(' '){
				space_count++;
			}
		}
		
		char[] URL_string = new char[(string.length()-space_count) + (space_count * 3)];
		
		int j = 0;
		for(int i; i < string.length(); i++){
			if(string.chatAt(i).equals(' ')){
				URL_string[j] = '%';
				URL_string[j+1] = '2';
				URL_string[j+2] = '0';
				j +=3;
			}
			else
				URL_string[j] = string.charAt(i);
				j++;
		}
	return URL_string;
	}
}