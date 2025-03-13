-- 1) Acrescentar aos médicos uma indicação sobre se estão ativos ou aposentados (inativos).
select * from medicos;

alter table medicos
add ativo char(1) default 'S' not null;

alter table medicos
add constraint ck_med_ativo check (ativo IN('S', 'N'));
-- 2) Criar também uma visão com o crm, o nome e o código da especialidade dos médicos ativos.
create view medicos_ativos as 
select crm, nome,especialidade
from medicos
where ativo = 'S';
-- 3) Em seguida, criar um mecanismo para garantir que somente médicos ativos possam solicitar novos exames.

-- 4) Depois, experimentar:
-- • Para um médico ativo, criar uma nova ficha e solicitar dois exames disponíveis quaisquer;
-- • Marcar esse médico como aposentado e tentar repetir a ação anterior.
