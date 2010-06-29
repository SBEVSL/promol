'''
FUNC:P_1cns_3_2_1_14
PDB:1cns
EC:3.2.1.14
RESI:glu,glu,ser
'''
cmd.select('ser1', 'n. CB&r. ser w. %s of n. CB&r. glu'%(d*11.52))
cmd.select('ser2', 'n. CB&r. ser w. %s of n. CG&r. glu'%(d*11.56))
cmd.select('ser3', 'n. CB&r. ser w. %s of n. CD&r. glu'%(d*11.29))
cmd.select('ser4', 'n. CB&r. ser w. %s of n. OE1&r. glu'%(d*10.48))
cmd.select('ser5', 'n. CB&r. ser w. %s of n. OE2&r. glu'%(d*12.04))
cmd.select('ser6', 'n. OG&r. ser w. %s of n. CB&r. glu'%(d*11.14))
cmd.select('ser7', 'n. OG&r. ser w. %s of n. CG&r. glu'%(d*11.01))
cmd.select('ser8', 'n. OG&r. ser w. %s of n. CD&r. glu'%(d*10.58))
cmd.select('ser9', 'n. OG&r. ser w. %s of n. OE1&r. glu'%(d*9.77))
cmd.select('ser10', 'n. OG&r. ser w. %s of n. OE2&r. glu'%(d*11.22))
cmd.select('ser11', 'n. CB&r. ser w. %s of n. CB&r. glu'%(d*8.33))
cmd.select('ser12', 'n. CB&r. ser w. %s of n. CG&r. glu'%(d*8.71))
cmd.select('ser13', 'n. CB&r. ser w. %s of n. CD&r. glu'%(d*7.70))
cmd.select('ser14', 'n. CB&r. ser w. %s of n. OE1&r. glu'%(d*6.46))
cmd.select('ser15', 'n. CB&r. ser w. %s of n. OE2&r. glu'%(d*8.31))
cmd.select('ser16', 'n. OG&r. ser w. %s of n. CB&r. glu'%(d*8.97))
cmd.select('ser17', 'n. OG&r. ser w. %s of n. CG&r. glu'%(d*9.19))
cmd.select('ser18', 'n. OG&r. ser w. %s of n. CD&r. glu'%(d*8.11))
cmd.select('ser19', 'n. OG&r. ser w. %s of n. OE1&r. glu'%(d*6.93))
cmd.select('ser20', 'n. OG&r. ser w. %s of n. OE2&r. glu'%(d*8.61))
cmd.select('ser',' br. ser1&br. ser2&br. ser3&br. ser4&br. ser5&br. ser6&br. ser7&br. ser8&br. ser9&br. ser10&br. ser11&br. ser12&br. ser13&br. ser14&br. ser15&br. ser16&br. ser17&br. ser18&br. ser19&br. ser20')
cmd.delete('ser1')
cmd.delete('ser2')
cmd.delete('ser3')
cmd.delete('ser4')
cmd.delete('ser5')
cmd.delete('ser6')
cmd.delete('ser7')
cmd.delete('ser8')
cmd.delete('ser9')
cmd.delete('ser10')
cmd.delete('ser11')
cmd.delete('ser12')
cmd.delete('ser13')
cmd.delete('ser14')
cmd.delete('ser15')
cmd.delete('ser16')
cmd.delete('ser17')
cmd.delete('ser18')
cmd.delete('ser19')
cmd.delete('ser20')
cmd.select('glu1', 'n. CB&r. glu w. %s of n. CB&ser'%(d*11.52))
cmd.select('glu2', 'n. CB&r. glu w. %s of n. OG&ser'%(d*11.14))
cmd.select('glu3', 'n. CG&r. glu w. %s of n. CB&ser'%(d*11.56))
cmd.select('glu4', 'n. CG&r. glu w. %s of n. OG&ser'%(d*11.01))
cmd.select('glu5', 'n. CD&r. glu w. %s of n. CB&ser'%(d*11.29))
cmd.select('glu6', 'n. CD&r. glu w. %s of n. OG&ser'%(d*10.58))
cmd.select('glu7', 'n. OE1&r. glu w. %s of n. CB&ser'%(d*10.48))
cmd.select('glu8', 'n. OE1&r. glu w. %s of n. OG&ser'%(d*9.77))
cmd.select('glu9', 'n. OE2&r. glu w. %s of n. CB&ser'%(d*12.04))
cmd.select('glu10', 'n. OE2&r. glu w. %s of n. OG&ser'%(d*11.22))
cmd.select('glu11', 'n. CB&r. glu w. %s of n. CB&r. glu'%(d*11.29))
cmd.select('glu12', 'n. CB&r. glu w. %s of n. CG&r. glu'%(d*11.88))
cmd.select('glu13', 'n. CB&r. glu w. %s of n. CD&r. glu'%(d*12.15))
cmd.select('glu14', 'n. CB&r. glu w. %s of n. OE1&r. glu'%(d*11.64))
cmd.select('glu15', 'n. CB&r. glu w. %s of n. OE2&r. glu'%(d*13.03))
cmd.select('glu16', 'n. CG&r. glu w. %s of n. CB&r. glu'%(d*12.23))
cmd.select('glu17', 'n. CG&r. glu w. %s of n. CG&r. glu'%(d*12.74))
cmd.select('glu18', 'n. CG&r. glu w. %s of n. CD&r. glu'%(d*12.83))
cmd.select('glu19', 'n. CG&r. glu w. %s of n. OE1&r. glu'%(d*12.25))
cmd.select('glu20', 'n. CG&r. glu w. %s of n. OE2&r. glu'%(d*13.65))
cmd.select('glu21', 'n. CD&r. glu w. %s of n. CB&r. glu'%(d*12.11))
cmd.select('glu22', 'n. CD&r. glu w. %s of n. CG&r. glu'%(d*12.44))
cmd.select('glu23', 'n. CD&r. glu w. %s of n. CD&r. glu'%(d*12.41))
cmd.select('glu24', 'n. CD&r. glu w. %s of n. OE1&r. glu'%(d*11.87))
cmd.select('glu25', 'n. CD&r. glu w. %s of n. OE2&r. glu'%(d*13.11))
cmd.select('glu26', 'n. OE1&r. glu w. %s of n. CB&r. glu'%(d*11.07))
cmd.select('glu27', 'n. OE1&r. glu w. %s of n. CG&r. glu'%(d*11.31))
cmd.select('glu28', 'n. OE1&r. glu w. %s of n. CD&r. glu'%(d*11.25))
cmd.select('glu29', 'n. OE1&r. glu w. %s of n. OE1&r. glu'%(d*10.74))
cmd.select('glu30', 'n. OE1&r. glu w. %s of n. OE2&r. glu'%(d*11.91))
cmd.select('glu31', 'n. OE2&r. glu w. %s of n. CB&r. glu'%(d*13.21))
cmd.select('glu32', 'n. OE2&r. glu w. %s of n. CG&r. glu'%(d*13.47))
cmd.select('glu33', 'n. OE2&r. glu w. %s of n. CD&r. glu'%(d*13.36))
cmd.select('glu34', 'n. OE2&r. glu w. %s of n. OE1&r. glu'%(d*12.82))
cmd.select('glu35', 'n. OE2&r. glu w. %s of n. OE2&r. glu'%(d*13.99))
cmd.select('glu',' br. glu1&br. glu2&br. glu3&br. glu4&br. glu5&br. glu6&br. glu7&br. glu8&br. glu9&br. glu10&br. glu11&br. glu12&br. glu13&br. glu14&br. glu15&br. glu16&br. glu17&br. glu18&br. glu19&br. glu20&br. glu21&br. glu22&br. glu23&br. glu24&br. glu25&br. glu26&br. glu27&br. glu28&br. glu29&br. glu30&br. glu31&br. glu32&br. glu33&br. glu34&br. glu35')
cmd.delete('glu1')
cmd.delete('glu2')
cmd.delete('glu3')
cmd.delete('glu4')
cmd.delete('glu5')
cmd.delete('glu6')
cmd.delete('glu7')
cmd.delete('glu8')
cmd.delete('glu9')
cmd.delete('glu10')
cmd.delete('glu11')
cmd.delete('glu12')
cmd.delete('glu13')
cmd.delete('glu14')
cmd.delete('glu15')
cmd.delete('glu16')
cmd.delete('glu17')
cmd.delete('glu18')
cmd.delete('glu19')
cmd.delete('glu20')
cmd.delete('glu21')
cmd.delete('glu22')
cmd.delete('glu23')
cmd.delete('glu24')
cmd.delete('glu25')
cmd.delete('glu26')
cmd.delete('glu27')
cmd.delete('glu28')
cmd.delete('glu29')
cmd.delete('glu30')
cmd.delete('glu31')
cmd.delete('glu32')
cmd.delete('glu33')
cmd.delete('glu34')
cmd.delete('glu35')
cmd.select('glui1', 'n. CB&r. glu w. %s of n. CB&ser'%(d*8.33))
cmd.select('glui2', 'n. CB&r. glu w. %s of n. OG&ser'%(d*8.97))
cmd.select('glui3', 'n. CG&r. glu w. %s of n. CB&ser'%(d*8.71))
cmd.select('glui4', 'n. CG&r. glu w. %s of n. OG&ser'%(d*9.19))
cmd.select('glui5', 'n. CD&r. glu w. %s of n. CB&ser'%(d*7.70))
cmd.select('glui6', 'n. CD&r. glu w. %s of n. OG&ser'%(d*8.11))
cmd.select('glui7', 'n. OE1&r. glu w. %s of n. CB&ser'%(d*6.46))
cmd.select('glui8', 'n. OE1&r. glu w. %s of n. OG&ser'%(d*6.93))
cmd.select('glui9', 'n. OE2&r. glu w. %s of n. CB&ser'%(d*8.31))
cmd.select('glui10', 'n. OE2&r. glu w. %s of n. OG&ser'%(d*8.61))
cmd.select('glui11', 'n. CB&r. glu w. %s of n. CB&glu'%(d*11.29))
cmd.select('glui12', 'n. CB&r. glu w. %s of n. CG&glu'%(d*12.23))
cmd.select('glui13', 'n. CB&r. glu w. %s of n. CD&glu'%(d*12.11))
cmd.select('glui14', 'n. CB&r. glu w. %s of n. OE1&glu'%(d*11.07))
cmd.select('glui15', 'n. CB&r. glu w. %s of n. OE2&glu'%(d*13.21))
cmd.select('glui16', 'n. CG&r. glu w. %s of n. CB&glu'%(d*11.88))
cmd.select('glui17', 'n. CG&r. glu w. %s of n. CG&glu'%(d*12.74))
cmd.select('glui18', 'n. CG&r. glu w. %s of n. CD&glu'%(d*12.44))
cmd.select('glui19', 'n. CG&r. glu w. %s of n. OE1&glu'%(d*11.31))
cmd.select('glui20', 'n. CG&r. glu w. %s of n. OE2&glu'%(d*13.47))
cmd.select('glui21', 'n. CD&r. glu w. %s of n. CB&glu'%(d*12.15))
cmd.select('glui22', 'n. CD&r. glu w. %s of n. CG&glu'%(d*12.83))
cmd.select('glui23', 'n. CD&r. glu w. %s of n. CD&glu'%(d*12.41))
cmd.select('glui24', 'n. CD&r. glu w. %s of n. OE1&glu'%(d*11.25))
cmd.select('glui25', 'n. CD&r. glu w. %s of n. OE2&glu'%(d*13.36))
cmd.select('glui26', 'n. OE1&r. glu w. %s of n. CB&glu'%(d*11.64))
cmd.select('glui27', 'n. OE1&r. glu w. %s of n. CG&glu'%(d*12.25))
cmd.select('glui28', 'n. OE1&r. glu w. %s of n. CD&glu'%(d*11.87))
cmd.select('glui29', 'n. OE1&r. glu w. %s of n. OE1&glu'%(d*10.74))
cmd.select('glui30', 'n. OE1&r. glu w. %s of n. OE2&glu'%(d*12.82))
cmd.select('glui31', 'n. OE2&r. glu w. %s of n. CB&glu'%(d*13.03))
cmd.select('glui32', 'n. OE2&r. glu w. %s of n. CG&glu'%(d*13.65))
cmd.select('glui33', 'n. OE2&r. glu w. %s of n. CD&glu'%(d*13.11))
cmd.select('glui34', 'n. OE2&r. glu w. %s of n. OE1&glu'%(d*11.91))
cmd.select('glui35', 'n. OE2&r. glu w. %s of n. OE2&glu'%(d*13.99))
cmd.select('glui',' br. glui1&br. glui2&br. glui3&br. glui4&br. glui5&br. glui6&br. glui7&br. glui8&br. glui9&br. glui10&br. glui11&br. glui12&br. glui13&br. glui14&br. glui15&br. glui16&br. glui17&br. glui18&br. glui19&br. glui20&br. glui21&br. glui22&br. glui23&br. glui24&br. glui25&br. glui26&br. glui27&br. glui28&br. glui29&br. glui30&br. glui31&br. glui32&br. glui33&br. glui34&br. glui35')
cmd.delete('glui1')
cmd.delete('glui2')
cmd.delete('glui3')
cmd.delete('glui4')
cmd.delete('glui5')
cmd.delete('glui6')
cmd.delete('glui7')
cmd.delete('glui8')
cmd.delete('glui9')
cmd.delete('glui10')
cmd.delete('glui11')
cmd.delete('glui12')
cmd.delete('glui13')
cmd.delete('glui14')
cmd.delete('glui15')
cmd.delete('glui16')
cmd.delete('glui17')
cmd.delete('glui18')
cmd.delete('glui19')
cmd.delete('glui20')
cmd.delete('glui21')
cmd.delete('glui22')
cmd.delete('glui23')
cmd.delete('glui24')
cmd.delete('glui25')
cmd.delete('glui26')
cmd.delete('glui27')
cmd.delete('glui28')
cmd.delete('glui29')
cmd.delete('glui30')
cmd.delete('glui31')
cmd.delete('glui32')
cmd.delete('glui33')
cmd.delete('glui34')
cmd.delete('glui35')
cmd.select('P_1cns_3_2_1_14', 'ser|glu|glui')
cmd.delete('ser')
cmd.delete('glu')
cmd.delete('glui')
