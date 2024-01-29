from ftplib import FTP


def copy_files_between_ftp(source_ftp, source_path, dest_ftp, dest_path, file_extension=None):
    with FTP(source_ftp) as source_connection, FTP(dest_ftp) as dest_connection:
        source_connection.login()
        dest_connection.login()

        source_connection.cwd(source_path)

        file_list = source_connection.nlst()

        if file_extension:
            file_list = [file for file in file_list if file.endswith(file_extension)]

        for file in file_list:
            source_file_path = f"{source_path}/{file}"
            dest_file_path = f"{dest_path}/{file}"

            with source_connection.retrbinary(f"RETR {source_file_path}",
                                              dest_connection.storbinary(f"STOR {dest_file_path}",
                                                                         open(file, 'wb').write)):
                pass

