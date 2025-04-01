--Tabela Construtora
create table construtora( 
    cod_construtora int, 
    nome varchar(100) not null, 
    telefone varchar(15) null, 
    nome_fantasia varchar(100) null, 
    cnpj char(14) null,
    
    constraint pk_cod_construtura primary key(cod_construtora) 
); 

--Tabela Telefones
create table telefones(
    telefone_construtora varchar(15),
    cod_construtora int,
    
    constraint fk_construtora foreign key (cod_construtora) references construtora(cod_construtora)
);

--Tabela Obras
create table obras(
    cod_obra int,
    logradouro_endereco varchar(100),
    numero_endereco int,
    complemento_endereco varchar(100) null,
    nome varchar(100),
    cod_construtora int,

    constraint pk_cod_obra primary key(cod_obra),
    constraint fk_cod_construtora foreign key (cod_construtora) references construtora(cod_construtora)
); 


--Tabela Trabalhador
create table trabalhador(
    cpf char(14), 
    nome varchar(100) not null, 
    salario decimal(10,2) not null, 
    cod_obra int not null,
    
    constraint pk_cpf primary key(cpf),
    constraint fk_cod_obra foreign key(cod_obra) references obras(cod_obra)
);  


--Tabela Equipamentos
create table equipamentos(
    cod_equipamento int,
    nome varchar(100),
    valor_uso_diario decimal(10,2) not null,
    cod_categoria int not null,

    constraint pk_cod_equipamento primary key(cod_equipamento),
    constraint fk_categoria foreign key(cod_categoria) references categoria(cod_categoria)
);


--Tabela Categoria
create table categoria( 
    cod_categoria int, 
    descricao varchar(100) not null, 
    
    constraint pk_cod_categoria primary key(cod_categoria) 
);  


--Tabela Obras_equipamentos
create table obras_equipamentos(
    cod_obra int not null,
    cod_equipamento int not null,
    data_inicio date not null,
    data_termino date not null,

    constraint pk_obras_equipamentos primary key (cod_obra, cod_equipamento, data_inicio), 
    constraint fk_obra_equipamento foreign key (cod_obra) references obras(cod_obra),
    constraint fk_equipamento_obra foreign key (cod_equipamento) references equipamentos(cod_equipamento)
);