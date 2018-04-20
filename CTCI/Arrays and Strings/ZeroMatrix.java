import java.util.Arrays;
import java.util.*;

public class ZeroMatrix{
	
	public static int[][] zM(int[][] M){
		boolean flag = false;
		
		for(int[] currArr: M){
			
			if(currArr[0] == 0)
				flag = true;
			
			for(int ele: currArr){
				if(ele == 0){
					currArr[0] = 0;
				}
			}
		}

		for(int i = 0; i < M.length; i++){
			if(M[i][0] == 0){
				for(int j = 0; j < M[i].length; j++){
					if(M[i][j] == 0 && j != 0){
						for(int k = 0; k < M.length; k++){
							M[k][j] = 0;
						}
					}
					M[i][j] = 0;
				}
			}
		}

		if(flag){
			for(int i = 0; i < M.length; i++){
				M[i][0] = 0;
			}
		}
		
		return M;
	}


	public static int[][] zM1(int[][] M){
		Set<Integer> row = new HashSet<Integer>();
		Set<Integer> col = new HashSet<Integer>();

		for(int i = 0; i < M.length; i++){
			for(int j = 0; j <M[i].length; j++){
				if(M[i][j] == 0){
					row.add(i);
					col.add(j);
				}
			}
		}

		Iterator itRow = row.iterator();
		Iterator itCol = col.iterator();

		while(itRow.hasNext()){
			int x = (Integer)itRow.next();
			for(int i = 0; i < M.length; i++){
				M[x][i] = 0;
			}
		}

		while(itCol.hasNext()){
			int x = (Integer)itCol.next();
			for(int i = 0; i < M.length; i++){
				M[i][x] = 0;
			}
		}
		
		return M;
	}

	public static void main(String[] args){
		
		int [][] M = new int[5][5];
		for(int i = 0; i < M.length; i++){
			for(int j = 0; j < M.length; j++){
				M[i][j] = i+j;
			}
		}

		M[4][4] = 0;

		System.out.println(Arrays.deepToString(M));
		System.out.println(Arrays.deepToString(zM1(M)));
	}
}
