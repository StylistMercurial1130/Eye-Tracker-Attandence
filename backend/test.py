from server import * 

def main():

    server = DB_Backend(
        "postgres",
        "localhost",
        "1234",
        "theater"
    )

if __name__ == "__main__":
    main()
