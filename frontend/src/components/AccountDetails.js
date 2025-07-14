import React, { useState } from 'react';
import axios from 'axios';

const AccountDetails= () => {
  const [accountNo, setAccountNo] = useState('');
  const [account, setAccount] = useState(null);
  const [error, setError] = useState('');
  const handleChange = (e) => {
    setAccountNo(e.target.value);
  };
  const handleFetch = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.get(`http://localhost:8000/account/${accountNo}`);
      setAccount(res.data);    
      setError('');            
    } catch (err) {
      setAccount(null);        
      setError(err.response?.data?.detail || err.message);
    }
  };

  return (
    <form onSubmit={handleFetch}>
      <h2>Account Details</h2>

      <label>Account Number:</label><br />
      <input
        type="text" value={accountNo} onChange={handleChange}/><br />
      <button type="submit">Fetch</button><br />

      {error && <p>{error}</p>}
      {account && (
        <div>
          <p>Account No: {account.account_no}</p>
          <p>Name: {account.name}</p>
          <p>Age: {account.age}</p>
          <p>Branch: {account.branch}</p>
          <p>Balance: {account.balance}</p>
        </div>
      )}
    </form>
  );
};

export default AccountDetails;
