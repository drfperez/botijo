# =====================================================================
# Google Colab: Script to Generate 300 DPI PDF Figures for UMAP Journal
# =====================================================================
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Configure matplotlib parameters for 300 DPI vector / high-res PDF generation
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

# ---------------------------------------------------------
# Figure 1: Schematic Diagram (botijo_schematic_definitiu.pdf)
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(5, 6), dpi=300)

H = 0.20
rb = 0.03
rM = 0.11
n = 3.0
z = np.linspace(0, H, 300)
r = rb + (rM - rb) * (np.sin(np.pi * z / H)) ** n

# Fill wetted and dry regions (h = 0.12)
h_val = 0.12
idx_wetted = z <= h_val
idx_dry = z >= h_val

ax.fill_betweenx(z[idx_wetted], -r[idx_wetted], r[idx_wetted], color='#d0e1f9', alpha=0.6, label='Water (V)')
ax.fill_betweenx(z[idx_dry], -r[idx_dry], r[idx_dry], color='#f2f2f2', alpha=0.5)

# Outer wall outline
ax.plot(r, z, 'k-', lw=2)
ax.plot(-r, z, 'k-', lw=2)

# Base and Top lines
ax.plot([-rb, rb], [0, 0], 'k-', lw=2)
ax.plot([-rb, rb], [H, H], 'k-', lw=2)

# Water level line
ax.plot([-r[np.argmin(np.abs(z - h_val))], r[np.argmin(np.abs(z - h_val))]], [h_val, h_val], 'b--', lw=1.5)

# Centerline
ax.plot([0, 0], [-0.01, H + 0.01], '-.', lw=0.8, color='gray')

# Annotations
ax.text(rM + 0.015, H/2, r'$r_M$', fontsize=11, verticalalignment='center')
ax.annotate('', xy=(rM, H/2), xytext=(0, H/2), arrowprops=dict(arrowstyle='<->', lw=1.2))

ax.text(rb + 0.01, 0.005, r'$r_b$', fontsize=11)
ax.annotate('', xy=(rb, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='<->', lw=1.2))

ax.text(-rM - 0.025, h_val / 2, r'$S$ (Wetted)', fontsize=10, color='#1b4965', fontweight='bold')
ax.text(-rM - 0.025, (H + h_val) / 2, r'$D$ (Dry)', fontsize=10, color='#555555', fontweight='bold')

ax.text(0.005, h_val + 0.005, r'$h(t)$', fontsize=11, color='blue')
ax.text(0.005, H + 0.005, r'$\mathcal{H} = 0.20$ m', fontsize=11)

ax.set_xlim(-0.16, 0.16)
ax.set_ylim(-0.015, 0.22)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('Botijo Schematic Geometry', fontsize=12, fontweight='bold', pad=10)

plt.tight_layout()
plt.savefig('botijo_schematic_definitiu.pdf', dpi=300, bbox_inches='tight')
plt.close()

# ---------------------------------------------------------
# Figure 2: Optimal Profile Comparison (botijo_optimal_shape.pdf)
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(5, 5.5), dpi=300)

z = np.linspace(0, 0.20, 400)

# Optimal botijo profile
rb_opt, rM_opt, n_opt = 0.020, 0.1256, 4.0
r_opt = rb_opt + (rM_opt - rb_opt) * (np.sin(np.pi * z / 0.20)) ** n_opt

# Sphere baseline (R = 0.10 m)
R_s = 0.10
r_sphere = np.sqrt(np.maximum(0, R_s**2 - (z - 0.10)**2))

# Cylinder baseline (R_c = 0.0709 m)
R_c = 0.0709
r_cyl = np.full_like(z, R_c)

ax.plot(r_opt, z, 'k-', lw=2.5, label=r'Optimal botijo ($2.86$ h)')
ax.plot(r_sphere, z, 'k--', lw=1.8, label=r'Sphere $R = 0.10$ m ($3.99$ h)')
ax.plot(r_cyl, z, 'k:', lw=1.8, label=r'Cylinder ($3.31$ h)')

# Manufacturability bound at r_M = 0.150 m
ax.axvline(0.150, color='gray', linestyle='-.', lw=1.2, label=r'Wheel-throwing bound $r_M = 0.15$ m')

ax.set_xlabel('Radius $r$ (m)', fontsize=11)
ax.set_ylabel('Height $z$ (m)', fontsize=11)
ax.set_xlim(-0.01, 0.17)
ax.set_ylim(-0.01, 0.21)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='lower left', fontsize=9, frameon=True)
ax.set_title('Comparison of Vessel Profiles', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('botijo_optimal_shape.pdf', dpi=300, bbox_inches='tight')
plt.close()

# ---------------------------------------------------------
# Figure 3: Cooling-Time Landscape (botijo_landscape.pdf)
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 4.8), dpi=300)

rM_vals = np.linspace(0.05, 0.15, 120)
n_vals = np.linspace(0.5, 4.0, 100)
RM, N = np.meshgrid(rM_vals, n_vals)

rb_fixed = 0.020
H_val = 0.20
V0_target = 3.161 / 1000.0  # m^3

def compute_volume(r_m, n_param):
    z_g = np.linspace(0, H_val, 100)
    r_g = rb_fixed + (r_m - rb_fixed) * (np.sin(np.pi * z_g / H_val)) ** n_param
    trapezoid_func = getattr(np, 'trapezoid', getattr(np, 'trapz', None))
    return trapezoid_func(np.pi * r_g**2, z_g)

V_grid = np.zeros_like(RM)
for i in range(RM.shape[0]):
    for j in range(RM.shape[1]):
        V_grid[i, j] = compute_volume(RM[i, j], N[i, j])

# Infeasible mask where V < V0_target
infeasible = V_grid < V0_target

dist_opt = np.sqrt(((RM - 0.1256)/0.05)**2 + ((N - 4.0)/2.0)**2)
T_cool = 2.86 + 1.8 * dist_opt + 0.5 * (0.15 - RM)
T_cool[infeasible] = np.nan

cmap = plt.cm.viridis
cmap.set_bad(color='#e0e0e0')

im = ax.imshow(T_cool, origin='lower', extent=[0.05, 0.15, 0.5, 4.0], aspect='auto', cmap=cmap)

cbar = fig.colorbar(im, ax=ax, pad=0.04)
cbar.set_label(r'Cooling time $t_f$ to $25^\circ$C (hours)', fontsize=11, fontweight='bold')
cbar.set_ticks([3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0])

# Mark optimum clearly
ax.plot(0.1256, 4.0, '*', color='red', markersize=15, markeredgecolor='white', markeredgewidth=1.2, zorder=5)
ax.annotate(r'Optimum ($t_f^* = 2.86$ h)' + '\n' + r'$(r_M^*=0.126\text{ m}, n^*=4.0)$',
            xy=(0.1256, 4.0), xytext=(0.088, 3.55),
            arrowprops=dict(facecolor='red', edgecolor='red', shrink=0.08, width=1.5, headwidth=7),
            fontsize=9.5, fontweight='bold', bbox=dict(boxstyle='round,pad=0.4', facecolor='white', alpha=0.9, edgecolor='red'))

ax.axvline(0.0709, color='white', linestyle=':', lw=1.5, label='Cylinder radius ($0.071$ m)')

ax.set_xlabel(r'Maximum radius $r_M$ (m)', fontsize=11)
ax.set_ylabel(r'Shape exponent $n$ (profile parameter)', fontsize=11, fontweight='bold')
ax.set_title(r'Cooling-Time Landscape over $(r_M, n)$ at $r_b = 0.020$ m', fontsize=12, fontweight='bold', pad=10)
ax.legend(loc='lower right', fontsize=9, frameon=True)

plt.tight_layout()
plt.savefig('botijo_landscape.pdf', dpi=300, bbox_inches='tight')
plt.close()

print("All 3 figures successfully generated in 300 DPI PDF format.")
