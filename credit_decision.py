def evaluar_credito(
    edad,
    ingresos_mensuales,
    deuda_actual,
    historial_crediticio,
    empleo_estable,
    monto_solicitado
):
    """
    Evalúa si se concede un crédito basado en múltiples criterios.
    Devuelve True si se aprueba, False en caso contrario.
    """
    mensaje = ""
    # Condición 1: Edad debe estar entre 18 y 70 años
    if edad < 18 or edad > 70:
        print("Rechazado por edad fuera de rango permitido")
        return False  # Rechazado por edad fuera de rango permitido

    # Condición 2: Ingresos mensuales deben ser mayores a 1000€
    if ingresos_mensuales <= 1000:
        print("Ingresos insuficientes")
        return False  # Ingresos insuficientes

    # Condición 3: La deuda actual no debe superar el 50% de los ingresos mensuales
    if deuda_actual > ingresos_mensuales * 0.5:
        print("Alta carga de deuda")
        return False  # Alta carga de deuda

    # Condición 4: Si el historial crediticio es "malo", se rechaza automáticamente
    if historial_crediticio == "malo":
        print("riesgo muy alto")
        return False  # Riesgo muy alto

    # Condición 5: Si el historial es "regular", se requiere empleo estable y deuda baja
    if historial_crediticio == "regular":
        if not empleo_estable or deuda_actual > ingresos_mensuales * 0.3:
            print("Condiciones insuficientes para historial regular")
            return False  # Condiciones insuficientes para historial regular
        else:
            return True

    # Condición 6: El monto solicitado no debe exceder 4 veces los ingresos anuales
    ingresos_anuales = ingresos_mensuales * 12
    if monto_solicitado > ingresos_anuales * 4:
        print("Solicitud excesiva respecto a capacidad de pago")
        return False  # Solicitud excesiva respecto a capacidad de pago

    # Condición 7: Si tiene historial "bueno", empleo estable y cumplió todo lo anterior, se aprueba
    if historial_crediticio == "bueno" and empleo_estable:
        print("Aprobado Buen perfil")
        return True  # Aprobado con buen perfil
    else:
        print("no aprobado")
     
    # Condición 8: Caso límite: historial "bueno" pero sin empleo estable → se evalúa carga de deuda
    if historial_crediticio == "bueno" and not empleo_estable:
        if deuda_actual <= ingresos_mensuales * 0.2:
            print("Aprobado por bajo endeudamiento a pesar de inestabilidad")
            return True  # Aprobado por bajo endeudamiento a pesar de inestabilidad
        else:
            print("Rechazado por riesgo combinado")
            return False  # Rechazado por riesgo combinado

    # Por defecto, rechazar (seguridad)
    return False