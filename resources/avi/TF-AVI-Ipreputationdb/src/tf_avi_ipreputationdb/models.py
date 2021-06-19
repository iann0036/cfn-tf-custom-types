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
    BaseFileRefs: Optional[Sequence[str]]
    Description: Optional[str]
    Id: Optional[str]
    IncrementalFileRefs: Optional[Sequence[str]]
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    Vendor: Optional[str]
    Version: Optional[str]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    ServiceStatus: Optional[Sequence["_ServiceStatusDefinition"]]

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
            BaseFileRefs=json_data.get("BaseFileRefs"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IncrementalFileRefs=json_data.get("IncrementalFileRefs"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            Vendor=json_data.get("Vendor"),
            Version=json_data.get("Version"),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            ServiceStatus=deserialize_list(json_data.get("ServiceStatus"), ServiceStatusDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class MarkersDefinition(BaseModel):
    Key: Optional[str]
    Values: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MarkersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MarkersDefinition"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Values=json_data.get("Values"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MarkersDefinition = MarkersDefinition


@dataclass
class ServiceStatusDefinition(BaseModel):
    Error: Optional[str]
    LastSuccessfulUpdateCheck: Optional[Sequence["_LastSuccessfulUpdateCheckDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ServiceStatusDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ServiceStatusDefinition"]:
        if not json_data:
            return None
        return cls(
            Error=json_data.get("Error"),
            LastSuccessfulUpdateCheck=deserialize_list(json_data.get("LastSuccessfulUpdateCheck"), LastSuccessfulUpdateCheckDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ServiceStatusDefinition = ServiceStatusDefinition


@dataclass
class LastSuccessfulUpdateCheckDefinition(BaseModel):
    Secs: Optional[float]
    Usecs: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_LastSuccessfulUpdateCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LastSuccessfulUpdateCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            Secs=json_data.get("Secs"),
            Usecs=json_data.get("Usecs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LastSuccessfulUpdateCheckDefinition = LastSuccessfulUpdateCheckDefinition


