bool isPowerOfTwo(int x) {
    /*
    Try multiline comment
    */
	// First x in the below expression is
	// for the case when x is 0
	if (x == 0) 
		if (x == 1)
			return true;
		else
			return false;
		// else
		// 	return false;
		

	return x && (!(x & (x - 1)));
}