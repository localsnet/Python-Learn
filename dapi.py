#!/usr/bin/python3
import docker
client = docker.from_env()
conlist=[]
for container in docker.from_env().containers.list():
  print(container.name)
  conlist.append(container.name)
print(conlist)
