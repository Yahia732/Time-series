from Save.save_file import file_save


class csv_file(file_save):
    def save(self):
        """
        Saves the generated time series into a csv file

        """
        self.data.to_csv(self.file_name,encoding='utf-8', index=False)