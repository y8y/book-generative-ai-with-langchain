from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict


class JobApplicationState(TypedDict):
    job_description: str
    is_suitable: bool
    application: str


def analyze_job_description(state):
    print("...Analyzing a provided job description ...")
    return {"is_suitable": len(state["job_description"]) > 100}


def generate_application(state):
    print("...generating application...")
    return {"application": "some_fake_application"}


builder = StateGraph(JobApplicationState)

# 节点
builder.add_node("analyze_job_description", analyze_job_description)
builder.add_node("generate_application", generate_application)

# 边
builder.add_edge(START, "analyze_job_description")
builder.add_edge("analyze_job_description", "generate_application")
builder.add_edge("generate_application", END)

graph = builder.compile()

# 生成图并保存为 PNG 文件
png_bytes = graph.get_graph().draw_mermaid_png()

output_path = "/Users/chenbing/Downloads/graph.png"
with open(output_path, "wb") as f:
    f.write(png_bytes)

print(f"Graph image saved to {output_path}")

res = graph.invoke({"job_description": "fake_jd"})
print(res)
