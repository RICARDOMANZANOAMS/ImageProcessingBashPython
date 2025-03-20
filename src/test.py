import argparse
def test(value):
    print(f"test ricardo {value}")


if __name__ == "__main__":
    # Add argparse to read input parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('readVar', type=str, help='Path to the geojson which contains the tiles for whole Canada')
   
    args = parser.parse_args()
    test(args.readVar)
    # try:
    #     #Call the function with the passed parameters
    #     test(args.readVar       

    #     )
        
    #     logger.info("END STAGE: getHRandMRToProcess. Successfully executed.")
        
    # except Exception as e:
    #     logger.error(f"ERROR: STAGE: getHRandMRToProcess with error {e}")
        