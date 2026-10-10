# 增量蒸馏审计日志（v1.1 · 2026-10-09）

> 本文件保留本次增补的**审计轨迹**：候选池、三重验证结果、晋级门决策、淘汰理由、合规处理、立场冲突。
> 对应 cangjie-skill 的阶段 1.5 / 1.6，以及质量红线第 6 条（保留审计轨迹）。

## 0. 本次增补的基本信息

| 项 | 内容 |
|---|---|
| 时间 | 2026-10-09 |
| 方法 | cangjie-skill RIA-TV++ 增量蒸馏（沿用原输出模式 single，不新增来源路由入口） |
| 材料来源 | 技能包 B：LuDamo_Master《鲁大魔·全能逆袭智库》—— SKILL.md、logic/methodology.md、logic/sub_skills/{job_hunting,encouragement,relationships}.md、database/biography.md、templates/*、scripts/feishu_sync.py |
| 原包来源 | A：141 条抖音直播切片口播转写（2026-06-09 ~ 2026-09-30，约 21.7 万字） |
| **来源差异（关键）** | A 的来源是**可溯源的口播原文**；B 的来源是**他人归纳的技能包文本**，无口播原文、无带结果的应用案例。因此增补卡的证据等级整体低于原卡。 |
| 产出 | 8 张能力卡 + biography-facts.md + persona-and-style.md + 7 套模板 + feishu_sync.py（改写）+ config.example.json |
| 版本 | 1.0.0 → 1.1.0，capability-count 13 → 21 |

## 1. 候选池（B 有而 A 无的 14 项）

| # | 候选 | 来源文件 | 处置 |
|---|---|---|---|
| 1 | 处世三红线（亲人/朋友/合伙人） | methodology.md 二、relationships.md | ✅ 成卡 `chu-shi-san-hong-xian` |
| 2 | 求职避坑（查资质/薪酬/识陷阱） | job_hunting.md、job_audit.md | ✅ 与 #3 合并成卡 `qiu-zhi-bi-keng-yu-mian-shi` |
| 3 | 简历放大与面试实话术 | job_hunting.md §3–4、job_audit.md §3 | ✅ 并入 #2（同一契约：求职） |
| 4 | 避坑优先法（拆 3 个失败案例） | methodology.md 心法 2、pitfalls.md、SKILL.md | ✅ 成卡 `bi-keng-you-xian` |
| 5 | 流量匹配法则 | methodology.md 心法 3、biography.md、pitfalls.md | ✅ 成卡 `liu-liang-pi-pei` |
| 6 | 人才优先与区域围剿 | methodology.md 心法 4、biography.md、personnel_module.md | ✅ 成卡 `ren-cai-you-xian` |
| 7 | 李鬼矩阵打法 | methodology.md 心法 6、SKILL.md 金句 | ⚠️ 成卡 `li-gui-ju-zhen`（高风险，见 §4） |
| 8 | 区域聚焦与降维 | methodology.md 心法 7、biography.md | ✅ 与 #9 合并成卡 `qu-yu-yu-qie-kou` |
| 9 | 最小切口分析 | methodology.md 心法 8 | ✅ 并入 #8（同一决策：在哪个战场切多深） |
| 10 | 逆袭觉醒（对抗内耗） | encouragement.md、SKILL.md、biography.md | ⚠️ 成卡 `ni-xi-jue-xing`（立场冲突，见 §5） |
| 11 | 生平事实库与防伪声明 | biography.md、SKILL.md §3 | ✅ 非能力资产 → `biography-facts.md` + 路由表一行 |
| 12 | 人格与口吻引擎 | SKILL.md §1/§4/§5 | ✅ 非能力资产 → `persona-and-style.md`，**默认关闭**（nuwa 域） |
| 13 | 6 套交付模板 | templates/* | ✅ 非能力资产 → `templates/`（7 个文件，平铺避免三级嵌套） |
| 14 | 飞书同步脚本 | scripts/feishu_sync.py | ✅ 改写后纳入（补 config.example.json、加脱敏与错误处理） |

## 2. 三重验证结果

| 能力 | V1 跨域 | V2 预测力 | V3 独特性 | 证据等级 |
|---|---|---|---|---|
| 处世三红线 | ✓ methodology.md + relationships.md | ✓ 可外推到"老同学想入股" | ✓ 金钱隔离+决策权唯一+零容忍止损 | 规则级 |
| 求职避坑与面试 | ✓ job_hunting.md + job_audit.md | ✓ 可外推到"要不要交押金的兼职" | ✓ 薪酬五问项 + 三级评级 | 规则级 |
| 避坑优先法 | ✓ 心法 2 + pitfalls.md + SKILL.md 三处 | ✓ 可外推到"要不要加盟" | ✓ 强制 3 个 + 拆到结构层 + 先坑后利 | 规则级 + 1 跨包案例 |
| 流量匹配 | ✓ 心法 3 + biography（听泉/海鸥）+ pitfalls | ✓ 可外推到"知识付费账号该不该接广告" | ✓ 配对表 + "错位禁止加量" | 规则级 + 3 自述案例 |
| 人才优先与区域围剿 | ✓ 心法 4 + biography（灵匠/海鸥） | ✓ 可外推到"县城做本地生活先找什么人" | ✓ 人才可数化 + 用户转销售 | 规则级 + 2 自述案例 |
| 李鬼矩阵 | ✓ 心法 6 + SKILL.md 金句 | ✓ 可外推到"同行开了名字很像的店" | ✓ 矩阵截流思路非常识 | **主张级**（无案例） |
| 区域聚焦与最小切口 | ✓ 心法 7 + 心法 8 + biography（徐州/域名/校园墙） | ✓ 可外推到"县城宠物殡葬切哪一环" | ✓ 「可独立运行 + 高利润」双筛 | 规则级 + 3 自述案例 |
| 逆袭觉醒 | ✓ encouragement.md + SKILL.md + biography | ✓ 可外推到"被裁后三个月没行动" | ⚠️ **边缘通过**：纯情绪动员不过 V3，靠"绑定动作 + 8 年锚点 + 判停条件"通过 | 单一自述样本 |

## 3. 晋级门（阶段 1.6）

| 能力 | 独立意图 | 独立契约 | 独立运行 | 独立复用 | 独立评测 | 去向 |
|---|---|---|---|---|---|---|
| 处世三红线 | ✓ | ✓ | ✓ | ✓ | ✓ | **promoted** |
| 求职避坑与面试 | ✓ | ✓ | ✓ | ✓ | ✓ | **promoted** |
| 避坑优先法 | ✓ | ✓ | ✓ | ✓ | ✓ | **promoted** |
| 流量匹配 | ✓ | ✓ | ✓ | ✓ | ✓ | **promoted** |
| 人才优先与区域围剿 | ✓ | ✓ | ~ | ✓ | ✓ | router |
| 李鬼矩阵 | ✓ | ✓ | ~ | ✓ | ✓ | router（风险项不宜作为独立入口） |
| 区域聚焦与最小切口 | ✓ | ✓ | ~ | ✓ | ✓ | router |
| 逆袭觉醒 | ✓ | ~ | ~ | ✓ | ✓ | router（立场冲突项降为路由访问） |

- 未晋级项**保留为能力卡**，经来源路由入口可达，不进入 rejected。
- single 变体下 promoted 不产出独立 Skill 目录，可发现入口仍为 1，未触及软预算 8。

## 4. 合规处理记录

| 风险项 | 原始内容 | 处理方式 | 用户确认 |
|---|---|---|---|
| 李鬼矩阵 | "注册近似品牌抢占头部品牌流量" | 用户选择「原样纳入并标注风险」→ I 段保留原始描述，**E 段只给合法动作**（自有矩阵/品类词/差异化定位/被截流防御），B 段列四项法律风险 + 四条硬门 | ✓ 2026-10-09 |
| 用户转销售（海鸥模式） | "把用户转化为销售" | 加**分销硬门**：禁多层级、禁入门费、返佣须来自真实成交 | 本次增补主动加入 |
| 人才围剿/挖人 | "区域化创业先搞定顶尖人才" | 加判停：不硬挖有竞业限制的在职人员，注意商业秘密边界 | 本次增补主动加入 |
| 逆袭觉醒 | 心态干预 | 加硬门：出现抑郁/自伤倾向即转介专业机构，本卡不作治疗手段 | 本次增补主动加入 |
| 飞书脚本 | 原脚本读 config.json 且无脱敏 | 改写：补 config.example.json、加凭据行脱敏、加异常处理与超时、标注"不生成内容只同步" | — |
| 作者生平（含服刑经历） | biography.md | 事实库内**就事论事**，不作道德评价，不作为能力或品格证明 | — |

## 5. 立场冲突记录

| 冲突 | A 原立场 | 本次处理 |
|---|---|---|
| 心态类内容 | overview.md「适用性」判为低优先级，理由"V3 不通过"，**已批量剔除** | 用户明确要求补入 → 成卡 `ni-xi-jue-xing`，卡首声明冲突，使用限制为"只处理阻碍行动的四种情绪、必须落到动作、不做情绪安抚、不替代专业帮助、不输出金句" |
| 人格口吻 | A 是中立蒸馏产物，无人格层 | 补 `persona-and-style.md` 但**默认关闭**，仅在用户明确要求时加载，且要求"口吻可以糙，依据不能糙" |
| 数据可信度 | A 的数据已声明"主播自述，未核验" | 增补卡沿用同一口径，并在各卡审计信息与 cheatsheet 中重复标注 |

## 6. 淘汰 / 降级项

| 项 | 处置 | 理由 |
|---|---|---|
| 工具化沉淀（心法 9） | 不入卡，降为 also_read 引用 | V1 不足（仅 methodology.md 一处）；且"把能力做成产品"接近常识，V3 不通过 |
| 先就业再择业（心法 10） | 不单独成卡 | 与 A 原有 `da-gong-qi-bu` 高度重合，A 版更完整 |
| 刺客式调研（心法 1） | 不单独成卡 | 与 A 原有 `kan-guang-gao` 重合，已在 `bi-keng-you-xian` 的 also_read 中引用 |
| 轻量起盘法（心法 5） | 不单独成卡 | 与 A 原有 `zui-xiao-shi-yan-ti` 重合，A 版有完整判停规则 |

> **v1.2 复核（2026-10-09）**：上表四项中，**工具化沉淀**与**刺客式调研**已在 v1.2 成卡（见第 9 节），依据分别是「用户要求补入」与「原判定有误——两者契约不同」。**先就业再择业**与**轻量起盘法**维持原判定：复核确认 A 版 `da-gong-qi-bu` / `zui-xiao-shi-yan-ti` 更完整，且来源包这两项没有 A 版之外的增量信息，成卡会造成抢调用。

## 7. 上架前待办（平台合规）

- ⚠️ `references/capabilities/` 为三级嵌套，上架平台要求包目录最多两级。上架前需执行 flatten（把 `capabilities/*.md` 上移到 `references/`），并**同步修改** SKILL.md、capability-index.md、cheatsheet.md、各卡「相关能力」段中的路径引用。
- 本次增补未修改原有 13 张卡的内容，因此 flatten 涉及的引用点包含原有 13 张卡。
- 若保留中文 `name`，上架需走 CLI 渠道并用 `--slug ludamo-dai-ni-chuang-ye` 显式指定线上 slug。

## 8. 来源清单

- 技能包 B《鲁大魔·全能逆袭智库》：SKILL.md、logic/methodology.md、logic/sub_skills/encouragement.md、logic/sub_skills/job_hunting.md、logic/sub_skills/relationships.md、database/biography.md、templates/{blueprint,execution_logs,job_audit,pitfalls}.md、templates/large_project/{personnel,supply_chain,traffic}_module.md、scripts/feishu_sync.py
- 跨包互证引用：A 包 `di-er-zeng-zhang-qu-xian`（大兵/电竞椅案例）被 `bi-keng-you-xian` 借用

---

# 9. v1.2 缺口补齐审计（2026-10-09）

> 本次不是新的蒸馏，而是对 v1.1 的一次**覆盖审计 + 缺口补齐**。审计对象是来源包 B 的 14 项材料。

## 9.1 审计方法

逐项列出来源包 B 的 14 项材料，检查其是否已在 v1.1 落地。判定标准**不是字面出现**，而是"**能力契约是否被承接**"——某项材料若在包内找不到承担同一契约的卡/资产，即判为缺口。核查手段：`SUPPLEMENT_LOG.md` §1 候选池 + 全包关键词 grep + 逐文件比对。

## 9.2 结果总览

| 处置 | 数量 | 项 |
|---|---|---|
| 完全收录 | 11 | 心法 2/3/4/6/7/8/10、处世三红线、求职避坑、逆袭觉醒、生平事实库 |
| 合并收录 | 2 | 心法 7+8 → `qu-yu-yu-qie-kou`；心法 10 → `da-gong-qi-bu` |
| v1.1 淘汰 | 4 | 心法 1、心法 5、心法 9、心法 10 |
| **v1.2 改判成卡** | **2** | 心法 1 → `ci-ke-shi-diao-yan`；心法 9 → `gong-ju-hua-chen-dian` |
| 维持淘汰 | 2 | 心法 5（轻量起盘）、心法 10（先就业再择业） |
| 遗漏（非能力） | 3 条金句 | 已补入 `persona-and-style.md` |

**结论**：v1.1 的能力覆盖是完整的，但**字面内容层面存在三处缺口**（见 §9.3、§9.5）。

## 9.3 改判记录

| 项 | v1.1 判定 | v1.2 复核结论 | 依据 |
|---|---|---|---|
| 刺客式调研（心法 1） | "与 `kan-guang-gao` 重合"，不单独成卡 | **原判定有误，改判成卡** `ci-ke-shi-diao-yan` | 两者契约不同：看广告是**被动观察公开信号**（零接触、面向行业）；刺客式调研是**主动以买家身份接触**（有接触成本、面向具体标的）。v1.1 的合并导致「加微信 → 看朋友圈 → 套话术 → 摸价格 → 踩坑点」这组动作全包零命中（grep "套话" 0 结果） |
| 工具化沉淀（心法 9） | "V1 不足 + 接近常识"，淘汰 | **按用户要求补入，成卡但保留边缘标记** `gong-ju-hua-chen-dian` | V3 靠三条反直觉判据通过（可复制性判定 / 时机滞后 / 载体不跳级）。**但 V1 不足的理由至今成立**——全来源包仅一处表述、零案例，本包亦未找到第二处独立来源。因此证据等级定为「主张级」，为全包 23 卡中最低 |

## 9.4 维持淘汰的复核依据

| 项 | 复核结论 | 依据 |
|---|---|---|
| 轻量起盘法（心法 5） | 维持不单独成卡 | `zui-xiao-shi-yan-ti` 已完整承接"撮合、不囤货、不压资金"，且 A 版有判停规则与案例（033 域名撮合）。来源包版本无增量信息 |
| 先就业再择业（心法 10） | 维持不单独成卡 | `da-gong-qi-bu` + `sheng-cun-ji-neng` 已承接，且 A 版给出了"信息位/体力位"这一来源包没有的选岗判据。成卡会造成抢调用 |

## 9.5 金句补齐清单（v1.1 遗漏）

| 金句 | 来源 | v1.2 处置 |
|---|---|---|
| "这就是典型的李鬼打法。" | methodology.md 二·金句库 | 补入 `persona-and-style.md`，**加使用限制**：仅用于指认他人行为，不用于建议用户去做 |
| "学会自己消化情绪。躲在车里哭完，推开门你还得是那个顶梁柱。" | relationships.md §4 社交金句 | 补入，标注配合 `chu-shi-san-hong-xian` |
| "尊重家人的认知水平。他们只是想让你稳当点，这没错。你做成了，他们自然就信了。" | relationships.md §4 社交金句 | 补入，标注配合 `chu-shi-san-hong-xian` 亲人红线 |

> v1.1 已收录的 6 条（沉淀吧 / 吃亏踩坑 / 先看别人怎么死的 / 人才比业务更重要 / 太刑了 / 又懒又想投机）本次未改动。

## 9.6 合规处理（本次新增）

| 风险项 | 来源包原文 | 处理方式 |
|---|---|---|
| 刺客式调研 | "全程伪装客户" | **收窄为"保留购买意图"**：不主动纠正对方的买家假设可以；虚构法人主体、伪造资质、假签意向合同不可以。另加五条硬门（见卡内 B 段），其中"不得索取成本表/客户名单/技术资料"是对来源包"套话术"补的边界 |
| 刺客式调研的样本量 | 来源包未提 | 主动补上"**至少摸 3 家交叉验证**"（数量下限沿用 `bi-keng-you-xian`）。单家可能是表演 |
| 工具化沉淀 | "把能力做成可复制的产品（如 AI 工具）" | 加判停：涉及持牌专业判断（法律/医疗/财务）不得产品化；并在 B 段点明**可复制性与护城河的矛盾**——越标准化越易被 AI 替代，与 overview「AI 替代速度」这一时代局限直接冲突 |

## 9.7 本次产出与版本

| 项 | 内容 |
|---|---|
| 版本 | 1.1.0 → **1.2.0** |
| 新增能力卡 | 2 张：`ci-ke-shi-diao-yan`（promoted）、`gong-ju-hua-chen-dian`（router，⚠️ 主张级） |
| capability-count | 21 → **23** |
| 同步修改 | SKILL.md（版本/描述/路由表/加载规则/新增 v1.2 说明）、capability-index.md、cheatsheet.md、glossary.md（新增 2 条术语 + 「当刺客」加防混淆提示）、overview.md（能力分布 + 新增 v1.2 说明）、persona-and-style.md（3 条金句） |
| 交叉引用 | `kan-guang-gao`、`bi-keng-you-xian`、`di-er-zeng-zhang-qu-xian`、`sheng-cun-ji-neng`、`zui-xiao-shi-yan-ti` 的相关能力段 |

## 9.8 上架前待办（继承 §7，仍未处理）

- ⚠️ `references/capabilities/` 三级嵌套仍需 flatten 才能上架，并同步 SKILL.md、capability-index.md、cheatsheet.md、各卡「相关能力」段中的路径引用。**v1.2 新增的 2 张卡也在此目录内，flatten 时需一并处理。**
- 若保留中文 `name`，上架走 CLI 渠道并用 `--slug ludamo-dai-ni-chuang-ye` 显式指定线上 slug（不变）。

---

## 10. v1.2.1 一致性修补（2026-10-09）

v1.2 补入 2 张卡后做了一次全包检查。结论：**两张卡本体与全部同步落点均无误**（与桌面副本 `diff` 逐字一致），但外围有三处没跟上。

### 10.1 检查结论（通过项）

| 项 | 结果 |
|---|---|
| 卡片文件与桌面副本 | 两份均 IDENTICAL |
| SKILL.md 路由表 / 加载规则 / 核心原则 | 已加（路由 2 行、防抢调用 2 条、核心原则第 11 条） |
| capability-index.md | 2 行已加，总 23 行 = `capability-count: 23` |
| cheatsheet.md / overview.md / glossary.md | 均已同步 |
| BUILD_MANIFEST.json | 两文件路径已列入 |
| 卡内引用的相邻 slug | 15 个全部存在，全包无死链 |

### 10.2 修补项

| # | 缺口 | 处置 |
|---|---|---|
| 1 | 顶层合规硬门停留在 v1.1 的 6 条，未覆盖 `ci-ke-shi-diao-yan` 的调研硬门（卡内有，但加载规则是"只加载 1 张卡"，路由未命中时顶层无兜底） | 补第 7 条（不虚构主体／不假签／不骗取商业秘密／不偷拍偷录／不骚扰）；顺带补第 8 条（`gong-ju-hua-chen-dian`：未跑通的能力不得包装成产品出售，持牌领域不得产品化） |
| 2 | `templates/research-log.md` 头部声明是 `ci-ke-shi-diao-yan` 的作业载体，但表内只有看广告／失败案例／实验／打工四节，缺摸底字段 | 新增第 5 节「标的摸底记录」：要拿的 3 个数字 → 摸底采集（公开痕迹／三层价格／成交流程／失败条款／危险信号）→ 三家交叉对比 → 合规自查勾选；原第 5 节顺延为第 6 节 |
| 3 | 6 张老卡与新卡有显式契约却无反向链接 | 补 `luo-ji-si-wei-lian`（摸底数字进数据层）、`xing-jia-bi-yu-gong-ying-lian`（产品化后定价 + 对手价格输入）、`si-ge-ji-ben-dian`（隐性判断显性化验收）、`liu-liang-pi-pei`（产品化后的变现匹配）、`da-gong-qi-bu`（内部流程面 vs 外部交易面）、`qiu-zhi-bi-keng-yu-mian-shi`（把公司当标的摸） |
| 4 | 打包残留 `scripts/__pycache__/feishu_sync.cpython-313.pyc` | 已删除 |

### 10.3 版本

- 1.2.0 → **1.2.1**；`cangjie.increment` 追加 `v1.2.1-20261009-consistency-fix`
- 能力卡数量、路由表、capability-index 均未变动（仍 23）
- 本次改动未触及任何卡片的原文、判据与证据等级标记


---

## 11. v1.2.2 上架适配修补（2026-10-09）

针对 Skill 包在平台上架时的两类解析失败做的修补，与能力内容无关。

### 11.1 改动清单

| # | 问题 | 处置 |
|---|---|---|
| 1 | 包内含 `references/capabilities/` 三级嵌套，平台要求目录最多两级 | 23 张能力卡上移至 `references/`；同步 SKILL.md（29 处引用）与 `capability-index.md`（23 处引用）的路径 |
| 2 | `description_en` plain scalar 含 `: `（`capability units: starting`），YAML 报 mapping values are not allowed | 与 `display_name_en` 一并补双引号；`name`（中文）与 `description_zh` 无风险字符，未改 |
| 3 | `qiu-zhi-bi-keng-yu-mian-shi.md` 引用 `templates/job_audit.md`（下划线），实际文件为 `job-audit.md`（连字符） | 该卡正文中统一为连字符写法；**带「B 包」前缀的溯源标注保留 `job_audit.md` 原样**（那是源素材技能包的真实文件名） |
| 4 | 打包偶发夹带 `scripts/__pycache__/` | 打包脚本已固定排除 `__pycache__`/`*.pyc`/`.DS_Store` |

### 11.2 未改动项

- `BUILD_MANIFEST.json` 的 `version`（1.2.0）与 `published_hashes`：属 v1.2.0 归档基准，保持不动
- 第 10 节及此前的历史记录：均为历史档案，不随版本改写
- 所有能力卡原文、判据、证据等级标记

### 11.3 版本

- 1.2.1 → **1.2.2**；`cangjie.increment` 追加 `v1.2.2-20261009-frontmatter-fix`
- 能力卡数量、路由表、capability-index 均未变动（仍 23）
