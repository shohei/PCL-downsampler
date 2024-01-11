import streamlit as st


import open3d as o3d
import numpy as np
import plotly.graph_objects as go
import tempfile 
import os

st.title("Point Cloud Downsampler")
tempfile_dir = tempfile.TemporaryDirectory()
file = st.file_uploader("Choose file")

if file is not None:
    pcd_file_path = os.path.join(tempfile_dir.name, 'file.ply') 
    st.text(pcd_file_path)
    with open(pcd_file_path,"wb") as f:
        f.write(file.getbuffer())

    voxel_size_rate = st.slider("voxel size",0,100,50)
    voxel_max = 0.05
    voxel_size = voxel_size_rate/100.0 * voxel_max
    
    pcd = o3d.io.read_point_cloud(pcd_file_path)
    points = np.asarray(pcd.points)
    
    pcd1 =pcd.voxel_down_sample(voxel_size=voxel_size)
    points1 = np.asarray(pcd1.points)
    
    print(pcd)
    print(pcd1)
    print("voxel_size",voxel_size)
    
    fig = go.Figure(
      data=[
        go.Scatter3d(
          x=points[:,0], y=points[:,1], z=points[:,2],
          mode='markers',
          #marker=dict(size=2, color=colors)
          marker=dict(size=2)
    )
    ],
      layout=dict(
        scene=dict(
          xaxis=dict(visible=False),
          yaxis=dict(visible=False),
          zaxis=dict(visible=False)
    )
    )
    )
    
    fig1 = go.Figure(
      data=[
        go.Scatter3d(
          x=points1[:,0], y=points1[:,1], z=points1[:,2],
          mode='markers',
          #marker=dict(size=2, color=colors)
          marker=dict(size=2)
    )
    ],
      layout=dict(
        scene=dict(
          xaxis=dict(visible=False),
          yaxis=dict(visible=False),
          zaxis=dict(visible=False)
    )
    )
    )
    
    st.text(pcd)
    st.plotly_chart(fig, use_container_width=True)
    st.text(pcd1)

    f1 = st.empty()
    f1.plotly_chart(fig1, use_container_width=True)
