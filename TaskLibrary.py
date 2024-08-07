class TaskLibrary:
    def __init__(self):
        self.tasks = {
            'identify_missing_values': self.identify_missing_values,
            'identify_duplicate_rows': self.identify_duplicate_rows
        }

    def run_task(self, task_name, params):
        return self.tasks[task_name](**params)

    def identify_missing_values(self, data, columns, thresholds):
        # Implement logic to identify missing values
        print(data[data[columns].isna()])
        pass

    def identify_duplicate_rows(self, data, columns):
        # Implement logic to identify duplicate rows
        duplicates = data[data.duplicated(subset=[columns], keep=False)]
        print(duplicates)
        pass
