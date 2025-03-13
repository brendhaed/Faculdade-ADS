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
create or replace  trigger fichas_medicos_ativos
before insert or update on fichas
for each row
declare 
    ex_medico_inativo exception;
    crm_medico_qtd number;
begin
select count(*) INTO crm_medico_qtd
    from medicos_ativos
where crm = :NEW.crm;

if(nvl(crm_medico_qtd, 0)=0) then
    RAISE ex_medico_inativo
end if;

exception 
    when ex_medico_inativo then
    RAISE_APPLICATION_ERROR(-20225, 'Somente medicos ativos podem criar fichas e solicitar exames!');

end;

-- 4) Depois, experimentar:
-- • Para um médico ativo, criar uma nova ficha e solicitar dois exames disponíveis quaisquer;
insert into fichas (nro_ficha, cod_paciente, crm, data)
values(99, 1, "38222", sysdate);

insert into fichas_exames (nro_ficha,cod_exame)
values(99,2)
insert into fichas_exames (nro_ficha,cod_exame)
values(99,3)
-- • Marcar esse médico como aposentado e tentar repetir a ação anterior.
update medicos
set ativo = 'N'
where crm = '38222';
