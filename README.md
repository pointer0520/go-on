## 📁 Django 项目结构说明

一个标准的 Django 项目在创建后会包含以下核心文件和目录。

---

### 核心文件和目录说明

| 文件/目录 | 描述 | 官方文档链接 |
| :--- | :--- |:-----------------------------------------------------------------------------------------|
| **`manage.py`** | 一个**命令行工具**，用于管理 Django 项目的各种任务，例如运行服务器、创建应用、进行数据库迁移等。 | [Django-admin 和 manage.py](https://docs.djangoproject.com/zh-hans/5.2/ref/django-admin/) |
| **`mysite/`** | 实际的**项目包**（Project Package）。这是用于导入其中任何内容的 Python 包的名称（例如 `mysite.urls`）。这个目录下的文件定义了项目的配置和路由。 | - |
| **`mysite/__init__.py`** | 一个空文件（或包含初始化代码的文件），用于告诉 Python 解释器：该目录应被视为一个 **Python 包**。 | [Python 教程：包](https://docs.python.org/3/tutorial/modules.html#tut-packages) |
| **`mysite/settings.py`** | **Django 项目的配置文件**。它包含了所有项目级别的配置，如数据库连接、安装的应用、中间件、静态文件路径等。 | [Django Settings](https://docs.djangoproject.com/zh-hans/5.2/topics/settings/) |
| **`mysite/urls.py`** | **Django 项目的 URL 声明**（URL Dispatcher）。它负责将传入的 HTTP 请求路由到对应的视图（View）上。 | [URL调度器](https://docs.djangoproject.com/zh-hans/5.2/topics/http/urls/) |
| **`mysite/asgi.py`** | 项目运行在 **ASGI 兼容的 Web 服务器**上的入口。ASGI（Asynchronous Server Gateway Interface）用于支持异步请求，常用于 WebSockets 等场景。 | - |
| **`mysite/wsgi.py`** | 项目运行在 **WSGI 兼容的 Web 服务器**上的入口。WSGI（Web Server Gateway Interface）是 Python Web 应用和 Web 服务器之间的一个通用接口标准。 | - |

---

### 💡 关键点提示

* `manage.py` 位于项目根目录下，而其他配置文件则位于以项目名称命名的内部配置目录（例如 `mysite/`）中。
* `mysite/` 目录的名称通常与您创建项目时指定的名称一致。
* 在现代 Django 开发中，`urls.py` 通常只会包含项目级别的路由，而应用（App）级别的具体路由则分散在各个应用自己的 `urls.py` 文件中，通过 `include()` 函数引入。
* `asgi.py` 和 `wsgi.py` 允许您的 Django 项目与不同的 Web 服务器环境进行交互。

---
---

## FBV 和 CBV：Django 中的视图实现方式

在 Django 中，可以使用 **函数视图 (Function-Based Views, FBV)** 和 **类视图 (Class-Based Views, CBV)** 来处理 API 请求。这两种方式各有其优势和劣势，适用于不同的场景。

---

### 🟢 FBV（函数视图 / Function-Based Views）

FBV 是基于函数的视图，是 Django 早期以及简单应用中常用的方式。

#### **👍 优点**

* **简单直观：** FBV 的实现方式与 Python 函数调用相似，逻辑流程**线性**且易于理解，特别适用于处理简单的逻辑和**单一功能**的 API 接口。
* **开发自由度高：** 在 FBV 中，可以完全定制 API 请求的处理流程的每一个细节，不依赖于固定的类结构，**灵活性很高**。
* **易于调试：** 由于逻辑集中在一个函数内，调试和跟踪代码执行过程通常比较直接。

#### **👎 缺点**

* **代码复用性低：** 如果多个视图有相似的处理逻辑（如权限验证、表单处理等），FBV 可能会导致**重复代码**。需要通过额外的装饰器（Decorators）或辅助函数来进行代码复用，可能会使代码结构复杂化。
* **扩展性有限：** 对于复杂和多变的业务逻辑，单个 FBV 函数可能会变得**过长、职责过多**，难以维护和扩展。难以清晰地分离 HTTP 方法的处理逻辑（如 `GET`, `POST`）。

---

### 🔵 CBV（类视图 / Class-Based Views）

CBV 是基于 Python 类的视图，通过类继承和方法重写来组织视图逻辑。

#### **👍 优点**

* **代码复用性高：** CBV 通过 **继承 (Inheritance)** 和 **混入 (Mixins)** 机制，使得代码复用更为方便。常见的行为（如权限检查、数据预处理、模板渲染）可以通过**基类**和**混入类**实现，易于管理和复用。
* **组织性好（职责分离）：** CBV 允许通过类的方法来组织视图逻辑，每个 **HTTP 方法**（如 `get()`, `post()`, `put()`, `delete()`）都用一个单独的方法来处理，使得视图的结构更清晰，**职责分离**更明确。
* **与 Django REST Framework (DRF) 高度兼容：** Django REST Framework 提供了大量的基于 CBV 的**通用基类**（如 `APIView`, `GenericAPIView`, `ViewSet`），极大地简化了 RESTful API 的开发，是现代 Django API 开发的**主流选择**。
* **结构化和标准化：** 通过使用 Django 提供的通用基类，可以保持项目视图代码的结构和风格一致性。

#### **👎 缺点**

* **学习曲线稍陡：** 相较于 FBV，CBV 引入了**更多的抽象层次**（继承、混入、方法调度），初学者可能需要时间来理解这些机制及其背后的工作原理。
* **开发自由度稍差：** 虽然 CBV 使代码组织更加结构化，但在某些**非常规**或**高度定制化**的逻辑处理场景中，受限于其固定的继承和方法调度结构，可能会**限制处理特定逻辑的灵活性**。
* **方法调度：** 当请求到达 CBV 时，Django 会通过反射机制自动调用对应 HTTP 方法的函数，这个过程相较于 FBV 的直接函数调用，**多了一层间接性**。

---

### 💡 总结与实践建议

| 特性 | FBV（函数视图） | CBV（类视图） |
| :--- | :--- | :--- |
| **适用场景** | 简单的、单一职责的 API 接口 | 复杂的、有 CRUD 需求的、需要高复用的接口 |
| **代码结构** | 线性，逻辑集中 | 结构化，逻辑分散到不同方法中 |
| **代码复用** | 低，依赖装饰器/辅助函数 | 高，依赖继承和混入（Mixins） |
| **扩展性** | 维护复杂逻辑时较差 | 维护复杂逻辑时较好（基于继承） |
| **DRF 兼容性** | 较差，需要手动处理很多细节 | **极高**，是 DRF 的核心 |

在实际的 Django 项目中，尤其是在使用 **Django REST Framework** 进行 API 开发时，**CBV 的使用率会更高**，因为它们提供了更好的结构、可复用性和与 DRF 的原生集成。

**建议：**

* 对于**简单、快速实现**且逻辑不易变化的页面或 API，可以使用 **FBV**。
* 对于需要处理**多种 HTTP 方法**、涉及**数据模型操作 (CRUD)**、或者需要**高度代码复用**的 API 接口，应优先使用 **CBV**（特别是在 DRF 中）。