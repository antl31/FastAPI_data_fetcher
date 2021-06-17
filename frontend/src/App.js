import React, {useState, useEffect} from "react";
import axios from "axios";
import {Button} from '@material-ui/core';
import GetAppIcon from '@material-ui/icons/GetApp';
import Table from './table';
import './App.css';


function App() {
  const [jobId, setJobId] = useState(null);
  const [data, setData] = useState([]);
  const [status, setStatus] = useState("");

  useEffect(() => {
    console.log('alert');
  }, [])

  const createJobHandler = () => {
    setStatus('started');
    axios.get('http://0.0.0.0:8000/api/book/')
        .then(function (response) {
          // handle success
          console.log(response);
          setJobId(response.data?.data?.job_id);
        })
        .catch(function (error) {
          // handle error
          console.log(error);
        });
  };

  const showStatusHandler = (jobId) => {
    axios.get(`http://0.0.0.0:8000/api/book/job_status/${jobId}`)
        .then(function (response) {
          // handle success
          console.log(response);
          setStatus(response.data.data.status);
        })
        .catch(function (error) {
          // handle error
          console.log(error);
        });
  }

  const downloadHandler = (jobId) => {
    axios.get(`http://0.0.0.0:8000/api/book/result/${jobId}`)
        .then(function (response) {
          // handle success
          console.log(response);
          setData(response.data?.data)
        })
  }


  return (
      <main className="main">
        <header>
          <h1>Outflink - Interview Exercise</h1>
          <Button variant="contained" color="primary" onClick={createJobHandler}>Create job</Button>&nbsp;
          <Button variant="contained" disabled={!jobId} onClick={() => {
            showStatusHandler(jobId);
          }}>Update status</Button>&nbsp;
          <Button color="primary" aria-label="download results" disabled={status !== 'finished'} onClick={() => {
            downloadHandler(jobId)
          }}>
            <GetAppIcon/> Render Table
          </Button>
        </header>
        {jobId && <h2>Job ID: {jobId}</h2>}
        {status && <h3>Status: {status}</h3>}
        <br/>
        <br/>
        <Table rows={data} />
      </main>
  );
}

export default App;
