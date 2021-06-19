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
    CreateTime: Optional[str]
    DataprocServiceAccount: Optional[str]
    Description: Optional[str]
    EnableStackdriverLogging: Optional[bool]
    EnableStackdriverMonitoring: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    Options: Optional[Sequence["_OptionsDefinition"]]
    PrivateInstance: Optional[bool]
    Project: Optional[str]
    Region: Optional[str]
    ServiceAccount: Optional[str]
    ServiceEndpoint: Optional[str]
    State: Optional[str]
    StateMessage: Optional[str]
    Type: Optional[str]
    UpdateTime: Optional[str]
    Version: Optional[str]
    NetworkConfig: Optional[Sequence["_NetworkConfigDefinition"]]
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
            CreateTime=json_data.get("CreateTime"),
            DataprocServiceAccount=json_data.get("DataprocServiceAccount"),
            Description=json_data.get("Description"),
            EnableStackdriverLogging=json_data.get("EnableStackdriverLogging"),
            EnableStackdriverMonitoring=json_data.get("EnableStackdriverMonitoring"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            Options=deserialize_list(json_data.get("Options"), OptionsDefinition),
            PrivateInstance=json_data.get("PrivateInstance"),
            Project=json_data.get("Project"),
            Region=json_data.get("Region"),
            ServiceAccount=json_data.get("ServiceAccount"),
            ServiceEndpoint=json_data.get("ServiceEndpoint"),
            State=json_data.get("State"),
            StateMessage=json_data.get("StateMessage"),
            Type=json_data.get("Type"),
            UpdateTime=json_data.get("UpdateTime"),
            Version=json_data.get("Version"),
            NetworkConfig=deserialize_list(json_data.get("NetworkConfig"), NetworkConfigDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


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
class OptionsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OptionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OptionsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OptionsDefinition = OptionsDefinition


@dataclass
class NetworkConfigDefinition(BaseModel):
    IpAllocation: Optional[str]
    Network: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworkConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworkConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            IpAllocation=json_data.get("IpAllocation"),
            Network=json_data.get("Network"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworkConfigDefinition = NetworkConfigDefinition


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


