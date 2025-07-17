import React, {useRef,useState} from "react";
import axios from "axios";
const WebcamFeed=()=>{
    const videoRef=useRef(null);
    const recordRef=useRef(null);
    const storeRef=useRef([]);
    const [message,setMessage]=useState("");
    const [recordings,setRecordings]=useState([]);
    const startCamera=async()=>{
        try{
        const stream=await navigator.mediaDevices.getUserMedia({video:true});
        videoRef.current.srcObject=stream;
        videoRef.current.play();
        setMessage("webcam started");
        }
        catch(err){
            setMessage(`error: ${err}`);
        }
    }
    const startRecording=()=>{
        const stream=videoRef.current.srcObject;
        if(!stream){
            setMessage("please ,turn on your camera");
            return;
        }
        const recorder=new MediaRecorder(stream);
        storeRef.current=[];
        recorder.ondataavailable=(e)=>{
            if(e.data&& e.data.size>0){
                storeRef.current.push(e.data);
            }
        };
        recorder.onstop=async()=>{
            const videoblob=new Blob(storeRef.current,{type:"video/webm"});
            setRecordings((prev)=>[...prev,videoblob]);
            setMessage("Recording stopped and saved");
            try{
                const formData=new FormData();
                formData.append("video",videoblob);

                await axios.post("http://localhost:8000/upload-video",formData,{
                    headers:{
                        "content-Type":"multipart/form-data"
                    }
                });
                setMessage("video sent to api successfully"); 
            }
            catch(err){
                setMessage(`unable to sent to api ${err}`)
            }
        };
            recordRef.current=recorder;
            recorder.start();
            setMessage("Recording started");

        };
    const stopRecording=()=>{
            if (recordRef.current && recordRef.current.start !== "inactive") {
                recordRef.current.stop();
            }
        }
    return(
        <div>
            <h2>webcam recorder</h2>
            <video ref={videoRef} autoPlay></video>
            <div>
                <button onClick={startCamera}>start Camera</button>
                <button onClick={startRecording}>record</button>
                <button onClick={stopRecording}>stop</button>
            </div>
            <p>{message}</p>
            {recordings.length>0 &&(
                <div>
                    <h3>saved recordings</h3>
                    {recordings.map((blob,index)=>(
                        <video key={index} controls width="300">
                            <source src={URL.createObjectURL(blob)} type="video/webm" />
                            your browser does not support the video tag
                        </video>
                    ))}
                    </div>
            )}
        </div>    
    );
};
export default WebcamFeed;