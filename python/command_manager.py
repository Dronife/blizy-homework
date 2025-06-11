from src.service.manager.fundamentals_scrape_manager import fundamentals_scrape_manager

def manage(argv):
    if len(argv) < 2:
        print("No command provided. Use 'scrape-fundamentals' or 'scrape-products'")
        return

    command = argv[1]

    if command == "scrape-fundamentals":
        fundamentals_scrape_manager.scrape()
    elif command == "scrape-products":
        print("Not implemented")
    else:
        print(f"Unknown command: {command}")