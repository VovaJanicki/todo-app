import zipfile


def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("compressed.zip",
                    "C:/Users/Volodymyr.Yanytskyi/PycharmProjects/udemi_bolgar_day1/day_18/dest/")
