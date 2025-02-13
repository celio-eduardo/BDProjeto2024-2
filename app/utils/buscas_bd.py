from app.database import execute_sql


def buscar_cpf_tutor_por_id(id_tutor):
    query = "SELECT cpf FROM Tutor WHERE id_tutor = %s"
    cpf = execute_sql(query, (id_tutor,), fetch_one=True)
    return cpf[0] if cpf else None


def buscar_id_tutor_por_cpf(cpf):
    query = "SELECT id_tutor FROM Tutor WHERE cpf = %s"
    id_tutor = execute_sql(query, (cpf,), fetch_one=True)
    return id_tutor[0] if id_tutor else None


def buscar_id_tutor_por_id_animal(id_animal):
    query = "SELECT id_tutor FROM Animal WHERE id_animal = %s"
    id_tutor = execute_sql(query, (id_animal,), fetch_one=True)
    return id_tutor[0] if id_tutor else None


def buscar_animais_por_id_tutor(id_tutor):
    query = "SELECT * FROM Animal WHERE id_tutor = %s"
    animais = execute_sql(query, (id_tutor,), fetch_all=True)
    return animais if animais else None


def buscar_animais_por_cpf_tutor(cpf):
    query = "SELECT * FROM Animal WHERE id_tutor = (SELECT id_tutor FROM Tutor WHERE cpf = %s)"
    animais = execute_sql(query, (cpf,), fetch_all=True)
    return animais if animais else None


def buscar_vet_por_especialidade_turno(especialidade_id, turno_id=None):
    query = """
            SELECT v.id_veterinario, u.nome AS nome_veterinario
            FROM Veterinario v
            JOIN Usuario u ON v.id_veterinario = u.id_usuario
            WHERE v.id_especialidade = %s
        """
    params = [especialidade_id]
    if turno_id:
        query += """
                AND v.id_veterinario IN (
                    SELECT id_veterinario FROM Carga_Horaria WHERE turno = %s
                )
            """
        params.append(turno_id)

    veterinarios = execute_sql(query, tuple(params), fetch_all=True)
    veterinarios_lista = [{"id": v[0], "nome": v[1]} for v in veterinarios]

    return veterinarios_lista if veterinarios_lista else None
