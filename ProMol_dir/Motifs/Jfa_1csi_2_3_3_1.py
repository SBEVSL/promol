'''
FUNC:Jfa_1csi_2_3_3_1
PDB:1csi
EC:2.3.3.1
RESI:his,his,asp
'''
cmd.select('temp0', 'n. cg')
cmd.select('temp1', 'r. his')
cmd.select('jessatom0', 'temp0&temp1')
cmd.select('temp2', 'n. nd1')
cmd.select('temp3', 'r. his')
cmd.select('temp4', 'all w. %s of jessatom0'%(d*1.403900))
cmd.select('temp5', 'br. jessatom0')
cmd.select('jessatom1', 'temp2&temp3&temp4&temp5')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom1'%(d*1.403900))
cmd.select('temp6', 'n. ne2')
cmd.select('temp7', 'all w. %s of jessatom0'%(d*2.222000))
cmd.select('temp8', 'br. jessatom0')
cmd.select('temp9', 'all w. %s of jessatom1'%(d*2.191700))
cmd.select('jessatom2', 'temp6&temp3&temp7&temp8&temp9')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom2'%(d*2.222000))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom2'%(d*2.191700))
cmd.select('temp10', 'all w. %s of jessatom0'%(d*10.180800))
cmd.select('temp11', 'all w. %s of jessatom1'%(d*9.059700))
cmd.select('temp12', 'all w. %s of jessatom2'%(d*10.443400))
cmd.select('jessatom3', 'temp0&temp3&temp10&temp11&temp12')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom3'%(d*10.180800))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom3'%(d*9.059700))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom3'%(d*10.443400))
cmd.select('temp13', 'all w. %s of jessatom0'%(d*10.251500))
cmd.select('temp14', 'all w. %s of jessatom1'%(d*9.160700))
cmd.select('temp15', 'all w. %s of jessatom2'%(d*10.281800))
cmd.select('temp16', 'all w. %s of jessatom3'%(d*1.403900))
cmd.select('temp17', 'br. jessatom3')
cmd.select('jessatom4', 'temp2&temp3&temp13&temp14&temp15&temp16&temp17')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom4'%(d*10.251500))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom4'%(d*9.160700))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom4'%(d*10.281800))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom4'%(d*1.403900))
cmd.select('temp18', 'all w. %s of jessatom0'%(d*8.736500))
cmd.select('temp19', 'all w. %s of jessatom1'%(d*7.514400))
cmd.select('temp20', 'all w. %s of jessatom2'%(d*8.675900))
cmd.select('temp21', 'all w. %s of jessatom3'%(d*2.242200))
cmd.select('temp22', 'br. jessatom3')
cmd.select('temp23', 'all w. %s of jessatom4'%(d*2.222000))
cmd.select('jessatom5', 'temp6&temp3&temp18&temp19&temp20&temp21&temp22&temp23')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom5'%(d*8.736500))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom5'%(d*7.514400))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom5'%(d*8.675900))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom5'%(d*2.242200))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom5'%(d*2.222000))
cmd.select('temp24', 'r. asp')
cmd.select('temp25', 'r. glu')
cmd.select('temp26', 'all w. %s of jessatom0'%(d*8.009300))
cmd.select('temp27', 'all w. %s of jessatom1'%(d*7.140700))
cmd.select('temp28', 'all w. %s of jessatom2'%(d*8.888000))
cmd.select('temp29', 'all w. %s of jessatom3'%(d*9.524300))
cmd.select('temp30', 'all w. %s of jessatom4'%(d*10.453500))
cmd.select('temp31', 'all w. %s of jessatom5'%(d*8.574900))
cmd.select('jessatom6', '((temp0&temp24)|(temp0&temp25))&temp26&temp27&temp28&temp29&temp30&temp31')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom6'%(d*8.009300))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom6'%(d*7.140700))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom6'%(d*8.888000))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom6'%(d*9.524300))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom6'%(d*10.453500))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom6'%(d*8.574900))
cmd.select('temp32', 'n. od1')
cmd.select('temp33', 'n. od2')
cmd.select('temp34', 'n. oe1')
cmd.select('temp35', 'n. oe2')
cmd.select('temp36', 'all w. %s of jessatom0'%(d*8.160800))
cmd.select('temp37', 'all w. %s of jessatom1'%(d*7.282100))
cmd.select('temp38', 'all w. %s of jessatom2'%(d*8.807200))
cmd.select('temp39', 'all w. %s of jessatom3'%(d*10.291900))
cmd.select('temp40', 'all w. %s of jessatom4'%(d*11.130200))
cmd.select('temp41', 'all w. %s of jessatom5'%(d*9.130400))
cmd.select('temp42', 'all w. %s of jessatom6'%(d*1.323100))
cmd.select('temp43', 'br. jessatom6')
cmd.select('jessatom7', '(((temp32|temp33)&temp24)|((temp34|temp35)&temp25))&temp36&temp37&temp38&temp39&temp40&temp41&temp42&temp43')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom7'%(d*8.160800))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom7'%(d*7.282100))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom7'%(d*8.807200))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom7'%(d*10.291900))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom7'%(d*11.130200))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom7'%(d*9.130400))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom7'%(d*1.323100))
cmd.select('temp44', 'n. od2')
cmd.select('temp45', 'n. od1')
cmd.select('temp46', 'n. oe2')
cmd.select('temp47', 'n. oe1')
cmd.select('temp48', 'all w. %s of jessatom0'%(d*7.100300))
cmd.select('temp49', 'all w. %s of jessatom1'%(d*6.191300))
cmd.select('temp50', 'all w. %s of jessatom2'%(d*8.069900))
cmd.select('temp51', 'all w. %s of jessatom3'%(d*8.585000))
cmd.select('temp52', 'all w. %s of jessatom4'%(d*9.483900))
cmd.select('temp53', 'all w. %s of jessatom5'%(d*7.645700))
cmd.select('temp54', 'all w. %s of jessatom6'%(d*1.212000))
cmd.select('temp55', 'br. jessatom6')
cmd.select('temp56', 'all w. %s of jessatom7'%(d*2.232100))
cmd.select('jessatom8', '(((temp44|temp45)&temp24)|((temp46|temp47)&temp25))&temp48&temp49&temp50&temp51&temp52&temp53&temp54&temp55&temp56')
cmd.select('jessatom0', 'jessatom0 w. %s of jessatom8'%(d*7.100300))
cmd.select('jessatom1', 'jessatom1 w. %s of jessatom8'%(d*6.191300))
cmd.select('jessatom2', 'jessatom2 w. %s of jessatom8'%(d*8.069900))
cmd.select('jessatom3', 'jessatom3 w. %s of jessatom8'%(d*8.585000))
cmd.select('jessatom4', 'jessatom4 w. %s of jessatom8'%(d*9.483900))
cmd.select('jessatom5', 'jessatom5 w. %s of jessatom8'%(d*7.645700))
cmd.select('jessatom6', 'jessatom6 w. %s of jessatom8'%(d*1.212000))
cmd.select('jessatom7', 'jessatom7 w. %s of jessatom8'%(d*2.232100))
cmd.select('Jfa_1csi_2_3_3_1', 'br. jessatom0|br. jessatom1|br. jessatom2|br. jessatom3|br. jessatom4|br. jessatom5|br. jessatom6|br. jessatom7|br. jessatom8')
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
