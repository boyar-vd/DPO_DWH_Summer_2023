CREATE OR REPLACE FUNCTION fgiski.complex_program_update()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
	begin
		--Check value in id_program
		if new.id_programs is not null then
			new.complex_program := True;
		else new.complex_program := false;
		end if;	
		return new;
	end;
$function$
;

--
CREATE OR REPLACE FUNCTION public.state_history_insert()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
	BEGIN
		IF tg_op = 'INSERT' THEN 
			-- Insert new status into public.documents_id_doc_status_s for history
			INSERT INTO public.documents_id_doc_status_s 
			(id_documents, id_doc_status)
			VALUES
			(NEW.id, NEW.id_doc_status); 		
		END IF;
		return new;
	end;
$function$
;



create trigger state_history_insert after
insert
    on
    public.documents for each row
    when ((pg_trigger_depth() = 0)) execute function state_history_insert();