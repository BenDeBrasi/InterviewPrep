public class StringRotation{
	//Index by index method
	public static boolean StringRotation1(String s1, String s2){
		String master = s1 + s1;
		for(int i = 0; i < master.length(); i++){
			if(i + s2.length() > master.length())
				return false;
			for(int j = 0; j < s2.length(); j++){
				if(master.charAt(i+j) == s2.charAt(j)){
					if(j == s2.length()-1){
						return true;
					}
				}else{
					break;
				}
			}
		}
		return false;
	}

	//Using contains
	public static boolean StringRotation2(String s1, String s2){
		String master = s1 + s1;
		if(master.contains(s2))
			return true;
		return false;
	}

	public static void main(String[] args){
		System.out.println(StringRotation1("lewaterbott","waterbottle"));
	}
}
