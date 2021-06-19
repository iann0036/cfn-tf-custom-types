# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

from cloudformation_cli_python_lib.interface import (
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class ResourceHandlerRequest(BaseResourceHandlerRequest):
    # pylint: disable=invalid-name
    desiredResourceState: Optional["ResourceModel"]
    previousResourceState: Optional["ResourceModel"]


@dataclass
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    Annotations: Optional[Sequence["_AnnotationsDefinition"]]
    ClusterId: Optional[str]
    Description: Optional[str]
    EnableProjectMonitoring: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    PodSecurityPolicyTemplateId: Optional[str]
    WaitForCluster: Optional[bool]
    ContainerResourceLimit: Optional[Sequence["_ContainerResourceLimitDefinition"]]
    ProjectMonitoringInput: Optional[Sequence["_ProjectMonitoringInputDefinition"]]
    ResourceQuota: Optional[Sequence["_ResourceQuotaDefinition"]]
    Timeouts: Optional["_TimeoutsDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Annotations=deserialize_list(json_data.get("Annotations"), AnnotationsDefinition),
            ClusterId=json_data.get("ClusterId"),
            Description=json_data.get("Description"),
            EnableProjectMonitoring=json_data.get("EnableProjectMonitoring"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            PodSecurityPolicyTemplateId=json_data.get("PodSecurityPolicyTemplateId"),
            WaitForCluster=json_data.get("WaitForCluster"),
            ContainerResourceLimit=deserialize_list(json_data.get("ContainerResourceLimit"), ContainerResourceLimitDefinition),
            ProjectMonitoringInput=deserialize_list(json_data.get("ProjectMonitoringInput"), ProjectMonitoringInputDefinition),
            ResourceQuota=deserialize_list(json_data.get("ResourceQuota"), ResourceQuotaDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AnnotationsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnnotationsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnnotationsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnnotationsDefinition = AnnotationsDefinition


@dataclass
class LabelsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LabelsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LabelsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LabelsDefinition = LabelsDefinition


@dataclass
class ContainerResourceLimitDefinition(BaseModel):
    LimitsCpu: Optional[str]
    LimitsMemory: Optional[str]
    RequestsCpu: Optional[str]
    RequestsMemory: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ContainerResourceLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ContainerResourceLimitDefinition"]:
        if not json_data:
            return None
        return cls(
            LimitsCpu=json_data.get("LimitsCpu"),
            LimitsMemory=json_data.get("LimitsMemory"),
            RequestsCpu=json_data.get("RequestsCpu"),
            RequestsMemory=json_data.get("RequestsMemory"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ContainerResourceLimitDefinition = ContainerResourceLimitDefinition


@dataclass
class ProjectMonitoringInputDefinition(BaseModel):
    Answers: Optional[Sequence["_AnswersDefinition"]]
    Version: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectMonitoringInputDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectMonitoringInputDefinition"]:
        if not json_data:
            return None
        return cls(
            Answers=deserialize_list(json_data.get("Answers"), AnswersDefinition),
            Version=json_data.get("Version"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectMonitoringInputDefinition = ProjectMonitoringInputDefinition


@dataclass
class AnswersDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AnswersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AnswersDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AnswersDefinition = AnswersDefinition


@dataclass
class ResourceQuotaDefinition(BaseModel):
    NamespaceDefaultLimit: Optional[Sequence["_NamespaceDefaultLimitDefinition"]]
    ProjectLimit: Optional[Sequence["_ProjectLimitDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceQuotaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceQuotaDefinition"]:
        if not json_data:
            return None
        return cls(
            NamespaceDefaultLimit=deserialize_list(json_data.get("NamespaceDefaultLimit"), NamespaceDefaultLimitDefinition),
            ProjectLimit=deserialize_list(json_data.get("ProjectLimit"), ProjectLimitDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceQuotaDefinition = ResourceQuotaDefinition


@dataclass
class NamespaceDefaultLimitDefinition(BaseModel):
    ConfigMaps: Optional[str]
    LimitsCpu: Optional[str]
    LimitsMemory: Optional[str]
    PersistentVolumeClaims: Optional[str]
    Pods: Optional[str]
    ReplicationControllers: Optional[str]
    RequestsCpu: Optional[str]
    RequestsMemory: Optional[str]
    RequestsStorage: Optional[str]
    Secrets: Optional[str]
    Services: Optional[str]
    ServicesLoadBalancers: Optional[str]
    ServicesNodePorts: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NamespaceDefaultLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NamespaceDefaultLimitDefinition"]:
        if not json_data:
            return None
        return cls(
            ConfigMaps=json_data.get("ConfigMaps"),
            LimitsCpu=json_data.get("LimitsCpu"),
            LimitsMemory=json_data.get("LimitsMemory"),
            PersistentVolumeClaims=json_data.get("PersistentVolumeClaims"),
            Pods=json_data.get("Pods"),
            ReplicationControllers=json_data.get("ReplicationControllers"),
            RequestsCpu=json_data.get("RequestsCpu"),
            RequestsMemory=json_data.get("RequestsMemory"),
            RequestsStorage=json_data.get("RequestsStorage"),
            Secrets=json_data.get("Secrets"),
            Services=json_data.get("Services"),
            ServicesLoadBalancers=json_data.get("ServicesLoadBalancers"),
            ServicesNodePorts=json_data.get("ServicesNodePorts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NamespaceDefaultLimitDefinition = NamespaceDefaultLimitDefinition


@dataclass
class ProjectLimitDefinition(BaseModel):
    ConfigMaps: Optional[str]
    LimitsCpu: Optional[str]
    LimitsMemory: Optional[str]
    PersistentVolumeClaims: Optional[str]
    Pods: Optional[str]
    ReplicationControllers: Optional[str]
    RequestsCpu: Optional[str]
    RequestsMemory: Optional[str]
    RequestsStorage: Optional[str]
    Secrets: Optional[str]
    Services: Optional[str]
    ServicesLoadBalancers: Optional[str]
    ServicesNodePorts: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ProjectLimitDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ProjectLimitDefinition"]:
        if not json_data:
            return None
        return cls(
            ConfigMaps=json_data.get("ConfigMaps"),
            LimitsCpu=json_data.get("LimitsCpu"),
            LimitsMemory=json_data.get("LimitsMemory"),
            PersistentVolumeClaims=json_data.get("PersistentVolumeClaims"),
            Pods=json_data.get("Pods"),
            ReplicationControllers=json_data.get("ReplicationControllers"),
            RequestsCpu=json_data.get("RequestsCpu"),
            RequestsMemory=json_data.get("RequestsMemory"),
            RequestsStorage=json_data.get("RequestsStorage"),
            Secrets=json_data.get("Secrets"),
            Services=json_data.get("Services"),
            ServicesLoadBalancers=json_data.get("ServicesLoadBalancers"),
            ServicesNodePorts=json_data.get("ServicesNodePorts"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ProjectLimitDefinition = ProjectLimitDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition


