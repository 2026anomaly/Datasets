# Anomalydetection Datasets

课题组公用异常检测数据集仓库。每个数据集一个目录，目录内 `README.md` 说明来源与字段。

## 数据集清单

| 目录 | 数据集 | 类型 | 说明 |
|---|---|---|---|
| `SWaT/` | SWaT | 工控系统 | 安全水处理测试床数据集 |
| `TON_IoT/` | TON_IoT | 物联网安全 | 异构图/物联网络流量与遥测 |
| `metropt-3/` | MetroPT-3 | 工业设备 | 地铁空压机传感器数据 |
| `NASA_POWER/` | NASA POWER | 气象时序 | 三站 10 年逐小时多变量气象观测 |

## 约定

1. 一个数据集一个目录，目录名用英文。
2. 目录内必须有 `README.md`，至少包含：数据集名称、数据集类型、上传成员、数据集说明。
3. 大文件走 **Git LFS**（`*.zip`、`*.csv` 已在 `.gitattributes` 中配置）。
   首次使用前请先安装 LFS：

   ```bash
   git lfs install
   ```

   克隆时如提示 `smudge filter lfs failed`，说明本机未装 LFS，装好后再
   `git lfs pull`。
4. 单文件请控制在 100 MB 以内（GitHub 硬限制）。更大的数据请用外链，
   或在 `README.md` 中说明获取方式。
