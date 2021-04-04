# results_stat by Fei Li
import numpy as np
import os


def results_stat():
    rlt_path = './results'
    if not os.path.exists(rlt_path):
        os.mkdir(rlt_path)
    stat_path = './stat'
    if not os.path.exists(stat_path):
        os.mkdir(stat_path)
    for file in os.listdir(rlt_path):
        if file.endswith('.txt'):
            file_path = os.path.join(rlt_path, file)
            data = [[], [], [], []]
            with open(file_path, 'r') as f:
                lines = f.read().split('\n')
                for line in lines:
                    if len(line) > 0:
                        line_data = map(eval, line.split())
                        for i in range(4):
                            data[i].append(line_data[i])
            lines = [[], [], [], []]
            for i in range(4):
                lines[i].append(np.mean(data[i]))
                lines[i].append(np.std(data[i]))
                lines[i].append(np.min(data[i]))
                lines[i].append(np.percentile(data[i], 25))
                lines[i].append(np.percentile(data[i], 50))
                lines[i].append(np.percentile(data[i], 75))
                lines[i].append(np.max(data[i]))
            output_path = os.path.join(stat_path, file)
            with open(output_path, 'w') as f:
                for line in lines:
                    f.write('\t'.join(map(str, line)) + '\n')


if __name__ == '__main__':
    results_stat()
