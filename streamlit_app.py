import requests,streamlit as st
st.set_page_config(page_title='College AI Assistant',page_icon='🎓')
st.title('🎓 College Campus AI Assistant')
st.caption('Ask about students, staff, departments and attendance.')
with st.sidebar:
    api=st.text_input('AI API URL','http://127.0.0.1:8000').rstrip('/')
    if st.button('Check backend'):
        try:
            d=requests.get(api+'/health',timeout=5).json()
            st.success('AI API running')
            st.write('ERP available:',d.get('erp_available'))
        except requests.RequestException as e: st.error(str(e))
    examples=['How many students are studying in the college?','Show student ID 1001 details.','List students in Computer Science.','Show staff details of Information Technology.','Who is the class teacher for Computer Science?','Summarize the attendance report.']
    for q in examples:
        if st.button(q,use_container_width=True): st.session_state.pending=q
if 'messages' not in st.session_state: st.session_state.messages=[]
for m in st.session_state.messages:
    with st.chat_message(m['role']): st.markdown(m['content'])
prompt=st.chat_input('Ask your college ERP question...')
if st.session_state.get('pending'):
    prompt=st.session_state.pop('pending')
if prompt:
    st.session_state.messages.append({'role':'user','content':prompt})
    with st.chat_message('user'): st.markdown(prompt)
    with st.chat_message('assistant'):
        try:
            r=requests.post(api+'/chat',json={'question':prompt},timeout=90)
            r.raise_for_status()
            d=r.json(); answer=d['answer']; st.markdown(answer)
            if d.get('tools_used'): st.caption('ERP tools: '+', '.join(d['tools_used']))
            st.session_state.messages.append({'role':'assistant','content':answer})
        except requests.RequestException as e:
            answer=f'Unable to connect: {e}'; st.error(answer)
            st.session_state.messages.append({'role':'assistant','content':answer})
