public class isUnique{
	
	//Array for ascii value approach. Time: O(n) Space: 0(n)
	static boolean isUnique1(String str){
		int[] alphabet = new int[128];
		for(int i = 0; i < str.length(); i++){
			alphabet[str.charAt(i)] += 1;
			if(alphabet[str.charAt(i)] > 1)
				return false;
		}
		return true;
	}

	public static void main(String[] args){
		System.out.println(isUnique1("Helo"));
		return;
	}
}
