import axios from 'axios'
import React from 'react'

function EmployeeItem(props){
    const deleteEmployeeHandler = (id) => {
        axios.delete('http://localhost:8000/api/delete_employee/id=${id}')
        .then(res => console.log(res.data)) }
  
    return (
        <div>
            <p>
                <span style={{ fontWeight: 'bold, underline' }}>{props.employee.id} : </span> 
                {props.employee.name} 
                <button onClick={() => deleteEmployeeHandler(props.employee.id)} className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px',}}>X</button>
                <hr></hr>
            </p>
        </div>
    )
}

export default EmployeeItem;