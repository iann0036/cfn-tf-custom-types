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
    Description: Optional[str]
    Id: Optional[str]
    ImageId: Optional[str]
    Name: Optional[str]
    TenantRef: Optional[str]
    UseExternalAsg: Optional[bool]
    Uuid: Optional[str]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    Mesos: Optional[Sequence["_MesosDefinition"]]
    Openstack: Optional[Sequence["_OpenstackDefinition"]]

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
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            ImageId=json_data.get("ImageId"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            UseExternalAsg=json_data.get("UseExternalAsg"),
            Uuid=json_data.get("Uuid"),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            Mesos=deserialize_list(json_data.get("Mesos"), MesosDefinition),
            Openstack=deserialize_list(json_data.get("Openstack"), OpenstackDefinition),
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
class MesosDefinition(BaseModel):
    Force: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_MesosDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MesosDefinition"]:
        if not json_data:
            return None
        return cls(
            Force=json_data.get("Force"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MesosDefinition = MesosDefinition


@dataclass
class OpenstackDefinition(BaseModel):
    HeatScaleDownUrl: Optional[str]
    HeatScaleUpUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OpenstackDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OpenstackDefinition"]:
        if not json_data:
            return None
        return cls(
            HeatScaleDownUrl=json_data.get("HeatScaleDownUrl"),
            HeatScaleUpUrl=json_data.get("HeatScaleUpUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OpenstackDefinition = OpenstackDefinition


