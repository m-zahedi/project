package recursive;
public class recursive { 
	
	 public static void main(String args[]) { 
		 //AAM63747_cl_6
	     String string1 = "MASSSALALRRLL";
	     		        //+ "LDPFTPTRSLSQMLNFMDQVSEIPLVSATRGMGASGVRRGWNVKEKDDALHLRIDMPGLSREDVKLALEQ"
	     	         	//+ "NTLVIRGEGETEEGEDVSGDGRRFTSRIELPEKVYKTDEIKAEMKNGVLKVVIPKIKEDERNNIRHINVD"; 
	     //AAM67165_cl_2
	     String string2 = "MSAVAINHFFGLPET";
	     		     // + "VEEERTLVIKSNGKRKRDDDESEEGSKYIRLERRLAQNLVKKFRLPEDADMASVTAKYQEGILTVVIKKL"
	     	         //	+ "PPQPPKPKTVQIAVS"; 
	     System.out.println("AAM63747_cl_6 " + "protein sequence:");
	     System.out.println(string1);
	     System.out.println("AAM67165_cl_2 " + "protein sequence:");
	     System.out.println(string2);
	     System.out.println("optimized number of operations: ");
	     System.out.println(recursive_edit_dst(string1, string2, string1.length(), string2.length())); 
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
	 
	 static int recursive_edit_dst(String str1, String str2, int length1, int length2){ 
	
		// length of string 1 is zero
	     if (length1 == 0) 
	         return length2; 
	     // length of string 2 is zero  
	     if (length2 == 0) 
	         return length1; 
	     
	     // last characters are equal -> smaller subproblem 
	     if (str1.charAt(length1 - 1) == str2.charAt(length2 - 1)) 
	         return recursive_edit_dst(str1, str2, length1 - 1, length2 - 1); 
	
	     // last characters are not equal
	     return 1 + minimum(recursive_edit_dst(str1, str2, length1,     length2 - 1),    // insert 
	    		            recursive_edit_dst(str1, str2, length1 - 1, length2    ),    // remove 
	    		            recursive_edit_dst(str1, str2, length1 - 1, length2 - 1));   // modify  
	 	} 
  
} 