import React, { useEffect, useState } from "react";
import Sidebar from "../components/Sidebar";

function Gallery() {

  const [photos, setPhotos] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/photos")
      .then((res) => res.json())
      .then((data) => {
        setPhotos(data);
      })
      .catch((error) => {
        console.error("Error loading photos:", error);
      });
  }, []);

  return (
    <div style={{ display: "flex" }}>

      <Sidebar />

      <div style={{ marginLeft: "40px", marginTop: "40px" }}>
        <h1>Photo Gallery</h1>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(3, 1fr)",
            gap: "20px",
            marginTop: "20px"
          }}
        >

          {photos.map((photo) => (
            <div key={photo.id} style={{ textAlign: "center" }}>

              <img
                src={`http://localhost:5000${photo.image_url}`}
                alt="photo"
                width="200"
                style={{
                  border: "3px solid #ddd",
                  borderRadius: "10px"
                }}
              />

              <p><b>Age:</b> {photo.age ? photo.age : "Unknown"}</p>
              <p><b>Gender:</b> {photo.gender ? photo.gender : "Unknown"}</p>

            </div>
          ))}

        </div>
      </div>

    </div>
  );
}

export default Gallery;