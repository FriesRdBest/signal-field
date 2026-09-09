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

        .stApp {
            background: #F5F5F5;
            color: #212529;
        }

        .signal-hero {
            background: #110617;
            border-radius: 20px;
            padding: 3.5rem 4rem;
            margin: 0 0 2rem 0;
            color: #FFFFFF;
        }

        .signal-kicker {
            color: #C9BFD3;
            font-size: 0.85rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.8rem;
        }

        .signal-hero h1 {
            color: #FFFFFF;
            font-size: clamp(2.6rem, 6vw, 5.5rem);
            font-weight: 800;
            letter-spacing: -0.04em;
            line-height: 0.98;
            margin: 0;
        }

        .signal-hero p {
            color: #D9D0E5;
            font-size: 1.2rem;
            line-height: 1.55;
            max-width: 48rem;
            margin: 1.5rem 0 0 0;
        }

        .signal-card {
            background: #FFFFFF;
            border: 1px solid #E1E5E9;
            border-radius: 16px;
            padding: 1.5rem;
            min-height: 170px;
            margin-bottom: 1rem;
        }

        .signal-card h3 {
            color: #632CA6;
            font-size: 1.05rem;
            margin: 0 0 0.6rem 0;
        }

        .signal-card p {
            color: #4A4F55;
            font-size: 0.98rem;
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

        @media (prefers-color-scheme: dark) {
            .stApp {
                background: #110617;
                color: #F7F3FA;
            }

            .signal-card {
                background: #1D1424;
                border-color: #3B2E46;
            }

            .signal-card p,
            .signal-footer {
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
            An interactive companion exploring how visual direction can help
            people find meaning, orientation, and confidence in complex AI
            product experiences.
        </p>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown("### Explore the system")

col_one, col_two, col_three, col_four = st.columns(4)

with col_one:
    st.markdown(
        """
        <section class="signal-card">
            <h3>Explore</h3>
            <p>See one visual language adapt across an AI investigation, monitoring workspace, and operational summary.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )

with col_two:
    st.markdown(
        """
        <section class="signal-card">
            <h3>System</h3>
            <p>Inspect the tokens, hierarchy, semantic colour, spacing, and component rules behind the direction.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )

with col_three:
    st.markdown(
        """
        <section class="signal-card">
            <h3>Decisions</h3>
            <p>Understand the tradeoffs behind visible AI reasoning, useful density, and contextual adaptation.</p>
        </section>
        """,
        unsafe_allow_html=True,
    )

with col_four:
    st.markdown(
        """
        <section class="signal-card">
            <h3>Validation</h3>
            <p>Review the criteria used to assess clarity, accessibility, consistency, and implementation readiness.</p>
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
