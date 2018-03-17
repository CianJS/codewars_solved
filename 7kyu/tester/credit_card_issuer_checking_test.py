# -*- coding: utf-8 -*-

import unittest
from .. import Credit_card_issuer_checking as main

def assert_equals(function_result, credit):
    return function_result == credit

class CheckCreditCardProgram(unittest.TestCase):
    def test_VISA(self):
        self.assertTrue(assert_equals(main.getIssuer(4329555890424166), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4329555890424166), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4808625548940), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4955591833207), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4818936613393094), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4481130859922591), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4896139489641757), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4407734298655), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4857778440182953), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4500663951171), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4773834386711), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4198684192349), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4613849217332432), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4034084955899), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4465472502659), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4035942221140953), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4993939324218), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4768671839049601), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4501953714970603), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4836424205977), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4717932737711), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4975864229685), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4983088365194760), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4713663299155), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4086024854114012), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4772549516306159), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4441762857748770), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4147886706845), 'VISA'))
        self.assertTrue(assert_equals(main.getIssuer(4095303036777402), 'VISA'))

    def test_AMEX(self):
        self.assertTrue(assert_equals(main.getIssuer(348742814236952), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(371902374999721), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(377372683348301), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(343968003658123), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(346626970190297), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(344299688215766), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(374512680741387), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(343348159680662), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(346571517561021), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(340153997975538), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(379076160079530), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(374632673061160), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(379729139432173), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(340349175791831), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(344974532142307), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(375956523748541), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(374244303777032), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(377601731249084), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(371292229951713), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(345850016184750), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(347069029670014), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(343827951484692), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(377064258979348), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(376310822047773), 'AMEX'))
        self.assertTrue(assert_equals(main.getIssuer(343150594876733), 'AMEX'))

    def test_Unknown(self):
        self.assertTrue(assert_equals(main.getIssuer(3864123471046), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(7860540203134173), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(7922775784056738), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(8905299555341744), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(2835532515968), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(7322188184261554), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(9668775964086901), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(3671924706729), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(6172639945580667), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(7595526966304131), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(2209411410513), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(8733207832690790), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(9314274499161961), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(7618572812128027), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(9475022703153205), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(3902065959509), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(6733438204304087), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(8965732293733824), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(1084934870573), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(8175421285885290), 'Unknown'))
        self.assertTrue(assert_equals(main.getIssuer(6416130086908048), 'Unknown'))

    def test_Mastercard(self):
        self.assertTrue(assert_equals(main.getIssuer(5560992956176522), 'Mastercard'))
        self.assertTrue(assert_equals(main.getIssuer(5129252664174119), 'Mastercard'))
        self.assertTrue(assert_equals(main.getIssuer(5256473260302356), 'Mastercard'))
        self.assertTrue(assert_equals(main.getIssuer(5491479171305734), 'Mastercard'))
        self.assertTrue(assert_equals(main.getIssuer(5312209035627281), 'Mastercard'))
        self.assertTrue(assert_equals(main.getIssuer(5212907242466085), 'Mastercard'))
        self.assertTrue(assert_equals(main.getIssuer(5252823694263417), 'Mastercard'))
        self.assertTrue(assert_equals(main.getIssuer(5304511403528491), 'Mastercard'))
        self.assertTrue(assert_equals(main.getIssuer(5359601362236973), 'Mastercard'))
        self.assertTrue(assert_equals(main.getIssuer(5562197950541074), 'Mastercard'))

    def test_Discover(self):
        self.assertTrue(assert_equals(main.getIssuer(6011760793779037), 'Discover'))
        self.assertTrue(assert_equals(main.getIssuer(6011650822182312), 'Discover'))
        self.assertTrue(assert_equals(main.getIssuer(6011925281961563), 'Discover'))
        self.assertTrue(assert_equals(main.getIssuer(6011120325769758), 'Discover'))
        self.assertTrue(assert_equals(main.getIssuer(6011990929651397), 'Discover'))
        self.assertTrue(assert_equals(main.getIssuer(6011633821822131), 'Discover'))
        self.assertTrue(assert_equals(main.getIssuer(6011719895308753), 'Discover'))
        self.assertTrue(assert_equals(main.getIssuer(6011758799287867), 'Discover'))
        self.assertTrue(assert_equals(main.getIssuer(6011711798725994), 'Discover'))
        self.assertTrue(assert_equals(main.getIssuer(6011221381922686), 'Discover'))
        self.assertTrue(assert_equals(main.getIssuer(6011784947430625), 'Discover'))
        self.assertTrue(assert_equals(main.getIssuer(6011458776475852), 'Discover'))
        self.assertTrue(assert_equals(main.getIssuer(6011389468672619), 'Discover'))
        self.assertTrue(assert_equals(main.getIssuer(6011480919641341), 'Discover'))
        self.assertTrue(assert_equals(main.getIssuer(6011231652095589), 'Discover'))
        self.assertTrue(assert_equals(main.getIssuer(6011002902710826), 'Discover'))

if __name__ == "__main__":
    test_case = CheckCreditCardProgram()
    test_suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
