bool isPowerOfTwo(int x) {
    /*
    Try multiline comment
    */
	// First x in the below expression is
	// for the case when x is 0
	return x && (!(x & (x - 1)));
}
