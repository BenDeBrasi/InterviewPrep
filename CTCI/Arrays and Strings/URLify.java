class URLify{
	public static String URLify(String string){
		int space_count = 0;
		
		for(int i= 0; i < string.length(); i++){
			if(string.charAt(i) == ' ')
				space_count++;	
		}
		
		char[] URL_string = new char[(string.length()-space_count) + (space_count * 3)];
		
		int j = 0;
		for(int i = 0; i < string.length(); i++){
			if(string.charAt(i) == ' '){
				URL_string[j] = '%';
				URL_string[j+1] = '2';
				URL_string[j+2] = '0';
				j+=2;
			}
			else
				URL_string[j] = string.charAt(i);
				j++;
		}
		return new String(URL_string);
	}

	public static void main(String[] args){
		System.out.println(URLify("hello world"));
	}
}
