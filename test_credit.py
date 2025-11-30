import unittest
from credit_decision import evaluar_credito

class TestCreditDecision(unittest.TestCase):

    def test_aprobado_perfil_ideal(self):
        self.assertTrue(evaluar_credito(
            edad=35,
            ingresos_mensuales=3000,
            deuda_actual=500,
            historial_crediticio="bueno",
            empleo_estable=True,
            monto_solicitado=50000
        ))

    def test_rechazado_edad_menor_18(self):
        self.assertFalse(evaluar_credito(
            edad=17,
            ingresos_mensuales=2000,
            deuda_actual=0,
            historial_crediticio="bueno",
            empleo_estable=True,
            monto_solicitado=10000
        ))

    def test_rechazado_historial_malo(self):
        self.assertFalse(evaluar_credito(
            edad=40,
            ingresos_mensuales=5000,
            deuda_actual=0,
            historial_crediticio="malo",
            empleo_estable=True,
            monto_solicitado=20000
        ))

    def test_rechazado_ingresos_bajos(self):
        self.assertFalse(evaluar_credito(
            edad=25,
            ingresos_mensuales=800,
            deuda_actual=200,
            historial_crediticio="bueno",
            empleo_estable=True,
            monto_solicitado=10000
        ))

    def test_aprobado_historial_regular_con_empleo(self):
        self.assertTrue(evaluar_credito(
            edad=30,
            ingresos_mensuales=2500,
            deuda_actual=600,  
            historial_crediticio="regular",
            empleo_estable=True,
            monto_solicitado=30000
        ))

    def test_rechazado_historial_regular_sin_empleo(self):
        self.assertFalse(evaluar_credito(
            edad=30,
            ingresos_mensuales=2500,
            deuda_actual=600,
            historial_crediticio="regular",
            empleo_estable=False,
            monto_solicitado=30000
        ))

    def test_rechazado_monto_excesivo(self):
        self.assertFalse(evaluar_credito(
            edad=40,
            ingresos_mensuales=2000,
            deuda_actual=0,
            historial_crediticio="bueno",
            empleo_estable=True,
            monto_solicitado=100000  # Ingresos anuales = 24k → límite = 96k
        ))

if __name__ == '__main__':
    unittest.main()