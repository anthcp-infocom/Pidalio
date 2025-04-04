# generated by datamodel-codegen:
#   filename:  openapi-v2.json
#   timestamp: 2021-04-29T07:54:09+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, conint, constr

from ...k8s.apimachinery.pkg.apis.meta import v1


class Cores(BaseModel):
    max: int
    min: conint(ge=0)


class Gpu(BaseModel):
    max: conint(ge=1)
    min: conint(ge=0)
    type: constr(min_length=1)


class Memory(BaseModel):
    max: int
    min: conint(ge=0)


class ResourceLimits(BaseModel):
    cores: Optional[Cores] = Field(
        None,
        description='Minimum and maximum number of cores in cluster, in the format <min>:<max>. Cluster autoscaler will not scale the cluster beyond these numbers.',
    )
    gpus: Optional[List[Gpu]] = Field(
        None,
        description='Minimum and maximum number of different GPUs in cluster, in the format <gpu_type>:<min>:<max>. Cluster autoscaler will not scale the cluster beyond these numbers. Can be passed multiple times.',
    )
    maxNodesTotal: Optional[conint(ge=0)] = Field(
        None,
        description='Maximum number of nodes in all node groups. Cluster autoscaler will not grow the cluster beyond this number.',
    )
    memory: Optional[Memory] = Field(
        None,
        description='Minimum and maximum number of gigabytes of memory in cluster, in the format <min>:<max>. Cluster autoscaler will not scale the cluster beyond these numbers.',
    )


class ScaleDown(BaseModel):
    delayAfterAdd: Optional[constr(regex=r'([0-9]*(\.[0-9]*)?[a-z]+)+')] = Field(
        None, description='How long after scale up that scale down evaluation resumes'
    )
    delayAfterDelete: Optional[constr(regex=r'([0-9]*(\.[0-9]*)?[a-z]+)+')] = Field(
        None,
        description='How long after node deletion that scale down evaluation resumes, defaults to scan-interval',
    )
    delayAfterFailure: Optional[constr(regex=r'([0-9]*(\.[0-9]*)?[a-z]+)+')] = Field(
        None,
        description='How long after scale down failure that scale down evaluation resumes',
    )
    enabled: bool = Field(..., description='Should CA scale down the cluster')
    unneededTime: Optional[constr(regex=r'([0-9]*(\.[0-9]*)?[a-z]+)+')] = Field(
        None,
        description='How long a node should be unneeded before it is eligible for scale down',
    )


class Spec(BaseModel):
    balanceSimilarNodeGroups: Optional[bool] = Field(
        None,
        description='BalanceSimilarNodeGroups enables/disables the `--balance-similar-node-groups` cluster-autocaler feature. This feature will automatically identify node groups with the same instance type and the same set of labels and try to keep the respective sizes of those node groups balanced.',
    )
    ignoreDaemonsetsUtilization: Optional[bool] = Field(
        None,
        description='Enables/Disables `--ignore-daemonsets-utilization` CA feature flag. Should CA ignore DaemonSet pods when calculating resource utilization for scaling down. false by default',
    )
    maxNodeProvisionTime: Optional[
        constr(regex=r'^([0-9]+(\.[0-9]+)?(ns|us|µs|ms|s|m|h))+$')
    ] = Field(None, description='Maximum time CA waits for node to be provisioned')
    maxPodGracePeriod: Optional[int] = Field(
        None, description='Gives pods graceful termination time before scaling down'
    )
    podPriorityThreshold: Optional[int] = Field(
        None,
        description='To allow users to schedule "best-effort" pods, which shouldn\'t trigger Cluster Autoscaler actions, but only run when there are spare resources available, More info: https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-cluster-autoscaler-work-with-pod-priority-and-preemption',
    )
    resourceLimits: Optional[ResourceLimits] = Field(
        None, description='Constraints of autoscaling resources'
    )
    scaleDown: Optional[ScaleDown] = Field(
        None, description='Configuration of scale down operation'
    )
    skipNodesWithLocalStorage: Optional[bool] = Field(
        None,
        description='Enables/Disables `--skip-nodes-with-local-storage` CA feature flag. If true cluster autoscaler will never delete nodes with pods with local storage, e.g. EmptyDir or HostPath. true by default at autoscaler',
    )


class ClusterAutoscaler(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ObjectMetaV2] = Field(
        None,
        description="Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata",
    )
    spec: Optional[Spec] = Field(
        None, description='Desired state of ClusterAutoscaler resource'
    )
    status: Optional[Dict[str, Any]] = Field(
        None, description='Most recently observed status of ClusterAutoscaler resource'
    )


class ClusterAutoscalerList(BaseModel):
    apiVersion: Optional[str] = Field(
        None,
        description='APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources',
    )
    items: List[ClusterAutoscaler] = Field(
        ...,
        description='List of clusterautoscalers. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md',
    )
    kind: Optional[str] = Field(
        None,
        description='Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
    metadata: Optional[v1.ListMeta] = Field(
        None,
        description='Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds',
    )
