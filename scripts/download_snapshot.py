DATA_SOURCE_URL = "https://s3.amazonaws.com/dl.ncsbe.gov/data/Snapshots/VR_Snapshot_20051125.zip"
#TEXT_FILE_NAME = "VR_20051125.txt"

zipfile = ZIP_FILE_NAME
if zipfile.exists():
    # Make sure the zipfile isn't a partial one
    try:
        with ZipFile(zipfile) as _:
            pass
    except BadZipFile as ex:
        errmsg = f"{zipfile} is not a full zip file"
        raise RuntimeError(errmsg)
    logging.info(f"Using existing zip file {zipfile}")
else:
    source = DATA_SOURCE_URL
    logging.info(f"start, source={source}")

    # Make an HTTP request for the source zip file
    resp = requests.get(source, stream=True)
    if resp.status_code != HTTPStatus.OK:  # Expecting a status code of 200
        errmsg = f"HTTP status {resp.status_code} returned for request to {source}"
        raise RuntimeError(errmsg)

    # Read the response and write the zip file a chunk at a time
    with open(zipfile, "wb") as fp:
        total_bytes = 0
        for chunk in resp.iter_content(chunk_size=ZIP_CHUNK_SIZE):
            total_bytes += len(chunk)
            logging.info(f"{total_bytes=:,}")
            fp.write(chunk)

    # Remember the resulting size
    zipfile_size = total_bytes
    logging.info(f"end, {total_bytes=:,}")
