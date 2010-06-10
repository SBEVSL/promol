'''
FUNC:Jfa_1que_1_18_1_2
PDB:1que
EC:1.18.1.2
RESI:ser,cys,glu
'''
cmd.select('temp0', 'n. ca')
cmd.select('temp1', 'r. ser')
cmd.select('temp2', 'r. thr')
cmd.select('jessatom0', '((temp0&temp1)|(temp0&temp2))')
cmd.select('temp3', 'n. cb')
cmd.select('temp4', 'all w. %s of jessatom0'%(d*1.535200))
cmd.select('temp5', 'br. jessatom0')
cmd.select('jessatom1', '((temp3&temp1)|(temp3&temp2))&temp4&temp5')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom1'%(d*1.535200))
cmd.select('temp6', 'n. og')
cmd.select('temp7', 'all w. %s of jessatom0'%(d*2.444200))
cmd.select('temp8', 'br. jessatom0')
cmd.select('temp9', 'all w. %s of jessatom1'%(d*1.424100))
cmd.select('jessatom2', '((temp6&temp1)|(temp6&temp2))&temp7&temp8&temp9')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom2'%(d*2.444200))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom2'%(d*1.424100))
cmd.select('temp10', 'r. cys')
cmd.select('temp11', 'all w. %s of jessatom0'%(d*9.625300))
cmd.select('temp12', 'all w. %s of jessatom1'%(d*8.231500))
cmd.select('temp13', 'all w. %s of jessatom2'%(d*7.251800))
cmd.select('jessatom3', 'temp0&temp10&temp11&temp12&temp13')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom3'%(d*9.625300))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom3'%(d*8.231500))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom3'%(d*7.251800))
cmd.select('temp14', 'all w. %s of jessatom0'%(d*8.413300))
cmd.select('temp15', 'all w. %s of jessatom1'%(d*6.979100))
cmd.select('temp16', 'all w. %s of jessatom2'%(d*6.120600))
cmd.select('temp17', 'all w. %s of jessatom3'%(d*1.545300))
cmd.select('temp18', 'br. jessatom3')
cmd.select('jessatom4', 'temp3&temp10&temp14&temp15&temp16&temp17&temp18')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom4'%(d*8.413300))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom4'%(d*6.979100))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom4'%(d*6.120600))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom4'%(d*1.545300))
cmd.select('temp19', 'n. sg')
cmd.select('temp20', 'all w. %s of jessatom0'%(d*6.797300))
cmd.select('temp21', 'all w. %s of jessatom1'%(d*5.413600))
cmd.select('temp22', 'all w. %s of jessatom2'%(d*4.423800))
cmd.select('temp23', 'all w. %s of jessatom3'%(d*2.828000))
cmd.select('temp24', 'br. jessatom3')
cmd.select('temp25', 'all w. %s of jessatom4'%(d*1.828100))
cmd.select('jessatom5', 'temp19&temp10&temp20&temp21&temp22&temp23&temp24&temp25')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom5'%(d*6.797300))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom5'%(d*5.413600))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom5'%(d*4.423800))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom5'%(d*2.828000))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom5'%(d*1.828100))
cmd.select('temp26', 'n. cd')
cmd.select('temp27', 'r. glu')
cmd.select('temp28', 'r. asp')
cmd.select('temp29', 'all w. %s of jessatom0'%(d*5.767100))
cmd.select('temp30', 'all w. %s of jessatom1'%(d*5.221700))
cmd.select('temp31', 'all w. %s of jessatom2'%(d*4.110700))
cmd.select('temp32', 'all w. %s of jessatom3'%(d*6.464000))
cmd.select('temp33', 'all w. %s of jessatom4'%(d*5.757000))
cmd.select('temp34', 'all w. %s of jessatom5'%(d*4.514700))
cmd.select('jessatom6', '((temp26&temp27)|(temp26&temp28))&temp29&temp30&temp31&temp32&temp33&temp34')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom6'%(d*5.767100))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom6'%(d*5.221700))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom6'%(d*4.110700))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom6'%(d*6.464000))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom6'%(d*5.757000))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom6'%(d*4.514700))
cmd.select('temp35', 'n. oe1')
cmd.select('temp36', 'n. oe2')
cmd.select('temp37', 'n. od1')
cmd.select('temp38', 'n. od2')
cmd.select('temp39', 'all w. %s of jessatom0'%(d*5.979200))
cmd.select('temp40', 'all w. %s of jessatom1'%(d*5.625700))
cmd.select('temp41', 'all w. %s of jessatom2'%(d*4.747000))
cmd.select('temp42', 'all w. %s of jessatom3'%(d*7.423500))
cmd.select('temp43', 'all w. %s of jessatom4'%(d*6.645800))
cmd.select('temp44', 'all w. %s of jessatom5'%(d*5.544900))
cmd.select('temp45', 'all w. %s of jessatom6'%(d*1.262500))
cmd.select('temp46', 'br. jessatom6')
cmd.select('jessatom7', '(((temp35|temp36)&temp27)|((temp37|temp38)&temp28))&temp39&temp40&temp41&temp42&temp43&temp44&temp45&temp46')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom7'%(d*5.979200))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom7'%(d*5.625700))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom7'%(d*4.747000))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom7'%(d*7.423500))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom7'%(d*6.645800))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom7'%(d*5.544900))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom7'%(d*1.262500))
cmd.select('temp47', 'n. oe2')
cmd.select('temp48', 'n. oe1')
cmd.select('temp49', 'n. od2')
cmd.select('temp50', 'n. od1')
cmd.select('temp51', 'all w. %s of jessatom0'%(d*4.736900))
cmd.select('temp52', 'all w. %s of jessatom1'%(d*4.060200))
cmd.select('temp53', 'all w. %s of jessatom2'%(d*2.878500))
cmd.select('temp54', 'all w. %s of jessatom3'%(d*6.251900))
cmd.select('temp55', 'all w. %s of jessatom4'%(d*5.393400))
cmd.select('temp56', 'all w. %s of jessatom5'%(d*3.898600))
cmd.select('temp57', 'br. jessatom6')
cmd.select('temp58', 'all w. %s of jessatom7'%(d*2.222000))
cmd.select('jessatom8', '(((temp47|temp48)&temp27)|((temp49|temp50)&temp28))&temp51&temp52&temp53&temp54&temp55&temp56&temp45&temp57&temp58')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom8'%(d*4.736900))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom8'%(d*4.060200))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom8'%(d*2.878500))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom8'%(d*6.251900))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom8'%(d*5.393400))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom8'%(d*3.898600))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom8'%(d*1.262500))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom8'%(d*2.222000))
cmd.select('Jfa_1que_1_18_1_2', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
cmd.delete('jessatom0')
cmd.delete('jessatom1')
cmd.delete('jessatom2')
cmd.delete('jessatom3')
cmd.delete('jessatom4')
cmd.delete('jessatom5')
cmd.delete('jessatom6')
cmd.delete('jessatom7')
cmd.delete('jessatom8')
cmd.delete('temp0')
cmd.delete('temp1')
cmd.delete('temp2')
cmd.delete('temp3')
cmd.delete('temp4')
cmd.delete('temp5')
cmd.delete('temp6')
cmd.delete('temp7')
cmd.delete('temp8')
cmd.delete('temp9')
cmd.delete('temp10')
cmd.delete('temp11')
cmd.delete('temp12')
cmd.delete('temp13')
cmd.delete('temp14')
cmd.delete('temp15')
cmd.delete('temp16')
cmd.delete('temp17')
cmd.delete('temp18')
cmd.delete('temp19')
cmd.delete('temp20')
cmd.delete('temp21')
cmd.delete('temp22')
cmd.delete('temp23')
cmd.delete('temp24')
cmd.delete('temp25')
cmd.delete('temp26')
cmd.delete('temp27')
cmd.delete('temp28')
cmd.delete('temp29')
cmd.delete('temp30')
cmd.delete('temp31')
cmd.delete('temp32')
cmd.delete('temp33')
cmd.delete('temp34')
cmd.delete('temp35')
cmd.delete('temp36')
cmd.delete('temp37')
cmd.delete('temp38')
cmd.delete('temp39')
cmd.delete('temp40')
cmd.delete('temp41')
cmd.delete('temp42')
cmd.delete('temp43')
cmd.delete('temp44')
cmd.delete('temp45')
cmd.delete('temp46')
cmd.delete('temp47')
cmd.delete('temp48')
cmd.delete('temp49')
cmd.delete('temp50')
cmd.delete('temp51')
cmd.delete('temp52')
cmd.delete('temp53')
cmd.delete('temp54')
cmd.delete('temp55')
cmd.delete('temp56')
cmd.delete('temp57')
cmd.delete('temp58')
