 import React,{useState} from 'react';
 import axios from 'axios';
 const DepositForm=()=>{
    const[form,setForm]=useState({
        account_no:'',
        amount:'',
    });
    const[message,setMessage]=useState('');
    const handleChange=(e)=>{
        setForm({
            ...form,
            [e.target.name]:e.target.value
        });
    };
    const handleSubmit=async(e)=>{
        e.preventDefault();
        try{
            const res=await axios.post('http://localhost:8000/deposit',{
                account_no:form.account_no,amount:parseFloat(form.amount)
            });
            setMessage(`Amount Credited of ${res.data.amount} to ${res.data.account_no}.Total balance rs.${res.data.new_balance} `);
        }catch(error){
           setMessage(error.response?.data?.detail || error.message);
        }
    }
    return(
        <form onSubmit={handleSubmit}>
            <h2>Deposit Money</h2>
            <label>Account Number</label><br />
            <input type="text" name="account_no" value={form.account_no} onChange={handleChange}/><br />
            <label>Amount:</label><br />
            <input type="text" name="amount" value={form.amount} onChange={handleChange}/><br />
            <button type="submit">Deposit</button><br/>
            {message &&<p>{message}</p>}
        </form>
    )
 };
 export default DepositForm