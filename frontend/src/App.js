import './App.css';
import React, {useState, useEffect} from 'react';
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.min.css'
import EmployeesView from './components/EmployeesListView';

function App() {

  const [employeesList, setEmployeeList] = useState([{}])
  const [id, setId] = useState('') 
  const [name, setName] = useState('')
  const [surname, setSurname] = useState('')
  const [address, setAddress] = useState('')
  const [phone_number, setPhoneNumber] = useState('')

  // Read all employees after every render
  useEffect(() => {
    axios.get('http://localhost:8000/api/get_employees_list')
      .then(res => {
        setEmployeeList(res.data)
      })
  });

  const updateEmployeeList = () => {
  axios.get('http://localhost:8000/api/get_employees_list')
      .then(res => setEmployeeList(res.data))
    };

  // Post an employee
  const addEmployeeHandler = () => {
    axios.post('http://localhost:8000/api/add_employee/', { 'id': id, 'name': name, 'surname': surname, 'address': address, 'phone_number': phone_number })
      .then(res => console.log(res))
  };

  return (
  <div className="App list-group-item  justify-content-center align-items-center mx-auto" style={{"width":"600px", "backgroundColor":"white", "marginTop":"15px"}} >
      <h1 className="card text-white bg-primary mb-1" styleName="max-width: 20rem;">React-FastAPI-MongoDB Sample</h1>
     <div className="card-body">
      <h5 className="card text-white bg-dark mb-3">Create new employee</h5>
      <span className="card-text"> 
        <input className="mb-2 form-control titleIn" onChange={event => setId(event.target.value)} placeholder='Id'/> 
        <input className="mb-2 form-control desIn" onChange={event => setName(event.target.value)}   placeholder='Name'/>
        <input className="mb-2 form-control desIn" onChange={event => setSurname(event.target.value)}   placeholder='Surname'/>
        <input className="mb-2 form-control desIn" onChange={event => setAddress(event.target.value)}   placeholder='Address'/>
        <input className="mb-2 form-control desIn" onChange={event => setPhoneNumber(event.target.value)}   placeholder='Phone Number'/>
      <button className="btn btn-outline-primary mx-2 mb-3" style={{'borderRadius':'50px',"font-weight":"bold"}}  onClick={addEmployeeHandler}>Add employee</button>
      <button className="btn btn-outline-primary mx-2 mb-3" style={{'borderRadius':'50px',"font-weight":"bold"}}  onClick={updateEmployeeList}>Update list</button>
      </span>
      <h5 className="card text-white bg-dark mb-3">Employees list</h5>
      <div >
      <EmployeesView employeesList={employeesList} />
      </div>
      </div>
      <h6 className="card text-dark bg-warning py-1 mb-0" >Created by Lucio Grimaldi</h6>
    </div>
  );
}

export default App;
