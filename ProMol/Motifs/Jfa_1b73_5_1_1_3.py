'''
FUNC:Jfa_1b73_5_1_1_3
PDB:1b73
EC:5.1.1.3
RESI:asp,ser,cys,cys
LOCI:a-7,8,70,178;
'''
jesstemp0 ='n.  cg '
jesstemp1 ='r. asp'
jesstemp2 ='r. glu'
cmd.select('jessatom0', '(((('+jesstemp0+')&('+jesstemp1+'))|(('+jesstemp0+')&('+jesstemp2+'))))')
jesstemp3 ='n.  od1'
jesstemp4 ='n.  od2'
jesstemp5 ='n.  oe1'
jesstemp6 ='n.  oe2'
jesstemp7 ='jessatom0 x. %s'%(1.252400+(d*0.300000))
jesstemp8 ='br. jessatom0'
cmd.select('jessatom1', '((((('+jesstemp3+')|('+jesstemp4+'))&('+jesstemp1+'))|((('+jesstemp5+')|('+jesstemp6+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp8+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom1 x. %s)'%(1.252400+(d*0.300000)))
jesstemp9 ='n.  od2'
jesstemp10 ='n.  od1'
jesstemp11 ='n.  oe2'
jesstemp12 ='n.  oe1'
jesstemp13 ='br. jessatom0'
jesstemp14 ='jessatom1 x. %s'%(2.181600+(d*0.300000))
cmd.select('jessatom2', '((((('+jesstemp9+')|('+jesstemp10+'))&('+jesstemp1+'))|((('+jesstemp11+')|('+jesstemp12+'))&('+jesstemp2+')))&('+jesstemp7+')&('+jesstemp13+')&('+jesstemp14+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom2 x. %s)'%(1.252400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom2 x. %s)'%(2.181600+(d*0.300000)))
jesstemp15 ='n.  ca '
jesstemp16 ='r. ser'
jesstemp17 ='r. thr'
jesstemp18 ='jessatom0 x. %s'%(4.363200+(d*0.300000))
jesstemp19 ='jessatom1 x. %s'%(3.575400+(d*0.300000))
jesstemp20 ='jessatom2 x. %s'%(5.494400+(d*0.300000))
cmd.select('jessatom3', '(((('+jesstemp15+')&('+jesstemp16+'))|(('+jesstemp15+')&('+jesstemp17+')))&('+jesstemp18+')&('+jesstemp19+')&('+jesstemp20+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom3 x. %s)'%(4.363200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom3 x. %s)'%(3.575400+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom3 x. %s)'%(5.494400+(d*0.300000)))
jesstemp21 ='n.  cb '
jesstemp22 ='jessatom0 x. %s'%(4.989400+(d*0.300000))
jesstemp23 ='jessatom1 x. %s'%(3.908700+(d*0.300000))
jesstemp24 ='jessatom2 x. %s'%(6.029700+(d*0.300000))
jesstemp25 ='jessatom3 x. %s'%(1.525100+(d*0.300000))
jesstemp26 ='br. jessatom3'
cmd.select('jessatom4', '(((('+jesstemp21+')&('+jesstemp16+'))|(('+jesstemp21+')&('+jesstemp17+')))&('+jesstemp22+')&('+jesstemp23+')&('+jesstemp24+')&('+jesstemp25+')&('+jesstemp26+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom4 x. %s)'%(4.989400+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom4 x. %s)'%(3.908700+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom4 x. %s)'%(6.029700+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom4 x. %s)'%(1.525100+(d*0.300000)))
jesstemp27 ='n.  og '
jesstemp28 ='jessatom0 x. %s'%(4.302600+(d*0.300000))
jesstemp29 ='jessatom1 x. %s'%(3.090600+(d*0.300000))
jesstemp30 ='jessatom2 x. %s'%(5.191400+(d*0.300000))
jesstemp31 ='jessatom3 x. %s'%(2.424000+(d*0.300000))
jesstemp32 ='br. jessatom3'
jesstemp33 ='jessatom4 x. %s'%(1.424100+(d*0.300000))
cmd.select('jessatom5', '(((('+jesstemp27+')&('+jesstemp16+'))|(('+jesstemp27+')&('+jesstemp17+')))&('+jesstemp28+')&('+jesstemp29+')&('+jesstemp30+')&('+jesstemp31+')&('+jesstemp32+')&('+jesstemp33+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom5 x. %s)'%(4.302600+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom5 x. %s)'%(3.090600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom5 x. %s)'%(5.191400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom5 x. %s)'%(2.424000+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom5 x. %s)'%(1.424100+(d*0.300000)))
jesstemp34 ='r. cys'
jesstemp35 ='jessatom0 x. %s'%(4.777300+(d*0.300000))
jesstemp36 ='jessatom1 x. %s'%(4.464200+(d*0.300000))
jesstemp37 ='jessatom2 x. %s'%(5.029800+(d*0.300000))
jesstemp38 ='jessatom3 x. %s'%(6.958900+(d*0.300000))
jesstemp39 ='jessatom4 x. %s'%(6.696300+(d*0.300000))
jesstemp40 ='jessatom5 x. %s'%(5.716600+(d*0.300000))
cmd.select('jessatom6', '(('+jesstemp15+')&('+jesstemp34+')&('+jesstemp35+')&('+jesstemp36+')&('+jesstemp37+')&('+jesstemp38+')&('+jesstemp39+')&('+jesstemp40+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom6 x. %s)'%(4.777300+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom6 x. %s)'%(4.464200+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom6 x. %s)'%(5.029800+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom6 x. %s)'%(6.958900+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom6 x. %s)'%(6.696300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom6 x. %s)'%(5.716600+(d*0.300000)))
jesstemp41 ='jessatom0 x. %s'%(4.464200+(d*0.300000))
jesstemp42 ='jessatom1 x. %s'%(3.888500+(d*0.300000))
jesstemp43 ='jessatom2 x. %s'%(5.090400+(d*0.300000))
jesstemp44 ='jessatom3 x. %s'%(5.686300+(d*0.300000))
jesstemp45 ='jessatom4 x. %s'%(5.383300+(d*0.300000))
jesstemp46 ='jessatom5 x. %s'%(4.595500+(d*0.300000))
jesstemp47 ='jessatom6 x. %s'%(1.585700+(d*0.300000))
jesstemp48 ='br. jessatom6'
cmd.select('jessatom7', '(('+jesstemp21+')&('+jesstemp34+')&('+jesstemp41+')&('+jesstemp42+')&('+jesstemp43+')&('+jesstemp44+')&('+jesstemp45+')&('+jesstemp46+')&('+jesstemp47+')&('+jesstemp48+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom7 x. %s)'%(4.464200+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom7 x. %s)'%(3.888500+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom7 x. %s)'%(5.090400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom7 x. %s)'%(5.686300+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom7 x. %s)'%(5.383300+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom7 x. %s)'%(4.595500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom7 x. %s)'%(1.585700+(d*0.300000)))
jesstemp49 ='n.  sg '
jesstemp50 ='jessatom0 x. %s'%(5.443900+(d*0.300000))
jesstemp51 ='jessatom1 x. %s'%(4.504600+(d*0.300000))
jesstemp52 ='jessatom2 x. %s'%(6.150900+(d*0.300000))
jesstemp53 ='jessatom3 x. %s'%(5.464100+(d*0.300000))
jesstemp54 ='jessatom4 x. %s'%(4.686400+(d*0.300000))
jesstemp55 ='jessatom5 x. %s'%(3.888500+(d*0.300000))
jesstemp56 ='jessatom6 x. %s'%(2.999700+(d*0.300000))
jesstemp57 ='br. jessatom6'
jesstemp58 ='jessatom7 x. %s'%(1.858400+(d*0.300000))
cmd.select('jessatom8', '(('+jesstemp49+')&('+jesstemp34+')&('+jesstemp50+')&('+jesstemp51+')&('+jesstemp52+')&('+jesstemp53+')&('+jesstemp54+')&('+jesstemp55+')&('+jesstemp56+')&('+jesstemp57+')&('+jesstemp58+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom8 x. %s)'%(5.443900+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom8 x. %s)'%(4.504600+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom8 x. %s)'%(6.150900+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom8 x. %s)'%(5.464100+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom8 x. %s)'%(4.686400+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom8 x. %s)'%(3.888500+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom8 x. %s)'%(2.999700+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom8 x. %s)'%(1.858400+(d*0.300000)))
jesstemp59 ='jessatom0 x. %s'%(11.211000+(d*0.300000))
jesstemp60 ='jessatom1 x. %s'%(10.695900+(d*0.300000))
jesstemp61 ='jessatom2 x. %s'%(10.665600+(d*0.300000))
jesstemp62 ='jessatom3 x. %s'%(13.099700+(d*0.300000))
jesstemp63 ='jessatom4 x. %s'%(12.210900+(d*0.300000))
jesstemp64 ='jessatom5 x. %s'%(10.827200+(d*0.300000))
jesstemp65 ='jessatom6 x. %s'%(9.453600+(d*0.300000))
jesstemp66 ='jessatom7 x. %s'%(10.291900+(d*0.300000))
jesstemp67 ='jessatom8 x. %s'%(9.908100+(d*0.300000))
cmd.select('jessatom9', '(('+jesstemp15+')&('+jesstemp34+')&('+jesstemp59+')&('+jesstemp60+')&('+jesstemp61+')&('+jesstemp62+')&('+jesstemp63+')&('+jesstemp64+')&('+jesstemp65+')&('+jesstemp66+')&('+jesstemp67+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom9 x. %s)'%(11.211000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom9 x. %s)'%(10.695900+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom9 x. %s)'%(10.665600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom9 x. %s)'%(13.099700+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom9 x. %s)'%(12.210900+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom9 x. %s)'%(10.827200+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom9 x. %s)'%(9.453600+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom9 x. %s)'%(10.291900+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom9 x. %s)'%(9.908100+(d*0.300000)))
jesstemp68 ='jessatom0 x. %s'%(10.453500+(d*0.300000))
jesstemp69 ='jessatom1 x. %s'%(9.807100+(d*0.300000))
jesstemp70 ='jessatom2 x. %s'%(10.059600+(d*0.300000))
jesstemp71 ='jessatom3 x. %s'%(11.978600+(d*0.300000))
jesstemp72 ='jessatom4 x. %s'%(10.988800+(d*0.300000))
jesstemp73 ='jessatom5 x. %s'%(9.635400+(d*0.300000))
jesstemp74 ='jessatom6 x. %s'%(8.564800+(d*0.300000))
jesstemp75 ='jessatom7 x. %s'%(9.251600+(d*0.300000))
jesstemp76 ='jessatom8 x. %s'%(8.675900+(d*0.300000))
jesstemp77 ='jessatom9 x. %s'%(1.515000+(d*0.300000))
jesstemp78 ='br. jessatom9'
cmd.select('jessatom10', '(('+jesstemp21+')&('+jesstemp34+')&('+jesstemp68+')&('+jesstemp69+')&('+jesstemp70+')&('+jesstemp71+')&('+jesstemp72+')&('+jesstemp73+')&('+jesstemp74+')&('+jesstemp75+')&('+jesstemp76+')&('+jesstemp77+')&('+jesstemp78+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom10 x. %s)'%(10.453500+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom10 x. %s)'%(9.807100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom10 x. %s)'%(10.059600+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom10 x. %s)'%(11.978600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom10 x. %s)'%(10.988800+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom10 x. %s)'%(9.635400+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom10 x. %s)'%(8.564800+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom10 x. %s)'%(9.251600+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom10 x. %s)'%(8.675900+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom10 x. %s)'%(1.515000+(d*0.300000)))
jesstemp79 ='jessatom0 x. %s'%(9.494000+(d*0.300000))
jesstemp80 ='jessatom1 x. %s'%(8.898100+(d*0.300000))
jesstemp81 ='jessatom2 x. %s'%(9.130400+(d*0.300000))
jesstemp82 ='jessatom3 x. %s'%(11.271600+(d*0.300000))
jesstemp83 ='jessatom4 x. %s'%(10.352500+(d*0.300000))
jesstemp84 ='jessatom5 x. %s'%(8.978900+(d*0.300000))
jesstemp85 ='jessatom6 x. %s'%(7.029600+(d*0.300000))
jesstemp86 ='jessatom7 x. %s'%(7.857800+(d*0.300000))
jesstemp87 ='jessatom8 x. %s'%(7.443700+(d*0.300000))
jesstemp88 ='jessatom9 x. %s'%(2.686600+(d*0.300000))
jesstemp89 ='br. jessatom9'
jesstemp90 ='jessatom10 x. %s'%(1.807900+(d*0.300000))
cmd.select('jessatom11', '(('+jesstemp49+')&('+jesstemp34+')&('+jesstemp79+')&('+jesstemp80+')&('+jesstemp81+')&('+jesstemp82+')&('+jesstemp83+')&('+jesstemp84+')&('+jesstemp85+')&('+jesstemp86+')&('+jesstemp87+')&('+jesstemp88+')&('+jesstemp89+')&('+jesstemp90+'))')
cmd.select('jessatom0', 'jessatom0 & (jessatom11 x. %s)'%(9.494000+(d*0.300000)))
cmd.select('jessatom1', 'jessatom1 & (jessatom11 x. %s)'%(8.898100+(d*0.300000)))
cmd.select('jessatom2', 'jessatom2 & (jessatom11 x. %s)'%(9.130400+(d*0.300000)))
cmd.select('jessatom3', 'jessatom3 & (jessatom11 x. %s)'%(11.271600+(d*0.300000)))
cmd.select('jessatom4', 'jessatom4 & (jessatom11 x. %s)'%(10.352500+(d*0.300000)))
cmd.select('jessatom5', 'jessatom5 & (jessatom11 x. %s)'%(8.978900+(d*0.300000)))
cmd.select('jessatom6', 'jessatom6 & (jessatom11 x. %s)'%(7.029600+(d*0.300000)))
cmd.select('jessatom7', 'jessatom7 & (jessatom11 x. %s)'%(7.857800+(d*0.300000)))
cmd.select('jessatom8', 'jessatom8 & (jessatom11 x. %s)'%(7.443700+(d*0.300000)))
cmd.select('jessatom9', 'jessatom9 & (jessatom11 x. %s)'%(2.686600+(d*0.300000)))
cmd.select('jessatom10', 'jessatom10 & (jessatom11 x. %s)'%(1.807900+(d*0.300000)))
cmd.select('Jfa_1b73_5_1_1_3', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8|br. jessatom9|br. jessatom10|br. jessatom11')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
cmd.delete('jessatom9')
cmd.delete('jessatom10')
cmd.delete('jessatom11')
