-- Armazenar automaticamente o histórico de reajustes de exames.

CREATE TABLE EXAMES_HISTORICO_REAJUSTES (
    data_reajuste DATE NOT NULL,
    cod_exame NUMERIC(3) NOT NULL,
    valor_original NUMERIC(6,2) NOT NULL,
    valor_reajustado NUMERIC(6,2) NOT NULL,
    CONSTRAINT FK_EXAMES_REAJUSTES
    FOREIGN KEY (cod_exame)
    REFERENCES Exames (cod_exame)
);

CREATE OR REPLACE TRIGGER EXAMES_VALORES_UPDATE
BEFORE UPDATE OF valor ON Exames
REFERENCING NEW AS NEW OLD AS OLD
FOR EACH ROW
BEGIN
    INSERT INTO EXAMES_HISTORICO_REAJUSTES (data_reajuste, cod_exame, valor_original, valor_reajustado)
    VALUES (sysdate, :NEW.cod_exame, :OLD.valor, :NEW.valor);
END;

exec reajustar_valor ('HEMO', 3.5);

update exames set valor = valor + 1
where prazo_de_entrega = 2;

 -- Impedir que reajustes aconteçam durante o horário comercial
CREATE OR REPLACE TRIGGER horarios_reajustes
BEFORE UPDATE ON exames
DECLARE
    ex_horario_comercial EXCEPTION;
    PRAGMA EXCEPTION_INIT (ex_horario_comercial, -4099);
BEGIN
    IF (TO_CHAR(SYSDATE, 'HH24') >= 8 AND TO_CHAR(SYSDATE, 'HH24') <= 18) THEN
        RAISE ex_horario_comercial;
    END IF;
EXCEPTION
    WHEN ex_horario_comercial THEN
        RAISE_APPLICATION_ERROR(-20222, 'Reajustes de exames somente permitidos fora do horario comercial.');
END;

--------------------------
update exames set valor = 60.99
where cod_exame = 1;
