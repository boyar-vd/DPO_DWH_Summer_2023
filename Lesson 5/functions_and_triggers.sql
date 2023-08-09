CREATE OR REPLACE FUNCTION "RAW".insert_new_merchants()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
	BEGIN
--		IF tg_op = 'INSERT' THEN 
			-- Check values in merchant_list
		IF NEW.merchant IS NOT NULL AND (SELECT id
			  FROM "RAW".merchant_list ml
			 WHERE ml.merchant_name = NEW.merchant) IS NULL
			 THEN 
			 INSERT INTO "RAW".merchant_list
			 (merchant_name)
			 VALUES
			 (NEW.merchant);
		END IF;
--		END IF;
		RETURN NEW;
	END;
$function$
;


CREATE TRIGGER insert_new_merchants AFTER
INSERT
    OR
UPDATE
    ON
    "RAW".table_test FOR EACH ROW
    WHEN ((pg_trigger_depth() = 0)) EXECUTE FUNCTION "RAW".insert_new_merchants();
   

ALTER TABLE "RAW".table_test ENABLE TRIGGER insert_new_merchants;


