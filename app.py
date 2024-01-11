import streamlit as st


import open3d as o3d
import numpy as np
import plotly.graph_objects as go
import tempfile 
import os

st.title("Point Cloud Downsampler")
tempfile_dir = tempfile.NamedTemporaryFile()
file = st.file_uploader("Choose file")
voxel_size = st.slider("voxel size",0.0,1.0,0.00818)
pcd_file = ""
if file:
    pcd_file = os.path.join(tempfile_dir.name, 'file.ply') 
    with open(tmpfile,"wb") as f:
        f.write(file)

pcd = o3d.io.read_point_cloud(pcd_file)
points = np.asarray(pcd.points)

pcd1 =pcd.voxel_down_sample(voxel_size=0.00818)
points1 = np.asarray(pcd1.points)

print(pcd)
print(pcd1)

fig = go.Figure(
  data=[
    go.Scatter3d(
      x=points[:,0], y=points[:,1], z=points[:,2],
      mode='markers',
      marker=dict(size=2, color=colors)
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
      marker=dict(size=2, color=colors)
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

#fig.show()
#fig1.show()
