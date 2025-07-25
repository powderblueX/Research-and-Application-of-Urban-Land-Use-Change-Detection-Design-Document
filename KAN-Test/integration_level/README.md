# 集成级（Integration Level）测试说明

本目录用于存放项目各服务之间的集成测试用例，主要关注服务间接口、数据流、协作流程的正确性。

---

## 一、测试目标
- 验证各微服务之间的接口调用、数据交互、协作流程是否正确。
- 检查数据库、缓存、外部API等依赖的集成效果。
- 发现单元测试无法覆盖的跨模块/跨服务问题。

---

## 二、测试方法
- 采用 **黑盒+白盒结合**，以接口调用、数据流转为主。
- 推荐使用 `pytest` + `requests`/`httpx` 进行接口级集成测试。
- 可用 `docker-compose` 启动多服务环境，保证测试环境一致。
- 可用 `FastAPI TestClient` 进行本地服务集成测试。

---

## 三、如何运行

1. **确保所有依赖服务已启动**（可用 `start_all_services.bat` 或 `docker-compose`）。
2. 运行集成测试：
   ```bash
   pytest test/integration_level
   ```

---

## 四、如何扩展/补充测试

1. 新建测试文件，以 `test_xxx.py` 命名，放在本目录下。
2. 编写跨服务、跨模块的接口调用、数据流转等集成测试用例。
3. 可用 `pytest` fixture 管理测试前置/后置操作。
4. 可用 `requests`/`httpx` 直接请求服务API。

---

## 五、注意事项
- 测试前请确保各服务端口、数据库等配置正确。
- 避免污染生产数据，建议使用测试数据库或mock。
- 集成测试应覆盖典型业务流程、异常流程、边界情况。

---

如需补充具体集成场景的测试用例模板，请联系开发负责人或参考已有测试文件。 