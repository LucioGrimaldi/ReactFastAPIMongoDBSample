import axios from 'axios'
import React from 'react'

function EmployeeItem(props){
    const deleteEmployeeHandler = (id) => {
        axios.delete('http://localhost:8000/api/delete_employee/id=' + id)
        .then(res => console.log(res.data)) }
  
    return (
        <div>
            <p>
                <span style={{ fontWeight: 'bold, underline' }}>id = {props.employee.id} , name = {props.employee.name} , surname = {props.employee.surname} , address = {props.employee.address} , phone_number = {props.employee.phone_number}</span> 
                 
                
                <button onClick={() => deleteEmployeeHandler(props.employee.id)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px',}}>delete</button>
                <hr></hr>
            </p>
        </div>
    )
}

export default EmployeeItem;