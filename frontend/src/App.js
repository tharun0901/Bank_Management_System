import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import CreateAccountForm from './components/CreateAccount';
import DepositForm from './components/Deposit';
import WithdrawForm from './components/Withdraw';
import AccountDetails from './components/AccountDetails';
import WebcamFeed from './components/Webcam';

function App() {
  return (
    <Router>
      <div>
       <h1>Bank Management System </h1>
       <nav>
        <Link to="/create">Create Account</Link> <br/>
        <Link to="/account">Account Details</Link><br/>
        <Link to ="/deposit">Deposit</Link><br/>
        <Link to= "/withdraw">Withdraw</Link><br/>
        <Link to="/webcam">Webcam</Link><br/>

       </nav>
       <Routes>
        <Route path="/create" element={<CreateAccountForm />} />
        <Route path="/account" element={<AccountDetails/>}/>
        <Route path="/deposit" element={<DepositForm />} />
        <Route path="/withdraw" element={<WithdrawForm />} />
        <Route path="/webcam" element={<WebcamFeed/>}/>
       </Routes>
    </div>
    </Router>

    
  );
}

export default App;

