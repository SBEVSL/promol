'''
FUNC:Jfa_1njs_2_1_2_2
PDB:1njs
EC:2.1.2.2
RESI:asn,his,thr,asp
LOCI:a-106,108,135,144;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. asn'
jesstemp2 ='r. gln'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  od1'
jesstemp4 ='jessatom0 x. %s'%(1.242300+(d*0.300000))
jesstemp5 ='br. jessatom0'
cmd.select('jessatom1', '(((('+jesstemp3+')&('+jesstemp1+'))|(('+jesstemp3+')&('+jesstemp2+')))&('+jesstemp4+')&('+jesstemp5+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.242300+(d*0.300000)))
jesstemp6 ='n.  nd2'
jesstemp7 ='jessatom0 x. %s'%(1.333200+(d*0.300000))
jesstemp8 ='br. jessatom0'
jesstemp9 ='jessatom1 x. %s'%(2.262400+(d*0.300000))
cmd.select('jessatom2', '(((('+jesstemp6+')&('+jesstemp1+'))|(('+jesstemp6+')&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+')&('+jesstemp9+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.333200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.262400+(d*0.300000)))
jesstemp10 ='r. his'
jesstemp11 ='jessatom0 x. %s'%(6.211500+(d*0.300000))
jesstemp12 ='jessatom1 x. %s'%(6.817500+(d*0.300000))
jesstemp13 ='jessatom2 x. %s'%(4.959100+(d*0.300000))
cmd.select('jessatom3', '(('+jesstemp0+')&('+jesstemp10+')&('+jesstemp11+')&('+jesstemp12+')&('+jesstemp13+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(6.211500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(6.817500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(4.959100+(d*0.300000)))
jesstemp14 ='n.  nd1'
jesstemp15 ='jessatom0 x. %s'%(6.241800+(d*0.300000))
jesstemp16 ='jessatom1 x. %s'%(6.696300+(d*0.300000))
jesstemp17 ='jessatom2 x. %s'%(4.999500+(d*0.300000))
jesstemp18 ='jessatom3 x. %s'%(1.393800+(d*0.300000))
jesstemp19 ='br. jessatom3'
cmd.select('jessatom4', '(('+jesstemp14+')&('+jesstemp10+')&('+jesstemp15+')&('+jesstemp16+')&('+jesstemp17+')&('+jesstemp18+')&('+jesstemp19+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(6.241800+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(6.696300+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(4.999500+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.393800+(d*0.300000)))
jesstemp20 ='n.  ne2'
jesstemp21 ='jessatom0 x. %s'%(8.241600+(d*0.300000))
jesstemp22 ='jessatom1 x. %s'%(8.787000+(d*0.300000))
jesstemp23 ='jessatom2 x. %s'%(6.948800+(d*0.300000))
jesstemp24 ='jessatom3 x. %s'%(2.222000+(d*0.300000))
jesstemp25 ='br. jessatom3'
jesstemp26 ='jessatom4 x. %s'%(2.171500+(d*0.300000))
cmd.select('jessatom5', '(('+jesstemp20+')&('+jesstemp10+')&('+jesstemp21+')&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(8.241600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(8.787000+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(6.948800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.222000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(2.171500+(d*0.300000)))
jesstemp27 ='r. asp'
jesstemp28 ='r. glu'
jesstemp29 ='jessatom0 x. %s'%(6.201400+(d*0.300000))
jesstemp30 ='jessatom1 x. %s'%(6.878100+(d*0.300000))
jesstemp31 ='jessatom2 x. %s'%(5.009600+(d*0.300000))
jesstemp32 ='jessatom3 x. %s'%(4.161200+(d*0.300000))
jesstemp33 ='jessatom4 x. %s'%(3.545100+(d*0.300000))
jesstemp34 ='jessatom5 x. %s'%(4.534900+(d*0.300000))
cmd.select('jessatom6', '(((('+jesstemp0+')&('+jesstemp27+'))|(('+jesstemp0+')&('+jesstemp28+')))&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+')&('+jesstemp34+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(6.201400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(6.878100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.009600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(4.161200+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(3.545100+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(4.534900+(d*0.300000)))
jesstemp35 ='n.  od2'
jesstemp36 ='n.  oe1'
jesstemp37 ='n.  oe2'
jesstemp38 ='jessatom0 x. %s'%(4.938900+(d*0.300000))
jesstemp39 ='jessatom1 x. %s'%(5.635800+(d*0.300000))
jesstemp40 ='jessatom2 x. %s'%(3.747100+(d*0.300000))
jesstemp41 ='jessatom3 x. %s'%(3.949100+(d*0.300000))
jesstemp42 ='jessatom4 x. %s'%(3.464300+(d*0.300000))
jesstemp43 ='jessatom5 x. %s'%(4.928800+(d*0.300000))
jesstemp44 ='jessatom6 x. %s'%(1.272600+(d*0.300000))
jesstemp45 ='br. jessatom6'
cmd.select('jessatom7', '((((('+jesstemp3+')|('+jesstemp35+'))&('+jesstemp27+'))|((('+jesstemp36+')|('+jesstemp37+'))&('+jesstemp28+')))&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(4.938900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(5.635800+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(3.747100+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(3.949100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(3.464300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(4.928800+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.272600+(d*0.300000)))
jesstemp46 ='n.  od2'
jesstemp47 ='n.  od1'
jesstemp48 ='n.  oe2'
jesstemp49 ='n.  oe1'
jesstemp50 ='jessatom0 x. %s'%(6.857900+(d*0.300000))
jesstemp51 ='jessatom1 x. %s'%(7.362900+(d*0.300000))
jesstemp52 ='jessatom2 x. %s'%(5.676200+(d*0.300000))
jesstemp53 ='jessatom3 x. %s'%(4.252100+(d*0.300000))
jesstemp54 ='jessatom4 x. %s'%(3.282500+(d*0.300000))
jesstemp55 ='jessatom5 x. %s'%(4.181400+(d*0.300000))
jesstemp56 ='jessatom6 x. %s'%(1.262500+(d*0.300000))
jesstemp57 ='br. jessatom6'
jesstemp58 ='jessatom7 x. %s'%(2.181600+(d*0.300000))
cmd.select('jessatom8', '((((('+jesstemp46+')|('+jesstemp47+'))&('+jesstemp27+'))|((('+jesstemp48+')|('+jesstemp49+'))&('+jesstemp28+')))&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(6.857900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(7.362900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(5.676200+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(4.252100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(3.282500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(4.181400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(1.262500+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(2.181600+(d*0.300000)))
cmd.select('Jfa_1njs_2_1_2_2', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
