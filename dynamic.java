package dynamic;


public class dynamic { 
	
	 public static void main(String args[]) { 
		 //AAM63747_cl_6
	     String string1 = "MASSSALALRRLL"
	     		        + "LDPFTPTRSLSQMLNFMDQVSEIPLVSATRGMGASGVRRGWNVKEKDDALHLRIDMPGLSREDVKLALEQ"
	     	         	+ "NTLVIRGEGETEEGEDVSGDGRRFTSRIELPEKVYKTDEIKAEMKNGVLKVVIPKIKEDERNNIRHINVD"; 
	     //AAM67165_cl_2
	     String string2 = "MSAVAINHFFGLPET"
	     		        + "VEEERTLVIKSNGKRKRDDDESEEGSKYIRLERRLAQNLVKKFRLPEDADMASVTAKYQEGILTVVIKKL"
	     	         	+ "PPQPPKPKTVQIAVS"; 
	     System.out.println("AAM63747_cl_6 " + "protein sequence:");
	     System.out.println(string1);
	     System.out.println("AAM67165_cl_2 " + "protein sequence:");
	     System.out.println(string2);
	     System.out.println("optimized number of operations: ");
	     System.out.println(dynamic_edit_dst(string1, string2, string1.length(), string2.length())); 
	 } 
	
	 static int minimum(int insert, int remove, int modify) { 
	     if (insert <= remove && insert <= modify) {
	         return insert; 
	     } 
	     if (remove <= insert && remove <= modify) {
	         return remove; 
	     } 
	     else {
	         return modify; 
	     }
	 } 

	static int dynamic_edit_dst(String string1, String string2, int length1, int length2) { 
		
		int dynamic_programming_array[][] = new int[length1 + 1][length2 + 1]; 
		
		for (int i = 0; i <= length1; i++) { 
			for (int j = 0; j <= length2; j++) { 
			    // length of string1 is 0
				if (i == 0) 
					dynamic_programming_array[i][j] = j;  
				// length of string2 is 0
				else if (j == 0) 
					dynamic_programming_array[i][j] = i; 
				//last chars are equal 
				else if (string1.charAt(i - 1) == string2.charAt(j - 1)) 
					dynamic_programming_array[i][j] = dynamic_programming_array[i - 1][j - 1]; 
				else
					dynamic_programming_array[i][j] = 1 + minimum(dynamic_programming_array[i][j - 1], // insert 
							dynamic_programming_array[i - 1][j],        // remove 
							dynamic_programming_array[i - 1][j - 1]);   // modify 
			} 
		} 

		return dynamic_programming_array[length1][length2]; 
	} 
} 

