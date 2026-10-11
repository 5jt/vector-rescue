---
title: Within ASL - Basic Statistics
authors: []
volume: '7'
issue: '3'
page: '38'
unindexed: true
transcribed: 'from page images of VOL.7-NO.3-JANUARY-1991.pdf, pages 44–46 (printed 38–40; follows art10006250, within The Random Vector); Claude, 2026-10-11'
review: draft
tags:
- mathematics and statistics
- APL community
queries:
- "Unsigned item in The Random Vector (the ASL newsletter), printed heading “Within ASL - Basic Statistics”; it follows Tony O’Hagan’s “The Genesis of ASL (1)” at the top of p.38 and is followed by the Function Catalogue of the Basic Statistics volume (pp.39–40), printed in an APL font and transcribed here as a code listing. The next item is O’Hagan’s “WAGS” (p.41)."
- "In the catalogue the SYNTAX column has a quad where the function name would stand (`R←A⎕B`, `R← ⎕B`, `A⎕B`, `⎕B`); transcribed as printed. The comments are printed in the italic lower case of the APL font, in which w looks like v; read as w. In SEMIIQR the operator in `(Q3-Q1)÷2` is read as ÷."
- "Kept as printed: “numerical suffices”; “Times series”; CORR “:or product moment” (for “or”?); TWOWAY’s comment “Calculate oneway analysis of variance”; “spearmans”, “poisson”, “weibull” in lower case."
---

## Within ASL - Basic Statistics

The first three volumes of software have been issued for beta test. In this issue of our newsletter, I shall be taking a quick look at what is in one of our first volumes of software - the Basic Statistics volume. Subsequent issues will look at the other shelves.

The Basic Statistics volume owes much to the work of Norman Thomson who made the initial suggestions regarding the scope of the Bottom Shelf at Gregynog in 1989 (and at earlier meetings). Norman’s document (called, not surprisingly, ‘The Bottom Shelf’) contains details of virtually all the statistical routines contained in the Basic Statistics volume, using APL2 as the specification language. The ASL Documentation Working Party is currently aiming to bring Basic Statistics documentation and functions fully into line. As with other ASL documents, copies of Norman’s paper are obtainable from the Management Team.

A review of the contents of the Basic Statistics Volume gives the best idea of its scope, as in most cases the function name alone tells us all we need to know. The workspace contains almost 100 functions, with some duplication covering alternate algorithms (coding for speed, elegance, workspace economy with variants using numerical suffices). Symbol table usage is some 700 symbols.

The contents of the Basic Statistics volume is designed to address the needs of ‘A’ level or first year university students, with groupings suggested as follows:

> Univariate Statistics  
> Distribution Functions  
> Elementary multi-variate statistics  
> Estimation and significance testing  
> Non-parametric statistics  
> Times series  
> ANOVA  
> Combinatorics

The full list of functions in the beta test version of this volume of ASL follows.

```apl
FUNCTION CATALOGUE
------------------

NAME          SYNTAX  SIZE  COMMENT
-------------------------------------------------------------------------------------

BARCHART      R← ⎕B    780  ⍝ FN: Visual representation of frequency table
BINDEN        R←A⎕B    816  ⍝ FN: Values of the binomial probability density function
CHICDF        R←A⎕B   1650  ⍝ FN: Cumulative function values of the chi-square distribution
CHICONT       R← ⎕B    550  ⍝ FN: Calculate chi-square value of a contingency table
CHIDEN        R←A⎕B    759  ⍝ FN: Values of the chi-squared probability density function
CHIGOF        R←A⎕B    672  ⍝ FN: Calculate goodness of fit chi-square value
CHIQUANT      R←A⎕B   1008  ⍝ FN: Calculate chi-square quantiles
CHITAIL       R←A⎕B   1675  ⍝ FN: Upper tail probability of chi-square distribution
COLUMN        R←A⎕B    550  ⍝ FN: Selects columns from a matrix
COMB          R←A⎕B    994  ⍝ FN: All combinations, of a certain length, from a dataset

CORR          R←A⎕B    819  ⍝ FN: Calculates the correlation coefficient :or product moment
CORRMAT       R← ⎕B   1056  ⍝ FN: Calculates correlation matrix
COVMAT        R← ⎕B    845  ⍝ FN: Calculates covariance matrix
EWMA          R←A⎕B   1330  ⍝ FN: Exponentially weighted moving average of a time series
FDEN          R←A⎕B    840  ⍝ FN: Returns values of the F probability density function
FREAD         R← ⎕B   1364  ⍝ FN: Read whole native file as characters
FREQ          R← ⎕B   1403  ⍝ FN: Returns the frequencies of unique values in a data set
FREQTAB       R←A⎕B   2077  ⍝ FN: Converts a dataset to frequency table
FREQTABIRREG  R←A⎕B    910  ⍝ FN: Converts dataset to frequency table with irregular intervals
FTAIL         R←A⎕B   2150  ⍝ FN: Calculate upper tail probabilities of F distribution

FWRITE          A⎕B   2232  ⍝ FN: Create and write to a native file
GAMMADEN      R←A⎕B    864  ⍝ FN: Returns values of the gamma probability density function
HYPGEOMDEN    R←A⎕B    936  ⍝ FN: Values of the discrete hypergeometric probability function
INTADAPT      R←A⎕B   1340  ⍝ FN: Adaptive integration
INTSIMP       R←A⎕B    812  ⍝ FN: Simpsons numerical integration
KENDALCON     R← ⎕B   1587  ⍝ FN: Calculate Kendall's concordance, a rank corr'n coefficient
KENDALCONTS   R← ⎕B   1650  ⍝ FN: Calculate Kendall's concordance test statistic
KENDALTAU     R←A⎕B   1560  ⍝ FN: Calculate Kendall's Tau, a rank correlation coefficient
KENDALTAUTS   R←A⎕B   1525  ⍝ FN: Calculate Kendall's Tau, a rank correlation coefficient
KURTOSIS      R← ⎕B    792  ⍝ FN: Calculates kurtosis of a set of values
MANNWHIT      R←A⎕B    672  ⍝ FN: Mann-Whitney rank sum signed rank test

MANNWHITTS    R←A⎕B   1105  ⍝ FN: Mann-Whitney rank sum signed rank normalised test statistic
MAX           R← ⎕B    756  ⍝ FN: Calculates maximum of a set of values
MEAN          R← ⎕B    720  ⍝ FN: Calculates mean of a set of values
MEANFT        R← ⎕B    505  ⍝ FN: Calculates mean of a frequency table
MEDIAN        R← ⎕B    590  ⍝ FN: Calculates median of set of values
MIDPOINTS     R← ⎕B    600  ⍝ FN: Calculates midpoints of increasing pairs of endpoints
MIN           R← ⎕B    756  ⍝ FN: Calculates minimum of a set of values
MODE          R← ⎕B    969  ⍝ FN: Calculates mode of set of values
MOMENT        R←A⎕B    524  ⍝ FN: Calculates a moment about the origin
MOVA          R←A⎕B   1140  ⍝ FN: Calculate moving average of a time series
NORMCDF       R←A⎕B   1224  ⍝ FN: Calculate cum function values of a normal distribution

NORMDEN       R←A⎕B   1088  ⍝ FN: Returns values of the normal probability density function
NORMQUANT     R←A⎕B   1320  ⍝ FN: Calculate normal statistic values or quantiles
NORMTAIL      R←A⎕B   1224  ⍝ FN: Calculate upper tail areas of standard normal distribution
ON            R←A⎕B    418  ⍝ FN: Combines datasets into a matrix
ONEWAY        R←A⎕B   1876  ⍝ FN: Calculate oneway analysis of variance
PCTILE        R←A⎕B    756  ⍝ FN: Calculates percentile of set of values
PERM          R← ⎕B   1311  ⍝ FN: Generates all permutations of order num
POISDEN       R←A⎕B    768  ⍝ FN: Returns values of the poisson probability function
RANDBOOL      R←A⎕B    768  ⍝ FN: Generates random boolean values
RANDEXP       R←A⎕B    649  ⍝ FN: Generates random values from exponential distribution
RANDNORM      R←A⎕B    966  ⍝ FN: Generates random values from normal distribution
RANDNORMS     R←A⎕B   1449  ⍝ FN: Generates random values from normal distribution
RANDPOIS      R←A⎕B   1624  ⍝ FN: Generates random values from poisson distribution
RANDPROBTAB   R←A⎕B    715  ⍝ FN: Generates random values from discrete distribution
RANDWEIB      R←A⎕B    672  ⍝ FN: Generates random weibull distribution values
RANDBIN       R←A⎕B    696  ⍝ FN: Generates random values from binomial distribution

RANDUNIF      R←A⎕B    737  ⍝ FN: Generates random values from uniform distribution
RANGE         R← ⎕B    732  ⍝ FN: Calculates range of a set of values
RANK          R← ⎕B    450  ⍝ FN: Returns the ranks of a data set
REG           R← ⎕B    798  ⍝ FN: Calculates least squares regression coefficients
REGEST        R← ⎕B    728  ⍝ FN: Predicts dependent values using regression
REGLIN        R← ⎕B    792  ⍝ FN: Calculates simple linear regression coefficients
REGLINEST     R← ⎕B    792  ⍝ FN: Predicts dependent values using simple linear regression
REGLINREP     R← ⎕B   1820  ⍝ FN: Reports on simple linear regression
REGLINRESID   R← ⎕B    828  ⍝ FN: Calculates residuals of simple linear regression
REGPOLY       R←A⎕B    975  ⍝ FN: Calculates least-squares regression polynomial coefficients

REGPOLYEST    R←A⎕B    895  ⍝ FN: Predicts dependent values using polynomial regression
REGPOLYREP      A⎕B   1944  ⍝ FN: Reports on the polynomial least squares regression
REGPOLYRESID  R←A⎕B    896  ⍝ FN: Calculates residuals of polynomial regression
REGREP        R← ⎕B   1736  ⍝ FN: Reports on least squares regression
REGRESID      R← ⎕B    720  ⍝ FN: Calculates residuals of least squares regression
RUNS          R← ⎕B    560  ⍝ FN: Calculates the maximum run length in a data vector
SDEV          R← ⎕B    840  ⍝ FN: Calculates standard deviation across first dimension
SDEVFT        R← ⎕B    804  ⍝ FN: Calculates standard deviation of a frequency table
SEASA         R←A⎕B   1272  ⍝ FN: Seasonally adjust time series
SEMIIQR       R← ⎕B    876  ⍝ FN: Calculates the semi interquartile range (Q3-Q1)÷2

SIGN          R←A⎕B    795  ⍝ FN: Calculates the no. of positive signs from the median
SIGNTS        R←A⎕B    870  ⍝ FN: Calculates the normalised sign test statistic
SKEWNESS      R← ⎕B    804  ⍝ FN: Calculates skewness of set of values
SPEARMAN      R←A⎕B    550  ⍝ FN: Calculate spearmans correlation coefficient
STANDARDISE   R← ⎕B    858  ⍝ FN: Standardises a set of values
STATS            ⎕B   1566  ⍝ FN: Calculates various statistical summaries of a set of values
STRIPMEAN     R← ⎕B    624  ⍝ FN: Subtracts the mean from a set of values
STRIPOFF      R←A⎕B    870  ⍝ FN: Subtracts constant(s) from a set of values
TCDF          R←A⎕B   1464  ⍝ FN: Calculate cumulative function of Student T distribution
TDEN          R←A⎕B    871  ⍝ FN: Returns values of the Student T probability density function

TQUANT        R←A⎕B   1403  ⍝ FN: Calculate T statistic values or quantiles
TSTAT         R←A⎕B    935  ⍝ FN: Calculates the one-sample T statistic
TTAIL         R←A⎕B   1541  ⍝ FN: Calculate upper tail area of student T distribution
TWOSAMT       R←A⎕B    880  ⍝ FN: Calculates the two-sample T statistic
TWOWAY        R← ⎕B   1809  ⍝ FN: Calculate oneway analysis of variance
UNIQUE        R← ⎕B    624  ⍝ FN: Returns the unique values in a data set
VAR           R← ⎕B    671  ⍝ FN: Calculates variance of set of values
VARFT         R← ⎕B    732  ⍝ FN: Calculates variance of a frequency table
VARRATIO      R←A⎕B    504  ⍝ FN: Returns variance ratio of 2 datasets
WILCOXON      R←A⎕B    780  ⍝ FN: Wilcoxon signed rank test (allows for rank ties)
WILCOXONTS    R←A⎕B   1104  ⍝ FN: Wilcoxon signed rank test statistic, normalised form
```
