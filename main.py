from genesis_engine import knowledge_genesis, persona_builder, lazy_approval
from oss_loader import ToolLoader


def main():
    print("🔧 加载本地核心引擎...")
    print(f"  ✅ 知识创生引擎: genesis_engine.knowledge_genesis")
    print(f"  ✅ 人格生成器: genesis_engine.persona_builder")
    print(f"  ✅ 闲时审批: genesis_engine.lazy_approval")

    print("📦 加载本地扩展工具...")
    loader = ToolLoader()
    tools_status = {}
    for tool_name in [
        "ima_capsule_adapter.py",
        "order_tracker.py",
        "referral_engine.py",
        "serendipity_engine.py",
        "wechat_poster_gen.py",
    ]:
        try:
            loader.load_tool(tool_name)
            tools_status[tool_name] = "✅"
        except Exception as e:
            tools_status[tool_name] = f"⚠️ {e}"

    for name, status in tools_status.items():
        print(f"  {status} {name}")

    print("\n✅ 系统启动成功！")


if __name__ == "__main__":
    main()