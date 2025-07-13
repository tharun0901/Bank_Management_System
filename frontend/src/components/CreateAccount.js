import React,{useState} from 'react';
import axios from 'axios';
const CreateAccountForm =()=>{
    const [form,setForm]=useState({
        name:"",
        age:"",
        branch:"",
        account_no:"",
        balance:"",
    });
    const [message,setMessage]=useState("");
    const handleChange=(e)=>{
        setForm({
            ...form,
            [e.target.name]:e.target.value
        });
    };
    const handleSubmit=async(e)=>{
        e.preventDefault();
        try{
            const res=await axios.post('http://localhost:8000/create_account',{
                name: form.name,
                age: parseInt(form.age),              
                branch: form.branch,
                account_no: form.account_no,
                balance: parseFloat(form.balance),
            });
            setMessage(res.data.message);
        }catch(error){
            setMessage(error.response?.data?.detail || error.message);
        }
    };
    return(
        <form onSubmit={handleSubmit}>
            <h2>Create bank Account</h2>
            <label>Name:</label><br />
            <input type="text" name="name" value={form.name} onChange={handleChange}/><br></br>
            <label>Age:</label><br />
            <input type="number" name="age" value={form.age} onChange={handleChange}/><br />
            <label>Branch:</label><br />
            <input type="text" name="branch" value={form.branch} onChange={handleChange}/><br />
            <label>Account Number:</label><br />
            <input type="text" name="account_no" value={form.account_no} onChange={handleChange}/><br />
            <label> Balance:</label><br />
            <input type="number" name="balance" value={form.balance} onChange={handleChange}/><br />
            <button type="submit">Create Account</button><br />
            {message && <p>{message}</p>}

        </form>
    );
}
export default CreateAccountForm;