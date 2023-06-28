@REM mkdir ChatSalesMaster
@REM cd ChatSalesMaster

mkdir main
cd main

mkdir agent
cd agent
echo. > receive_user_input.py
echo. > determine_current_stage.py
echo. > add_user_input_to_history.py
echo. > call_stage_chain.py
echo. > call_speech_chain.py
echo. > output_message.py
cd ..

mkdir stage_chain
cd stage_chain
echo. > determine_stage.py
cd ..

mkdir speech_chain
cd speech_chain
echo. > generate_message.py
cd ..

mkdir qa_template
cd qa_template
echo. > get_template.py
cd ..

mkdir llm
cd llm
echo. > configure_llm.py
cd ..

cd ..

mkdir db
cd db

mkdir customer_db
cd customer_db
echo. > add_customer.py
echo. > delete_customer.py
echo. > get_customer.py
cd ..

mkdir history_db
cd history_db
echo. > add_history.py
echo. > delete_history.py
echo. > get_history.py
cd ..

mkdir task_db
cd task_db
echo. > add_task.py
echo. > delete_task.py
echo. > get_task.py
cd ..

cd ..

mkdir parts
cd parts

mkdir reservation
cd reservation
echo. > add_reservation.py
echo. > get_reservation.py
cd ..

mkdir gmail
cd gmail
echo. > send_email.py
cd ..

cd ..

@REM cd ChatSalesMaster

cd main
echo. > __init__.py
cd agent
echo from .receive_user_input import receive_user_input > __init__.py
echo from .determine_current_stage import determine_current_stage >> __init__.py
echo from .add_user_input_to_history import add_user_input_to_history >> __init__.py
echo from .call_stage_chain import call_stage_chain >> __init__.py
echo from .call_speech_chain import call_speech_chain >> __init__.py
echo from .output_message import output_message >> __init__.py
cd ..

cd stage_chain
echo. > __init__.py
echo from .determine_stage import determine_stage > __init__.py
cd ..

cd speech_chain
echo. > __init__.py
echo from .generate_message import generate_message > __init__.py
cd ..

cd qa_template
echo. > __init__.py
echo from .get_template import get_template > __init__.py
cd ..

cd llm
echo. > __init__.py
echo from .configure_llm import configure_llm > __init__.py
cd ..

cd ..

cd db
echo. > __init__.py
cd customer_db
echo. > __init__.py
echo from .add_customer import add_customer > __init__.py
echo from .delete_customer import delete_customer >> __init__.py
echo from .get_customer import get_customer >> __init__.py
cd ..

cd history_db
echo. > __init__.py
echo from .add_history import add_history > __init__.py
echo from .delete_history import delete_history >> __init__.py
echo from .get_history import get_history >> __init__.py
cd ..

cd task_db
echo. > __init__.py
echo from .add_task import add_task > __init__.py
echo from .delete_task import delete_task >> __init__.py
echo from .get_task import get_task >> __init__.py
cd ..

cd ..

cd parts
echo. > __init__.py
cd reservation
echo. > __init__.py
echo from .add_reservation import add_reservation > __init__.py
echo from .get_reservation import get_reservation >> __init__.py
cd ..

cd gmail
echo. > __init__.py
echo from .send_email import send_email > __init__.py
cd ..

cd ..
