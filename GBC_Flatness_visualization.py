import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------------------
# 1. Flatness measurement data (Thesis Table 4-4)
# --------------------------------------------------
part_A = np.array([0.1601, 0.1617, 0.1636, 0.1599, 0.1596,
                   0.1597, 0.1572, 0.1567, 0.1607, 0.1590])
part_B = np.array([0.0942, 0.0922, 0.0929, 0.0931, 0.0936,
                   0.0906, 0.0960, 0.0918, 0.0929, 0.0924])
part_C = np.array([0.1331, 0.1330, 0.1332, 0.1401, 0.1347,
                   0.1339, 0.1402, 0.1414, 0.1400, 0.1401])

n = np.arange(1, 11)  # Measurement number (n = 1~10)

# --------------------------------------------------
# 2. GBC parameters (TL, uc, w, AL)
# --------------------------------------------------
TL = 0.1500                # Tolerance Limit (mm)
uc_um = 2.5856             # Combined standard uncertainty [µm]
uc = uc_um * 0.001         # -> mm
k = 2.0
w = k * uc                 # Guard band width [mm]

w_list  = [1, 2, 3]        # 1w, 2w, 3w
titles = ["AL (1w)", "AL (2w)", "AL (3w)"]

# 공통 y축 범위 (예시 그림과 유사하게)
y_min = 0.0
y_max = 0.165

# --------------------------------------------------
# 3. Draw GBC line charts for 1w / 2w / 3w
# --------------------------------------------------
for n_w, title in zip(w_list, titles):
    AL = TL - n_w * w

    fig, ax = plt.subplots(figsize=(7, 3))

    # ---- Background zones ----
    ax.fill_between([1, 10], TL, y_max,
                    color="#ffe6e6", alpha=1.0, label="Nonconforming Zone")
    ax.fill_between([1, 10], AL, TL,
                    color="#fff9d6", alpha=1.0, label="Conditional Zone")
    ax.fill_between([1, 10], y_min, AL,
                    color="#e6ffe6", alpha=1.0, label="Fully Conforming Zone")

    # ---- Decision limits ----
    ax.axhline(TL, color="black", linestyle="--", linewidth=1.0,
               label="TL (0.1500 mm)")
    ax.axhline(AL, color="orange", linestyle="dashdot", linewidth=1.0,
               label=title)

    # ---- Measurement trends (Part A/B/C) ----
    ax.plot(n, part_A, marker="o", color="red",   linewidth=1.2, label="Part A")
    ax.plot(n, part_B, marker="o", color="green", linewidth=1.2, label="Part B")
    ax.plot(n, part_C, marker="o", color="blue",  linewidth=1.2, label="Part C")

    # ---- Axes & style ----
    ax.set_xlabel("Measurement Number (n)")
    ax.set_ylabel("Measured Flatness (mm)")
    ax.set_xlim(1, 10)
    ax.set_ylim(y_min, y_max)
    ax.grid(alpha=0.3)

    # ---- Legend 정리 (중복 label 정리 & 순서 조정) ----
    handles, labels = ax.get_legend_handles_labels()
    order = [labels.index("Part A"),
             labels.index("Part B"),
             labels.index("Part C"),
             labels.index("TL (0.1500 mm)"),
             labels.index(title),
             labels.index("Nonconforming Zone"),
             labels.index("Conditional Zone"),
             labels.index("Fully Conforming Zone")]

    ax.legend([handles[i] for i in order],
              [labels[i] for i in order],
              loc="lower right", fontsize=7, framealpha=0.9)

    plt.tight_layout()
    plt.show()
