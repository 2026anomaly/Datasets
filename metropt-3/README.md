<!DOCTYPE html><html lang="zh-CN"><head>
<meta charset="UTF-8">
<title>MetroPT-3 数据集说明文档</title>
<style>
@page { size: 210mm 297mm; margin: 0; }
*, *::before, *::after { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
html { background-color: #ffffff; }
@media (prefers-color-scheme: dark) {
    html { background-color: #1f1f1f; }
}
body {
    padding: 24px 0;
    margin: 0 auto;
    max-width: 1160px !important;
    border: none !important;
    background: transparent !important;
    font-family: 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', 'Noto Sans CJK SC', 'Source Han Sans SC', sans-serif;
    color: #1e293b;
    font-size: 10.5pt;
    line-height: 1.45;
}
.page {
    width: 210mm;
    height: 297mm;
    margin: 0 auto 12px auto;
    padding: 16mm 18mm 12mm 18mm;
    background-color: #ffffff;
    border: 1px solid rgba(0, 0, 0, 0.12);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
}
@media screen and (max-width: 600px) {
    body { padding: 16px 0; }
    .page { width: 100%; margin: 0 auto 8px auto; border: none; padding: 12px 20px; }
}
.page-content {
    flex: 1 1 0;
    min-height: 0;
    overflow: hidden;
}
.page-content > * + * {
    margin-top: 12px;
}
.page-content > :is(h1, h2, h3, h4) + * {
    margin-top: 4px;
}
.page-footer {
    flex-shrink: 0;
    margin-top: auto;
    padding-top: 3mm;
    border-top: 1px solid #e2e8f0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 8.5pt;
    color: #64748b;
}
@media print {
    *, *::before, *::after {
        box-shadow: none !important;
        text-shadow: none !important;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }
    body { padding: 0; background: none; }
    .page { margin: 0; border: none; break-after: page; page-break-after: always; }
    .page:last-child { break-after: auto; page-break-after: auto; }
}
[contenteditable]:focus { outline: none; }

/* Document Styling matching NASA POWER style */
h1 {
    font-size: 16pt;
    font-weight: 700;
    color: #0f172a;
    margin: 0 0 8px 0;
    border-bottom: 2px solid #0f172a;
    padding-bottom: 6px;
}
h2 {
    font-size: 11.5pt;
    font-weight: 700;
    color: #0f172a;
    margin: 10px 0 4px 0;
    padding-bottom: 2px;
    border-bottom: 1px solid #cbd5e1;
}
p {
    margin: 0;
    text-align: justify;
}
ul, ol {
    margin: 0;
    padding-left: 18px;
}
li {
    margin-bottom: 2px;
}
a {
    color: #1d4ed8;
    text-decoration: none;
    overflow-wrap: break-word;
    word-break: break-all;
}
table {
    width: 100%;
    border-collapse: collapse;
    font-size: 8.5pt;
}
th, td {
    border: 1px solid #cbd5e1;
    padding: 4px 6px;
    text-align: left;
    vertical-align: middle;
    overflow-wrap: break-word;
}
th {
    background-color: #f1f5f9;
    color: #0f172a;
    font-weight: 600;
}
.meta-info p {
    margin-bottom: 3px;
}
.code-block {
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 8.5pt;
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    padding: 6px 10px;
    border-radius: 3px;
}
</style>
</head>
<body>
<div contenteditable="true">
<section class="page">
  <div class="page-content">
    <h1>MetroPT-3 数据集</h1>
    
    <div class="meta-info">
      <p><strong>数据集名称：</strong>MetroPT-3 压缩机空气产生单元（APU）运营多元时间序列数据</p>
      <p><strong>数据集类型：</strong>多元时间序列 / 工业物联网 / 异常检测与预测性维护</p>
      <p><strong>上传成员：</strong>2026anomaly</p>
    </div>

    <h2>数据集说明</h2>
    <p>该数据集收集自实际运营环境中的地铁列车压缩机空气产生单元（APU）。数据跨度从 2020 年 2 月至 8 月，由车载嵌入式设备以 1Hz 的频率记录，共包含 15,169,480 条记录。数据集用于支持预测性维护、异常解释及剩余寿命（RUL）预测模型研究。</p>

    <h2>字段说明（15个特征传感器）</h2>
    <table>
      <thead>
        <tr>
          <th scope="col" style="width: 22%;">列名 / 传感器</th>
          <th scope="col" style="width: 48%;">含义与物理测量说明</th>
          <th scope="col" style="width: 15%;">单位</th>
          <th scope="col" style="width: 15%;">属性分类</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>TP2</strong></td>
          <td>压缩机上的压力测量值</td>
          <td>bar</td>
          <td>模拟信号 (1)</td>
        </tr>
        <tr>
          <td><strong>TP3</strong></td>
          <td>气动面板上生成的压力测量值</td>
          <td>bar</td>
          <td>模拟信号 (2)</td>
        </tr>
        <tr>
          <td><strong>H1</strong></td>
          <td>旋风分离器过滤器排气时压降产生的压力</td>
          <td>bar</td>
          <td>模拟信号 (3)</td>
        </tr>
        <tr>
          <td><strong>DV pressure</strong></td>
          <td>干燥器排气压降（零表示负载运行）</td>
          <td>bar</td>
          <td>模拟信号 (4)</td>
        </tr>
        <tr>
          <td><strong>Reservoirs</strong></td>
          <td>储气筒下游压力（应接近TP3）</td>
          <td>bar</td>
          <td>模拟信号 (5)</td>
        </tr>
        <tr>
          <td><strong>Motor Current</strong></td>
          <td>三相电机一相电流（0:关, 4:卸载, 7:负载, 9:启动）</td>
          <td>A</td>
          <td>模拟信号 (6)</td>
        </tr>
        <tr>
          <td><strong>Oil Temperature</strong></td>
          <td>压缩机油温测量值</td>
          <td>°C</td>
          <td>模拟信号 (7)</td>
        </tr>
        <tr>
          <td><strong>COMP</strong></td>
          <td>进气阀电气信号（无进气/关闭或卸载时激活）</td>
          <td>—</td>
          <td>数字信号 (8)</td>
        </tr>
        <tr>
          <td><strong>DV electric</strong></td>
          <td>控制出气阀电气信号（负载下工作时激活）</td>
          <td>—</td>
          <td>数字信号 (9)</td>
        </tr>
        <tr>
          <td><strong>TOWERS</strong></td>
          <td>干燥塔与排水塔状态切换信号</td>
          <td>—</td>
          <td>数字信号 (10)</td>
        </tr>
        <tr>
          <td><strong>MPG</strong></td>
          <td>压力低于8.2 bar时在负载下启动压缩机的信号</td>
          <td>—</td>
          <td>数字信号 (11)</td>
        </tr>
        <tr>
          <td><strong>LPS</strong></td>
          <td>压力降至7 bar以下时激活的低压检测信号</td>
          <td>—</td>
          <td>数字信号 (12)</td>
        </tr>
        <tr>
          <td><strong>Pressure Switch</strong></td>
          <td>检测空气干燥塔排气的信号</td>
          <td>—</td>
          <td>数字信号 (13)</td>
        </tr>
        <tr>
          <td><strong>Oil Level</strong></td>
          <td>压缩机油位检测信号（油位低于预期时激活）</td>
          <td>—</td>
          <td>数字信号 (14)</td>
        </tr>
        <tr>
          <td><strong>Cudal Impulse</strong></td>
          <td>计算APU流向储气筒绝对空气流量的脉冲输出</td>
          <td>—</td>
          <td>数字信号 (15)</td>
        </tr>
      </tbody>
    </table>

    <h2>数据完整性</h2>
    <p>数据集跨度 2020-02 至 2020-08，按 1Hz 持续采样，总记录数约 1516 万行。未发现明显系统性缺失值（$N/A$），数据包含了列车真实的运行波动与噪声，非常适合用于无监督及半监督异常检测算法的压力测试。</p>
  </div>
  <footer class="page-footer">
    <span>MetroPT-3 数据集说明文档</span>
    <span>Page 1 of 2</span>
  </footer>
</section>

<section class="page">
  <div class="page-content">
    <h2>故障信息与报告记录</h2>
    <p>虽然数据集为无标签（Unlabeled）状态，但公司提供了以下真实的故障记录，可用于评估异常检测及 RUL 算法的有效性：</p>

    <table>
      <thead>
        <tr>
          <th scope="col" style="width: 10%;">编号</th>
          <th scope="col" style="width: 22%;">开始时间</th>
          <th scope="col" style="width: 22%;">结束时间</th>
          <th scope="col" style="width: 18%;">故障类型</th>
          <th scope="col" style="width: 14%;">严重程度</th>
          <th scope="col" style="width: 14%;">维护报告</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>#1</td>
          <td>4/18/2020 0:00</td>
          <td>4/18/2020 23:59</td>
          <td>漏气 (Air leak)</td>
          <td>高应力</td>
          <td>无</td>
        </tr>
        <tr>
          <td>#2</td>
          <td>5/29/2020 23:30</td>
          <td>5/30/2020 6:00</td>
          <td>漏气 (Air Leak)</td>
          <td>高应力</td>
          <td>4月30日 12:00维护</td>
        </tr>
        <tr>
          <td>#3</td>
          <td>6/5/2020 10:00</td>
          <td>6/7/2020 14:30</td>
          <td>漏气 (Air Leak)</td>
          <td>高应力</td>
          <td>6月8日 16:00维护</td>
        </tr>
        <tr>
          <td>#4</td>
          <td>7/15/2020 14:30</td>
          <td>7/15/2020 19:00</td>
          <td>漏气 (Air Leak)</td>
          <td>高应力</td>
          <td>7月16日 00:00维护</td>
        </tr>
      </tbody>
    </table>

    <h2>相关学术论文参考</h2>
    <ul>
      <li>[1] Davari, N., et al. "Predictive maintenance based on anomaly detection using deep learning for air production unit in the railway industry." <em>2021 IEEE 8th International Conference on Data Science and Advanced Analytics (DSAA)</em>, pp. 1-10 (2021).</li>
      <li>[2] Veloso, B., et al. "The MetroPT dataset for predictive maintenance." <em>Scientific Data</em> 9, no. 1 (2022): 764.</li>
      <li>[3] Barros, M., et al. "Failure detection of an air production unit in the operational context." <em>IoT Streams for Data-Driven Predictive Maintenance</em>, pp. 61-74. Springer (2020).</li>
    </ul>

    <h2>数据来源与作者联系方式</h2>
    <p><strong>INESC TEC - 人工智能与决策支持实验室及波尔图大学：</strong></p>
    <ul>
      <li>Narjes Davari: <a href="mailto:narjes.davari@inesctec.pt">narjes.davari@inesctec.pt</a></li>
      <li>Bruno Veloso (波尔图大学经济学院): <a href="mailto:bveloso@fep.up.pt">bveloso@fep.up.pt</a></li>
      <li>Rita P. Ribeiro (波尔图大学科学学院): <a href="mailto:rpribeiro@fc.up.pt">rpribeiro@fc.up.pt</a></li>
      <li>Joao Gama (波尔图大学经济学院): <a href="mailto:jgama@fep.up.pt">jgama@fep.up.pt</a></li>
    </ul>
  </div>
  <footer class="page-footer">
    <span>MetroPT-3 数据集说明文档</span>
    <span>Page 2 of 2</span>
  </footer>
</section>
</div>

</body></html>
