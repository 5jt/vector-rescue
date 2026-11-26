/ Amortization scheme for annuity 
/ Variables: amount(bd), duration(d), interest rate(i), marg IRS(IB)
 \m f courier new-9
/ \m l arial-8
  \m c 0 -1 808080
  \p 16
  \c 0

/Global functions
f:{100*((1+0.01*x%y)^y)-1}/ real interest 
vn:{(1+0.01*z%y)^-x*y}/ present value
an:{(1-vn[x;y;z])%0.01*z%y}/ annuity

/ Dictionaries

\d .k.B
bd: 1.0*120000; bd..l:""; bd..f:12.2$
incbd:"bd+:1000"; decbd:"bd-:1000"		
incbd..c:decbd..c:`button
incbd..l:"+"; decbd..l:"-"
incbd..f:16.2$
.k.B..l:"Amount of annuity loan"
.k.B..a:(`bd;`incbd`decbd)

\d .k.nR
nbd: 1.0*0; nbd..l:""; nbd..f:12.2$
incnbd:"nbd+:1000"; decnbd:"nbd-:1000"		
incnbd..c:decnbd..c:`button
incnbd..l:"+"; decnbd..l:"-"
.k.nR..l:"Non Repayable"
.k.nR.[`x]:12
.k.nR..a:(`nbd;`incnbd`decnbd)

\d .k.D
d: 30; d..f:4$; d..l:""
incd:"d+:1"; decd:"d-:1"	
incd..c:decd..c:`button
incd..l:"+"; decd..l:"-"
.k.D..l:"Duration"
.k.D..a:(`d;`incd`decd)

\d .k.I
i:4.50; i..f:5.2$; i..l:""
inci:"i+:0.01"; deci:"i-:0.01"	
inci..c:deci..c:`button
inci..l:"+"; deci..l:"-"
.k.I..l:"Interest rate"
.k.I..a:(`i;`inci`deci)

/In some countries interest paid on a (mortgage) loan is deductable 
/from income for IRS; 

\d .k.IB
ib:40; ib..f:4$; ib..l:""
incib:"ib+:1"; decib:"ib-:1"	
incib..c:decib..c:`button
incib..l:"+"; decib..l:"-"
.k.IB..l:"Marg IRS %"
.k.IB..a:(`ib;`incib`decib)

\d ^

eff..e:ann..e:0
eff..l:"    Effective interest rate    "
ann..l:"    Periodical payment"

Yearly:1; Half_yearly:2; Quarterly:4; Monthly:12
term:`Monthly
term..l:"Frequency of payments"
term..c:`radio
term..o:(`Yearly `Half_yearly `Quarterly `Monthly)
term..x:18

t..d:".$term"
eff..d:"f[I.i;t]"
eff..f:5.2$
ann..d:"B.bd*%an[D.d;t;I.i]"
ann..f:8.2$
tm..d:"!D.d*t"
at..d:"sumrnd[0.01;(ann-B.bd*0.01*I.i%t)*(1+0.01*I.i%t)^!D.d*t]"
it..d:"(nR.nbd*0.01*I.i%t)+ann-at"
ml..d:"at+(1-0.01*IB.ib)*it"
rs..d:"nR.nbd+B.bd-+\\0,-1 _ at"

/ Survey
hdr:`Period`Repayment`Interest`NetPayment`Balance
fs:("6$.k.tm";"13.2$.k.at";"13.2$.k.it";"13.2$.k.ml";"15.2$.k.rs")
comp:{[x;y;z]
	a:.,(`e;0)
	t:.+(x;y;a)
	.[t;(~x;`d);:;z]}
Survey:comp[hdr;&#hdr;fs]
Survey..l:"Survey amortization schedule"

.k..l:"Amortization of Annuity"
.k..a:((`B`D`I`IB);(`nR;`term;`eff`ann);`Survey)  	/ rearrange display

`show$`.k	

/=====================================================================
\
Description: 
This program produces a survey of the amortization of an annuity loan. 
In the top section of the screen are four controls for the data. 
In the middle section are two controls and display of real interest and 
yearly annuity. 
The bottom section shows the amortization scheme with one line for 
every payment, giving redemption part, interest part, net cost and 
balance.
The + and - buttons are supposed to behave like spinboxes.


\
 Comments & questions welcome
 Middelburg (Neth), January 2006
 info@ganuenta.com


