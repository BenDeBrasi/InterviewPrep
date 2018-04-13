import java.util.Arrays;

public class RotateMatrix{
	public static int[][] RotMat(int[][] M){
		for(int layer = 0; layer < Math.floor(M.length/2); layer++){
			int first = layer;
			int end = M.length - layer - 1;
			for(int i = first; i < end; i++){
				int offset = i - first;
				int tmp = M[first][first+offset];
				M[first][first+offset] = M[end-offset][first];
				M[end-offset][first] = M[end][end-offset];
				M[end][end-offset]= M[first+offset][end];
				M[first+offset][end]= tmp;
			}
		}
		return M;
	}
	public static void main(String[] args){
		int[][] M = new int[5][5];
		for(int i = 0; i < 5; i++){
			for(int j = 0; j < 5; j++){
				M[i][j] = j;
			}
		}

		System.out.println(Arrays.deepToString(M));
		System.out.println(Arrays.deepToString(RotMat(M)));
	}
}
