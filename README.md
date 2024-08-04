# inception
---
# Table of content


1. [Containers](#containers)
    1. [Container overview](#container-overview)
    2. [Dive into containers](#dive-into-containers)
        1. [Namespaces](#namespaces)
        2. [Cgroups](#cgroups)
        3. [Capabilities](#capabilities)
    3. [Difference between container and VM](#difference-between-container-and-VMS)
2. [Docker]()
    1. []()
    2. []()
3. []()

<!-- curl --ftp-ssl -k -u sabat ftp://vsftpd/ -->
---
# Containers

## **Container overview**

Containers are packages of software that contain all of the necessary elements to run in any environment. In this way, containers virtualize the operating system and run anywhere, from a private data center to the public cloud or even on a developer’s personal laptop. 

**key features :**

- A container is a lightweight, standalone, and executable software package that includes everything needed to run a piece of software, including the code, a runtime, libraries, environment variables, and config files.

- Containers provide a consistent and reproducible environment, which makes it easier to develop, test, and deploy applications across different environments and platforms.

- Containers are isolated from each other and from the host system. Each container runs in its own namespace, which means it has its own view of the operating system, processes, file system, network, and mounted volumes.

- Containers use the host system's kernel and resources, but they do not require a full operating system per application like virtual machines do. This makes them more lightweight and efficient than virtual machines.

- Containers can be managed by container orchestration tools like Kubernetes, which handle deployment, scaling, networking, and availability of containers.

- The concept of a container as an isolated running process is fundamental to container technologies like Docker, LXC, and others.

### **Dive into containers**
#### **Namespaces**

In the context of containers, a namespace is a technology that provides isolation for running processes. Each aspect of a container runs in a separate namespace and its access is limited to that namespace. 

Namespaces are a feature of the Linux kernel that partitions kernel resources such that one set of processes sees one set of resources while another set of processes sees a different set of resources. The feature works by having the same namespace for a set of resources and processes, but those namespaces refer to distinct resources. 

Resources may be various aspects of a system like network access, process IDs, user IDs, and filesystems. 

For example, the PID namespace isolates the process ID number space, meaning that processes in different PID namespaces can have the same PID. Or, the network namespace isolates network interfaces, so containers can have their own virtual network interfaces and IP addresses.

Namespaces provide the isolation that makes containers possible, so each container can run its own isolated processes, have its own network configuration, its own users, and its own filesystem.

#### **Cgroups**


#### **Capabilities**

## Diff between hypervisor and namspaces
A hypervisor, also known as a virtual machine monitor, is a type of software that creates and runs virtual machines. It allows multiple operating systems to share a single hardware host. Each operating system appears to have the host's processor, memory, and other resources all to itself. However, the hypervisor is actually controlling the host processor and resources, allocating what is needed to each operating system in turn and making sure that the guest operating systems (called "virtual machines") cannot disrupt each other.

On the other hand, a namespace is a feature of the Linux kernel that isolates and partitions kernel resources for processes. It's a key technology used in containers, which are a lightweight alternative to virtual machines. Unlike virtual machines, containers do not have their own kernels or virtualize hardware. Instead, they share the host system's kernel and isolate the application processes using namespaces.

So, while both hypervisors and namespaces are used to create isolated environments, they operate at different levels and are not the same thing.


# resources
- [Use containers to Build, Share and Run your applications](https://www.docker.com/resources/what-container/)