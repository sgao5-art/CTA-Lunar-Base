
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# ==================================================
# NASA 2040 - CTA Lunar Base Management System
# ==================================================

st.set_page_config(
    page_title="Lunar Base Management System",
    page_icon="🌕",
    layout="wide"
)

# -------------------- UI Design --------------------

st.markdown("""
<style>
    .stApp {
        background-color: #080f1e;
        color: #e2e8f0;
    }

    [data-testid="stSidebar"] {
        background-color: #111c30;
    }

    [data-testid="stMetric"] {
        background-color: #142238;
        border: 1px solid #2c4563;
        padding: 18px;
        border-radius: 12px;
    }

    [data-testid="stMetricValue"] {
        color: #60d5fa;
    }

    h1, h2, h3 {
        color: #e2e8f0;
    }

    .stButton > button {
        background-color: #1d4ed8;
        color: white;
        border: none;
        border-radius: 8px;
        width: 100%;
    }

    .mission-header {
        background: linear-gradient(120deg, #142238, #203d60);
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #345578;
        margin-bottom: 25px;
    }

    .mission-header h1 {
        color: #7dd3fc;
        margin: 0;
    }

    .mission-header p {
        color: #b0c4de;
    }
</style>
""", unsafe_allow_html=True)

# -------------------- Session State --------------------

defaults = {
    "battery": 86,
    "temperature": 22.4,
    "oxygen": 21.0,
    "pressure": 101.3,
    "cargo_status": "Awaiting Inspection",
    "cargo_risk": "Unknown",
    "robot_status": "Standby",
    "decision": "Pending Human Review",
    "logs": []
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def add_log(action):
    st.session_state.logs.append({
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Action": action
    })


# -------------------- Sidebar --------------------

with st.sidebar:

    st.title("🌕 LUNAR COMMAND")

    st.caption("NASA 2040 | CTA Prototype")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "⚡ Energy Management",
            "🌡️ Environmental Monitoring",
            "📦 Cargo Inspection",
            "🤖 Robotics Management",
            "🛡️ CTA & Risk Assessment"
        ]
    )

    st.divider()

    st.success("Communication Online")

    st.write("Mission: Lunar Base 2040")
    st.write("Location: Lunar South Pole")
    st.write("Crew: 12 Members")
    st.write("Mode: Human-AI Collaboration")

    st.caption("Educational simulation — not an official NASA system")


# ==================================================
# 1. DASHBOARD
# ==================================================

if page == "🏠 Dashboard":

    st.markdown("""
    <div class="mission-header">
        <h1>LUNAR BASE MANAGEMENT SYSTEM</h1>
        <p>NASA 2040 | Critical Technology Assessment</p>
        <p>Integrated Human-AI Mission Control Center</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Mission Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Battery Level", f"{st.session_state.battery}%")
    c2.metric("Temperature", f"{st.session_state.temperature} °C")
    c3.metric("Oxygen Level", f"{st.session_state.oxygen}%")
    c4.metric("Air Pressure", f"{st.session_state.pressure} kPa")

    st.divider()

    left, right = st.columns(2)

    with left:

        st.subheader("Power Consumption")

        hours = np.arange(24)

        power = 45 + 8 * np.sin(hours * np.pi / 12)

        data = pd.DataFrame({
            "Hour": hours,
            "Power (kW)": power
        }).set_index("Hour")

        st.line_chart(data)

    with right:

        st.subheader("Subsystem Status")

        st.success("Energy System: Operational")
        st.success("Life Support: Operational")
        st.success("Communication: Connected")

        st.info(
            "Cargo System: " +
            st.session_state.cargo_status
        )

        st.info(
            "Robotics: " +
            st.session_state.robot_status
        )

    st.divider()

    st.subheader("Mission Alerts")

    if st.session_state.cargo_risk == "High":
        st.error(
            "Potential cargo contamination detected. "
            "Human authorization is required."
        )
    else:
        st.info(
            "No high-risk cargo alert is currently active."
        )

    if st.session_state.battery < 30:
        st.warning("Low battery level. Energy review required.")

    st.subheader("Mission Objective")

    st.write(
        "This prototype demonstrates how future lunar "
        "engineers may monitor infrastructure, manage "
        "resources, supervise autonomous systems, and "
        "evaluate technological risks in 2040."
    )


# ==================================================
# 2. ENERGY MANAGEMENT
# ==================================================

elif page == "⚡ Energy Management":

    st.title("⚡ Energy Management")

    st.caption("Solar generation, battery storage and power allocation")

    c1, c2, c3 = st.columns(3)

    c1.metric("Solar Generation", "72 kW")
    c2.metric("Power Demand", "48 kW")
    c3.metric("Battery Level", f"{st.session_state.battery}%")

    st.progress(st.session_state.battery / 100)

    st.subheader("Simulate Battery Conditions")

    battery = st.slider(
        "Battery State of Charge (%)",
        0, 100,
        st.session_state.battery
    )

    st.session_state.battery = battery

    if battery < 30:
        st.error(
            "Critical energy shortage. "
            "Human intervention required."
        )
    elif battery < 60:
        st.warning("Moderate energy reserves.")
    else:
        st.success("Energy reserves are sufficient.")

    st.divider()

    st.subheader("Power Distribution")

    life = st.slider("Life Support (kW)", 20, 40, 25)
    research = st.slider("Research Laboratory (kW)", 0, 20, 10)
    robotics = st.slider("Robotics (kW)", 0, 20, 8)
    communication = st.slider("Communication (kW)", 2, 10, 5)

    total = life + research + robotics + communication

    distribution = pd.DataFrame({
        "Subsystem": [
            "Life Support",
            "Research",
            "Robotics",
            "Communication"
        ],
        "Power (kW)": [
            life, research, robotics, communication
        ]
    }).set_index("Subsystem")

    st.bar_chart(distribution)

    st.metric("Total Allocated Power", f"{total} kW")

    if total > 72:
        st.error("Power allocation exceeds solar generation.")
    else:
        st.success("Power allocation is within generation capacity.")

    if st.button("Confirm Power Allocation"):

        if total <= 72:
            add_log(f"Human approved power allocation: {total} kW")
            st.success("Power allocation approved.")
        else:
            st.error("Approval blocked by simulated safety limits.")


# ==================================================
# 3. ENVIRONMENTAL MONITORING
# ==================================================

elif page == "🌡️ Environmental Monitoring":

    st.title("🌡️ Environmental Monitoring")

    st.caption("Habitat and crew safety monitoring")

    st.subheader("Simulated Sensor Controls")

    st.session_state.temperature = st.slider(
        "Habitat Temperature (°C)",
        0.0, 50.0,
        float(st.session_state.temperature)
    )

    st.session_state.oxygen = st.slider(
        "Oxygen Concentration (%)",
        10.0, 30.0,
        float(st.session_state.oxygen)
    )

    st.session_state.pressure = st.slider(
        "Air Pressure (kPa)",
        50.0, 120.0,
        float(st.session_state.pressure)
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Temperature",
        f"{st.session_state.temperature:.1f} °C"
    )

    c2.metric(
        "Oxygen",
        f"{st.session_state.oxygen:.1f}%"
    )

    c3.metric(
        "Air Pressure",
        f"{st.session_state.pressure:.1f} kPa"
    )

    st.divider()

    st.subheader("AI Environmental Assessment")

    alerts = []

    if not 18 <= st.session_state.temperature <= 26:
        alerts.append("Abnormal habitat temperature.")

    if not 19.5 <= st.session_state.oxygen <= 23.5:
        alerts.append("Abnormal oxygen concentration.")

    if not 90 <= st.session_state.pressure <= 105:
        alerts.append("Abnormal habitat pressure.")

    if alerts:
        for alert in alerts:
            st.error(alert)

        st.warning("Engineering review is required.")

        if st.button("Request Human Inspection"):
            add_log("Environmental inspection requested")
            st.success("Inspection request recorded.")

    else:
        st.success("All simulated environmental parameters are normal.")

    st.caption(
        "Thresholds are illustrative prototype values, "
        "not certified lunar habitat safety standards."
    )


# ==================================================
# 4. CARGO INSPECTION
# ==================================================

elif page == "📦 Cargo Inspection":

    st.title("📦 Lunar Cargo Inspection Station")

    st.caption("AI-assisted cargo screening with human authorization")

    cargo_id = st.text_input(
        "Cargo Identification",
        "LUNAR-CARGO-001"
    )

    cargo_type = st.selectbox(
        "Cargo Type",
        [
            "Food and Water",
            "Electronic Equipment",
            "Scientific Instruments",
            "Construction Materials",
            "Medical Supplies"
        ]
    )

    weight = st.number_input(
        "Cargo Weight (kg)",
        min_value=0.0,
        value=25.0
    )

    contamination = st.checkbox(
        "Simulate Contamination Detection"
    )

    damaged = st.checkbox(
        "Simulate Structural Damage"
    )

    if st.button("Start AI Inspection"):

        with st.spinner("Analyzing simulated cargo data..."):

            if contamination or damaged:
                st.session_state.cargo_risk = "High"
                st.session_state.cargo_status = "Quarantined"
            else:
                st.session_state.cargo_risk = "Low"
                st.session_state.cargo_status = "Awaiting Approval"

            st.session_state.decision = "Pending Human Review"

            add_log(
                f"Cargo {cargo_id} inspected: "
                f"{st.session_state.cargo_risk} risk"
            )

    st.divider()

    st.subheader("AI Inspection Result")

    st.metric("Risk Level", st.session_state.cargo_risk)

    st.write(
        "Cargo Status:",
        st.session_state.cargo_status
    )

    if st.session_state.cargo_risk == "High":

        st.error(
            "AI detected a possible safety hazard. "
            "Cargo has been placed in simulated quarantine."
        )

        st.write("AI Recommendation: Reject or investigate further.")

    elif st.session_state.cargo_risk == "Low":

        st.success("No simulated hazard detected.")

        st.write("AI Recommendation: Approve cargo.")

    else:

        st.info("Start an inspection to generate an assessment.")

    st.divider()

    st.subheader("Human Decision")

    st.warning(
        "AI recommendations do not replace engineering judgment."
    )

    reason = st.text_area(
        "Engineer Decision / Justification"
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        if st.button("Approve Cargo"):

            if st.session_state.cargo_risk == "Unknown":
                st.error("Inspection required before approval.")

            elif st.session_state.cargo_risk == "High":
                st.error("High-risk cargo requires further investigation.")

            elif not reason.strip():
                st.warning("Please enter a justification.")

            else:
                st.session_state.cargo_status = "Approved"
                st.session_state.decision = "Approved by Engineer"

                add_log(f"Cargo approved: {reason}")

                st.success("Cargo approved.")

    with c2:

        if st.button("Reject Cargo"):

            if reason.strip():
                st.session_state.cargo_status = "Rejected"
                st.session_state.decision = "Rejected by Engineer"

                add_log(f"Cargo rejected: {reason}")

                st.success("Cargo rejected.")
            else:
                st.warning("Please enter a justification.")

    with c3:

        if st.button("Request Reinspection"):

            st.session_state.cargo_status = "Reinspection Required"
            st.session_state.decision = "Further Investigation"

            add_log("Cargo reinspection requested")

            st.info("Reinspection requested.")

    st.write(
        "Current Decision:",
        st.session_state.decision
    )


# ==================================================
# 5. ROBOTICS MANAGEMENT
# ==================================================

elif page == "🤖 Robotics Management":

    st.title("🤖 Robotics Management")

    robots = pd.DataFrame({
        "Robot ID": ["ROVER-01", "ROVER-02", "ARM-01", "DRONE-01"],
        "Mission": [
            "Surface Exploration",
            "Cargo Transportation",
            "Equipment Maintenance",
            "Indoor Inspection"
        ],
        "Battery": ["84%", "72%", "95%", "63%"],
        "Status": [
            "Operational",
            "Standby",
            "Operational",
            "Charging"
        ]
    })

    st.dataframe(robots, use_container_width=True, hide_index=True)

    st.divider()

    st.subheader("Robot Control Panel")

    selected_robot = st.selectbox(
        "Select Robot",
        robots["Robot ID"].tolist()
    )

    mode = st.radio(
        "Control Mode",
        [
            "Autonomous Operation",
            "Human Supervised Operation",
            "Manual Control"
        ]
    )

    mission = st.selectbox(
        "Assign Mission",
        [
            "Inspect Equipment",
            "Transport Cargo",
            "Explore Surface",
            "Return to Base"
        ]
    )

    if st.button("Authorize Mission"):

        st.session_state.robot_status = "Mission Authorized"

        add_log(
            f"{selected_robot}: {mission} — {mode}"
        )

        st.success(f"Mission authorized for {selected_robot}.")

    if st.button("Emergency Stop"):

        st.session_state.robot_status = "Emergency Stop"

        add_log(f"Emergency stop activated for {selected_robot}")

        st.error("Simulated emergency stop activated.")

    st.write("Current Control Status:", st.session_state.robot_status)

    st.info(
        "Human operators retain the authority to supervise "
        "and interrupt autonomous robotic operations."
    )


# ==================================================
# 6. CTA AND RISK ASSESSMENT
# ==================================================

elif page == "🛡️ CTA & Risk Assessment":

    st.title("🛡️ Critical Technology Assessment")

    st.caption("Evaluating technology, uncertainty and human responsibility")

    st.subheader("Technology Risk Register")

    risks = pd.DataFrame({
        "Technology": [
            "Artificial Intelligence",
            "Autonomous Robotics",
            "Solar Power Systems",
            "Life Support Systems",
            "Communication Systems"
        ],
        "Potential Risk": [
            "Incorrect automated decisions",
            "Loss of human control",
            "Energy supply interruption",
            "Sensor or equipment failure",
            "Communication delays"
        ],
        "Mitigation": [
            "Human verification",
            "Manual override",
            "Energy storage and redundancy",
            "Independent safety monitoring",
            "Local decision-making authority"
        ]
    })

    st.dataframe(risks, use_container_width=True, hide_index=True)

    st.divider()

    st.subheader("Interactive Risk Assessment")

    technology = st.selectbox(
        "Technology",
        [
            "Artificial Intelligence",
            "Autonomous Robotics",
            "Energy Infrastructure",
            "Life Support",
            "Cargo Inspection"
        ]
    )

    likelihood = st.slider(
        "Likelihood of Failure",
        1, 5, 3
    )

    severity = st.slider(
        "Severity of Consequences",
        1, 5, 4
    )

    risk_score = likelihood * severity

    st.metric("Risk Score", f"{risk_score} / 25")

    if risk_score >= 15:
        st.error("High Risk — Human intervention required.")

    elif risk_score >= 6:
        st.warning("Moderate Risk — Additional monitoring required.")

    else:
        st.success("Low Risk — Continue monitoring.")

    assessment = st.text_area(
        "Engineer Assessment and Mitigation Strategy"
    )

    if st.button("Record Risk Assessment"):

        if assessment.strip():

            add_log(
                f"CTA assessment: {technology}, "
                f"Score {risk_score}, {assessment}"
            )

            st.success("Risk assessment recorded.")

        else:
            st.warning("Please enter an assessment.")

    st.divider()

    st.subheader("Human Responsibilities in 2040")

    st.markdown("""
    - Maintain meaningful human oversight.
    - Evaluate the reliability of automated decisions.
    - Recognize technological uncertainty.
    - Protect astronaut safety.
    - Ensure accountability and transparency.
    - Balance technological efficiency with ethical responsibility.
    """)

    st.divider()

    st.subheader("Decision and Activity Log")

    if st.session_state.logs:

        log_data = pd.DataFrame(st.session_state.logs)

        st.dataframe(
            log_data,
            use_container_width=True,
            hide_index=True
        )

        st.download_button(
            "Download Activity Report",
            log_data.to_csv(index=False),
            file_name="CTA_Mission_Report.csv",
            mime="text/csv"
        )

    else:

        st.info("No engineering decisions have been recorded.")


# -------------------- Footer --------------------

st.divider()

st.caption(
    "NASA 2040 Lunar Base Management System | "
    "Critical Technology Assessment Artifact | "
    "Educational Concept Prototype"
)
