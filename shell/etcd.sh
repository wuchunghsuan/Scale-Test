#!/bin/bash
REGISTRY=quay.io/coreos/etcd

ETCD_VERSION=latest
TOKEN=incongruous
CLUSTER_STATE=new
NAME_1=etcd-node-0
NAME_2=etcd-node-1
NAME_3=etcd-node-2
NAME_4=etcd-node-3
NAME_5=etcd-node-4
NAME_6=etcd-node-5
HOST_1=10.11.0.101
HOST_2=10.11.0.102
HOST_3=10.11.0.103
HOST_4=10.11.0.104
HOST_5=10.11.0.105
HOST_6=10.11.0.106
CLUSTER=${NAME_1}=http://${HOST_1}:2380,${NAME_2}=http://${HOST_2}:2380,${NAME_3}=http://${HOST_3}:2380,${NAME_4}=http://${HOST_4}:2380,${NAME_5}=http://${HOST_5}:2380,${NAME_6}=http://${HOST_6}:2380

DATA_DIR=/home/wuchunghsuan/etcd

THIS_NAME=${NAME_1}
THIS_IP=${HOST_1}
docker run \
  -p 2379:2379 \
  -p 2380:2380 \
  -d \
  --net=net1 \
  --hostname ${THIS_NAME} \
  --ip ${THIS_IP} \
  --volume=${DATA_DIR}:/etcd-data \
  --name etcd ${REGISTRY}:${ETCD_VERSION} \
  /usr/local/bin/etcd \
  --data-dir=/etcd-data --name ${THIS_NAME} \
  --initial-advertise-peer-urls http://${THIS_IP}:2380 --listen-peer-urls http://0.0.0.0:2380 \
  --advertise-client-urls http://${THIS_IP}:2379 --listen-client-urls http://0.0.0.0:2379 \
  --initial-cluster ${CLUSTER} \
  --initial-cluster-state ${CLUSTER_STATE} --initial-cluster-token ${TOKEN}
