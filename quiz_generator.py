import streamlit as st
import random
from langchain.chains import ConversationalRetrievalChain

def generate_quiz_questions(vector_store, num_questions=5):
    """Generate quiz questions from documents"""
    try:
        # First verify we can access the document content
        docs = vector_store.similarity_search("", k=10)
        if not docs:
            st.error("No document content found.")
            return []
        
        # Show the content we're working with
        st.write("Document content preview:")
        content_preview = docs[0].page_content[:200]
        st.code(content_preview + "...")
        
        # Initialize variables
        questions = []
        used_questions = set()
        attempts = 0
        max_attempts = num_questions * 3  # Allow multiple attempts per question
        
        while len(questions) < num_questions and attempts < max_attempts:
            # Get a different document chunk for each attempt
            doc = docs[attempts % len(docs)]
            
            # Create a focused prompt for this chunk
            prompt = f"""
            Based on this text from the document:
            {doc.page_content[:500]}

            Create ONE multiple-choice question following these rules:
            1. Question must be about specific information from the text above
            2. Correct answer must be found in the text
            3. Create three wrong but plausible answers
            4. Make the question clear and specific

            Format your response exactly like this:
            Question: What is the capital of France?
            Correct: Paris
            Distractors: London, Berlin, Madrid

            Generate a question now:
            """
            
            try:
                with st.spinner(f"Generating question {len(questions) + 1}/{num_questions} (Attempt {attempts + 1})"):
                    # Get response from LLM
                    response = st.session_state.llm(prompt)
                    st.write(f"Debug - Response from LLM (Attempt {attempts + 1}):", response)
                    
                    # Parse response
                    lines = [line.strip() for line in response.split('\n') if line.strip()]
                    question = None
                    correct = None
                    distractors = None
                    
                    for line in lines:
                        if line.startswith('Question:'):
                            question = line[9:].strip()
                        elif line.startswith('Correct:'):
                            correct = line[8:].strip()
                        elif line.startswith('Distractors:'):
                            distractor_text = line[11:].strip()
                            distractors = [d.strip() for d in distractor_text.split(',')]
                    
                    st.write(f"Debug - Parsed question: {question}")
                    st.write(f"Debug - Parsed correct answer: {correct}")
                    st.write(f"Debug - Parsed distractors: {distractors}")
                    
                    # Validate the question
                    if (question and correct and distractors and 
                        len(question) > 10 and 
                        len(correct) > 3 and 
                        len(distractors) >= 3 and 
                        question.lower() not in used_questions):
                        
                        # Verify answer appears in the document
                        if correct.lower() in doc.page_content.lower():
                            used_questions.add(question.lower())
                            all_answers = distractors[:3] + [correct]
                            random.shuffle(all_answers)
                            
                            questions.append({
                                "question": question,
                                "correct": correct,
                                "options": all_answers
                            })
                            
                            st.success(f"✅ Generated question {len(questions)}/{num_questions}")
                        else:
                            st.warning("Answer not found in document section")
                    else:
                        st.warning("Invalid question format or duplicate question")
                
            except Exception as e:
                st.error(f"Error in attempt {attempts + 1}: {str(e)}")
            
            attempts += 1
        
        if not questions:
            st.error("Failed to generate any valid questions.")
            return []
        
        if len(questions) < num_questions:
            st.warning(f"Only generated {len(questions)} questions instead of the requested {num_questions}")
        
        st.write(f"Debug - Final number of questions: {len(questions)}")
        for i, q in enumerate(questions, 1):
            st.write(f"Debug - Question {i}: {q['question']}")
        
        return questions
    
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return []

def show_quiz_tab():
    st.subheader("🎯 Quiz Time!")
    
    if st.session_state.vector_store is None:
        st.info("Please upload some documents in the 'Upload Documents' tab first!")
        return
    
    if 'current_quiz' not in st.session_state:
        st.session_state.current_quiz = None
        st.session_state.quiz_score = 0
        st.session_state.chips = 0
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        num_questions = st.slider("Number of questions:", min_value=3, max_value=10, value=5)
        if st.button("Generate New Quiz"):
            with st.spinner("Generating quiz questions..."):
                questions = generate_quiz_questions(st.session_state.vector_store, num_questions)
                if questions:
                    st.session_state.current_quiz = {
                        'questions': questions,
                        'current_q': 0,
                        'answered': set(),
                        'score': 0
                    }
                    st.session_state.chips = 0
                    st.rerun()
    
    with col2:
        st.metric("💰 Chips Earned", f"£{st.session_state.chips}")
    
    if st.session_state.current_quiz:
        quiz = st.session_state.current_quiz
        current_q = quiz['questions'][quiz['current_q']]
        
        progress = (quiz['current_q'] + 1) / len(quiz['questions'])
        st.progress(progress)
        
        st.write(f"### Question {quiz['current_q'] + 1} of {len(quiz['questions'])}")
        st.write(current_q['question'])
        
        answer = st.radio("Choose your answer:", current_q['options'], key=f"q_{quiz['current_q']}")
        
        if st.button("Submit Answer"):
            if quiz['current_q'] not in quiz['answered']:
                quiz['answered'].add(quiz['current_q'])
                
                if answer == current_q['correct']:
                    st.success("✅ Correct!")
                    quiz['score'] += 1
                    st.session_state.chips += 5
                else:
                    st.error(f"❌ Wrong! The correct answer was: {current_q['correct']}")
                
                if quiz['current_q'] < len(quiz['questions']) - 1:
                    quiz['current_q'] += 1
                    st.rerun()
                else:
                    st.balloons()
                    st.success(f"Quiz complete! You scored {quiz['score']}/{len(quiz['questions'])} and earned £{st.session_state.chips} in chips!")
                    
                    if st.button("Start New Quiz"):
                        st.session_state.current_quiz = None
                        st.rerun()