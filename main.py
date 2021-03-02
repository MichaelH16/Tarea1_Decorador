from decorators import consulta_tipo_sangre


@consulta_tipo_sangre
def sangre_que_puedo_recibir(sangre_paciente):

    return sangre_paciente

sangre_que_puedo_recibir("O-")