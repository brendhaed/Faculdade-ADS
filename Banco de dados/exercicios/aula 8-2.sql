-- 2. Crie visões para consultas comuns:
-- a) VIEW PAC_IDADES
-- Paciente: nome (maiúsculas) e idade (omitindo informações sensíveis).
CREATE VIEW PAC_IDADES AS
select upper (nome) as paciente, floor(months_between(trunc(sysdate), data_nas)/12) as idade
    from pacientes;
-- b) VIEW MED_ESP
-- Médicos: crm, nome do médico e nome da especialidade.
CREATE OR REPLACE VIEW MED_ESP AS
select medicos.crm, medicos.nome as medico, especialidades.nome as especialidade
from medicos join especialidades on medicos.especialidade = especialidades.cod_especialidade;

-- c) VIEW PAC_REC
-- Paciente: cpf, nome e data da ficha mais recente.
CREATE VIEW PAC_REC AS
select pacientes.cpf, pacientes.nome, max(data) as ficha_mais_recente
from pacientes join fichas on pacientes.cod_paciente = fichas.cod_paciente
group by pacientes.cpf, paceintes.nome;

-- d) VIEW EXAM_QTD
-- Total de solicitações de cada exame
CREATE VIEW EXAM.QTD AS
select exames.sigla_exame, count(*) as qtd_pedidos
from exames join fichas_exames on exames.cod_exame = fichas_exames.cod_exame
group by exames.sigla_exame;
