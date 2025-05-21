import streamlit as st
import requests

# Page configuration
st.set_page_config(page_title="Smart Medical Bot", layout="centered")

# Title and instructions
st.title("🤖 Smart Medical Bot")
st.markdown("Enter the symptoms you're experiencing, and the bot will give you an initial medical suggestion.")

# Text input
user_input = st.text_input("✍️ Enter your symptoms:")

# Submit button
if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter your symptoms before submitting.")
    else:
        # API endpoint and headers
        url = "https://udify.app/chat/BXE7UHClh3Liaf7T"
        headers = {
            "Authorization": "Bearer app-MvMNfrvLnaD8mR9eKbP1Q4I1",
            "Content-Type": "application/json"
        }

        # Payload
        payload = {
            "inputs": user_input,
            "response_mode": "blocking"
        }

        # Send request
        with st.spinner("⏳ Please wait..."):
            try:
                response = requests.post(url, json=payload, headers=headers)
                response.raise_for_status()  # Raises error for bad responses (4xx or 5xx)

                # Try to parse JSON response
                try:
                    result = response.json()
                    reply = result.get("answer") or result.get("response") or "No answer received from the bot."
                except ValueError:
                    reply = response.text  # If not JSON, show raw response

                # Show reply
                st.success("🩺 Bot's Response:")
                st.write(reply)

            except requests.exceptions.HTTPError as e:
                st.error(f"🚫 HTTP error occurred: {e}")
                st.code(response.text)

            except requests.exceptions.RequestException as e:
                st.error(f"🚨 An error occurred while contacting the bot: {e}")
