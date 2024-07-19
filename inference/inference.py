import requests
import json

# 设置目标URL
url = "http://xx.xx.xx.xx:24100/generate"
input = 'We know that  compute-in-memory can be divided into different categories according to the computing paradigm. What are the main types of  compute-in-memory domains and what are their characteristics?'



system_template = "Below is an instruction that describes a task, paired with an input that provides further " \
                    "context. Write a response that appropriately completes the request. " \
                    "Please note that you need to think through your response logically and step by step.\n\n"
dialog_template = "### Instruction:\n{instruction}\n\n### Response:"

template = system_template + dialog_template




# 创建请求头
headers = {
    "Accept": "application/json",
    "Content-type": "application/json"
}

template = template.format(instruction=input)


# # 创建请求数据
data = {
    "inputs": template,
    "parameters": {
        "details": False,
        "do_sample": True,
        "repetition_penalty": 1.1,
        "return_full_text": False,
        "seed": None,
        "temperature": 0.2,
        "top_n_tokens": 5,
        "top_p": 0.9,
        "max_new_tokens": 1000
    },
}

# 发送POST请求
response = requests.post(url, headers=headers, data=json.dumps(data))

# 检查响应状态码
if response.status_code == 200:
    # 请求成功，打印响应内容
    print(response.json())
else:
    # 请求失败，打印状态码和错误信息
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
