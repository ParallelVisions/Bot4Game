script_dir = os.path.dirname(__file__)
    filepath = os.path.join(
        script_dir, 
        'recordings', 
        '{}.json'.format(OUTPUT_FILENAME)
    )
    with open(filepath, 'w') as outfile:
        json.dump(input_events, outfile, indent=4)