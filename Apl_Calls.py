import PipelineManager
from flask import Flask, request, jsonify

app = Flask(__name__)
pipeline_manager = PipelineManager()

@app.route('/run_pipeline', methods=['POST'])
def run_pipeline():
    tasks = request.json['tasks']
    report = pipeline_manager.run_pipeline(tasks)
    return jsonify(report)

if __name__ == '__main__':
    app.run(debug=True)

