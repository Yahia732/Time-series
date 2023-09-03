from Save.save_file import file_save


class save_configuration:

    class configuration_manager:
        def __init__(self, saver: file_save):
            self.saver = saver

        def read(self):
            """
            Saves the generated time series into a file

            """
            self.saver.save()