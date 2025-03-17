# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Write directly to the app
session = get_active_session()

st.title(":snowflake: Snowflake User Creation :snowflake:",anchor = False)
st.divider()
# Get the current credentials



form1 = st.form("user_form", clear_on_submit = False, border = True)
with form1:
    
    user_name = st.text_input("Username")
    user_password = st.text_input("Password")
    user_email = st.text_input("Email")
    user_first = st.text_input("First Name")
    user_last = st.text_input("Last Name")
    user_warehouse = st.text_input("Warehouse Name")
    user_role = st.text_input("Default Role")
    user_comment = st.text_input("Comment")
    
    pass_change = st.checkbox("Must Change Password",value=True)
    sec_roles = st.checkbox("Secondary Roles",value=True)

    st.divider()
    send_code = st.checkbox("Execute SQL")
    

    
    if st.form_submit_button("Generate SQL"):
        SQL_STR = f"CREATE USER {user_name}\n"
        if user_password:
            SQL_STR += f"\tPASSWORD = '{user_password}'\n"
        if user_email:
            SQL_STR += f"\tEMAIL = '{user_email}'\n"
        if user_first:
            SQL_STR += f"\tFIRST_NAME = '{user_first}'\n"
        if user_last:
            SQL_STR += f"\tLAST_NAME = '{user_last}'\n"
        SQL_STR += f"\tMUST_CHANGE_PASSWORD = {pass_change}\n"
        if sec_roles:
            SQL_STR += f"\tDEFAULT_SECONDARY_ROLES = ()\n"
        if user_comment:
            SQL_STR += f"\tCOMMENT = '{user_comment}'"
        if user_warehouse:
            SQL_STR += f"DEFAULT WAREHOUSE = {user_warehouse}\n"
        if user_role:
            SQL_STR += f"DEFAULT ROLE = {user_role}\n"
        SQL_STR += ';\n'
        if user_warehouse:
            SQL_STR += f"GRANT WAREHOUSE {user_warehouse};\n"
        if user_role:
            SQL_STR += f"GRANT ROLE {user_role} TO  USER {user_name};"
        st.code(SQL_STR,language='sql',wrap_lines=True)
        if send_code == True:
            #session.sql("USE ROLE SECURITYADMIN;")
            output = session.sql(f"SELECT 'CREATED USER {user_name.upper()}'").collect()
            st.write(output)
        
