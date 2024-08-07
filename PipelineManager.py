import TaskLibrary
class PipelineManager:
    def __init__(self):
        self.task_library = TaskLibrary()

    def run_pipeline(self, tasks):
        report = []
        for task in tasks:
            task_name = task['name']
            params = task['params']
            result = self.task_library.run_task(task_name, params)
            report.append(result)
        return report
