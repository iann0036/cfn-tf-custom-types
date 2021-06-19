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
    AcceleratorId: Optional[str]
    ClientAffinity: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    Protocol: Optional[str]
    ProxyProtocol: Optional[bool]
    Status: Optional[str]
    Certificates: Optional[Sequence["_CertificatesDefinition"]]
    PortRanges: Optional[Sequence["_PortRangesDefinition"]]
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
            AcceleratorId=json_data.get("AcceleratorId"),
            ClientAffinity=json_data.get("ClientAffinity"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Protocol=json_data.get("Protocol"),
            ProxyProtocol=json_data.get("ProxyProtocol"),
            Status=json_data.get("Status"),
            Certificates=deserialize_list(json_data.get("Certificates"), CertificatesDefinition),
            PortRanges=deserialize_list(json_data.get("PortRanges"), PortRangesDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class CertificatesDefinition(BaseModel):
    Id: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CertificatesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificatesDefinition"]:
        if not json_data:
            return None
        return cls(
            Id=json_data.get("Id"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificatesDefinition = CertificatesDefinition


@dataclass
class PortRangesDefinition(BaseModel):
    FromPort: Optional[float]
    ToPort: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_PortRangesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortRangesDefinition"]:
        if not json_data:
            return None
        return cls(
            FromPort=json_data.get("FromPort"),
            ToPort=json_data.get("ToPort"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortRangesDefinition = PortRangesDefinition


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


