import streamlit as st

st.set_page_config(
    page_title="Signal Field",
    page_icon="◌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .block-container {
            max-width: 1280px;
            padding: 2rem 2rem 3.5rem 2rem;
        }

        .stApp {
            background: #F5F5F5;
            color: #212529;
        }

        div[data-testid="stHorizontalBlock"] {
            gap: 1.15rem;
            align-items: stretch;
        }

        .signal-hero {
            background: linear-gradient(135deg, #110617 0%, #1D1424 100%);
            border: 1px solid #3B2E46;
            border-radius: 22px;
            box-shadow: 0 12px 32px rgba(17, 6, 23, 0.16);
            color: #FFFFFF;
            margin: 0 0 2.25rem 0;
            padding: 3.4rem 4rem;
        }

        .signal-kicker {
            color: #C9BFD3;
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.1em;
            margin-bottom: 0.75rem;
            text-transform: uppercase;
        }

        .signal-hero h1 {
            color: #FFFFFF;
            font-size: clamp(2.8rem, 6vw, 5.8rem);
            font-weight: 800;
            letter-spacing: -0.05em;
            line-height: 0.95;
            margin: 0;
        }

        .signal-hero p {
            color: #D9D0E5;
            font-size: 1.15rem;
            line-height: 1.55;
            margin: 1.5rem 0 0 0;
            max-width: 50rem;
        }

        .section-kicker {
            color: #632CA6;
            font-size: 0.76rem;
            font-weight: 800;
            letter-spacing: 0.1em;
            margin: 2.3rem 0 0.45rem 0;
            text-transform: uppercase;
        }

        .section-heading {
            color: #212529;
            font-size: clamp(1.8rem, 3.5vw, 3rem);
            font-weight: 800;
            letter-spacing: -0.035em;
            line-height: 1.05;
            margin: 0 0 0.85rem 0;
        }

        .section-copy {
            color: #4A4F55;
            font-size: 1.02rem;
            line-height: 1.55;
            margin: 0 0 1.45rem 0;
            max-width: 50rem;
        }

        .workspace {
            background: linear-gradient(135deg, #110617 0%, #1D1424 100%);
            border: 1px solid #3B2E46;
            border-radius: 20px;
            box-shadow: 0 12px 32px rgba(17, 6, 23, 0.16);
            margin: 1.25rem 0 1.2rem 0;
            padding: 1.6rem;
        }

        .workspace-label {
            color: #C9BFD3;
            font-size: 0.76rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            margin-bottom: 0.55rem;
            text-transform: uppercase;
        }

        .workspace-title {
            color: #FFFFFF;
            font-size: 1.65rem;
            font-weight: 800;
            letter-spacing: -0.025em;
            line-height: 1.15;
            margin: 0 0 0.85rem 0;
        }

        .workspace-card {
            background: linear-gradient(180deg, #251B2E 0%, #1D1424 100%);
            border: 1px solid #3B2E46;
            border-radius: 16px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.22);
            margin: 0;
            min-height: 0;
            padding: 1.25rem;
        }

        .workspace-card h3 {
            color: #FFFFFF;
            font-size: 1rem;
            line-height: 1.3;
            margin: 0 0 0.6rem 0;
        }

        .workspace-card p {
            color: #C9BFD3;
            font-size: 0.92rem;
            line-height: 1.5;
            margin: 0;
        }

        .insight-card {
            background: #FFFFFF;
            border: 1px solid #E1E5E9;
            border-radius: 18px;
            box-shadow: 0 1px 2px rgba(17, 6, 23, 0.04);
            margin: 0;
            min-height: 0;
            padding: 1.45rem;
        }

        .insight-card h3 {
            color: #632CA6;
            font-size: 1rem;
            line-height: 1.35;
            margin: 0 0 0.7rem 0;
        }

        .insight-card p {
            color: #4A4F55;
            font-size: 0.94rem;
            line-height: 1.55;
            margin: 0;
        }

        .metric-value {
            color: #FFFFFF;
            font-size: 2.15rem;
            font-weight: 800;
            letter-spacing: -0.04em;
            line-height: 1;
            margin: 0.5rem 0;
        }

        .metric-label {
            color: #C9BFD3;
            font-size: 0.85rem;
            margin: 0;
        }

        .status-good {
            color: #2E8B70;
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.06em;
            text-transform: uppercase;
        }

        .status-attention {
            color: #D97706;
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.06em;
            text-transform: uppercase;
        }

        .status-critical {
            color: #E26D76;
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.06em;
            text-transform: uppercase;
        }

        .validation-gap {
            height: 1.15rem;
        }

        .signal-footer {
            border-top: 1px solid #E1E5E9;
            color: #4A4F55;
            font-size: 0.82rem;
            line-height: 1.5;
            margin-top: 4rem;
            padding: 1.5rem 0 0 0;
        }

        [data-testid="stSegmentedControl"] {
            background: #FFFFFF;
            border: 1px solid #E1E5E9;
            border-radius: 14px;
            margin: 1.2rem 0 1.55rem 0;
            padding: 0.24rem;
            width: 100%;
        }

        [data-testid="stSegmentedControl"] > div {
            width: 100%;
        }

        [data-testid="stSegmentedControl"] button {
            border: 0 !important;
            border-radius: 10px !important;
            color: #4A4F55 !important;
            font-weight: 700 !important;
            line-height: 1.2 !important;
            min-height: 2.75rem;
            padding: 0.55rem 0.8rem !important;
            white-space: normal !important;
        }

        [data-testid="stSegmentedControl"] button[aria-checked="true"] {
            background: #632CA6 !important;
            box-shadow: 0 2px 7px rgba(99, 44, 166, 0.26);
            color: #FFFFFF !important;
        }

        [data-testid="stTabs"] {
            margin: 1.2rem 0 1.6rem 0;
            overflow-x: auto;
        }

        [data-testid="stTabs"] [data-baseweb="tab-list"] {
            border-bottom: 1px solid #E1E5E9;
            gap: 0.45rem;
        }

        [data-testid="stTabs"] button {
            border-radius: 10px 10px 0 0;
            color: #4A4F55 !important;
            font-weight: 700;
            min-height: 2.6rem;
            padding: 0.7rem 0.9rem;
            white-space: normal !important;
        }

        [data-testid="stTabs"] button[aria-selected="true"] {
            border-bottom: 3px solid #632CA6 !important;
            color: #632CA6 !important;
        }

        .stButton > button {
            background: #FFFFFF;
            border: 1px solid #632CA6;
            border-radius: 10px;
            color: #632CA6;
            font-weight: 750;
            min-height: 2.8rem;
        }

        .stButton > button:hover {
            background: #F1EAFE;
            border-color: #632CA6;
            color: #632CA6;
        }

        .stButton > button[kind="primary"] {
            background: #632CA6;
            border-color: #632CA6;
            box-shadow: 0 5px 14px rgba(99, 44, 166, 0.22);
            color: #FFFFFF;
        }

        .stButton > button[kind="primary"]:hover {
            background: #54248F;
            border-color: #54248F;
            color: #FFFFFF;
        }

        svg {
            height: auto;
            max-width: 100%;
        }

        .insight-card,
        .workspace-card,
        .workspace {
            overflow-wrap: anywhere;
            word-break: normal;
        }

        @media (max-width: 900px) {
            .block-container {
                max-width: 100%;
                padding-left: 1.25rem;
                padding-right: 1.25rem;
            }

            .signal-hero {
                padding: 2.6rem 2rem;
            }

            .workspace-title {
                font-size: 1.4rem;
            }
        }

        @media (max-width: 700px) {
            .block-container {
                padding: 1rem 0.85rem 2.5rem 0.85rem;
            }

            div[data-testid="stHorizontalBlock"] {
                gap: 0.85rem;
            }

            .signal-hero {
                border-radius: 16px;
                margin-bottom: 1.3rem;
                padding: 2rem 1.15rem;
            }

            .signal-hero h1 {
                font-size: clamp(2.55rem, 14vw, 4.2rem);
            }

            .signal-hero p {
                font-size: 1rem;
                line-height: 1.5;
            }

            .section-kicker {
                margin-top: 1.7rem;
            }

            .section-heading {
                font-size: clamp(1.8rem, 9vw, 2.7rem);
                line-height: 1.05;
            }

            .section-copy {
                font-size: 0.98rem;
            }

            .workspace {
                border-radius: 16px;
                margin: 1rem 0;
                padding: 1.1rem;
            }

            .workspace-title {
                font-size: 1.28rem;
            }

            .workspace-card,
            .insight-card {
                border-radius: 14px;
                padding: 1.1rem;
            }

            .metric-value {
                font-size: 1.95rem;
            }

            .signal-footer {
                font-size: 0.78rem;
                margin-top: 2.5rem;
            }
        }

        @media (max-width: 480px) {
            [data-testid="stSegmentedControl"] > div {
                display: grid;
                gap: 0.35rem;
                grid-template-columns: 1fr;
            }

            [data-testid="stSegmentedControl"] button {
                border-radius: 0.7rem !important;
                justify-content: flex-start;
                min-height: 2.8rem;
                text-align: left;
                width: 100%;
            }

            [data-testid="stTabs"] button {
                font-size: 0.78rem !important;
                padding-left: 0.55rem;
                padding-right: 0.55rem;
            }
        }

        @media (prefers-color-scheme: dark) {
            .stApp {
                background: #110617;
                color: #F7F3FA;
            }

            .section-heading {
                color: #F7F3FA;
            }

            .section-copy,
            .signal-footer {
                color: #C9BFD3;
            }

            .signal-footer {
                border-color: #3B2E46;
            }

            .insight-card {
                background: #1D1424;
                border-color: #3B2E46;
            }

            .insight-card p {
                color: #C9BFD3;
            }

            [data-testid="stSegmentedControl"] {
                background: #1D1424;
                border-color: #3B2E46;
            }

            [data-testid="stSegmentedControl"] button {
                color: #C9BFD3 !important;
            }

            [data-testid="stSegmentedControl"] button[aria-checked="true"] {
                background: #632CA6 !important;
                color: #FFFFFF !important;
            }

            [data-testid="stTabs"] [data-baseweb="tab-list"] {
                border-color: #3B2E46;
            }

            [data-testid="stTabs"] button {
                color: #C9BFD3 !important;
            }

            [data-testid="stTabs"] button[aria-selected="true"] {
                border-color: #8000FF !important;
                color: #FFFFFF !important;
            }

            .stButton > button {
                background: #1D1424;
                border-color: #632CA6;
                color: #F7F3FA;
            }

            .stButton > button:hover {
                background: #251B2E;
                border-color: #8000FF;
                color: #FFFFFF;
            }

            .stButton > button[kind="primary"] {
                background: #632CA6;
                border-color: #632CA6;
                color: #FFFFFF;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <section class="signal-hero">
        <div class="signal-kicker">Independent concept exploration</div>
        <h1>Signal Field</h1>
        <p>
            An interactive companion that explores how a visual system can help
            people find meaning, orientation, and confidence in complex AI
            product experiences.
        </p>
    </section>
    """,
    unsafe_allow_html=True,
)

page = st.segmented_control(
    "Navigate Signal Field",
    ["Explore", "System", "Decisions", "Validation"],
    default="Explore",
    label_visibility="collapsed",
    width="stretch",
)

if page == "Explore":
    st.markdown(
        """
        <div class="section-kicker">Explore</div>
        <div class="section-heading">One system, three contexts.</div>
        <p class="section-copy">
            Change the context to see how one visual language adapts its hierarchy,
            information depth, and primary action without losing its identity.
        </p>
        """,
        unsafe_allow_html=True,
    )

    context = st.segmented_control(
        "Choose a product context",
        ["AI investigation", "Monitoring", "Operational summary"],
        default="AI investigation",
        label_visibility="collapsed",
        width="stretch",
    )

    if context == "AI investigation":
        st.markdown(
            """
            <section class="workspace">
                <div class="workspace-label">AI investigation field</div>
                <div class="workspace-title">Payment service latency exceeds expected range</div>
            </section>
            """,
            unsafe_allow_html=True,
        )

        left, right = st.columns([1.35, 1])

        with left:
            st.markdown(
                """
                <section class="workspace-card">
                    <div class="status-good">High confidence</div>
                    <h3>Why this needs attention</h3>
                    <p>Trace volume increased by 38 percent.</p>
                    <p style="margin-top:0.55rem;">Database wait time increased by 22 percent.</p>
                    <p style="margin-top:0.55rem;">A related deployment occurred 14 minutes ago.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with right:
            st.markdown(
                """
                <section class="workspace-card">
                    <div class="workspace-label">Correlated signals</div>
                    <div style="display:flex; align-items:center; justify-content:center; height:105px;">
                        <div style="width:96px; height:96px; border:2px solid #632CA6; border-radius:50%; display:flex; align-items:center; justify-content:center; color:#FFFFFF; font-weight:800;">
                            Latency
                        </div>
                    </div>
                    <p style="text-align:center;">Traces · Database · Deployment</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        st.markdown('<div class="validation-gap"></div>', unsafe_allow_html=True)

        note_one, note_two, note_three = st.columns(3)

        with note_one:
            st.markdown(
                """
                <section class="insight-card">
                    <h3>Visible reasoning</h3>
                    <p>The recommendation never arrives as an unexplained instruction. Evidence has a deliberate place in the hierarchy.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with note_two:
            st.markdown(
                """
                <section class="insight-card">
                    <h3>Confidence with context</h3>
                    <p>Confidence is connected to the signals that make the recommendation credible.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with note_three:
            st.markdown(
                """
                <section class="insight-card">
                    <h3>Action after understanding</h3>
                    <p>Clear next steps appear after the primary condition and evidence, keeping the user in control.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

    elif context == "Monitoring":
        st.markdown(
            """
            <section class="workspace">
                <div class="workspace-label">Monitoring workspace</div>
                <div class="workspace-title">A dense field with a visible place to begin</div>
            </section>
            """,
            unsafe_allow_html=True,
        )

        metric_one, metric_two, metric_three, metric_four = st.columns(4)

        with metric_one:
            st.markdown(
                """
                <section class="workspace-card">
                    <div class="status-good">Healthy</div>
                    <div class="metric-value">99.97%</div>
                    <p class="metric-label">Service health</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with metric_two:
            st.markdown(
                """
                <section class="workspace-card">
                    <div class="status-attention">Elevated</div>
                    <div class="metric-value">187 ms</div>
                    <p class="metric-label">Request latency</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with metric_three:
            st.markdown(
                """
                <section class="workspace-card">
                    <div class="status-attention">Watch</div>
                    <div class="metric-value">0.24%</div>
                    <p class="metric-label">Error rate</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with metric_four:
            st.markdown(
                """
                <section class="workspace-card">
                    <div class="status-critical">Open</div>
                    <div class="metric-value">03</div>
                    <p class="metric-label">Active investigations</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        st.markdown('<div class="validation-gap"></div>', unsafe_allow_html=True)

        chart_column, change_column = st.columns([2.2, 1])

        with chart_column:
            st.markdown(
                """
                <section class="workspace-card">
                    <div class="workspace-label">Latency over the last hour</div>
                    <svg viewBox="0 0 700 170" width="100%" role="img" aria-label="Latency trend with late increase">
                        <line x1="15" y1="145" x2="685" y2="145" stroke="#3B2E46" stroke-width="2"/>
                        <polyline fill="none" stroke="#632CA6" stroke-width="5"
                        points="15,130 65,125 115,132 165,122 215,128 265,118 315,126 365,120 415,125 465,115 515,120 555,102 585,95 610,45 630,80 650,55 685,65"/>
                        <circle cx="610" cy="45" r="8" fill="#D97706"/>
                        <text x="455" y="35" fill="#D9D0E5" font-size="17" font-family="sans-serif">Deployment detected</text>
                    </svg>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with change_column:
            st.markdown(
                """
                <section class="workspace-card">
                    <div class="workspace-label">What changed</div>
                    <h3>Latency moved above baseline</h3>
                    <p>Database wait time increased after the latest deployment.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            """
            <p class="section-copy" style="margin-top:1.4rem;">
                The emphasis is not on making every metric equal. It is on making the next useful signal easier to find.
            </p>
            """,
            unsafe_allow_html=True,
        )

    else:
        st.markdown(
            """
            <section class="workspace">
                <div class="workspace-label">Operational summary</div>
                <div class="workspace-title">One event, different decision contexts</div>
            </section>
            """,
            unsafe_allow_html=True,
        )

        audience_one, audience_two, audience_three = st.columns(3)

        with audience_one:
            st.markdown(
                """
                <section class="workspace-card">
                    <div class="status-critical">Incident responder</div>
                    <h3 style="font-size:1.4rem; margin-top:1.2rem;">Latency is affecting checkout</h3>
                    <p>High confidence correlation across traces and database activity.</p>
                    <div style="margin-top:1.3rem; color:#FFFFFF; font-weight:800;">Open investigation →</div>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with audience_two:
            st.markdown(
                """
                <section class="workspace-card">
                    <div class="status-attention">Platform owner</div>
                    <h3 style="font-size:1.4rem; margin-top:1.2rem;">12 services show elevated dependency wait time</h3>
                    <p>The trend began after the latest production deployment.</p>
                    <div style="margin-top:1.3rem; color:#FFFFFF; font-weight:800;">View service map →</div>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with audience_three:
            st.markdown(
                """
                <section class="workspace-card">
                    <div class="status-good">Executive partner</div>
                    <h3 style="font-size:1.4rem; margin-top:1.2rem;">Customer impact contained</h3>
                    <p>The incident is understood and remediation is in progress.</p>
                    <div style="margin-top:1.3rem; color:#FFFFFF; font-weight:800;">Read operational summary →</div>
                </section>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            """
            <p class="section-copy" style="margin-top:1.4rem;">
                The same visual language remains familiar. The amount of detail changes with the decision each person needs to make.
            </p>
            """,
            unsafe_allow_html=True,
        )

elif page == "System":
    st.markdown(
        """
        <div class="section-kicker">System</div>
        <div class="section-heading">Expression becomes reliable when it becomes repeatable.</div>
        <p class="section-copy">
            Signal Field translates visual direction into a small set of reusable rules.
            Each rule helps people recognize importance, understand state, and retain orientation.
        </p>
        """,
        unsafe_allow_html=True,
    )

    token_tab, hierarchy_tab, spacing_tab, anatomy_tab = st.tabs(
        ["Tokens", "Hierarchy", "Spacing", "Component anatomy"]
    )

    with token_tab:
        st.markdown("#### Colour has a job")

        st.markdown(
            """
            <p class="section-copy">
                Colour is reserved for direction, state, and focus. It never carries meaning alone.
                Labels, position, and clear language remain visible in every condition.
            </p>
            """,
            unsafe_allow_html=True,
        )

        token_one, token_two, token_three, token_four, token_five = st.columns(5)

        token_data = [
            ("#110617", "Night field", "Focused inspection and immersive product fields."),
            ("#632CA6", "Signal violet", "Primary action, active state, and meaningful direction."),
            ("#8000FF", "Electric violet", "Rare moments of emphasis and future facing focus."),
            ("#2E8B70", "Confidence", "Positive state, paired with clear supporting language."),
            ("#D97706", "Attention", "Unresolved condition, paired with an explanation and next step."),
        ]

        for column, token in zip(
            [token_one, token_two, token_three, token_four, token_five],
            token_data,
        ):
            colour, name, description = token
            with column:
                st.markdown(
                    f"""
                    <section class="insight-card">
                        <div style="height:52px; border-radius:10px; background:{colour}; margin-bottom:1rem;"></div>
                        <h3>{name}</h3>
                        <p>{colour}<br>{description}</p>
                    </section>
                    """,
                    unsafe_allow_html=True,
                )

        st.markdown('<div class="validation-gap"></div>', unsafe_allow_html=True)

        surface_one, surface_two, surface_three, surface_four = st.columns(4)

        surface_data = [
            ("#F5F5F5", "Cloud surface", "Quiet page fields and secondary surfaces.", True),
            ("#FFFFFF", "White surface", "Primary reading and working surfaces.", True),
            ("#E1E5E9", "Structure line", "Dividers, boundaries, and low emphasis structure.", False),
            ("#4A4F55", "Quiet graphite", "Supporting copy, labels, and metadata.", False),
        ]

        for column, token in zip(
            [surface_one, surface_two, surface_three, surface_four],
            surface_data,
        ):
            colour, name, description, needs_border = token
            border = "border:1px solid #E1E5E9;" if needs_border else ""
            with column:
                st.markdown(
                    f"""
                    <section class="insight-card">
                        <div style="height:42px; border-radius:10px; background:{colour}; {border} margin-bottom:1rem;"></div>
                        <h3>{name}</h3>
                        <p>{colour}<br>{description}</p>
                    </section>
                    """,
                    unsafe_allow_html=True,
                )

    with hierarchy_tab:
        st.markdown("#### The eye needs a reliable path")

        st.markdown(
            """
            <p class="section-copy">
                The system moves from condition, to context, to action. Information may be dense,
                but its reading order should never be unclear.
            </p>
            """,
            unsafe_allow_html=True,
        )

        hierarchy_left, hierarchy_right = st.columns([1.2, 1])

        with hierarchy_left:
            st.markdown(
                """
                <section class="workspace">
                    <div class="workspace-label">Hierarchy example</div>
                    <div class="workspace-title">Payment service latency exceeds expected range</div>
                    <div class="status-good">High confidence</div>
                    <p style="color:#C9BFD3; font-size:1rem; line-height:1.55; margin:1rem 0 0 0;">
                        Trace volume and database wait time changed after a related deployment.
                    </p>
                    <div style="margin-top:1.4rem; color:#FFFFFF; font-weight:800;">
                        Create investigation →
                    </div>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with hierarchy_right:
            for title, copy in [
                ("01 Condition", "The primary condition earns the largest type and strongest contrast."),
                ("02 Context", "Evidence and confidence explain why the condition deserves attention."),
                ("03 Action", "A clear next step follows understanding rather than replacing it."),
            ]:
                st.markdown(
                    f"""
                    <section class="insight-card" style="margin-bottom:1rem;">
                        <h3>{title}</h3>
                        <p>{copy}</p>
                    </section>
                    """,
                    unsafe_allow_html=True,
                )

    with spacing_tab:
        st.markdown("#### Space gives information room to be understood")

        st.markdown(
            """
            <p class="section-copy">
                Signal Field uses a four point rhythm. Consistent spacing creates scan paths,
                separates tasks, and gives dense content a place to breathe.
            </p>
            """,
            unsafe_allow_html=True,
        )

        spacing_one, spacing_two, spacing_three, spacing_four, spacing_five = st.columns(5)

        spacing_values = [
            ("04", "Tight relationship", "Icon beside label"),
            ("08", "Related content", "Label beside value"),
            ("16", "Within a component", "Heading above supporting copy"),
            ("24", "Between components", "Card to card separation"),
            ("40", "Between sections", "New decision context"),
        ]

        for column, value in zip(
            [spacing_one, spacing_two, spacing_three, spacing_four, spacing_five],
            spacing_values,
        ):
            number, label, use = value
            with column:
                st.markdown(
                    f"""
                    <section class="insight-card">
                        <div style="color:#632CA6; font-size:2.4rem; font-weight:800; line-height:1;">{number}</div>
                        <h3 style="margin-top:1rem;">{label}</h3>
                        <p>{use}</p>
                    </section>
                    """,
                    unsafe_allow_html=True,
                )

        st.markdown('<div class="validation-gap"></div>', unsafe_allow_html=True)

        st.markdown(
            """
            <section class="workspace">
                <div class="workspace-label">Spacing in practice</div>
                <div style="background:#1D1424; border:1px solid #3B2E46; border-radius:14px; padding:24px;">
                    <div style="color:#FFFFFF; font-weight:800; font-size:1.35rem;">Primary condition</div>
                    <div style="height:8px;"></div>
                    <div style="color:#C9BFD3;">Evidence and confidence remain related without competing with the condition.</div>
                    <div style="height:16px;"></div>
                    <div style="border-top:1px solid #3B2E46;"></div>
                    <div style="height:16px;"></div>
                    <div style="color:#FFFFFF; font-weight:800;">Next action →</div>
                </div>
            </section>
            """,
            unsafe_allow_html=True,
        )

    with anatomy_tab:
        st.markdown("#### Components preserve a familiar reading pattern")

        st.markdown(
            """
            <p class="section-copy">
                A component has a stable anatomy. Context may change its content and emphasis,
                but people should recognize where to find the condition, evidence, state, and next action.
            </p>
            """,
            unsafe_allow_html=True,
        )

        anatomy_left, anatomy_right = st.columns([1.35, 1])

        with anatomy_left:
            st.markdown(
                """
                <section class="workspace">
                    <div class="workspace-label">Alert component</div>
                    <div style="background:#1D1424; border:1px solid #3B2E46; border-radius:14px; padding:1.5rem;">
                        <div style="color:#C9BFD3; font-size:0.78rem; font-weight:800; letter-spacing:0.08em; text-transform:uppercase;">01 Context label</div>
                        <div style="color:#FFFFFF; font-size:1.45rem; font-weight:800; margin-top:0.55rem;">Payment service latency exceeds expected range</div>
                        <div style="color:#2E8B70; font-size:0.82rem; font-weight:800; margin-top:1rem;">02 High confidence</div>
                        <div style="color:#C9BFD3; font-size:0.95rem; line-height:1.5; margin-top:0.45rem;">03 Correlated trace, database, and deployment signals explain the recommendation.</div>
                        <div style="color:#FFFFFF; font-size:0.95rem; font-weight:800; margin-top:1.25rem;">04 Create investigation →</div>
                    </div>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with anatomy_right:
            for title, copy in [
                ("01 Context", "Names the source or type of information."),
                ("02 State", "Communicates confidence or urgency with colour and written meaning."),
                ("03 Evidence", "Explains the condition with concise, inspectable signals."),
                ("04 Action", "Moves the user forward after they have enough context to act."),
            ]:
                st.markdown(
                    f"""
                    <section class="insight-card" style="margin-bottom:1rem;">
                        <h3>{title}</h3>
                        <p>{copy}</p>
                    </section>
                    """,
                    unsafe_allow_html=True,
                )

elif page == "Decisions":
    st.markdown(
        """
        <div class="section-kicker">Decisions</div>
        <div class="section-heading">Every visual decision has a tradeoff.</div>
        <p class="section-copy">
            Signal Field is guided by choices that protect clarity without reducing
            complexity into something less useful. Select a decision to inspect the
            tension, the direction, and the reason behind it.
        </p>
        """,
        unsafe_allow_html=True,
    )

    decision = st.segmented_control(
        "Choose a design decision",
        ["AI reasoning", "Information density", "Context adaptation"],
        default="AI reasoning",
        label_visibility="collapsed",
        width="stretch",
    )

    if decision == "AI reasoning":
        st.markdown(
            """
            <section class="workspace">
                <div class="workspace-label">Decision one</div>
                <div class="workspace-title">AI guidance must show its reasoning before it asks for trust.</div>
            </section>
            """,
            unsafe_allow_html=True,
        )

        tension_column, direction_column, outcome_column = st.columns(3)

        decision_cards = [
            (
                "The tension",
                "AI can make a recommendation quickly, but speed becomes unhelpful when the user cannot see why a conclusion was reached.",
            ),
            (
                "The direction",
                "Place confidence beside the primary condition, then make the supporting signals immediately visible and easy to inspect.",
            ),
            (
                "The outcome",
                "The user can understand the recommendation before acting on it, preserving judgment and trust during an investigation.",
            ),
        ]

        for column, card in zip(
            [tension_column, direction_column, outcome_column],
            decision_cards,
        ):
            title, copy = card
            with column:
                st.markdown(
                    f"""
                    <section class="insight-card">
                        <h3>{title}</h3>
                        <p>{copy}</p>
                    </section>
                    """,
                    unsafe_allow_html=True,
                )

        st.markdown('<div class="validation-gap"></div>', unsafe_allow_html=True)

        reasoning_left, reasoning_right = st.columns([1.35, 1])

        with reasoning_left:
            st.markdown(
                """
                <section class="workspace">
                    <div class="workspace-label">Chosen pattern</div>
                    <div class="workspace-title">Payment service latency exceeds expected range</div>
                    <div class="status-good">High confidence</div>
                    <p style="color:#C9BFD3; font-size:1rem; line-height:1.55; margin:1rem 0 0 0;">
                        Trace volume increased by 38 percent. Database wait time increased by 22 percent.
                        A related deployment occurred 14 minutes ago.
                    </p>
                    <div style="margin-top:1.35rem; color:#FFFFFF; font-weight:800;">
                        Inspect evidence →
                    </div>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with reasoning_right:
            st.markdown(
                """
                <section class="insight-card" style="margin-bottom:1rem;">
                    <h3>What is deliberately avoided</h3>
                    <p>A vague AI label, an unexplained confidence score, or an action that appears before the user has enough context to assess it.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
                <section class="insight-card">
                    <h3>System rule</h3>
                    <p>Confidence is always paired with a written explanation and inspectable supporting signals.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

    elif decision == "Information density":
        st.markdown(
            """
            <section class="workspace">
                <div class="workspace-label">Decision two</div>
                <div class="workspace-title">A dense surface needs a visible path through it.</div>
            </section>
            """,
            unsafe_allow_html=True,
        )

        tension_column, direction_column, outcome_column = st.columns(3)

        decision_cards = [
            (
                "The tension",
                "Observability work requires comprehensive data, but equal emphasis across every metric makes the next useful signal harder to find.",
            ),
            (
                "The direction",
                "Use contrast, grouping, stable card anatomy, and progressive emphasis to guide scanning toward what changed.",
            ),
            (
                "The outcome",
                "The user keeps access to broad system information while receiving a clear visual entry point for investigation.",
            ),
        ]

        for column, card in zip(
            [tension_column, direction_column, outcome_column],
            decision_cards,
        ):
            title, copy = card
            with column:
                st.markdown(
                    f"""
                    <section class="insight-card">
                        <h3>{title}</h3>
                        <p>{copy}</p>
                    </section>
                    """,
                    unsafe_allow_html=True,
                )

        st.markdown('<div class="validation-gap"></div>', unsafe_allow_html=True)

        density_left, density_right = st.columns([1.45, 1])

        with density_left:
            st.markdown(
                """
                <section class="workspace">
                    <div class="workspace-label">Chosen pattern</div>
                    <div style="display:flex; gap:12px; margin-top:0.9rem; flex-wrap:wrap;">
                        <div style="background:#251B2E; border:1px solid #3B2E46; border-radius:12px; padding:15px; flex:1; min-width:120px;">
                            <div style="color:#2E8B70; font-size:0.75rem; font-weight:800;">HEALTHY</div>
                            <div style="color:#FFFFFF; font-size:1.75rem; font-weight:800; margin-top:6px;">99.97%</div>
                            <div style="color:#C9BFD3; margin-top:4px;">Service health</div>
                        </div>
                        <div style="background:#251B2E; border:2px solid #632CA6; border-radius:12px; padding:15px; flex:1; min-width:120px;">
                            <div style="color:#D97706; font-size:0.75rem; font-weight:800;">ELEVATED</div>
                            <div style="color:#FFFFFF; font-size:1.75rem; font-weight:800; margin-top:6px;">187 ms</div>
                            <div style="color:#C9BFD3; margin-top:4px;">Request latency</div>
                        </div>
                        <div style="background:#251B2E; border:1px solid #3B2E46; border-radius:12px; padding:15px; flex:1; min-width:120px;">
                            <div style="color:#D97706; font-size:0.75rem; font-weight:800;">WATCH</div>
                            <div style="color:#FFFFFF; font-size:1.75rem; font-weight:800; margin-top:6px;">0.24%</div>
                            <div style="color:#C9BFD3; margin-top:4px;">Error rate</div>
                        </div>
                    </div>
                    <div style="margin-top:16px; background:#1D1424; border:1px solid #3B2E46; border-radius:12px; padding:16px;">
                        <div style="color:#C9BFD3; font-size:0.78rem; font-weight:800; letter-spacing:0.08em; text-transform:uppercase;">What changed</div>
                        <div style="color:#FFFFFF; font-size:1.15rem; font-weight:800; margin-top:8px;">Latency moved above baseline after deployment.</div>
                    </div>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with density_right:
            st.markdown(
                """
                <section class="insight-card" style="margin-bottom:1rem;">
                    <h3>What is deliberately avoided</h3>
                    <p>Making every metric bright, every card urgent, or every colour equally saturated. Visual urgency must be earned.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
                <section class="insight-card">
                    <h3>System rule</h3>
                    <p>Strong contrast and saturated colour are reserved for the condition that needs immediate attention.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

    else:
        st.markdown(
            """
            <section class="workspace">
                <div class="workspace-label">Decision three</div>
                <div class="workspace-title">Consistency should preserve identity, not flatten context.</div>
            </section>
            """,
            unsafe_allow_html=True,
        )

        tension_column, direction_column, outcome_column = st.columns(3)

        decision_cards = [
            (
                "The tension",
                "A shared system must remain recognizable, but different people need different levels of information and different next actions.",
            ),
            (
                "The direction",
                "Keep the same component anatomy while adapting the primary statement, evidence depth, semantic state, and action to context.",
            ),
            (
                "The outcome",
                "People recognize the system immediately while receiving the level of detail required for the decision in front of them.",
            ),
        ]

        for column, card in zip(
            [tension_column, direction_column, outcome_column],
            decision_cards,
        ):
            title, copy = card
            with column:
                st.markdown(
                    f"""
                    <section class="insight-card">
                        <h3>{title}</h3>
                        <p>{copy}</p>
                    </section>
                    """,
                    unsafe_allow_html=True,
                )

        st.markdown('<div class="validation-gap"></div>', unsafe_allow_html=True)

        audience_one, audience_two, audience_three = st.columns(3)

        audience_data = [
            (
                "status-critical",
                "Incident responder",
                "Latency is affecting checkout",
                "Immediate condition, direct evidence, and a practical investigation action.",
                "Open investigation →",
            ),
            (
                "status-attention",
                "Platform owner",
                "12 services show elevated dependency wait time",
                "Trend context, relationship visibility, and a system level action.",
                "View service map →",
            ),
            (
                "status-good",
                "Executive partner",
                "Customer impact contained",
                "Material change, operational confidence, and a concise summary action.",
                "Read summary →",
            ),
        ]

        for column, card in zip(
            [audience_one, audience_two, audience_three],
            audience_data,
        ):
            status_class, audience, title, copy, action = card
            with column:
                st.markdown(
                    f"""
                    <section class="workspace-card">
                        <div class="{status_class}">{audience}</div>
                        <h3 style="font-size:1.3rem; margin-top:1.1rem;">{title}</h3>
                        <p>{copy}</p>
                        <div style="margin-top:1.3rem; color:#FFFFFF; font-weight:800;">{action}</div>
                    </section>
                    """,
                    unsafe_allow_html=True,
                )

        st.markdown('<div class="validation-gap"></div>', unsafe_allow_html=True)

        avoid_column, rule_column = st.columns(2)

        with avoid_column:
            st.markdown(
                """
                <section class="insight-card">
                    <h3>What is deliberately avoided</h3>
                    <p>A generic screen that asks every audience to interpret the same volume of information before reaching their decision.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with rule_column:
            st.markdown(
                """
                <section class="insight-card">
                    <h3>System rule</h3>
                    <p>Preserve shared structure. Change only the information depth and action required by the user’s decision context.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

else:
    st.markdown(
        """
        <div class="section-kicker">Validation</div>
        <div class="section-heading">A pattern is ready when its purpose can be tested.</div>
        <p class="section-copy">
            Select a product context to see the evaluation questions that guide
            refinement before a pattern becomes part of a shared system.
        </p>
        """,
        unsafe_allow_html=True,
    )

    validation_context = st.segmented_control(
        "Choose a validation context",
        ["AI investigation", "Monitoring", "Operational summary"],
        default="AI investigation",
        label_visibility="collapsed",
        width="stretch",
    )

    validation_content = {
        "AI investigation": {
            "condition": "Payment service latency exceeds expected range",
            "purpose": "Help a responder understand an AI recommendation before taking action.",
            "clarity": "Can the responder identify the condition, confidence level, supporting evidence, and next action without searching across separate surfaces?",
            "accessibility": "Do written confidence labels, semantic colour, contrast, and reading order communicate the recommendation without relying on colour alone?",
            "consistency": "Does the investigation pattern preserve the familiar sequence of condition, context, evidence, and action?",
            "readiness": "Can confidence, evidence, and actions be expressed through reusable tokens, components, states, and content rules?",
            "status": "Ready for a focused comprehension review",
            "accent": "#2E8B70",
        },
        "Monitoring": {
            "condition": "Request latency moves above baseline after deployment",
            "purpose": "Help a platform owner identify the next useful signal inside a dense monitoring surface.",
            "clarity": "Can the user find the changed condition and its most relevant context before comparing every available metric?",
            "accessibility": "Do hierarchy, labels, contrast, chart annotations, and semantic states remain understandable at different screen sizes?",
            "consistency": "Do cards, chart annotation, and the change summary use familiar visual rules without making every signal compete?",
            "readiness": "Can visual emphasis, metric states, card anatomy, and chart annotation be implemented through reusable component variants?",
            "status": "Ready for density and scanning review",
            "accent": "#D97706",
        },
        "Operational summary": {
            "condition": "Customer impact is contained while remediation continues",
            "purpose": "Help an executive partner understand material status without requiring operational detail they do not need.",
            "clarity": "Can the user identify current impact, confidence in the response, and the next decision without entering an investigation view?",
            "accessibility": "Does plain language, hierarchy, contrast, and clear status wording support quick understanding for a broad audience?",
            "consistency": "Does the summary retain the same system identity while reducing information depth to match the decision context?",
            "readiness": "Can summary language, semantic state, and escalation rules be documented for consistent use across future operational views?",
            "status": "Ready for stakeholder comprehension review",
            "accent": "#632CA6",
        },
    }

    selected = validation_content[validation_context]

    st.markdown(
        f"""
        <section class="workspace">
            <div class="workspace-label">Selected context</div>
            <div class="workspace-title">{validation_context}</div>
            <p style="color:#C9BFD3; font-size:1rem; line-height:1.55; margin:0;">
                {selected["purpose"]}
            </p>
        </section>
        """,
        unsafe_allow_html=True,
    )

    summary_one, summary_two = st.columns([1.5, 1])

    with summary_one:
        st.markdown(
            f"""
            <section class="insight-card">
                <h3>Primary condition</h3>
                <p style="font-size:1.2rem; font-weight:750; color:#212529;">
                    {selected["condition"]}
                </p>
            </section>
            """,
            unsafe_allow_html=True,
        )

    with summary_two:
        st.markdown(
            f"""
            <section class="insight-card">
                <h3>Validation state</h3>
                <p style="color:{selected["accent"]}; font-size:1.05rem; font-weight:800;">
                    {selected["status"]}
                </p>
            </section>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="validation-gap"></div>', unsafe_allow_html=True)

    clarity_column, accessibility_column = st.columns(2)

    with clarity_column:
        st.markdown(
            f"""
            <section class="insight-card">
                <h3>01 Clarity</h3>
                <p>{selected["clarity"]}</p>
            </section>
            """,
            unsafe_allow_html=True,
        )

    with accessibility_column:
        st.markdown(
            f"""
            <section class="insight-card">
                <h3>02 Accessibility</h3>
                <p>{selected["accessibility"]}</p>
            </section>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="validation-gap"></div>', unsafe_allow_html=True)

    consistency_column, readiness_column = st.columns(2)

    with consistency_column:
        st.markdown(
            f"""
            <section class="insight-card">
                <h3>03 Consistency</h3>
                <p>{selected["consistency"]}</p>
            </section>
            """,
            unsafe_allow_html=True,
        )

    with readiness_column:
        st.markdown(
            f"""
            <section class="insight-card">
                <h3>04 Implementation readiness</h3>
                <p>{selected["readiness"]}</p>
            </section>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="validation-gap"></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <section class="workspace">
            <div class="workspace-label">Evaluation principle</div>
            <div class="workspace-title" style="font-size:1.35rem;">
                A pattern is not ready because it looks resolved. It is ready when people can understand,
                use, build, and evolve it with confidence.
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="signal-footer">
        Signal Field is an independent concept exploration created for a job application.
        It uses fictional product content and does not represent Datadog work, products,
        systems, or recommendations.
    </div>
    """,
    unsafe_allow_html=True,
)
