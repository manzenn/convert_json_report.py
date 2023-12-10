import json
import datetime
import os

#функция для получения нового отчета 
def vulnerability_report(names, counts):
    report = {
        "vulnerabilities": []
    }
    
    for name, count in zip(names, counts):
        vulnerability = {
            "name": name,
            "count": count
        }
        report["vulnerabilities"].append(vulnerability)
    
    return report

# путь к исходному файлу
input_name = 'D:\\Downloads\\Report\\2023-12-10-ZAP-Report-.json' 

with open(input_name, 'r') as file:
    data = json.load(file)

# получение данных
name,count=[],[]
for j in data['site']:
    for i in j['alerts']:
        name.append(i['name'])
        count.append(i['count'])

report = vulnerability_report(name, count)

# путь к конечному файлу
output_name = f"2023-12-10-ZAP-Report-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.json"
output_path = os.path.join("D:\\Downloads\\Report", output_name)

# сохранение отчета в файл
with open(output_path, "w") as output_file:
    json.dump(report, output_file, indent=4)