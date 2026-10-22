from tabulate import tabulate
import time

# 模拟传入的未格式化数据流
raw_stream = "SEN-01:IMU:NOMINAL:0.12|SEN-02:Depth:NOMINAL:4.85|SEN-03:Battery:WARNING:11.2|SEN-04:Thruster:CRITICAL:105.0|SEN-05:Leak:CLEAR:0.0"

def parse_raw_stream(stream):
    parsed_data = []
    
    # 按 '|' 切分出每个传感器
    records = stream.split("|")
    
    for record in records:
        # 按 ':' 切分出每个字段
        parts = record.split(":")
        
        sensor_id = parts[0]
        sensor_name = parts[1]
        status = parts[2]
        # 将提取到的数值字符串转为浮点数
        value = float(parts[3])
        
        # 异常检测规则
        if sensor_name == "Thruster" and value > 90.0:
            status = "CRITICAL ALERT"
        if sensor_name == "Battery" and value < 11.5:
            status = "CRITICAL ALERT"
            
        # 追加处理好的行
        parsed_data.append([sensor_id, sensor_name, status, value])
        
    return parsed_data

if __name__ == "__main__":
    print("[INFO] Initializing serial telemetry stream...")
    time.sleep(0.5)
    
    # 执行解析
    data = parse_raw_stream(raw_stream)
    
    # 打印表格
    headers = ["Sensor ID", "Sensor Name", "Status", "Value"]
    print("\n=== ROBOTIC SYSTEM TELEMETRY REPORT ===")
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
    print("[SUCCESS] Telemetry frame successfully parsed and verified.\n")