
-- inserções de dados nas tabelas:

-- Insert na tabela categorias 
insert into categoria values(1, 'Concretagem'); 
insert into categoria values(2, 'Acesso e Elevação'); 
insert into categoria values(3, 'Geradores e Compressores'); 
insert into categoria values(4, 'Andaimes'); 
insert into categoria values(5, 'Ferramenta Elétrica'); 


--Insert na tabela construtoras 
insert into construtora (cod_construtora, nome, nome_fantasia) values (10, 'Construtora Alfa S.A.', 'Alfa Incorporações');
--4) Criar (inserir) uma nova construtora, com o seu nome:
insert into construtora (cod_construtora, nome, nome_fantasia) values (20, 'Brendha', 'B Incorporações');

-- Insert na tabela obras 
insert into obras (cod_obra, logradouro_endereco, numero_endereco, complemento_endereco,nome, cod_construtora) 
    values (115, 'Travessa dos Lagos', 100, 'Norte','Condomínio dos Lagos', 10);
insert into obras (cod_obra, logradouro_endereco, numero_endereco, complemento_endereco, nome, cod_construtora)
    values (116,'Avenida Rio Grande', 22, 'Lado A', 'Condomínio Araras', 10);

-- -- i. Criar 2 obras 
insert into obras (cod_obra, logradouro_endereco, numero_endereco, complemento_endereco, nome, cod_construtora)
    values (118,'Avenida Porto Alegre', 123, 'Sul', 'Condomínio Sol nascente', 20);
insert into obras (cod_obra, logradouro_endereco, numero_endereco, complemento_endereco, nome, cod_construtora)
    values (122,'Avenida do comercio', 432, 'Centro', 'Condomínio Aguas claras', 20);


--Insert na tabela equipamentos  
insert into equipamentos values(301,'Betoneira',100.00, 1);  
insert into equipamentos values(302,'Cortadora de Piso',10.00, 1);  
insert into equipamentos values(303,'Mangote',30.50, 1);  
insert into equipamentos values(304,'Guincho',250.00, 2);  
insert into equipamentos values(305,'Gerador',451.00, 3);  
insert into equipamentos values(306,'Piso Metálico',150.00, 4);  
insert into equipamentos values(307,'Furadeira de bancada',65.00, 5);  
insert into equipamentos values(308,'Parafusadeira',37.00, 5);  
insert into equipamentos values(309,'Plaina',25.00, 5); 


-- ii. Alocar pelo menos 4 equipamentos (de categorias diferentes) à primeira obra que você criou.
insert into equipamentos values(310,'Carrinho de mão',50.00, 6);  
insert into equipamentos values(311,'Compactor de solo',180.00, 7);  
insert into equipamentos values(312,'Martelo demolidor',80.90, 8);  
insert into equipamentos values(313,'Guindaste',250.00, 2);  


-- Insert na tabela telefones 
insert into telefones values (51-3333-3334, 10);
insert into telefones values (51-3333-3335, 10);
insert into telefones values (51-3333-3336, 10);


-- Insert na tabela obras_equipamento 
insert into obras_equipamentos values(115, 301, TO_DATE('18/03/2022', 'DD/MM/YYYY'), TO_DATE('24/10/2022', 'DD/MM/YYYY'));
insert into obras_equipamentos values(115, 304, TO_DATE('20/04/2022', 'DD/MM/YYYY'), TO_DATE('02/08/2022', 'DD/MM/YYYY'));
insert into obras_equipamentos values(115, 306, TO_DATE('06/07/2021', 'DD/MM/YYYY'), TO_DATE('18/07/2021', 'DD/MM/YYYY'));
insert into obras_equipamentos values(115, 307, TO_DATE('04/03/2022', 'DD/MM/YYYY'), TO_DATE('20/03/2022', 'DD/MM/YYYY'));
insert into obras_equipamentos values(115, 309, TO_DATE('04/08/2021', 'DD/MM/YYYY'), TO_DATE('10/08/2021', 'DD/MM/YYYY'));
insert into obras_equipamentos values(116, 304, TO_DATE('22/10/2022', 'DD/MM/YYYY'), TO_DATE('25/10/2022', 'DD/MM/YYYY'));
insert into obras_equipamentos values(116, 305, TO_DATE('07/03/2022', 'DD/MM/YYYY'), TO_DATE('10/03/2022', 'DD/MM/YYYY'));
insert into obras_equipamentos values(116, 306, TO_DATE('12/09/2022', 'DD/MM/YYYY'), TO_DATE('21/09/2022', 'DD/MM/YYYY'));
insert into obras_equipamentos values(116, 307, TO_DATE('16/08/2022', 'DD/MM/YYYY'), TO_DATE('24/08/2022', 'DD/MM/YYYY'));
insert into obras_equipamentos values(116, 308, TO_DATE('23/10/2022', 'DD/MM/YYYY'), TO_DATE('25/10/2022', 'DD/MM/YYYY'));


-- Insert na tabela trabalhadores 
insert into trabalhador values('101.101.101-34', 'José Chaves', 2200.00, 115);
insert into trabalhador values('102.102.102-91' , 'Pedro Passos ', 3502.18 , 115);
insert into trabalhador values('103.103.103-18', 'Maria Aparecida ', 2800.87, 115);
insert into trabalhador values('104.104.104-52', 'Carlos Dutra ', 3100.00, 116);
insert into trabalhador values('105.105.105-85' , 'Mário Pires', 4323.29, 116);

-- i. Criar 2 obras e 5 funcionários para cada uma dessas obras;
insert into trabalhador values('106.106.106-99', 'João Santos', 2000.00, 118);
insert into trabalhador values('107.107.107-01' , 'Carlos Lopes', 3300.00 , 118);
insert into trabalhador values('108.108.108-12', 'Pedro Rodrigues', 2800.89, 118);
insert into trabalhador values('109.109.109-91', 'Ana Reis', 2100.00, 118);
insert into trabalhador values('115.115.115-96' , 'Marcio Silva', 2200.29, 118);

insert into trabalhador values('111.111.111-94', 'Pedro Ferreira', 2900.00, 122);
insert into trabalhador values('115.115.115-44' , 'Julio Souza ', 4100.00 , 122);
insert into trabalhador values('117.117.117-10', 'Maria Campos', 3700.00, 122);
insert into trabalhador values('118.118.118-90', 'Juliano Almeida', 2100.00, 122);
insert into trabalhador values('119.119.119-81' , 'Julia Alves', 2350.00, 122);


