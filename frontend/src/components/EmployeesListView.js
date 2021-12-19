import EmployeeItem from "./Employee";

export default function EmployeesView(props) {
    return (
        <div>
            <ul>
                {props.employeesList.map(employee => <EmployeeItem employee={employee} />)}
            </ul>
        </div>
    )
}