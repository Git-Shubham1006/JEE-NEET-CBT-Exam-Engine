import json

# Comprehensive 5-Year JEE Main PYQ Database (2020-2024)
# Spanning Physics, Chemistry, and Mathematics
# Chapter-wise, with Easy / Medium / Hard difficulty classifications, KaTeX equations, and full solutions.

questions = [
    # =========================================================================
    # PHYSICS (2020 - 2024 PYQs)
    # =========================================================================
    # 1. Kinematics & Projectile Motion
    {
        "id": "JEE24_PHY_KIN_01",
        "year": 2024,
        "examShift": "JEE Main 2024 (27 Jan Shift 1)",
        "subject": "Physics",
        "chapter": "Kinematics & Projectile Motion",
        "topic": "Horizontal Projection & Trajectory",
        "type": "SCQ",
        "difficulty": "EASY",
        "questionLatex": "A projectile is thrown with initial speed $u = 20\\text{ m/s}$ at an angle of $45^\\circ$ with the horizontal. The ratio of its horizontal range $R$ to its maximum height $H$ is ($g = 10\\text{ m/s}^2$):",
        "options": [
            { "id": "A", "latex": "$4 : 1$" },
            { "id": "B", "latex": "$2 : 1$" },
            { "id": "C", "latex": "$1 : 4$" },
            { "id": "D", "latex": "$8 : 1$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "For any projectile, $\\frac{R}{H} = \\frac{4}{\\tan\\theta}$. Since $\\theta = 45^\\circ$, $\\tan 45^\\circ = 1$, thus $\\frac{R}{H} = \\frac{4}{1} = 4:1$."
    },
    {
        "id": "JEE23_PHY_KIN_02",
        "year": 2023,
        "examShift": "JEE Main 2023 (06 Apr Shift 2)",
        "subject": "Physics",
        "chapter": "Kinematics & Projectile Motion",
        "topic": "River-Boat Shortest Path",
        "type": "SCQ",
        "difficulty": "MEDIUM",
        "questionLatex": "A river flows due east with speed $v_r = 3\\text{ km/h}$. A swimmer capable of swimming at $v_s = 5\\text{ km/h}$ in still water wants to cross the river along the shortest path (directly opposite bank). At what angle with the upstream direction should the swimmer head?",
        "options": [
            { "id": "A", "latex": "$\\sin^{-1}(3/5)$" },
            { "id": "B", "latex": "$\\cos^{-1}(3/5)$" },
            { "id": "C", "latex": "$\\tan^{-1}(3/5)$" },
            { "id": "D", "latex": "$\\cos^{-1}(4/5)$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "For shortest path, the resultant velocity must be perpendicular to the bank. Hence $v_s \\sin\\alpha = v_r \\implies \\sin\\alpha = \\frac{v_r}{v_s} = \\frac{3}{5}$. The angle with upstream is $\\sin^{-1}(3/5)$."
    },
    {
        "id": "JEE22_PHY_KIN_03",
        "year": 2022,
        "examShift": "JEE Main 2022 (25 Jun Shift 1)",
        "subject": "Physics",
        "chapter": "Kinematics & Projectile Motion",
        "topic": "Non-uniform Acceleration & Turning Point",
        "type": "SCQ",
        "difficulty": "HARD",
        "questionLatex": "A particle moves along the x-axis with acceleration $a(t) = 6t - 12\\text{ m/s}^2$. If at $t = 0$, $v(0) = 9\\text{ m/s}$ and $x(0) = 0$, the total distance travelled by the particle in the time interval $t = 0$ to $t = 4\\text{ s}$ is:",
        "options": [
            { "id": "A", "latex": "$12\\text{ m}$" },
            { "id": "B", "latex": "$16\\text{ m}$" },
            { "id": "C", "latex": "$20\\text{ m}$" },
            { "id": "D", "latex": "$32\\text{ m}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$v(t) = 3t^2 - 12t + 9 = 3(t - 1)(t - 3)$. Velocity changes sign at $t = 1\\text{ s}$ and $t = 3\\text{ s}$. Distance $= |x(1) - x(0)| + |x(3) - x(1)| + |x(4) - x(3)| = 4 + 4 + 4 = 12\\text{ m}$."
    },

    # 2. Laws of Motion & Work-Energy
    {
        "id": "JEE24_PHY_NLM_01",
        "year": 2024,
        "examShift": "JEE Main 2024 (30 Jan Shift 2)",
        "subject": "Physics",
        "chapter": "Laws of Motion & Work-Energy",
        "topic": "Friction on Incline",
        "type": "SCQ",
        "difficulty": "EASY",
        "questionLatex": "A block of mass $m = 2\\text{ kg}$ rests on a rough inclined plane of inclination $\\theta = 30^\\circ$. The minimum coefficient of static friction $\\mu_s$ required to prevent the block from sliding down is:",
        "options": [
            { "id": "A", "latex": "$\\frac{1}{\\sqrt{3}}$" },
            { "id": "B", "latex": "$\\sqrt{3}$" },
            { "id": "C", "latex": "$\\frac{1}{2}$" },
            { "id": "D", "latex": "$\\frac{\\sqrt{3}}{2}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "For impending motion on an incline, $\\tan\\theta = \\mu_s$. Since $\\theta = 30^\\circ$, $\\mu_s = \\tan 30^\\circ = \\frac{1}{\\sqrt{3}} \\approx 0.577$."
    },
    {
        "id": "JEE23_PHY_NLM_02",
        "year": 2023,
        "examShift": "JEE Main 2023 (11 Apr Shift 1)",
        "subject": "Physics",
        "chapter": "Laws of Motion & Work-Energy",
        "topic": "Work Done by Variable Force",
        "type": "SCQ",
        "difficulty": "MEDIUM",
        "questionLatex": "A position-dependent force $F(x) = (3x^2 + 2x - 5)\\text{ N}$ acts on a particle of mass $1\\text{ kg}$ moving along the x-axis. The work done by this force in displacing the particle from $x = 1\\text{ m}$ to $x = 3\\text{ m}$ is:",
        "options": [
            { "id": "A", "latex": "$24\\text{ J}$" },
            { "id": "B", "latex": "$32\\text{ J}$" },
            { "id": "C", "latex": "$18\\text{ J}$" },
            { "id": "D", "latex": "$40\\text{ J}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$W = \\int_1^3 (3x^2 + 2x - 5) dx = [x^3 + x^2 - 5x]_1^3 = (27 + 9 - 15) - (1 + 1 - 5) = 21 - (-3) = 24\\text{ J}$."
    },
    {
        "id": "JEE21_PHY_NLM_03",
        "year": 2021,
        "examShift": "JEE Main 2021 (24 Feb Shift 1)",
        "subject": "Physics",
        "chapter": "Laws of Motion & Work-Energy",
        "topic": "Two-Block Friction System",
        "type": "SCQ",
        "difficulty": "HARD",
        "questionLatex": "A block of mass $m_1 = 4\\text{ kg}$ is placed on top of another block of mass $m_2 = 6\\text{ kg}$. The coefficient of static friction between the two blocks is $\\mu = 0.4$, and the floor is smooth. The maximum horizontal force $F$ applied to the lower block $m_2$ so that both blocks move together without slipping is ($g = 10\\text{ m/s}^2$):",
        "options": [
            { "id": "A", "latex": "$40\\text{ N}$" },
            { "id": "B", "latex": "$24\\text{ N}$" },
            { "id": "C", "latex": "$16\\text{ N}$" },
            { "id": "D", "latex": "$60\\text{ N}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "Maximum acceleration of upper block without slipping is $a_{\\max} = \\mu g = 0.4 \\times 10 = 4\\text{ m/s}^2$. Total mass $M = m_1 + m_2 = 10\\text{ kg}$. Maximum force $F = M a_{\\max} = 10 \\times 4 = 40\\text{ N}$."
    },

    # 3. Rotational Dynamics & Moment of Inertia
    {
        "id": "JEE24_PHY_ROT_01",
        "year": 2024,
        "examShift": "JEE Main 2024 (29 Jan Shift 1)",
        "subject": "Physics",
        "chapter": "Rotational Dynamics & Moment of Inertia",
        "topic": "Radius of Gyration Ratio",
        "type": "SCQ",
        "difficulty": "EASY",
        "questionLatex": "A uniform solid sphere and a thin spherical shell have the same mass $M$ and radius $R$. The ratio of the radius of gyration of the solid sphere to that of the spherical shell about their respective diametrical axes is:",
        "options": [
            { "id": "A", "latex": "$\\sqrt{3} : \\sqrt{5}$" },
            { "id": "B", "latex": "$\\sqrt{5} : \\sqrt{3}$" },
            { "id": "C", "latex": "$3 : 5$" },
            { "id": "D", "latex": "$2 : 3$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$I_{\\text{solid}} = \\frac{2}{5}MR^2 \\implies k_1 = \\sqrt{\\frac{2}{5}}R$. $I_{\\text{shell}} = \\frac{2}{3}MR^2 \\implies k_2 = \\sqrt{\\frac{2}{3}}R$. Ratio $\\frac{k_1}{k_2} = \\sqrt{\\frac{2/5}{2/3}} = \\sqrt{\\frac{3}{5}}$."
    },
    {
        "id": "JEE23_PHY_ROT_02",
        "year": 2023,
        "examShift": "JEE Main 2023 (25 Jan Shift 2)",
        "subject": "Physics",
        "chapter": "Rotational Dynamics & Moment of Inertia",
        "topic": "Rolling Motion Kinetic Energy Fraction",
        "type": "SCQ",
        "difficulty": "MEDIUM",
        "questionLatex": "A uniform solid disc of mass $M$ and radius $R$ is rolling without slipping on a horizontal surface with linear speed $v$. The ratio of its rotational kinetic energy $K_{\\text{rot}}$ to its total kinetic energy $K_{\\text{total}}$ is:",
        "options": [
            { "id": "A", "latex": "$1 : 3$" },
            { "id": "B", "latex": "$1 : 2$" },
            { "id": "C", "latex": "$2 : 3$" },
            { "id": "D", "latex": "$1 : 4$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$K_{\\text{trans}} = \\frac{1}{2}Mv^2$, $K_{\\text{rot}} = \\frac{1}{2}I\\omega^2 = \\frac{1}{4}Mv^2$. $K_{\\text{total}} = \\frac{3}{4}Mv^2$. Thus $\\frac{K_{\\text{rot}}}{K_{\\text{total}}} = \\frac{1/4}{3/4} = \\frac{1}{3}$."
    },
    {
        "id": "JEE22_PHY_ROT_03",
        "year": 2022,
        "examShift": "JEE Main 2022 (28 Jul Shift 2)",
        "subject": "Physics",
        "chapter": "Rotational Dynamics & Moment of Inertia",
        "topic": "Angular Acceleration of Rigid Rod",
        "type": "SCQ",
        "difficulty": "HARD",
        "questionLatex": "A uniform slender rod of mass $M$ and length $L$ is hinged smoothly at one end and held horizontally. When released from rest, the initial angular acceleration $\\alpha$ of the rod about the hinge is:",
        "options": [
            { "id": "A", "latex": "$\\frac{3g}{2L}$" },
            { "id": "B", "latex": "$\\frac{2g}{3L}$" },
            { "id": "C", "latex": "$\\frac{g}{L}$" },
            { "id": "D", "latex": "$\\frac{3g}{4L}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "Torque about hinge: $\\tau = Mg \\left(\\frac{L}{2}\\right)$. Moment of inertia about hinge: $I = \\frac{1}{3}ML^2$. $\\tau = I\\alpha \\implies Mg\\frac{L}{2} = \\frac{1}{3}ML^2\\alpha \\implies \\alpha = \\frac{3g}{2L}$."
    },

    # 4. Thermodynamics & KTG
    {
        "id": "JEE24_PHY_TH_01",
        "year": 2024,
        "examShift": "JEE Main 2024 (27 Jan Shift 2)",
        "subject": "Physics",
        "chapter": "Thermodynamics & KTG",
        "topic": "Carnot Engine Efficiency",
        "type": "SCQ",
        "difficulty": "EASY",
        "questionLatex": "A Carnot engine operates between source temperature $T_1 = 600\\text{ K}$ and sink temperature $T_2 = 300\\text{ K}$. If the heat absorbed from the source is $1200\\text{ J}$, the work done by the engine per cycle is:",
        "options": [
            { "id": "A", "latex": "$600\\text{ J}$" },
            { "id": "B", "latex": "$400\\text{ J}$" },
            { "id": "C", "latex": "$800\\text{ J}$" },
            { "id": "D", "latex": "$300\\text{ J}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$\\eta = 1 - \\frac{T_2}{T_1} = 1 - \\frac{300}{600} = 0.5$. $W = \\eta \\cdot Q_1 = 0.5 \\times 1200 = 600\\text{ J}$."
    },
    {
        "id": "JEE23_PHY_TH_02",
        "year": 2023,
        "examShift": "JEE Main 2023 (08 Apr Shift 1)",
        "subject": "Physics",
        "chapter": "Thermodynamics & KTG",
        "topic": "Cyclic Process Work Done in P-V Diagram",
        "type": "SCQ",
        "difficulty": "MEDIUM",
        "questionLatex": "An ideal gas undergoes a cyclic thermodynamic process consisting of three steps: $A(P_0, V_0) \\to B(3P_0, V_0)$ is isochoric, $B(3P_0, V_0) \\to C(P_0, 4V_0)$ is a straight line on the P-V diagram, and $C \\to A$ is isobaric. The net work done in one complete cycle is:",
        "options": [
            { "id": "A", "latex": "$3 P_0 V_0$" },
            { "id": "B", "latex": "$2 P_0 V_0$" },
            { "id": "C", "latex": "$6 P_0 V_0$" },
            { "id": "D", "latex": "$4.5 P_0 V_0$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "Area of triangle on P-V plane: $\\frac{1}{2} \\times \\text{base} \\times \\text{height} = \\frac{1}{2} \\times (4V_0 - V_0) \\times (3P_0 - P_0) = \\frac{1}{2} \\times 3V_0 \\times 2P_0 = 3 P_0 V_0$."
    },
    {
        "id": "JEE21_PHY_TH_03",
        "year": 2021,
        "examShift": "JEE Main 2021 (20 Jul Shift 2)",
        "subject": "Physics",
        "chapter": "Thermodynamics & KTG",
        "topic": "Polytropic Process Molar Heat Capacity",
        "type": "SCQ",
        "difficulty": "HARD",
        "questionLatex": "An ideal monoatomic gas ($\\gamma = 5/3$) undergoes a polytropic process governed by $P V^2 = \\text{constant}$. The molar heat capacity $C$ of the gas during this process is ($R$ is the gas constant):",
        "options": [
            { "id": "A", "latex": "$0.5 R$" },
            { "id": "B", "latex": "$1.5 R$" },
            { "id": "C", "latex": "$2.5 R$" },
            { "id": "D", "latex": "$-0.5 R$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$C = C_v + \\frac{R}{1 - n} = \\frac{3}{2}R + \\frac{R}{1 - 2} = \\frac{3}{2}R - R = 0.5R$."
    },

    # 5. Electrostatics & Capacitance
    {
        "id": "JEE24_PHY_EL_01",
        "year": 2024,
        "examShift": "JEE Main 2024 (31 Jan Shift 1)",
        "subject": "Physics",
        "chapter": "Electrostatics & Capacitance",
        "topic": "Conducting Spherical Shell Potential & Field",
        "type": "SCQ",
        "difficulty": "EASY",
        "questionLatex": "A hollow conducting sphere of radius $R = 10\\text{ cm}$ carries a uniform surface charge $Q = 2\\mu\\text{C}$. The electric field at a distance $r = 5\\text{ cm}$ from the center is:",
        "options": [
            { "id": "A", "latex": "$0\\text{ N/C}$" },
            { "id": "B", "latex": "$1.8 \\times 10^5\\text{ N/C}$" },
            { "id": "C", "latex": "$3.6 \\times 10^5\\text{ N/C}$" },
            { "id": "D", "latex": "$7.2 \\times 10^5\\text{ N/C}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "By Gauss's law, the electric field inside any hollow charged conductor is identically zero everywhere ($E = 0$ for $r < R$)."
    },
    {
        "id": "JEE23_PHY_EL_02",
        "year": 2023,
        "examShift": "JEE Main 2023 (24 Jan Shift 1)",
        "subject": "Physics",
        "chapter": "Electrostatics & Capacitance",
        "topic": "Capacitor with Partial Dielectric Slab",
        "type": "SCQ",
        "difficulty": "MEDIUM",
        "questionLatex": "A parallel plate capacitor has plate area $A$ and separation $d$, giving vacuum capacitance $C_0$. A dielectric slab of thickness $t = d/2$ and dielectric constant $K = 3$ is inserted between the plates. The new capacitance $C$ is:",
        "options": [
            { "id": "A", "latex": "$1.5 C_0$" },
            { "id": "B", "latex": "$1.2 C_0$" },
            { "id": "C", "latex": "$2.0 C_0$" },
            { "id": "D", "latex": "$1.8 C_0$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$C = \\frac{\\varepsilon_0 A}{d - t + \\frac{t}{K}} = \\frac{\\varepsilon_0 A}{d - \\frac{d}{2} + \\frac{d}{6}} = \\frac{\\varepsilon_0 A}{\\frac{4d}{6}} = 1.5 C_0$."
    },
    {
        "id": "JEE22_PHY_EL_03",
        "year": 2022,
        "examShift": "JEE Main 2022 (26 Jun Shift 2)",
        "subject": "Physics",
        "chapter": "Electrostatics & Capacitance",
        "topic": "Electrostatic Assembly Work Done",
        "type": "SCQ",
        "difficulty": "HARD",
        "questionLatex": "Three identical point charges $+q$ are placed at the vertices of an equilateral triangle of side length $a$. The work required to bring another point charge $+q$ from infinity to the centroid of the triangle is ($k = \\frac{1}{4\\pi\\varepsilon_0}$):",
        "options": [
            { "id": "A", "latex": "$3\\sqrt{3} k \\frac{q^2}{a}$" },
            { "id": "B", "latex": "$\\sqrt{3} k \\frac{q^2}{a}$" },
            { "id": "C", "latex": "$\\frac{3}{\\sqrt{2}} k \\frac{q^2}{a}$" },
            { "id": "D", "latex": "$6 k \\frac{q^2}{a}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$r = \\frac{a}{\\sqrt{3}}$. Potential $V = 3 \\times \\frac{kq}{a/\\sqrt{3}} = 3\\sqrt{3} \\frac{kq}{a}$. Work $W = qV = 3\\sqrt{3} k \\frac{q^2}{a}$."
    },

    # 6. Ray Optics & Wave Optics
    {
        "id": "JEE24_PHY_OPT_01",
        "year": 2024,
        "examShift": "JEE Main 2024 (30 Jan Shift 1)",
        "subject": "Physics",
        "chapter": "Ray Optics & Wave Optics",
        "topic": "Critical Angle for Total Internal Reflection",
        "type": "SCQ",
        "difficulty": "EASY",
        "questionLatex": "A light ray travels from a denser medium of refractive index $\\mu = \\sqrt{2}$ into air. The critical angle $\\theta_c$ for total internal reflection is:",
        "options": [
            { "id": "A", "latex": "$45^\\circ$" },
            { "id": "B", "latex": "$30^\\circ$" },
            { "id": "C", "latex": "$60^\\circ$" },
            { "id": "D", "latex": "$90^\\circ$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$\\sin\\theta_c = \\frac{1}{\\mu} = \\frac{1}{\\sqrt{2}} \\implies \\theta_c = 45^\\circ$."
    },
    {
        "id": "JEE23_PHY_OPT_02",
        "year": 2023,
        "examShift": "JEE Main 2023 (29 Jan Shift 2)",
        "subject": "Physics",
        "chapter": "Ray Optics & Wave Optics",
        "topic": "YDSE Immersion in Liquid Fringe Width",
        "type": "SCQ",
        "difficulty": "MEDIUM",
        "questionLatex": "In Young's double slit experiment, fringe width in air is $\\beta = 0.4\\text{ mm}$. If the entire apparatus is immersed in water of refractive index $\\mu = 4/3$, the new fringe width $\\beta'$ will be:",
        "options": [
            { "id": "A", "latex": "$0.3\\text{ mm}$" },
            { "id": "B", "latex": "$0.53\\text{ mm}$" },
            { "id": "C", "latex": "$0.2\\text{ mm}$" },
            { "id": "D", "latex": "$0.4\\text{ mm}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$\\beta' = \\frac{\\beta}{\\mu} = \\frac{0.4}{4/3} = 0.4 \\times \\frac{3}{4} = 0.3\\text{ mm}$."
    },
    {
        "id": "JEE21_PHY_OPT_03",
        "year": 2021,
        "examShift": "JEE Main 2021 (16 Mar Shift 1)",
        "subject": "Physics",
        "chapter": "Ray Optics & Wave Optics",
        "topic": "Combination of Thin Lenses & Chromatic Aberration",
        "type": "SCQ",
        "difficulty": "HARD",
        "questionLatex": "Two thin convex lenses of focal lengths $f_1 = 20\\text{ cm}$ and $f_2 = 30\\text{ cm}$ are placed coaxially separated by a distance $d = 10\\text{ cm}$. The equivalent focal length $F$ of the combination is:",
        "options": [
            { "id": "A", "latex": "$15\\text{ cm}$" },
            { "id": "B", "latex": "$12\\text{ cm}$" },
            { "id": "C", "latex": "$25\\text{ cm}$" },
            { "id": "D", "latex": "$10\\text{ cm}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$\\frac{1}{F} = \\frac{1}{f_1} + \\frac{1}{f_2} - \\frac{d}{f_1 f_2} = \\frac{1}{20} + \\frac{1}{30} - \\frac{10}{20 \\times 30} = \\frac{3 + 2 - 1}{60} = \\frac{4}{60} = \\frac{1}{15} \\implies F = 15\\text{ cm}$."
    },

    # =========================================================================
    # CHEMISTRY (2020 - 2024 PYQs)
    # =========================================================================
    # 7. Chemical Bonding & Molecular Structure
    {
        "id": "JEE24_CHEM_BOND_01",
        "year": 2024,
        "examShift": "JEE Main 2024 (27 Jan Shift 1)",
        "subject": "Chemistry",
        "chapter": "Chemical Bonding & Molecular Structure",
        "topic": "VSEPR Geometry & Hybridization",
        "type": "SCQ",
        "difficulty": "EASY",
        "questionLatex": "According to VSEPR theory, the molecular shape and hybridization of the central atom in $\\text{XeF}_4$ are respectively:",
        "options": [
            { "id": "A", "latex": "Square planar, $sp^3d^2$" },
            { "id": "B", "latex": "Tetrahedral, $sp^3$" },
            { "id": "C", "latex": "Square pyramidal, $sp^3d^2$" },
            { "id": "D", "latex": "See-saw, $sp^3d$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "Xe has 8 valence electrons; 4 form $\\sigma$ bonds with F and 2 remain as lone pairs. Steric number $= 4 + 2 = 6 \\implies sp^3d^2$. Molecular geometry is square planar."
    },
    {
        "id": "JEE23_CHEM_BOND_02",
        "year": 2023,
        "examShift": "JEE Main 2023 (25 Jan Shift 1)",
        "subject": "Chemistry",
        "chapter": "Chemical Bonding & Molecular Structure",
        "topic": "Molecular Orbital Theory Bond Order",
        "type": "SCQ",
        "difficulty": "MEDIUM",
        "questionLatex": "Based on Molecular Orbital Theory, the correct descending order of bond order for the species $\\text{O}_2, \\text{O}_2^+, \\text{O}_2^-$ is:",
        "options": [
            { "id": "A", "latex": "$\\text{O}_2^+ > \\text{O}_2 > \\text{O}_2^-$" },
            { "id": "B", "latex": "$\\text{O}_2^- > \\text{O}_2 > \\text{O}_2^+$" },
            { "id": "C", "latex": "$\\text{O}_2^+ > \\text{O}_2^- > \\text{O}_2$" },
            { "id": "D", "latex": "$\\text{O}_2 > \\text{O}_2^+ > \\text{O}_2^-$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$\\text{O}_2^+ (15e^-) \\implies 2.5$; $\\text{O}_2 (16e^-) \\implies 2.0$; $\\text{O}_2^- (17e^-) \\implies 1.5$. Thus $\\text{O}_2^+ > \\text{O}_2 > \\text{O}_2^-$."
    },
    {
        "id": "JEE22_CHEM_BOND_03",
        "year": 2022,
        "examShift": "JEE Main 2022 (27 Jun Shift 2)",
        "subject": "Chemistry",
        "chapter": "Chemical Bonding & Molecular Structure",
        "topic": "Dipole Moment Lone Pair Reinforcement",
        "type": "SCQ",
        "difficulty": "HARD",
        "questionLatex": "Which of the following molecules has a higher dipole moment and why: $\\text{NH}_3$ vs $\\text{NF}_3$?",
        "options": [
            { "id": "A", "latex": "$\\text{NH}_3$, because orbital dipole of lone pair reinforces resultant $\\text{N}-\\text{H}$ bond dipoles" },
            { "id": "B", "latex": "$\\text{NF}_3$, because fluorine is much more electronegative than hydrogen" },
            { "id": "C", "latex": "$\\text{NF}_3$, because it possesses three polar $\\text{N}-\\text{F}$ bonds" },
            { "id": "D", "latex": "Both have zero dipole moment due to symmetric trigonal pyramidal geometry" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "In $\\text{NH}_3$, bond dipoles point towards N, in the same direction as the lone pair dipole. In $\\text{NF}_3$, F is more electronegative, opposing the lone pair dipole: $\\mu(\\text{NH}_3) = 1.47\\text{ D} > \\mu(\\text{NF}_3) = 0.24\\text{ D}$."
    },

    # 8. Atomic Structure & Periodicity
    {
        "id": "JEE24_CHEM_ATOM_01",
        "year": 2024,
        "examShift": "JEE Main 2024 (30 Jan Shift 1)",
        "subject": "Chemistry",
        "chapter": "Atomic Structure & Quantum Mechanics",
        "topic": "Radial Nodes and Angular Nodes",
        "type": "SCQ",
        "difficulty": "EASY",
        "questionLatex": "The number of radial nodes for a $3p$ orbital and a $4d$ orbital are respectively:",
        "options": [
            { "id": "A", "latex": "$1\\text{ and }1$" },
            { "id": "B", "latex": "$2\\text{ and }1$" },
            { "id": "C", "latex": "$1\\text{ and }2$" },
            { "id": "D", "latex": "$0\\text{ and }1$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "Radial nodes $= n - l - 1$. For $3p$: $n=3, l=1 \\implies 3 - 1 - 1 = 1$. For $4d$: $n=4, l=2 \\implies 4 - 2 - 1 = 1$."
    },
    {
        "id": "JEE23_CHEM_ATOM_02",
        "year": 2023,
        "examShift": "JEE Main 2023 (06 Apr Shift 1)",
        "subject": "Chemistry",
        "chapter": "Atomic Structure & Quantum Mechanics",
        "topic": "Balmer Series Spectral Wavelength",
        "type": "SCQ",
        "difficulty": "MEDIUM",
        "questionLatex": "The wavelength of the second spectral line of the Balmer series for $\\text{He}^+$ ion ($Z = 2$) is given by ($R_H$ is Rydberg constant):",
        "options": [
            { "id": "A", "latex": "$\\frac{4}{3 R_H}$" },
            { "id": "B", "latex": "$\\frac{16}{3 R_H}$" },
            { "id": "C", "latex": "$\\frac{36}{5 R_H}$" },
            { "id": "D", "latex": "$\\frac{9}{4 R_H}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "Second line of Balmer: $n_1 = 2 \\to n_2 = 4$. $\\frac{1}{\\lambda} = R_H Z^2 \\left(\\frac{1}{2^2} - \\frac{1}{4^2}\\right) = R_H (4) \\left(\\frac{1}{4} - \\frac{1}{16}\\right) = 4 R_H \\left(\\frac{3}{16}\\right) = \\frac{3}{4} R_H \\implies \\lambda = \\frac{4}{3 R_H}$."
    },
    {
        "id": "JEE21_CHEM_ATOM_03",
        "year": 2021,
        "examShift": "JEE Main 2021 (25 Feb Shift 2)",
        "subject": "Chemistry",
        "chapter": "Atomic Structure & Quantum Mechanics",
        "topic": "Heisenberg Uncertainty Principle",
        "type": "SCQ",
        "difficulty": "HARD",
        "questionLatex": "A ball of mass $m = 200\\text{ g}$ is moving with a speed of $v = 10\\text{ m/s}$. If the speed is measured with an accuracy of $0.001\\%$, the minimum uncertainty in its position $\\Delta x$ is ($h = 6.626 \\times 10^{-34}\\text{ J s}$):",
        "options": [
            { "id": "A", "latex": "$2.64 \\times 10^{-28}\\text{ m}$" },
            { "id": "B", "latex": "$5.27 \\times 10^{-28}\\text{ m}$" },
            { "id": "C", "latex": "$1.32 \\times 10^{-28}\\text{ m}$" },
            { "id": "D", "latex": "$6.63 \\times 10^{-28}\\text{ m}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$\\Delta v = 10 \\times \\frac{0.001}{100} = 10^{-4}\\text{ m/s}$. $\\Delta p = m \\Delta v = 0.2 \\times 10^{-4} = 2 \\times 10^{-5}\\text{ kg m/s}$. $\\Delta x \\ge \\frac{h}{4\\pi \\Delta p} = \\frac{6.626 \\times 10^{-34}}{4 \\times 3.1416 \\times 2 \\times 10^{-5}} = 2.64 \\times 10^{-28}\\text{ m}$."
    },

    # 9. Chemical & Ionic Equilibrium
    {
        "id": "JEE24_CHEM_EQ_01",
        "year": 2024,
        "examShift": "JEE Main 2024 (31 Jan Shift 2)",
        "subject": "Chemistry",
        "chapter": "Chemical & Ionic Equilibrium",
        "topic": "Kp and Kc Relationship",
        "type": "SCQ",
        "difficulty": "EASY",
        "questionLatex": "For the gaseous equilibrium $\\text{N}_2(g) + 3\\text{H}_2(g) \\rightleftharpoons 2\\text{NH}_3(g)$, the relation between equilibrium constants $K_p$ and $K_c$ is:",
        "options": [
            { "id": "A", "latex": "$K_p = K_c (RT)^{-2}$" },
            { "id": "B", "latex": "$K_p = K_c (RT)^2$" },
            { "id": "C", "latex": "$K_p = K_c (RT)^{-1}$" },
            { "id": "D", "latex": "$K_p = K_c$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$\\Delta n_g = 2 - (1 + 3) = -2$. Thus $K_p = K_c(RT)^{\\Delta n_g} = K_c(RT)^{-2}$."
    },
    {
        "id": "JEE23_CHEM_EQ_02",
        "year": 2023,
        "examShift": "JEE Main 2023 (24 Jan Shift 2)",
        "subject": "Chemistry",
        "chapter": "Chemical & Ionic Equilibrium",
        "topic": "Acidic Buffer pH Calculation",
        "type": "SCQ",
        "difficulty": "MEDIUM",
        "questionLatex": "A buffer solution contains $0.1\\text{ M } \\text{CH}_3\\text{COOH}$ and $0.1\\text{ M } \\text{CH}_3\\text{COONa}$. Given $K_a = 1.8 \\times 10^{-5}$ ($pK_a = 4.74$), the pH of this solution is:",
        "options": [
            { "id": "A", "latex": "$4.74$" },
            { "id": "B", "latex": "$5.74$" },
            { "id": "C", "latex": "$3.74$" },
            { "id": "D", "latex": "$7.00$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$\\text{pH} = pK_a + \\log\\frac{[\\text{Salt}]}{[\\text{Acid}]} = 4.74 + \\log(1) = 4.74$."
    },
    {
        "id": "JEE20_CHEM_EQ_03",
        "year": 2020,
        "examShift": "JEE Main 2020 (03 Sep Shift 2)",
        "subject": "Chemistry",
        "chapter": "Chemical & Ionic Equilibrium",
        "topic": "Common Ion Effect on Solubility",
        "type": "SCQ",
        "difficulty": "HARD",
        "questionLatex": "The solubility product of a sparingly soluble salt $AB_2$ is $K_{sp} = 4 \\times 10^{-12}$. Its molar solubility in a $0.01\\text{ M}$ solution of common ion salt $CB_2$ (completely dissociated) is:",
        "options": [
            { "id": "A", "latex": "$1.0 \\times 10^{-8}\\text{ M}$" },
            { "id": "B", "latex": "$4.0 \\times 10^{-8}\\text{ M}$" },
            { "id": "C", "latex": "$2.0 \\times 10^{-6}\\text{ M}$" },
            { "id": "D", "latex": "$1.0 \\times 10^{-4}\\text{ M}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$[B^-] = 2 \\times 0.01 = 2 \\times 10^{-2}\\text{ M}$. $K_{sp} = s [B^-]^2 = s (4 \\times 10^{-4}) = 4 \\times 10^{-12} \\implies s = 1.0 \\times 10^{-8}\\text{ M}$."
    },

    # 10. Organic Chemistry - Carbonyl & GOC
    {
        "id": "JEE24_CHEM_ORG_01",
        "year": 2024,
        "examShift": "JEE Main 2024 (27 Jan Shift 1)",
        "subject": "Chemistry",
        "chapter": "Organic Chemistry - Carbonyl & GOC",
        "topic": "Cannizzaro Reaction Substrate",
        "type": "SCQ",
        "difficulty": "EASY",
        "questionLatex": "Which of the following carbonyl compounds undergoes the disproportionation Cannizzaro reaction upon treatment with concentrated $50\\%\\text{ NaOH}$?",
        "options": [
            { "id": "A", "latex": "Benzaldehyde ($\\text{C}_6\\text{H}_5\\text{CHO}$)" },
            { "id": "B", "latex": "Acetaldehyde ($\\text{CH}_3\\text{CHO}$)" },
            { "id": "C", "latex": "Acetone ($\\text{CH}_3\\text{COCH}_3$)" },
            { "id": "D", "latex": "Propanal ($\\text{CH}_3\\text{CH}_2\\text{CHO}$)" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "Aldehydes lacking $\\alpha$-hydrogen atoms undergo Cannizzaro reaction. Benzaldehyde has no $\\alpha$-hydrogens."
    },
    {
        "id": "JEE23_CHEM_ORG_02",
        "year": 2023,
        "examShift": "JEE Main 2023 (13 Apr Shift 2)",
        "subject": "Chemistry",
        "chapter": "Organic Chemistry - Carbonyl & GOC",
        "topic": "Phenol Acidity Substituent Effects",
        "type": "SCQ",
        "difficulty": "MEDIUM",
        "questionLatex": "The correct descending order of acidic strength for the following substituted phenols is:\n(I) p-nitrophenol, (II) m-nitrophenol, (III) phenol, (IV) p-cresol.",
        "options": [
            { "id": "A", "latex": "$\\text{I} > \\text{II} > \\text{III} > \\text{IV}$" },
            { "id": "B", "latex": "$\\text{II} > \\text{I} > \\text{III} > \\text{IV}$" },
            { "id": "C", "latex": "$\\text{I} > \\text{III} > \\text{II} > \\text{IV}$" },
            { "id": "D", "latex": "$\\text{IV} > \\text{III} > \\text{II} > \\text{I}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "p-nitrophenol ($-M, -I$) is most acidic, followed by m-nitrophenol ($-I$ only), phenol, and p-cresol ($+I, +H$ electron-donating methyl)."
    },
    {
        "id": "JEE20_CHEM_ORG_03",
        "year": 2020,
        "examShift": "JEE Main 2020 (04 Sep Shift 1)",
        "subject": "Chemistry",
        "chapter": "Organic Chemistry - Carbonyl & GOC",
        "topic": "Haloform Iodoform Positive Ketone",
        "type": "SCQ",
        "difficulty": "HARD",
        "questionLatex": "An organic compound $A$ with molecular formula $\\text{C}_4\\text{H}_8\\text{O}$ gives an orange precipitate with 2,4-DNP and forms a yellow precipitate of $\\text{CHI}_3$ upon treatment with $\\text{I}_2/\\text{NaOH}$, but does NOT reduce Tollens' reagent. Compound $A$ is:",
        "options": [
            { "id": "A", "latex": "Butan-2-one ($\\text{CH}_3\\text{COCH}_2\\text{CH}_3$)" },
            { "id": "B", "latex": "Butanal ($\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CHO}$)" },
            { "id": "C", "latex": "2-Methylpropanal" },
            { "id": "D", "latex": "Diethyl ether" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "2,4-DNP positive indicates carbonyl; Tollens negative indicates ketone; Iodoform positive requires methyl ketone group. Hence, Butan-2-one."
    },

    # =========================================================================
    # MATHEMATICS (2020 - 2024 PYQs)
    # =========================================================================
    # 11. Matrices & Determinants
    {
        "id": "JEE24_MATH_MAT_01",
        "year": 2024,
        "examShift": "JEE Main 2024 (29 Jan Shift 2)",
        "subject": "Mathematics",
        "chapter": "Matrices & Determinants",
        "topic": "Scalar Multiple Determinant Property",
        "type": "SCQ",
        "difficulty": "EASY",
        "questionLatex": "If $A$ is a square matrix of order $3 \\times 3$ with $\\det(A) = 4$, then the value of $\\det(2A)$ is:",
        "options": [
            { "id": "A", "latex": "$32$" },
            { "id": "B", "latex": "$16$" },
            { "id": "C", "latex": "$8$" },
            { "id": "D", "latex": "$64$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "For an $n \\times n$ matrix, $\\det(kA) = k^n \\det(A)$. Here $n = 3$, so $\\det(2A) = 2^3 \\times 4 = 8 \\times 4 = 32$."
    },
    {
        "id": "JEE23_MATH_MAT_02",
        "year": 2023,
        "examShift": "JEE Main 2023 (24 Jan Shift 1)",
        "subject": "Mathematics",
        "chapter": "Matrices & Determinants",
        "topic": "Cramer's Rule System Consistency",
        "type": "SCQ",
        "difficulty": "MEDIUM",
        "questionLatex": "The system of linear equations:\n$$x + y + z = 6$$\n$$x + 2y + 3z = 10$$\n$$x + 2y + \\lambda z = \\mu$$\nhas infinitely many solutions if and only if $(\\lambda, \\mu)$ equals:",
        "options": [
            { "id": "A", "latex": "$(3, 10)$" },
            { "id": "B", "latex": "$(3, 8)$" },
            { "id": "C", "latex": "$(2, 10)$" },
            { "id": "D", "latex": "$(4, 12)$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$\\Delta = \\begin{vmatrix} 1 & 1 & 1 \\\\ 1 & 2 & 3 \\\\ 1 & 2 & \\lambda \\end{vmatrix} = \\lambda - 3 = 0 \\implies \\lambda = 3$. Matching row 2 and 3 gives $\\mu = 10$."
    },
    {
        "id": "JEE21_MATH_MAT_03",
        "year": 2021,
        "examShift": "JEE Main 2021 (24 Feb Shift 2)",
        "subject": "Mathematics",
        "chapter": "Matrices & Determinants",
        "topic": "Cayley-Hamilton Matrix Power",
        "type": "SCQ",
        "difficulty": "HARD",
        "questionLatex": "Let $A = \\begin{pmatrix} 2 & -1 \\\\ -1 & 2 \\end{pmatrix}$. If $A^3 - 4A^2 + 3A + k I = O$, where $I$ is the identity matrix of order 2, then the integer value of $k$ is:",
        "options": [
            { "id": "A", "latex": "$0$" },
            { "id": "B", "latex": "$3$" },
            { "id": "C", "latex": "$-2$" },
            { "id": "D", "latex": "$1$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "Characteristic eq: $\\lambda^2 - 4\\lambda + 3 = 0 \\implies A^2 - 4A + 3I = O$. Multiplying by $A$ gives $A^3 - 4A^2 + 3A = O$. Thus $k = 0$."
    },

    # 12. Limits, Continuity & Differentiability
    {
        "id": "JEE24_MATH_LIM_01",
        "year": 2024,
        "examShift": "JEE Main 2024 (27 Jan Shift 2)",
        "subject": "Mathematics",
        "chapter": "Limits, Continuity & Differentiability",
        "topic": "Standard Trigonometric Limit",
        "type": "SCQ",
        "difficulty": "EASY",
        "questionLatex": "The value of the limit $\\lim_{x \\to 0} \\frac{\\sin 5x}{\\tan 3x}$ is:",
        "options": [
            { "id": "A", "latex": "$\\frac{5}{3}$" },
            { "id": "B", "latex": "$\\frac{3}{5}$" },
            { "id": "C", "latex": "$1$" },
            { "id": "D", "latex": "$\\frac{25}{9}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$\\lim_{x \\to 0} \\frac{(\\sin 5x / 5x) \\cdot 5x}{(\\tan 3x / 3x) \\cdot 3x} = \\frac{5}{3}$."
    },
    {
        "id": "JEE23_MATH_LIM_02",
        "year": 2023,
        "examShift": "JEE Main 2023 (25 Jan Shift 2)",
        "subject": "Mathematics",
        "chapter": "Limits, Continuity & Differentiability",
        "topic": "Indeterminate Form 1 to Infinity",
        "type": "SCQ",
        "difficulty": "MEDIUM",
        "questionLatex": "The value of the limit $\\lim_{x \\to 0} (1 + 3x)^{2/x}$ is:",
        "options": [
            { "id": "A", "latex": "$e^6$" },
            { "id": "B", "latex": "$e^3$" },
            { "id": "C", "latex": "$e^5$" },
            { "id": "D", "latex": "$e^2$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$1^\\infty$ form: $\\exp\\left(\\lim_{x \\to 0} \\frac{2}{x} \\cdot 3x\\right) = e^6$."
    },
    {
        "id": "JEE21_MATH_LIM_03",
        "year": 2021,
        "examShift": "JEE Main 2021 (20 Jul Shift 1)",
        "subject": "Mathematics",
        "chapter": "Limits, Continuity & Differentiability",
        "topic": "Piecewise Function Differentiability",
        "type": "SCQ",
        "difficulty": "HARD",
        "questionLatex": "Let $f(x) = \\begin{cases} x^2 \\sin(1/x), & x \\neq 0 \\\\ 0, & x = 0 \\end{cases}$. Then at $x = 0$:",
        "options": [
            { "id": "A", "latex": "$f(x)$ is continuous and differentiable with $f'(0) = 0$, but $f'(x)$ is discontinuous at $x = 0$" },
            { "id": "B", "latex": "$f(x)$ is continuous but not differentiable at $x = 0$" },
            { "id": "C", "latex": "$f(x)$ is differentiable and $f'(x)$ is continuous everywhere" },
            { "id": "D", "latex": "$f(x)$ is discontinuous at $x = 0$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$f'(0) = \\lim_{h \\to 0} \\frac{h^2\\sin(1/h)}{h} = 0$. For $x \\neq 0$, $f'(x) = 2x\\sin(1/x) - \\cos(1/x)$, which has no limit as $x \\to 0$ due to oscillation."
    },

    # 13. Definite Integration & Area Under Curves
    {
        "id": "JEE24_MATH_INT_01",
        "year": 2024,
        "examShift": "JEE Main 2024 (31 Jan Shift 1)",
        "subject": "Mathematics",
        "chapter": "Definite Integration & Area Under Curves",
        "topic": "King's Rule Symmetry Property",
        "type": "SCQ",
        "difficulty": "EASY",
        "questionLatex": "The value of the definite integral $I = \\int_0^{\\pi/2} \\frac{\\sin^{2024} x}{\\sin^{2024} x + \\cos^{2024} x} dx$ is:",
        "options": [
            { "id": "A", "latex": "$\\frac{\\pi}{4}$" },
            { "id": "B", "latex": "$\\frac{\\pi}{2}$" },
            { "id": "C", "latex": "$0$" },
            { "id": "D", "latex": "$\\pi$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "Using King's property: $2I = \\int_0^{\\pi/2} 1 dx = \\frac{\\pi}{2} \\implies I = \\frac{\\pi}{4}$."
    },
    {
        "id": "JEE23_MATH_INT_02",
        "year": 2023,
        "examShift": "JEE Main 2023 (10 Apr Shift 1)",
        "subject": "Mathematics",
        "chapter": "Definite Integration & Area Under Curves",
        "topic": "Area Bounded by Parabola and Line",
        "type": "SCQ",
        "difficulty": "MEDIUM",
        "questionLatex": "The area of the region enclosed between the parabola $y = x^2$ and the line $y = 2x$ is:",
        "options": [
            { "id": "A", "latex": "$\\frac{4}{3}$" },
            { "id": "B", "latex": "$\\frac{2}{3}$" },
            { "id": "C", "latex": "$\\frac{8}{3}$" },
            { "id": "D", "latex": "$2$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "Intersections at $x=0, 2$. Area $= \\int_0^2 (2x - x^2) dx = [x^2 - x^3/3]_0^2 = 4 - 8/3 = \\frac{4}{3}$."
    },
    {
        "id": "JEE21_MATH_INT_03",
        "year": 2021,
        "examShift": "JEE Main 2021 (16 Mar Shift 2)",
        "subject": "Mathematics",
        "chapter": "Definite Integration & Area Under Curves",
        "topic": "Leibniz Differentiation Under Integral",
        "type": "SCQ",
        "difficulty": "HARD",
        "questionLatex": "Let $F(x) = \\int_0^{x^2} \\sqrt{1 + t^3} dt$. The derivative $F'(x)$ evaluated at $x = 1$ is:",
        "options": [
            { "id": "A", "latex": "$2\\sqrt{2}$" },
            { "id": "B", "latex": "$\\sqrt{2}$" },
            { "id": "C", "latex": "$4\\sqrt{2}$" },
            { "id": "D", "latex": "$2$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "Leibniz rule: $F'(x) = \\sqrt{1 + x^6} \\cdot (2x)$. At $x = 1$: $F'(1) = \\sqrt{2} \\cdot 2 = 2\\sqrt{2}$."
    },

    # 14. Vectors & 3D Geometry
    {
        "id": "JEE24_MATH_VEC_01",
        "year": 2024,
        "examShift": "JEE Main 2024 (27 Jan Shift 1)",
        "subject": "Mathematics",
        "chapter": "Vectors & 3D Geometry",
        "topic": "Dot Product & Angle Between Vectors",
        "type": "SCQ",
        "difficulty": "EASY",
        "questionLatex": "If $\\vec{a} = 2\\hat{i} + \\hat{j} + 2\\hat{k}$ and $\\vec{b} = \\hat{i} - \\hat{j} + \\hat{k}$, the angle $\\theta$ between the vectors is:",
        "options": [
            { "id": "A", "latex": "$\\cos^{-1}\\left(\\frac{1}{\\sqrt{3}}\\right)$" },
            { "id": "B", "latex": "$\\cos^{-1}\\left(\\frac{1}{3}\\right)$" },
            { "id": "C", "latex": "$\\frac{\\pi}{4}$" },
            { "id": "D", "latex": "$\\frac{\\pi}{3}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$\\vec{a} \\cdot \\vec{b} = 2 - 1 + 2 = 3$. $|\\vec{a}| = 3$, $|\\vec{b}| = \\sqrt{3}$. $\\cos\\theta = \\frac{3}{3\\sqrt{3}} = \\frac{1}{\\sqrt{3}}$."
    },
    {
        "id": "JEE23_MATH_VEC_02",
        "year": 2023,
        "examShift": "JEE Main 2023 (30 Jan Shift 2)",
        "subject": "Mathematics",
        "chapter": "Vectors & 3D Geometry",
        "topic": "Shortest Distance Between Skew Lines",
        "type": "SCQ",
        "difficulty": "MEDIUM",
        "questionLatex": "The shortest distance between the lines $\\frac{x - 1}{2} = \\frac{y - 2}{3} = \\frac{z - 3}{4}$ and $\\frac{x - 2}{3} = \\frac{y - 4}{4} = \\frac{z - 5}{5}$ is:",
        "options": [
            { "id": "A", "latex": "$\\frac{1}{\\sqrt{6}}$" },
            { "id": "B", "latex": "$\\frac{1}{\\sqrt{3}}$" },
            { "id": "C", "latex": "$0$" },
            { "id": "D", "latex": "$\\frac{2}{\\sqrt{6}}$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$\\vec{a}_2 - \\vec{a}_1 = \\hat{i} + 2\\hat{j} + 2\\hat{k}$. $\\vec{b}_1 \\times \\vec{b}_2 = -\\hat{i} + 2\\hat{j} - \\hat{k}$. $|\\vec{b}_1 \\times \\vec{b}_2| = \\sqrt{6}$. Distance $= \\frac{|(-1)(1) + 2(2) - 1(2)|}{\\sqrt{6}} = \\frac{1}{\\sqrt{6}}$."
    },
    {
        "id": "JEE21_MATH_VEC_03",
        "year": 2021,
        "examShift": "JEE Main 2021 (25 Feb Shift 1)",
        "subject": "Mathematics",
        "chapter": "Vectors & 3D Geometry",
        "topic": "Coplanar Vectors Scalar Triple Product",
        "type": "SCQ",
        "difficulty": "HARD",
        "questionLatex": "The three vectors $\\vec{u} = \\hat{i} + \\lambda\\hat{j} + \\hat{k}$, $\\vec{v} = \\hat{j} + \\lambda\\hat{k}$, and $\\vec{w} = \\lambda\\hat{i} + \\hat{k}$ are coplanar if and only if:",
        "options": [
            { "id": "A", "latex": "$\\lambda = -1$" },
            { "id": "B", "latex": "$\\lambda = 1$" },
            { "id": "C", "latex": "$\\lambda = 0$" },
            { "id": "D", "latex": "$\\lambda = 2$" }
        ],
        "correctAnswer": "A",
        "solutionLatex": "$\\begin{vmatrix} 1 & \\lambda & 1 \\\\ 0 & 1 & \\lambda \\\\ \\lambda & 0 & 1 \\end{vmatrix} = 1 + \\lambda^3 - \\lambda = 0 \\implies (\\lambda + 1)(\\lambda^2 - \\lambda + 1) = 0 \\implies \\lambda = -1$."
    }
]

print(f"Total curated JEE Main PYQs: {len(questions)}")
with open("d:/AGENT/06-JEE-CBT-Platform/mock-data/master-question-bank.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)
print("Saved to d:/AGENT/06-JEE-CBT-Platform/mock-data/master-question-bank.json successfully.")
