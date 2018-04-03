def oneAway(str1, str2):
	if str1 == str2:
		return True
		
	if len(str1) != len(str2) and len(str1)-1 != len(str2) and len(str1)+1 != len(str2):
		return False
	"Get smaller one. Iterate till difference. Skip first difference in bigger string (only iterate that strings index). If another difference comes up return false else true"
	"If same size iterate through. Skip first difference (iterate both strings indicies). If another comes up return false. Else return true"
	
	if len(str1) < len(str2):
		return compare(str1,str2)
	else 
		return compare(str2,str1)
		
	
"str1 is smaller or equal size"
def compare(str1,str2):
	"Get syntax to iterate through both in 1 for loop that Sakib showed you"
	difference = 0
	j = 0
	for i in xrange(str2):
		if str1[i] == str2[j]:
			j = i + 1
		else:
			if str1[i] != str2[j] and difference == 0:
				
				difference = 1
				
				if len(str1) < len(str2):
					j = i
				else:
					j = i + 1
			else:
				return False
	return True			
	
"Really bad variable names. Improve in Java version. Make 'str1' in compare smallerString  while 'str2' is largerString or something and then make i and j smallerIterator or largeriterator respectively. As currently stands, i, j, str1 and str2 are non descriptive."