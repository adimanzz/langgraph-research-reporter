from graph_setup import build_graph
import streamlit as st

st.set_page_config(page_title="Report Generator")
st.title("Research Report Generator")

st.markdown("Enter a research query (eg: coordinates or topic) to generate a report.")

query = st.text_input("Enter your query")

if st.button("Generate Report"):
    if query.strip():
        with st.spinner("Agents collaborating... please hold on."):
            try:
                graph = build_graph()
                result = graph.invoke({"query": query})
                st.success("Report is ready!")
                st. markdown("### Summary Report")
                st.write(result["report"])
            except Exception as ex:
                st.error(f"Error: {ex}")
    else:
        st.warning("please enter a valid query.")

