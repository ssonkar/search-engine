import generate_dump
import settings


if __name__ == "__main__":
    ## Initializes everything
    ## 1: Run everything
    ## 2: Only convert vec to idf
    choice =2
    if choice== 1:
        settings.init()
        generate_dump.read_texts(settings.zip_path)
    settings.load_data()
    generate_dump.convert_tf_vec()