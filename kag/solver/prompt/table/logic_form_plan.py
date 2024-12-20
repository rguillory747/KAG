import logging
from typing import List

from kag.common.base.prompt_op import PromptOp

logger = logging.getLogger(__name__)

from kag.common.base.prompt_op import PromptOp
import json


class LogicFormPlanPrompt(PromptOp):
    template_zh = """
{
  "task": "将给出的问题拆解为子问题，并将子问题分配给合适的代理(agent)。",
  "instruction": [
    "找出解决问题的核心关键步骤，总结为子问题。",
    "根据代理的能力，将子问题分配给合适的代理进行处理。"
  ],
  "pay_attention": [
    "你的数学计算能力和数值比较能力很差，需要借助python_coder才能得到正确结果。",
    "子问题的描述信息尽可能完整，使得代理易于理解和处理。"
  ],
  "agents": {
    "recall": {
      "desc": "包含一个知识库，可以根据给出的搜索条件(自然语言描述)，返回搜索结果。",
      "knowledge_base_content": "$kg_content",
      "examples": [
        {
          "input": "从资产负债信息中召回流动资产的所有子项",
          "output": "| 项目             | 2024年9月30日 | 2023年12月31日 |\n|------------------|---------------|----------------|\n| 流动资产：       |               |                |\n| 货币资金         | 29,878,544    | 51,235,370     |\n| 交易性金融资产   | 1,633,233     | 1,520,160      |\n| 衍生金融资产     | 494,335       | 303,397        |\n| 应收票据         | 528,810       | 442,456        |\n| 应收账款         | 3,428,498     | 3,501,291      |\n| 预付款项         | 552,591       | 751,860        |\n| 存货             | 20,168,932    | 19,377,706     |\n| 持有待售资产     | 154,434       | 156,033        |\n| 其他流动资产     | 2,392,787     | 4,000,122      |\n| 流动资产合计     | 77,297,667    | 96,573,772     |"
        }
      ]
    },
    "python_coder": {
      "desc": [
        "对给定的问题，进行编写python代码进行求解。",
        "善于回答精确数学计算问题",
        "可以回答当前时间，日期类问题"
      ],
      "pay_attention": "只允许使用python基础库，超出能力范围的问题会拒答",
      "examples": [
        {
          "input": "9.8和9.11哪个大？",
          "internal_processing_logic": "编写python代码```python\nanswer=max(9.8, 9.11)\nprint(answer)```, 调用执行器获得结果",
          "output": "9.11"
        }
      ]
    }
  },
  "output_format": [
    "输出json格式，output中包含子问题列表",
    "每个子问题由sub_question和process_agent组成"
  ],
  "cases": [
    {
      "question": "如果游戏收入按照目前的速度增长，2020年的游戏收入是多少？",
      "output": [
        {
          "sub_question": "查找2019年游戏收入",
          "process_agent": "recall"
        },
        {
          "sub_question": "查找2018年游戏收入",
          "process_agent": "recall"
        },
        {
          "sub_question": "计算2019年游戏收入增长率",
          "process_agent": "python_coder"
        },
        {
          "sub_question": "根据增长率，计算2020年游戏收入",
          "process_agent": "python_coder"
        }
      ]
    },
    {
      "question": "471乘以473等于多少？",
      "output": [
        {
          "sub_question": "计算471乘以473的结果",
          "process_agent": "python_coder"
        }
      ]
    },
    {
      "question": "资产负债信息中流动资产最高的子项是那个？其占流动资产的比例是多少？",
      "output": [
        {
          "sub_question": "从资产负债信息中召回流动资产的所有子项",
          "process_agent": "recall"
        },
        {
          "sub_question": "根据给出的流动资产子项，计算最高的子项是哪个？并计算最高子项占流动资产的比例是多少？",
          "process_agent": "python_coder"
        }
      ]
    }
  ],
  "question": "$question"
}    
"""

    template_en = template_zh

    def __init__(self, language: str):
        super().__init__(language)

    @property
    def template_variables(self) -> List[str]:
        return ["question", "kg_content"]

    def parse_response(self, response: str, **kwargs):
        rsp = response
        if isinstance(rsp, str):
            rsp = json.loads(rsp)
        if isinstance(rsp, dict) and "output" in rsp:
            rsp = rsp["output"]
        return rsp
