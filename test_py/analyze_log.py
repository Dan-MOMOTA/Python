def analyze_log(log_file):
    with open(log_file, 'r') as f:
        lines = f.readlines()

    error_count = 0
    for line in lines:
        if "ERROR" in line:
            error_count += 1

    print(f"日志文件中包含 {error_count} 条错误记录。")

# 使用示例：
analyze_log('application.log')