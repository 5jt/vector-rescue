NB.    Five-Integrator Differential Analyzer (J406 and J504)
NB.    Keith Smillie
NB.    Department of Computing Science
NB.    University of Alberta
NB.    Edmonton, Alberta T6G 2E8
NB.    March 2008

NB.   This program, which is designed for use with a Windows form, 
NB.   simulates a five-integrator Meccano differential analyzer. 
NB.   Input: Number of integrators (1, 2, 3, 4 or 5)
NB.          Definition of integrators
NB.          Definition of auxiliary buses and initial values, if required 
NB.          Minimum and maximum values of independent variable
NB.          Increment for independent variable
NB.          Initial values for integrators
NB.
NB.   Output: Final value of dependent variables for integrators
NB.           Graph of integrated function (The default graph is y vs x.) 
               
load 'format plot strings winlib'

NB. List of integrator tables
Tables=: 'TABLE0';'TABLE1';'TABLE2';'TABLE3';'TABLE4';'TABLE5'

NB. General utilities
hfu=: '_-'&charsub
Copy=: empty@(wdclipwrite@hfu@clipfmt)
EACH=: &>
cut=: <;._2
ap=: {.@]+1&{@]*i.@{:@]      

NB. Plot utilities
Plot=: 3 : 0
plot <"1 |: y.
)

WDplot=: 3 : 0
:
a=. conew 'jzplot'          
PForm__a=. 'myplot'           
PFormhwnd__a=. wd 'qhwndp'    
PId__a=. x. 
plot__a y.
)

PlotGraph=: 3 : 0
T1=: i. 0
if. rb20 = '1' do. 
   T1=: X
elseif. rb21 = '1' do.
   T1=: {:"1 TABLE1
elseif. (rb22 = '1') *. (n >: 2) do.
   T1=: {:"1 TABLE2
elseif. (rb23 = '1') *. (n >: 3) do.
   T1=: {:"1 TABLE3
elseif. (rb24 = '1') *. (n >: 4) do.
   T1=: {:"1 TABLE4
elseif. (rb25 = '1') *. (n = 5) do.
   T1=: {:"1 TABLE5
end.
T2=: i. 0
if. rb30 = '1' do.
   T2=: {:"1 TABLE1
elseif. (rb31 = '1') *. (n >: 2) do.
   T2=: {:"1 TABLE2
elseif. (rb32 = '1') *. (n >: 3) do.
   T2=: {:"1 TABLE3
elseif. (rb33 = '1') *. (n >: 4) do.
   T2=: {:"1 TABLE4
elseif. (rb34 = '1') *. (n = 5) do.
   T2=: {:"1 TABLE5
elseif. (rb35 = '1') *. (numaux >: 1) do.
   T2=: List6
elseif. (rb36 = '1') *. (numaux >: 2) do.
   T2=: List7
elseif. (rb37 = '1') *. (numaux >: 3) do.
   T2=: List8
elseif. (rb38 = '1') *. (numaux >: 4) do.
   T2=: List9
elseif. (rb39 = '1') *. (numaux >: 5) do.
   T2=: List10
end.
if. (1 < #T1) *. (1 < #T2) do.    
   'g1' WDplot T1;T2
   TABLE=: T1,.T2
end.
)

NB. Increment for integrators
Increment=: 3 : 0
r=: --/({:"1) _2 {. ".>y.{ Tables
)

NB. Integrators
I=: 3 : 0
:
inc=: Increment x.
R=. ({:{:TABLE1) +  inc*y.
R[TABLE1=: TABLE1, (({.{:TABLE1) + inc),R
)

II=: 3 : 0
:
inc=: Increment x.
R=. ({:{:TABLE2) +  inc*y.
R[TABLE2=: TABLE2, (({.{:TABLE2) + inc),R
)

III=: 3 : 0
:
inc=: Increment x.
R=. ({:{:TABLE3) +  inc*y.
R[TABLE3=: TABLE3, (({.{:TABLE3) + inc),R
)

IV=: 3 : 0
:
:inc=: Increment x.
R=. ({:{:TABLE4) +  inc*y.
R[TABLE4=: TABLE4, (({.{:TABLE4) + inc),R
)

V=: 3 : 0
:
inc=: Increment x.
R=. ({:{:TABLE5) +  inc*y.
R[TABLE5=: TABLE5, (({.{:TABLE5) + inc),R
)

NB. Integration
da5=: 3 : 0
:
num=. x. 
('xmin xmax incr z1 z2 z3 z4 z5')=: 8{.y. 
AuxillaryBuses=: cut busdef
numaux=: #AuxillaryBuses
'z6 z7 z8 z9 z10'=: 5{.". EACH cut businit
TABLE0=: 2 2$0,0,0,incr   
TABLE1=: 2 2$0,z1
TABLE2=: 2 2$0,z2
TABLE3=: 2 2$0,z3
TABLE4=: 2 2$0,z4
TABLE5=: 2 2$0,z5
List6=: z6
List7=: z7
List8=: z8
List9=: z9
List10=: z10
z0=: t=: x=: xmin
X=: xmin
while. x < xmax do.
   if. num >: 1 do. ". Iexp end.
   if. num >: 2 do. ". IIexp end.
   if. num >: 3 do. ". IIIexp end.
   if. num >: 4 do. ". IVexp end.
   if. num = 5  do. ". Vexp end.
   ". EACH AuxillaryBuses
   if. numaux >: 1 do. List6=: List6, z6 end.
   if. numaux >: 2 do. List7=: List7, z7 end.
   if. numaux >: 3 do. List8=: List8, z8 end.
   if. numaux >: 4 do. List9=: List9, z9 end.
   if. numaux >: 5 do. List10=: List10, z10 end.
   z0=: t=: x=: x + incr
   X=: X, x
end.
)

NB. Windows form
DA5=: 0 : 0
pc da5;
xywh 5 10 121 230;cc frame1 groupbox;cn " Integrators";
xywh 10 20 20 14;cc rb10 radiobutton;cn " 1";
xywh 30 20 20 14;cc rb11 radiobutton group;cn " 2";
xywh 55 20 20 14;cc rb12 radiobutton group;cn " 3";
xywh 80 20 20 14;cc rb13 radiobutton group;cn " 4";
xywh 105 20 20 14;cc rb14 radiobutton group;cn " 5";
xywh 10 40 100 20;cc integ1 editm ws_hscroll;
xywh 45 65 60 14;cc integ1name static;cn "Integrator 1";
xywh 10 80 100 20;cc integ2 editm ws_hscroll;
xywh 45 105 60 14;cc integ2name static;cn "Integrator 2";
xywh 10 120 100 20;cc integ3 editm ws_hscroll;
xywh 45 145 60 14;cc integ3name static;cn "Integrator 3";
xywh 10 160 100 20;cc integ4 editm ws_hscroll;
xywh 45 185 60 14;cc integ4name static;cn "Integrator 4";
xywh 10 200 100 20;cc integ5 editm ws_hscroll;
xywh 45 225 60 14;cc integ5name static;cn "Integrator 5";
xywh 24 250 34 14;cc ok button;cn " OK";
xywh 74 250 34 14;cc reset button;cn " Reset";
xywh 45 275 34 14;cc cancel button;cn "Cancel";
xywh 135 10 80 170;cc frame2 groupbox;cn " Initial values";
xywh 140 22 30 10;cc min edit;
xywh 175 23 30 10;cc minimum static;cn "Minimum";
xywh 140 42 30 10;cc max edit;
xywh 175 43 30 10;cc maxname static;cn "Maximum";
xywh 140 62 30 10;cc incr0 edit;
xywh 175 63 30 10;cc incr0name static;cn "Increment";
xywh 140 82 30 10;cc init1 edit;
xywh 175 83 30 10;cc init1name static;cn "Integrator 1";
xywh 140 102 30 10;cc init2 edit;
xywh 175 103 30 10;cc init2name static;cn "Integrator 2";
xywh 140 122 30 10;cc init3 edit;
xywh 175 123 30 10;cc init3name static;cn "Integrator 3";
xywh 140 142 30 10;cc init4 edit;
xywh 175 143 30 10;cc init4name static;cn "Integrator 4";
xywh 140 162 30 10;cc init5 edit;
xywh 175 163 30 10;cc init5name static;cn "Integrator 5";
xywh 135 190 80 110;cc frame3 groupbox;cn "Final values";
xywh 140 202 30 10;cc final1 edit;
xywh 175 203 30 10;cc final1name static;cn "Integrator 1";
xywh 140 222 30 10;cc final2 edit;
xywh 175 223 30 10;cc final2name static;cn "Integrator 2";
xywh 140 242 30 10;cc final3 edit;
xywh 175 243 30 10;cc final3name static;cn "Integrator 3";
xywh 140 262 30 10;cc final4 edit;
xywh 175 263 30 10;cc final4name static;cn "Integrator 4";
xywh 140 282 30 10;cc final5 edit;
xywh 175 283 30 10;cc final5name static;cn "Integrator 5";
xywh 225 13 200 150;cc g1 isigraph;
xywh 255 185 20 14;cc rb20 radiobutton;cn " 0";
xywh 280 185 20 14;cc rb21 radiobutton group;cn " 1";
xywh 305 185 20 14;cc rb22 radiobutton group;cn " 2";
xywh 330 185 20 14;cc rb23 radiobutton group;cn " 3";
xywh 355 185 20 14;cc rb24 radiobutton group;cn " 4";
xywh 380 185 20 14;cc rb25 radiobutton group;cn " 5";
xywh 244 175 162 60;cc frame4 groupbox;cn " Graphs";
xywh 280 200 20 14;cc rb30 radiobutton;cn " 1";
xywh 305 200 20 14;cc rb31 radiobutton group;cn " 2";
xywh 330 200 20 14;cc rb32 radiobutton group;cn " 3";
xywh 355 200 20 14;cc rb33 radiobutton group;cn " 4";
xywh 380 200 20 14;cc rb34 radiobutton group;cn " 5";
xywh 280 215 20 14;cc rb35 radiobutton group;cn " 6";
xywh 305 215 20 14;cc rb36 radiobutton group;cn " 7";
xywh 330 215 20 14;cc rb37 radiobutton group;cn " 8";
xywh 355 215 20 14;cc rb38 radiobutton group;cn " 9";
xywh 380 215 20 14;cc rb39 radiobutton group;cn " 10";
xywh 283 245 34 14;cc moreplot button;cn "Plot";
xywh 333 245 34 14;cc clear button;cn "Clear";
xywh 308 270 34 14;cc copy button;cn "Copy";
xywh 5 317 240 53;cc frame5 groupbox;cn " Additional Buses";
xywh 10 330 135 20;cc busdef editm ws_hscroll;
xywh 60 355 30 10;cc busdefname static;cn "Definitions";
xywh 160 330 70 20;cc businit editm ws_hscroll;
xywh 185 355 30 10;cc businitname static;cn "Initial values";
pas 6 6;pcenter;
rem form end;
)
  
Reset=: 3 : 0
wd 'set integ1 *',' '
wd 'set integ2 *',' '
wd 'set integ3 *',' '
wd 'set integ4 *',' '
wd 'set integ5 *',' '
wd 'set min *', ' '
wd 'set max *',' '
wd 'set incr0 *',' '
wd 'set init1 *',' '
wd 'set init2 *',' '
wd 'set init3 *',' '
wd 'set init4 *',' '
wd 'set init5 *',' '
wd 'set final1 *',' '
wd 'set final2 *',' '
wd 'set final3 *',' '
wd 'set final4 *',' '
wd 'set final5 *', ' ' 
wd 'set rb10 1'
wd 'set rb20 1'
wd 'set rb30 1'
wd 'set busdef *',' '
wd 'set businit *',' '
'g1' WDplot 0 0;0 0
TABLE0=: TABLE1=: TABLE2=: TABLE3=: TABLE4=: TABLE5=: i. 0 0
List6=: List7=: List8=: List9=: List10=: i. 0
)

da5_run=: 3 : 0
wd DA5
wd 'setfont integ1 "MS Sans Serif" 12 bold;'
wd 'setfont integ2 "MS Sans Serif" 12 bold;'
wd 'setfont integ3 "MS Sans Serif" 12 bold;'
wd 'setfont integ4 "MS Sans Serif" 12 bold;'
wd 'setfont integ5 "MS Sans Serif" 11 bold;'
wd 'setfont min "MS Sans Serif" 11 bold;'
wd 'setfont max "MS Sans Serif" 11 bold;'
wd 'setfont incr0 "MS Sans Serif" 11 bold;'
wd 'setfont init1 "MS Sans Serif" 11 bold;'
wd 'setfont init2 "MS Sans Serif" 11 bold;'
wd 'setfont init3 "MS Sans Serif" 11 bold;'
wd 'setfont init4 "MS Sans Serif" 11 bold;'
wd 'setfont init5 "MS Sans Serif" 11 bold;'
wd 'setfont final1 "MS Sans Serif" 11 bold;'
wd 'setfont final2 "MS Sans Serif" 11 bold;'
wd 'setfont final3 "MS Sans Serif" 11 bold;'
wd 'setfont final4 "MS Sans Serif" 11 bold;'
wd 'setfont final5 "MS Sans Serif" 11 bold;'
wd 'setfont busdef "MS Sans Serif" 11 bold;'
wd 'setfont businit "MS Sans Serif" 11 bold;'
'g1' WDplot 0 0;0 0
wd 'pshow'
)

da5_ok_button=: 3 : 0
if. rb10 = '1' do. 
   n =: 1
   Iexp=: integ1
   y=: 8{. ". min,' ', max,' ', incr0,' ', init1
   elseif. rb11 = '1' do. 
   n =: 2      
   Iexp=: integ1
   IIexp=: integ2
   y=: 8{. ". min,' ', max,' ', incr0,' ', init1,' ', init2
   elseif. rb12 = '1' do.
   n=: 3
   Iexp=: integ1
   IIexp=: integ2
   IIIexp=: integ3
   y=: 8{. ". min,' ', max,' ', incr0,' ', init1,' ', init2,' ',init3
   elseif. rb13 = '1' do.
   n=: 4
   Iexp=: integ1
   IIexp=: integ2
   IIIexp=: integ3
   IVexp=: integ4
   y=: 8{. ". min,' ', max,' ', incr0,' ', init1,' ', init2,' ', init3,' ', init4
   elseif. rb14 = '1' do.
   n =: 5
   Iexp=: integ1
   IIexp=: integ2
   IIIexp=: integ3
   IVexp=: integ4
   Vexp=: integ5
   y=: 8{. ". min,' ', max,' ', incr0,' ', init1,' ', init2,' ', init3,' ', init4,' ', init5
   end.
n da5 y
if. n = 1 do.
   wd 'set final1 *',10.5&":{:{:TABLE1
elseif. n = 2 do.
   wd 'set final1 *',10.5&":{:{:TABLE1  
   wd 'set final2 *',10.5&":{:{:TABLE2
elseif. n = 3 do.
   wd 'set final1 *',10.5&":{:{:TABLE1
   wd 'set final2 *',10.5&":{:{:TABLE2
   wd 'set final3 *',10.5&":{:{:TABLE3
elseif. n = 4 do.
   wd 'set final1 *',10.5&":{:{:TABLE1
   wd 'set final2 *',10.5&":{:{:TABLE2
   wd 'set final3 *',10.5&":{:{:TABLE3
   wd 'set final4 *',10.5&":{:{:TABLE4
elseif. n = 5 do.
   wd 'set final1 *',10.5&":{:{:TABLE1
   wd 'set final2 *',10.5&":{:{:TABLE2
   wd 'set final3 *',10.5&":{:{:TABLE3
   wd 'set final4 *',10.5&":{:{:TABLE4
   wd 'set final5 *',10.5&":{:{:TABLE5
end.
TABLE1=: }.TABLE1
TABLE2=: }.TABLE2
TABLE3=: }.TABLE3
TABLE4=: }.TABLE4
TABLE5=: }.TABLE5
PlotGraph ''
)

da5_moreplot_button=: 3 : 0
PlotGraph ''
)

da5_copy_button=: 3 : 0
Plot TABLE
)

da5_clear_button=: 3 : 0
'g1' WDplot 0 0;0 0
)

da5_reset_button=: 3 : 0
Reset ''
)

da5_close=: 3 : 0
wd'pclose'
)

da5_cancel_button=: 3 : 0
da5_close''
)

