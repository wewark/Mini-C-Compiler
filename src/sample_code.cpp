bool isPowerOfTwo(int x, int y[]) {
    /*
    Try multiline comment
    */
	// First x in the below expression is
	// for the case when x is 0
	
	int x, y;
	while (x > 10) {
		if (x == 0) 
			if (x == 1)
				return true;
			else
				return false;
			// else
			// 	return false;
		x = x + 1;
		break;
	}
		

	return x && (!(x & (x - 1)));
}

