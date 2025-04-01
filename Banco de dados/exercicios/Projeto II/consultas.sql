-- Enunciado 5:
-- a) Selecionar CPFs e nomes dos trabalhadores que ganham mais do que 2.500,00;  
select cpf, nome, salario as salario_menor from trabalhador 
where salario > 2500;

-- b) Selecionar nomes e salários dos trabalhadores da empresa ALFA, ordenados em ordem alfabética crescente;  
select t.nome,t.salario
from trabalhador t
join obras o on t.cod_obra = o.cod_obra
join construtora c on o.cod_construtora = c.cod_construtora
where c.nome = 'Construtora Alfa S.A.'
order by t.nome asc;

-- e) Selecionar os equipamentos que nunca foram utilizados em nenhuma obra;  
select e.cod_equipamento, e.nome from equipamentos e
left join obras_equipamentos u on e.cod_equipamento = u.cod_equipamento
WHERE u.cod_equipamento IS NULL;

--  f) Listar as categorias de equipamentos utilizadas nas obras da construtora ALFA.  
select distinct c.cod_categoria, c.descricao from categoria c
join equipamentos e on c.cod_categoria = e.cod_categoria
join obras_equipamentos oe on e.cod_equipamento = oe.cod_equipamento
join obras o on oe.cod_obra = o.cod_obra
join construtora co on o.cod_construtora = co.cod_construtora
where co.nome = 'Construtora Alfa S.A.';
