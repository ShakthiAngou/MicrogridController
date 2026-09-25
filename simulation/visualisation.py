"""
visualization.py

Charts and summary table for the microgrid simulation.
"""

import matplotlib.pyplot as matplot

COLORS = {
    "background": "#F3F6FA",
    "text": "#1F2937",
    "muted_text": "#64748B",
    "grid": "#DCE3EA",
    "solar": "#E69F00",
    "load": "#3478B8",
    "supercapacitor": "#16856B",
    "hydrogen": "#8064A2",
    "header": "#263746",
    "supercapacitor_header": "#176B56",
    "hydrogen_header": "#654A87",
}


def show_simulation_dashboard(
    hourly_results, supercapacitor_capacity_kwh, hydrogen_capacity_kg
):
    """
    Display the simulation charts, summary metrics, and hourly results table.

    Args:
        hourly_results (list[dict]): Per-hour simulation inputs, storage flows,
            remaining energy balance, and storage levels.
        supercapacitor_capacity_kwh (float): Supercapacitor energy capacity.
        hydrogen_capacity_kg (float): Hydrogen storage capacity.
    """
    hours = [row["hour"] for row in hourly_results]
    solar = [row["solar_power_kw"] for row in hourly_results]
    load = [row["load_power_kw"] for row in hourly_results]
    supercapacitor_energy = [row["supercapacitor_energy_kwh"] for row in hourly_results]
    hydrogen_inventory = [row["hydrogen_inventory_kg"] for row in hourly_results]

    solar_energy_kwh = sum(solar)
    load_energy_kwh = sum(load)
    unserved_energy_kwh = sum(
        max(0.0, -row["net_after_storage_kw"]) for row in hourly_results
    )
    curtailed_energy_kwh = sum(
        max(0.0, row["net_after_storage_kw"]) for row in hourly_results
    )
    final_supercapacitor_kwh = supercapacitor_energy[-1] if hours else 0.0
    final_hydrogen_kg = hydrogen_inventory[-1] if hours else 0.0

    style = {
        "font.family": "DejaVu Sans",
        "font.size": 9,
        "axes.labelcolor": COLORS["muted_text"],
        "axes.titlecolor": COLORS["text"],
        "xtick.color": COLORS["muted_text"],
        "ytick.color": COLORS["muted_text"],
        "text.color": COLORS["text"],
    }

    with matplot.rc_context(style):
        figure = matplot.figure(figsize=(16, 22))
        figure.patch.set_facecolor(COLORS["background"])
        grid = figure.add_gridspec(5, 1, height_ratios=[1, 1, 1, 1, 2.2])
        solar_ax = figure.add_subplot(grid[0, 0])
        load_ax = figure.add_subplot(grid[1, 0])
        supercapacitor_ax = figure.add_subplot(grid[2, 0])
        hydrogen_ax = figure.add_subplot(grid[3, 0])
        table_ax = figure.add_subplot(grid[4, 0])

        figure.suptitle(
            "Shakthi Energy | 24-Hour Microgrid Simulation",
            x=0.5,
            y=0.985,
            fontsize=19,
            fontweight="bold",
            color=COLORS["text"],
        )
        figure.text(
            0.5,
            0.963,
            "Solar, demand, and hybrid storage dispatch · Idealised instantaneous H₂ conversion",
            ha="center",
            va="center",
            fontsize=10,
            color=COLORS["muted_text"],
        )

        metrics = [
            ("SOLAR GENERATED", f"{solar_energy_kwh:.1f} kWh"),
            ("LOAD DEMAND", f"{load_energy_kwh:.1f} kWh"),
            ("UNSERVED ENERGY", f"{unserved_energy_kwh:.1f} kWh"),
            ("CURTAILED SURPLUS", f"{curtailed_energy_kwh:.1f} kWh"),
            (
                "FINAL SUPERCAPACITOR",
                f"{final_supercapacitor_kwh:.1f} / {supercapacitor_capacity_kwh:g} kWh",
            ),
            (
                "FINAL HYDROGEN",
                f"{final_hydrogen_kg:.3f} / {hydrogen_capacity_kg:g} kg",
            ),
        ]
        for index, (label, value) in enumerate(metrics):
            x = 0.085 + index * 0.166
            figure.text(
                x,
                0.93,
                f"{label}\n{value}",
                ha="center",
                va="center",
                fontsize=8,
                fontweight="bold",
                color=COLORS["text"],
                bbox={
                    "boxstyle": "round,pad=0.55",
                    "facecolor": "white",
                    "edgecolor": COLORS["grid"],
                    "linewidth": 0.8,
                },
            )

        plot_specs = [
            (
                solar_ax,
                "Solar Generation",
                "Solar generation (kW)",
                solar,
                COLORS["solar"],
            ),
            (load_ax, "Load Demand", "Load demand (kW)", load, COLORS["load"]),
            (
                supercapacitor_ax,
                "Supercapacitor Energy",
                "Stored energy (kWh)",
                supercapacitor_energy,
                COLORS["supercapacitor"],
            ),
            (
                hydrogen_ax,
                "Hydrogen Inventory",
                "Stored hydrogen (kg)",
                hydrogen_inventory,
                COLORS["hydrogen"],
            ),
        ]

        for axis, title, y_label, values, color in plot_specs:
            axis.set_facecolor("white")
            axis.set_title(title, loc="left", pad=8, fontweight="bold")
            axis.set_ylabel(y_label)
            axis.set_xlim(0, 23)
            axis.set_xticks(range(24))
            axis.set_xlabel("Time of day (hour)")
            axis.tick_params(axis="x", labelsize=8, rotation=0)
            axis.plot(
                hours,
                values,
                color=color,
                linewidth=2.2,
                marker="o",
                markersize=3.5,
                markerfacecolor="white",
                markeredgewidth=1.2,
            )
            axis.grid(axis="y", color=COLORS["grid"], linestyle="--", linewidth=0.8)
            axis.grid(
                axis="x", color=COLORS["grid"], linestyle=":", linewidth=0.5, alpha=0.7
            )
            axis.set_axisbelow(True)
            axis.spines["top"].set_visible(False)
            axis.spines["right"].set_visible(False)
            axis.spines["left"].set_color(COLORS["grid"])
            axis.spines["bottom"].set_color(COLORS["grid"])

        _set_capacity_limit(
            supercapacitor_ax,
            supercapacitor_capacity_kwh,
            "kWh",
            COLORS["supercapacitor"],
        )
        _set_capacity_limit(
            hydrogen_ax,
            hydrogen_capacity_kg,
            "kg",
            COLORS["hydrogen"],
        )

        _draw_results_table(table_ax, hourly_results)

        figure.subplots_adjust(
            left=0.09,
            right=0.98,
            top=0.895,
            bottom=0.025,
            hspace=0.72,
        )
        matplot.show()


def _set_capacity_limit(axis, capacity, unit, color):
    """Set a storage plot's capacity range and annotate its upper limit."""
    axis.set_ylim(0, capacity * 1.12 if capacity > 0 else 1)
    if capacity > 0:
        axis.axhline(capacity, color=color, linestyle="--", linewidth=1.1, alpha=0.75)
        axis.text(
            0.995,
            capacity,
            f"Capacity {capacity:g} {unit}",
            transform=axis.get_yaxis_transform(),
            ha="right",
            va="bottom",
            fontsize=8,
            color=color,
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.85, "pad": 2},
        )


def _draw_results_table(axis, hourly_results):
    """Draw the color-grouped hourly energy and storage results table."""
    axis.set_facecolor("white")
    axis.set_title(
        "Hourly Results  |  Green: supercapacitor  ·  Purple: hydrogen",
        loc="left",
        pad=10,
        fontweight="bold",
        fontsize=10,
    )
    axis.axis("off")

    column_labels = [
        "Hr",
        "Solar kW",
        "Load kW",
        "Pre-net kW",
        "SC chg kWh",
        "SC dis kWh",
        "H₂ prod kg",
        "H₂ use kg",
        "Residual kW",
        "SC level kWh",
        "SC SoC %",
        "H₂ level kg",
        "H₂ SoC %",
        "State",
    ]
    cell_values = []
    for row in hourly_results:
        cell_values.append(
            [
                f"{row['hour']:02d}",
                f"{row['solar_power_kw']:.2f}",
                f"{row['load_power_kw']:.2f}",
                f"{row['net_before_storage_kw']:.2f}",
                f"{row['supercapacitor_charged_kwh']:.2f}",
                f"{row['supercapacitor_discharged_kwh']:.2f}",
                f"{row['hydrogen_produced_kg']:.3f}",
                f"{row['hydrogen_used_kg']:.3f}",
                f"{row['net_after_storage_kw']:.2f}",
                f"{row['supercapacitor_energy_kwh']:.2f}",
                f"{row['supercapacitor_soc_percent']:.1f}",
                f"{row['hydrogen_inventory_kg']:.3f}",
                f"{row['hydrogen_soc_percent']:.1f}",
                row["energy_status"],
            ]
        )

    table = axis.table(
        cellText=cell_values,
        colLabels=column_labels,
        cellLoc="center",
        colLoc="center",
        loc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(7.5)
    table.scale(1.0, 1.3)

    supercapacitor_columns = {4, 5, 9, 10}
    hydrogen_columns = {6, 7, 11, 12}
    for column in range(len(column_labels)):
        header = table[(0, column)]
        header.set_text_props(color="white", weight="bold")
        if column in supercapacitor_columns:
            header.set_facecolor(COLORS["supercapacitor_header"])
        elif column in hydrogen_columns:
            header.set_facecolor(COLORS["hydrogen_header"])
        else:
            header.set_facecolor(COLORS["header"])

    status_colors = {
        "BALANCED": "#E6F4EA",
        "SURPLUS": "#FFF3D6",
        "DEFICIT": "#FCE8E6",
    }
    for row_index, result in enumerate(hourly_results, start=1):
        base_color = "#FFFFFF" if row_index % 2 else "#F7F9FC"
        for column in range(len(column_labels)):
            cell = table[(row_index, column)]
            cell.set_facecolor(base_color)
            if column in supercapacitor_columns:
                cell.set_facecolor("#EAF5F1" if row_index % 2 else "#E2F0EB")
            elif column in hydrogen_columns:
                cell.set_facecolor("#F2EDF8" if row_index % 2 else "#EBE4F4")
            cell.set_edgecolor(COLORS["grid"])
            cell.set_linewidth(0.45)

        status_cell = table[(row_index, len(column_labels) - 1)]
        status_cell.set_facecolor(status_colors[result["energy_status"]])
        status_cell.set_text_props(weight="bold")
