from create_tables import main as create_tables_main
from etl import main as etl_main
from etl_bulk import main as etl_bulk_main

if __name__ == '__main__':
    create_tables_main()
    etl_main()
    # etl_bulk_main()
