# import streamlit as st
# from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

# st.set_page_config(
#     page_title="Nexus Research",
#     page_icon="◈",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# # ── Design System ──────────────────────────────────────────────────────────────
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,600;1,9..144,300;1,9..144,400&family=Geist+Mono:wght@300;400;500&family=Instrument+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap');

# :root {
#     --bg:         #080910;
#     --bg-1:       #0d0e18;
#     --bg-2:       #12131e;
#     --bg-3:       #191b28;
#     --border:     #1c1e2e;
#     --border-hi:  #282b40;
#     --text-1:     #eceaf5;
#     --text-2:     #9896b2;
#     --text-3:     #52516a;
#     --accent:     #6966ff;
#     --accent-dim: rgba(105,102,255,0.1);
#     --amber:      #f5a623;
#     --amber-dim:  rgba(245,166,35,0.08);
#     --green:      #34d399;
#     --green-dim:  rgba(52,211,153,0.07);
#     --r-sm: 6px; --r-md: 10px; --r-lg: 16px;
#     --ff-display: 'Fraunces', Georgia, serif;
#     --ff-body:    'Instrument Sans', 'Helvetica Neue', sans-serif;
#     --ff-mono:    'Geist Mono', 'Fira Code', Menlo, monospace;
# }

# *, *::before, *::after { box-sizing: border-box; }

# /* ── App shell ── */
# html, body,
# [data-testid="stAppViewContainer"],
# [data-testid="stMain"],
# .main, .block-container,
# section[data-testid="stSidebar"],
# [data-testid="stHeader"] {
#     background: var(--bg) !important;
#     color: var(--text-2) !important;
# }
# #MainMenu, footer, header,
# [data-testid="stToolbar"],
# [data-testid="stDecoration"],
# [data-testid="stStatusWidget"] { display: none !important; }

# .block-container {
#     max-width: 820px !important;
#     padding: 4rem 2rem 7rem !important;
#     margin: 0 auto !important;
# }

# /* ── Base typography ── */
# p, li, span, div { font-family: var(--ff-body) !important; }

# /* ════════════ HERO ════════════ */
# .nx-eyebrow {
#     font-family: var(--ff-mono) !important;
#     font-size: 0.68rem;
#     letter-spacing: 0.24em;
#     text-transform: uppercase;
#     color: var(--accent);
#     display: flex;
#     align-items: center;
#     gap: 0.7rem;
#     margin-bottom: 1.2rem;
# }
# .nx-eyebrow::before {
#     content: '';
#     width: 20px; height: 1px;
#     background: var(--accent);
#     display: inline-block;
#     flex-shrink: 0;
# }

# .nx-h1 {
#     font-family: var(--ff-display) !important;
#     font-weight: 300;
#     font-size: clamp(2.6rem, 5.5vw, 4rem);
#     line-height: 1.1;
#     letter-spacing: -0.03em;
#     color: var(--text-1) !important;
#     margin: 0 0 0.6rem;
# }
# .nx-h1 em {
#     font-style: italic;
#     color: var(--text-3);
# }

# .nx-tagline {
#     font-family: var(--ff-body) !important;
#     font-size: 0.97rem;
#     font-weight: 400;
#     color: var(--text-3);
#     line-height: 1.65;
#     margin: 0.5rem 0 3rem;
#     max-width: 430px;
# }

# /* ════════════ RULE ════════════ */
# .nx-rule {
#     height: 1px;
#     background: linear-gradient(to right, var(--border-hi), transparent);
#     border: none;
#     margin: 1.8rem 0;
# }

# /* ════════════ INPUT ════════════ */
# [data-testid="stTextInput"] label {
#     font-family: var(--ff-mono) !important;
#     font-size: 0.66rem !important;
#     letter-spacing: 0.2em !important;
#     text-transform: uppercase !important;
#     color: var(--text-3) !important;
#     margin-bottom: 0.45rem !important;
#     display: block;
# }
# [data-testid="stTextInput"] input {
#     background: var(--bg-1) !important;
#     border: 1px solid var(--border-hi) !important;
#     border-radius: var(--r-md) !important;
#     color: var(--text-1) !important;
#     font-family: var(--ff-body) !important;
#     font-size: 0.97rem !important;
#     height: 50px !important;
#     padding: 0 1.1rem !important;
#     transition: border-color 0.18s, box-shadow 0.18s !important;
#     caret-color: var(--accent);
# }
# [data-testid="stTextInput"] input::placeholder {
#     color: var(--text-3) !important;
#     font-style: italic;
# }
# [data-testid="stTextInput"] input:focus {
#     border-color: var(--accent) !important;
#     box-shadow: 0 0 0 3px var(--accent-dim) !important;
#     outline: none !important;
# }

# /* ════════════ BUTTON ════════════ */
# [data-testid="stButton"] > button {
#     background: var(--accent) !important;
#     color: #fff !important;
#     border: none !important;
#     border-radius: var(--r-md) !important;
#     font-family: var(--ff-body) !important;
#     font-size: 0.88rem !important;
#     font-weight: 600 !important;
#     letter-spacing: 0.02em !important;
#     height: 50px !important;
#     padding: 0 1.4rem !important;
#     box-shadow: 0 2px 20px rgba(105,102,255,0.28) !important;
#     transition: opacity 0.14s, transform 0.12s, box-shadow 0.14s !important;
#     white-space: nowrap !important;
# }
# [data-testid="stButton"] > button:hover {
#     opacity: 0.88 !important;
#     transform: translateY(-1px) !important;
#     box-shadow: 0 6px 28px rgba(105,102,255,0.38) !important;
# }
# [data-testid="stButton"] > button:active {
#     transform: none !important; opacity: 1 !important;
# }

# [data-testid="stDownloadButton"] > button {
#     background: transparent !important;
#     color: var(--text-2) !important;
#     border: 1px solid var(--border-hi) !important;
#     border-radius: var(--r-md) !important;
#     font-family: var(--ff-mono) !important;
#     font-size: 0.75rem !important;
#     letter-spacing: 0.08em !important;
#     height: 40px !important;
#     padding: 0 1.2rem !important;
#     box-shadow: none !important;
#     transition: border-color 0.15s, color 0.15s !important;
# }
# [data-testid="stDownloadButton"] > button:hover {
#     border-color: var(--accent) !important;
#     color: var(--text-1) !important;
#     transform: none !important; opacity: 1 !important;
# }

# /* ════════════ PIPELINE LABEL ════════════ */
# .nx-label {
#     font-family: var(--ff-mono) !important;
#     font-size: 0.63rem;
#     letter-spacing: 0.22em;
#     text-transform: uppercase;
#     color: var(--text-3);
#     margin: 2.4rem 0 1rem;
#     display: flex;
#     align-items: center;
#     gap: 0.75rem;
# }
# .nx-label::after {
#     content: '';
#     flex: 1;
#     height: 1px;
#     background: var(--border);
# }

# /* ════════════ STEP CARD ════════════ */
# .nx-step {
#     position: relative;
#     background: var(--bg-1);
#     border: 1px solid var(--border);
#     border-radius: var(--r-lg);
#     padding: 1.2rem 1.5rem 1.2rem 1.7rem;
#     margin-bottom: 0.65rem;
#     overflow: hidden;
#     transition: border-color 0.25s, background 0.25s;
# }
# .nx-step::before {
#     content: '';
#     position: absolute;
#     left: 0; top: 0;
#     width: 2px; height: 100%;
#     border-radius: 2px 0 0 2px;
#     transition: background 0.3s;
# }

# .nx-step.idle { opacity: 0.3; }
# .nx-step.idle::before { background: var(--border-hi); }

# .nx-step.active {
#     border-color: rgba(245,166,35,0.25);
#     background: linear-gradient(100deg, var(--bg-2) 0%, var(--bg-1) 100%);
# }
# .nx-step.active::before {
#     background: var(--amber);
#     animation: nx-pulse 1.6s ease-in-out infinite;
# }
# @keyframes nx-pulse { 0%,100%{opacity:1} 50%{opacity:0.25} }

# .nx-step.done { border-color: rgba(52,211,153,0.2); }
# .nx-step.done::before { background: var(--green); }

# /* Step internals */
# .nx-step-row {
#     display: flex;
#     align-items: center;
#     gap: 0.7rem;
# }
# .nx-chip {
#     font-family: var(--ff-mono) !important;
#     font-size: 0.6rem;
#     letter-spacing: 0.12em;
#     text-transform: uppercase;
#     padding: 0.18rem 0.55rem;
#     border-radius: 30px;
#     border: 1px solid var(--border-hi);
#     color: var(--text-3);
#     line-height: 1.4;
#     flex-shrink: 0;
# }
# .nx-step.active .nx-chip { color: var(--amber); border-color: rgba(245,166,35,0.35); background: var(--amber-dim); }
# .nx-step.done   .nx-chip { color: var(--green); border-color: rgba(52,211,153,0.3); background: var(--green-dim); }

# .nx-step-name {
#     font-family: var(--ff-display) !important;
#     font-weight: 400;
#     font-size: 1.02rem;
#     letter-spacing: -0.015em;
#     color: var(--text-1) !important;
# }
# .nx-step-status {
#     font-family: var(--ff-body) !important;
#     font-size: 0.8rem;
#     color: var(--text-3);
#     margin-top: 0.28rem;
#     padding-left: 0.05rem;
# }
# .nx-step.active .nx-step-status { color: var(--amber); }
# .nx-step.done   .nx-step-status { color: var(--green); }

# .nx-output {
#     margin-top: 0.9rem;
#     padding: 0.85rem 1rem;
#     background: var(--bg);
#     border: 1px solid var(--border);
#     border-radius: var(--r-md);
#     font-family: var(--ff-mono) !important;
#     font-size: 0.73rem;
#     line-height: 1.7;
#     color: var(--text-3);
#     max-height: 200px;
#     overflow-y: auto;
#     white-space: pre-wrap;
#     word-break: break-word;
# }

# /* ════════════ REPORT ════════════ */
# .nx-report {
#     background: var(--bg-1);
#     border: 1px solid var(--border-hi);
#     border-radius: var(--r-lg);
#     padding: 2rem 2.2rem;
#     margin-top: 0.4rem;
# }
# .nx-report h1,.nx-report h2,.nx-report h3,.nx-report h4 {
#     font-family: var(--ff-display) !important;
#     font-weight: 400 !important;
#     letter-spacing: -0.02em !important;
#     color: var(--text-1) !important;
#     margin: 1.8rem 0 0.5rem !important;
#     line-height: 1.2 !important;
# }
# .nx-report h1 { font-size: 1.55rem !important; margin-top: 0 !important; }
# .nx-report h2 { font-size: 1.25rem !important; }
# .nx-report h3 { font-size: 1.05rem !important; }
# .nx-report p {
#     font-family: var(--ff-body) !important;
#     font-size: 0.95rem !important;
#     line-height: 1.88 !important;
#     color: var(--text-2) !important;
#     margin-bottom: 0.9rem !important;
# }
# .nx-report li {
#     font-family: var(--ff-body) !important;
#     font-size: 0.93rem !important;
#     line-height: 1.8 !important;
#     color: var(--text-2) !important;
#     margin-bottom: 0.25rem !important;
# }
# .nx-report strong, .nx-report b { font-weight: 600 !important; color: var(--text-1) !important; }
# .nx-report code {
#     font-family: var(--ff-mono) !important;
#     font-size: 0.8rem !important;
#     background: var(--bg-3) !important;
#     padding: 0.12em 0.4em !important;
#     border-radius: 4px !important;
#     color: var(--accent) !important;
# }
# .nx-report hr { border: none !important; border-top: 1px solid var(--border) !important; margin: 1.5rem 0 !important; }
# .nx-report blockquote {
#     border-left: 2px solid var(--accent);
#     padding-left: 1rem; margin: 1rem 0;
#     color: var(--text-3) !important; font-style: italic;
# }

# /* ════════════ FEEDBACK ════════════ */
# .nx-feedback {
#     background: var(--green-dim);
#     border: 1px solid rgba(52,211,153,0.15);
#     border-radius: var(--r-lg);
#     padding: 1.5rem 1.8rem;
#     margin-top: 0.4rem;
# }
# .nx-feedback p {
#     font-family: var(--ff-body) !important;
#     font-size: 0.92rem !important;
#     line-height: 1.82 !important;
#     color: #96e3c0 !important;
#     margin-bottom: 0.7rem !important;
# }
# .nx-feedback strong { color: var(--green) !important; font-weight: 600 !important; }
# .nx-feedback li {
#     font-family: var(--ff-body) !important;
#     font-size: 0.9rem !important;
#     color: #96e3c0 !important;
#     line-height: 1.75 !important;
# }

# /* ════════════ SCROLLBAR ════════════ */
# ::-webkit-scrollbar { width: 3px; height: 3px; }
# ::-webkit-scrollbar-track { background: transparent; }
# ::-webkit-scrollbar-thumb { background: var(--border-hi); border-radius: 10px; }

# /* ════════════ STREAMLIT CLEANUP ════════════ */
# [data-testid="stVerticalBlock"] { gap: 0 !important; }
# </style>
# """, unsafe_allow_html=True)


# # ── Hero ───────────────────────────────────────────────────────────────────────
# st.markdown("""
# <div style="margin-bottom:0.5rem">
#     <div class="nx-eyebrow">Nexus · Multi-Agent Research</div>
#     <h1 class="nx-h1">Deep research,<br><em>automated.</em></h1>
#     <p class="nx-tagline">
#         Enter any topic and four specialised agents will search the web,
#         scrape sources, write a report, and critique it — live.
#     </p>
# </div>
# """, unsafe_allow_html=True)


# # ── Topic input ───────────────────────────────────────────────────────────────
# col_in, col_btn = st.columns([5, 1], vertical_alignment="bottom")
# with col_in:
#     topic = st.text_input(
#         "Topic",
#         placeholder="e.g.  The future of nuclear fusion energy",
#         label_visibility="visible",
#     )
# with col_btn:
#     run_btn = st.button("Research →", use_container_width=True)

# st.markdown('<div class="nx-rule"></div>', unsafe_allow_html=True)


# # ── Step renderer ─────────────────────────────────────────────────────────────
# STEP_META = [
#     ("Search Agent",  "Queries the web for recent, reliable sources."),
#     ("Reader Agent",  "Scrapes the most relevant page for depth."),
#     ("Writer Chain",  "Synthesises findings into a structured report."),
#     ("Critic Chain",  "Reviews the draft and surfaces improvements."),
# ]
# ACTIVE_MSG = [
#     "Searching the web…",
#     "Scraping top source…",
#     "Writing the report…",
#     "Reviewing the report…",
# ]
# DONE_MSG = [
#     "Search complete ✓",
#     "Scraping complete ✓",
#     "Draft complete ✓",
#     "Review complete ✓",
# ]

# def render_step(ph, idx: int, status: str = "idle", content: str = None):
#     import html as _html
#     name, _ = STEP_META[idx]
#     if status == "idle":
#         status_txt = "Waiting"
#     elif status == "active":
#         status_txt = ACTIVE_MSG[idx]
#     else:
#         status_txt = DONE_MSG[idx]

#     out_html = ""
#     if content:
#         out_html = f'<div class="nx-output">{_html.escape(content)}</div>'

#     ph.markdown(f"""
#     <div class="nx-step {status}">
#         <div class="nx-step-row">
#             <span class="nx-chip">Step {idx + 1}</span>
#             <span class="nx-step-name">{name}</span>
#         </div>
#         <div class="nx-step-status">{status_txt}</div>
#         {out_html}
#     </div>
#     """, unsafe_allow_html=True)


# # ── Run pipeline ──────────────────────────────────────────────────────────────
# if run_btn:
#     if not topic.strip():
#         st.warning("Please enter a research topic to continue.")
#         st.stop()

#     state = {}

#     st.markdown('<div class="nx-label">Pipeline</div>', unsafe_allow_html=True)
#     ph = [st.empty() for _ in range(4)]
#     for i in range(4):
#         render_step(ph[i], i, "idle")

#     # — Step 0: Search —
#     render_step(ph[0], 0, "active")
#     res = build_search_agent().invoke({
#         "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
#     })
#     state["search_results"] = res["messages"][-1].content
#     preview = state["search_results"][:1400] + ("…" if len(state["search_results"]) > 1400 else "")
#     render_step(ph[0], 0, "done", content=preview)

#     # — Step 1: Reader —
#     render_step(ph[1], 1, "active")
#     res = build_reader_agent().invoke({
#         "messages": [("user",
#             f"Based on the following search results about '{topic}', "
#             f"pick the most relevant URL and scrape it for deeper content.\n\n"
#             f"Search Results:\n{state['search_results'][:800]}"
#         )]
#     })
#     state["scraped_content"] = res["messages"][-1].content
#     preview = state["scraped_content"][:1400] + ("…" if len(state["scraped_content"]) > 1400 else "")
#     render_step(ph[1], 1, "done", content=preview)

#     # — Step 2: Writer —
#     render_step(ph[2], 2, "active")
#     combined = (
#         f"SEARCH RESULTS:\n{state['search_results']}\n\n"
#         f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}"
#     )
#     state["report"] = writer_chain.invoke({"topic": topic, "research": combined})
#     render_step(ph[2], 2, "done")

#     # — Step 3: Critic —
#     render_step(ph[3], 3, "active")
#     state["feedback"] = critic_chain.invoke({"report": state["report"]})
#     render_step(ph[3], 3, "done")

#     # — Outputs —
#     report_text   = state["report"].content   if hasattr(state["report"],   "content") else str(state["report"])
#     feedback_text = state["feedback"].content if hasattr(state["feedback"], "content") else str(state["feedback"])

#     st.markdown('<div class="nx-label">Final Report</div>', unsafe_allow_html=True)
#     st.markdown(f'<div class="nx-report">{report_text}</div>', unsafe_allow_html=True)

#     st.markdown('<div class="nx-label">Critic Feedback</div>', unsafe_allow_html=True)
#     st.markdown(f'<div class="nx-feedback">{feedback_text}</div>', unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)
#     full_md = f"# {topic}\n\n{report_text}\n\n---\n\n## Critic Feedback\n\n{feedback_text}"
#     st.download_button(
#         label="↓  Download report (.md)",
#         data=full_md,
#         file_name=f"nexus_{topic[:45].replace(' ', '_').lower()}.md",
#         mime="text/markdown",
#     )

# else:
#     # — Idle preview —
#     st.markdown('<div class="nx-label">Pipeline</div>', unsafe_allow_html=True)
#     for i in range(4):
#         render_step(st.empty(), i, "idle")












import streamlit as st
from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Nexus Research",
    page_icon="◈",
    layout="wide"
)

st.title("🔍 Nexus Research AI")

# ---------------- INPUT ----------------
topic = st.text_input("Enter a research topic")
run_btn = st.button("Research")

# ---------------- HELPER ----------------
def safe_invoke(agent, payload, step_name):
    try:
        with st.spinner(f"{step_name}..."):
            res = agent.invoke(payload)
        return res.get("output", "No output returned")
    except Exception as e:
        st.error(f"{step_name} failed ❌")
        st.exception(e)
        st.stop()

# ---------------- PIPELINE ----------------
if run_btn:
    if not topic.strip():
        st.warning("Please enter a topic")
        st.stop()

    state = {}

    st.markdown("## ⚙️ Multi-Agent Pipeline")

    # -------- STEP 1: SEARCH --------
    st.markdown("### 🔎 Search Agent")
    search_agent = build_search_agent()

    search_output = safe_invoke(
        search_agent,
        {"input": f"Find recent, reliable and detailed information about: {topic}"},
        "Searching the web"
    )

    state["search_results"] = search_output

    with st.expander("View Search Results"):
        st.write(search_output)

    # -------- STEP 2: READER --------
    st.markdown("### 📄 Reader Agent")
    reader_agent = build_reader_agent()

    reader_output = safe_invoke(
        reader_agent,
        {
            "input": (
                f"Based on the following search results about '{topic}', "
                f"pick the most relevant URL and scrape it for deeper content.\n\n"
                f"Search Results:\n{state['search_results'][:1000]}"
            )
        },
        "Scraping content"
    )

    state["scraped_content"] = reader_output

    with st.expander("View Scraped Content"):
        st.write(reader_output)

    # -------- STEP 3: WRITER --------
    st.markdown("### ✍️ Writer Agent")

    combined = (
        f"SEARCH RESULTS:\n{state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}"
    )

    try:
        with st.spinner("Generating report..."):
            report = writer_chain.invoke({
                "topic": topic,
                "research": combined
            })
        report_text = report.content if hasattr(report, "content") else str(report)
    except Exception as e:
        st.error("Report generation failed ❌")
        st.exception(e)
        st.stop()

    state["report"] = report_text

    st.success("Report Generated ✅")
    st.markdown(report_text)

    # -------- STEP 4: CRITIC --------
    st.markdown("### 🧠 Critic Agent")

    try:
        with st.spinner("Reviewing report..."):
            feedback = critic_chain.invoke({
                "report": report_text
            })
        feedback_text = feedback.content if hasattr(feedback, "content") else str(feedback)
    except Exception as e:
        st.error("Critic failed ❌")
        st.exception(e)
        st.stop()

    state["feedback"] = feedback_text

    st.success("Review Complete ✅")
    st.markdown(feedback_text)

    # -------- DOWNLOAD --------
    st.markdown("### 📥 Download")

    full_report = f"# {topic}\n\n{report_text}\n\n---\n\n## Critic Feedback\n\n{feedback_text}"

    st.download_button(
        label="Download Full Report",
        data=full_report,
        file_name=f"{topic.replace(' ', '_')}.md",
        mime="text/markdown"
    )