import streamlit as st

st.set_page_config(
    page_title="Signal Field",
    page_icon="https://corp.dd-static.net/img/favicons/dd-favicon.png",
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
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        .stApp {
            background: #F5F5F5;
            color: #212529;
        }

        .signal-hero {
            background: #110617;
            border-radius: 22px;
            padding: 3.4rem 4rem;
            margin: 0 0 2rem 0;
            color: #FFFFFF;
        }

        .signal-kicker {
            color: #C9BFD3;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 0.75rem;
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
            max-width: 50rem;
            margin: 1.5rem 0 0 0;
        }

        .section-kicker {
            color: #632CA6;
            font-size: 0.76rem;
            font-weight: 800;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin: 2.5rem 0 0.4rem 0;
        }

        .section-heading {
            color: #212529;
            font-size: clamp(1.8rem, 3.5vw, 3rem);
            font-weight: 800;
            letter-spacing: -0.035em;
            line-height: 1.05;
            margin: 0 0 0.8rem 0;
        }

        .section-copy {
            color: #4A4F55;
            font-size: 1.02rem;
            line-height: 1.55;
            max-width: 48rem;
            margin: 0 0 1.4rem 0;
        }

        .workspace {
            background: #110617;
            border-radius: 20px;
            border: 1px solid #3B2E46;
            padding: 1.6rem;
            margin-top: 1rem;
        }

        .workspace-label {
            color: #C9BFD3;
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.5rem;
        }

        .workspace-title {
            color: #FFFFFF;
            font-size: 1.65rem;
            font-weight: 750;
            letter-spacing: -0.025em;
            margin: 0 0 1.25rem 0;
        }

        .workspace-card {
            background: #1D1424;
            border: 1px solid #3B2E46;
            border-radius: 14px;
            padding: 1.2rem;
            min-height: 150px;
            height: 100%;
        }

        .workspace-card h3 {
            color: #FFFFFF;
            font-size: 1rem;
            margin: 0 0 0.55rem 0;
        }

        .workspace-card p {
            color: #C9BFD3;
            font-size: 0.9rem;
            line-height: 1.45;
            margin: 0;
        }

        .metric-value {
            color: #FFFFFF;
            font-size: 2.25rem;
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

        .insight-card {
            background: #FFFFFF;
            border: 1px solid #E1E5E9;
            border-radius: 16px;
            padding: 1.35rem;
            min-height: 180px;
            height: 100%;
        }

        .insight-card h3 {
            color: #632CA6;
            font-size: 1rem;
            margin: 0 0 0.7rem 0;
        }

        .insight-card p {
            color: #4A4F55;
            font-size: 0.94rem;
            line-height: 1.5;
            margin: 0;
        }

        .signal-footer {
            border-top: 1px solid #E1E5E9;
            color: #4A4F55;
            font-size: 0.82rem;
            line-height: 1.45;
            margin-top: 4rem;
            padding: 1.5rem 0 0 0;
        }

        [data-testid="stSegmentedControl"] button {
            border-radius: 999px !important;
            font-weight: 700 !important;
        }

        @media (max-width: 700px) {
            .block-container {
                padding: 1.2rem 1rem 2rem 1rem;
            }

            .signal-hero {
                border-radius: 16px;
                padding: 2.2rem 1.5rem;
            }

            .workspace {
                padding: 1rem;
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

            .insight-card {
                background: #1D1424;
                border-color: #3B2E46;
            }

            .insight-card p {
                color: #C9BFD3;
            }

            .signal-footer {
                border-color: #3B2E46;
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
        ["AI investigation", "Monitoring workspace", "Operational summary"],
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
                    <p style="margin-top: 0.55rem;">Database wait time increased by 22 percent.</p>
                    <p style="margin-top: 0.55rem;">A related deployment occurred 14 minutes ago.</p>
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

        st.markdown("")

        action_one, action_two, action_three, action_space = st.columns([1, 1, 1.2, 1.6])

        with action_one:
            st.button("Inspect evidence", use_container_width=True)

        with action_two:
            st.button("Compare baseline", use_container_width=True)

        with action_three:
            st.button("Create investigation", type="primary", use_container_width=True)

        with action_space:
            st.empty()

        st.markdown("")

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
                    <p>Confidence is not decorative reassurance. It is connected to the signals that make the recommendation credible.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with note_three:
            st.markdown(
                """
                <section class="insight-card">
                    <h3>Action after understanding</h3>
                    <p>Clear next steps appear after the primary condition and evidence, keeping the user in control of the investigation.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

    elif context == "Monitoring workspace":
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

        chart_column, change_column = st.columns([2.2, 1])

        with chart_column:
            st.markdown(
                """
                <section class="workspace-card" style="margin-top:1rem;">
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
                <section class="workspace-card" style="margin-top:1rem;">
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
                    <h3 style="font-size:1.45rem; margin-top:1.2rem;">Latency is affecting checkout</h3>
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
                    <h3 style="font-size:1.45rem; margin-top:1.2rem;">12 services show elevated dependency wait time</h3>
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
                    <h3 style="font-size:1.45rem; margin-top:1.2rem;">Customer impact contained</h3>
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

        with token_one:
            st.markdown(
                """
                <section class="insight-card">
                    <div style="height:52px; border-radius:10px; background:#110617; margin-bottom:1rem;"></div>
                    <h3>Night field</h3>
                    <p>#110617<br>Focused inspection and immersive product fields.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with token_two:
            st.markdown(
                """
                <section class="insight-card">
                    <div style="height:52px; border-radius:10px; background:#632CA6; margin-bottom:1rem;"></div>
                    <h3>Signal violet</h3>
                    <p>#632CA6<br>Primary action, active state, and meaningful direction.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with token_three:
            st.markdown(
                """
                <section class="insight-card">
                    <div style="height:52px; border-radius:10px; background:#8000FF; margin-bottom:1rem;"></div>
                    <h3>Electric violet</h3>
                    <p>#8000FF<br>Rare moments of emphasis and future facing focus.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with token_four:
            st.markdown(
                """
                <section class="insight-card">
                    <div style="height:52px; border-radius:10px; background:#2E8B70; margin-bottom:1rem;"></div>
                    <h3>Confidence</h3>
                    <p>#2E8B70<br>Positive state, paired with clear supporting language.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with token_five:
            st.markdown(
                """
                <section class="insight-card">
                    <div style="height:52px; border-radius:10px; background:#D97706; margin-bottom:1rem;"></div>
                    <h3>Attention</h3>
                    <p>#D97706<br>Unresolved condition, paired with an explanation and next step.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("")

        surface_one, surface_two, surface_three, surface_four = st.columns(4)

        with surface_one:
            st.markdown(
                """
                <section class="insight-card">
                    <div style="height:42px; border-radius:10px; background:#F5F5F5; border:1px solid #E1E5E9; margin-bottom:1rem;"></div>
                    <h3>Cloud surface</h3>
                    <p>#F5F5F5<br>Quiet page fields and secondary surfaces.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with surface_two:
            st.markdown(
                """
                <section class="insight-card">
                    <div style="height:42px; border-radius:10px; background:#FFFFFF; border:1px solid #E1E5E9; margin-bottom:1rem;"></div>
                    <h3>White surface</h3>
                    <p>#FFFFFF<br>Primary reading and working surfaces.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with surface_three:
            st.markdown(
                """
                <section class="insight-card">
                    <div style="height:42px; border-radius:10px; background:#E1E5E9; margin-bottom:1rem;"></div>
                    <h3>Structure line</h3>
                    <p>#E1E5E9<br>Dividers, boundaries, and low emphasis structure.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

        with surface_four:
            st.markdown(
                """
                <section class="insight-card">
                    <div style="height:42px; border-radius:10px; background:#4A4F55; margin-bottom:1rem;"></div>
                    <h3>Quiet graphite</h3>
                    <p>#4A4F55<br>Supporting copy, labels, and metadata.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

    with hierarchy_tab:
        st.markdown("#### The eye needs a reliable path")

        st.markdown(
            """
            <p class="section-copy">
                The system uses hierarchy to move from condition, to context, to action.
                Information may be dense, but its reading order should never be unclear.
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
            st.markdown(
                """
                <section class="insight-card">
                    <h3>01 Condition</h3>
                    <p>The primary condition earns the largest type and strongest contrast.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
                <section class="insight-card">
                    <h3>02 Context</h3>
                    <p>Evidence and confidence explain why the condition deserves attention.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
                <section class="insight-card">
                    <h3>03 Action</h3>
                    <p>A clear next step follows understanding rather than replacing it.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

    with spacing_tab:
        st.markdown("#### Space gives information room to be understood")

        st.markdown(
            """
            <p class="section-copy">
                Signal Field uses a four point rhythm. The purpose is not visual decoration.
                Consistent spacing creates scan paths, separates tasks, and helps dense content breathe.
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

        st.markdown(
            """
            <section class="workspace" style="margin-top:1.5rem;">
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
            st.markdown(
                """
                <section class="insight-card">
                    <h3>01 Context</h3>
                    <p>Names the source or type of information.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
                <section class="insight-card">
                    <h3>02 State</h3>
                    <p>Communicates confidence or urgency with colour and written meaning.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
                <section class="insight-card">
                    <h3>03 Evidence</h3>
                    <p>Explains the condition with concise, inspectable signals.</p>
                </section>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
                <section class="insight-card">
                    <h3>04 Action</h3>
                    <p>Moves the user forward after they have enough context to act.</p>
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
            The next page will explain how Signal Field balances visible AI reasoning,
            useful information density, and contextual adaptation.
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.info("Decision content is the next build step.")

else:
    st.markdown(
        """
        <div class="section-kicker">Validation</div>
        <div class="section-heading">A pattern is ready when it can be evaluated clearly.</div>
        <p class="section-copy">
            The next page will show how the system is assessed for clarity, accessibility,
            consistency, and implementation readiness across product contexts.
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.info("Validation content is the next build step.")

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
