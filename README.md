# ddPython
A simple python implementation of the Linux dd command


Implements the operands bs, count, if, of, seek, skip, conv. Supports
the conversions lcase, ucase, sparse where case conversions are done only for ASCII, not Unicode,
characters. Handles multiplicative suffixes (ex. K, MB, M, etc.) as per dd’s specifications.
Files can only be passed in via if, not stdin. All else is NOT be re-implemented. No print output
is displayed.
