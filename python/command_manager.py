from src.service.manager.category_scrape_manager import category_scrape_manager

def manage(argv):
    if len(argv) < 2:
        print("No command provided. Use 'scrape-category' or 'scrape-products'")
        return

    command = argv[1]

    if command == "scrape-category":
        category_scrape_manager.scrape()
    elif command == "scrape-products":
        print("Not implemented")
    else:
        print(f"Unknown command: {command}")