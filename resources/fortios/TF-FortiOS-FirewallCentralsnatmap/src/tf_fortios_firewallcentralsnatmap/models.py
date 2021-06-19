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
    Comments: Optional[str]
    DynamicSortSubtable: Optional[str]
    Id: Optional[str]
    Nat: Optional[str]
    NatPort: Optional[str]
    OrigPort: Optional[str]
    Policyid: Optional[float]
    Protocol: Optional[float]
    Status: Optional[str]
    Type: Optional[str]
    Uuid: Optional[str]
    Vdomparam: Optional[str]
    DstAddr: Optional[Sequence["_DstAddrDefinition"]]
    DstAddr6: Optional[Sequence["_DstAddr6Definition"]]
    Dstintf: Optional[Sequence["_DstintfDefinition"]]
    NatIppool: Optional[Sequence["_NatIppoolDefinition"]]
    NatIppool6: Optional[Sequence["_NatIppool6Definition"]]
    OrigAddr: Optional[Sequence["_OrigAddrDefinition"]]
    OrigAddr6: Optional[Sequence["_OrigAddr6Definition"]]
    Srcintf: Optional[Sequence["_SrcintfDefinition"]]

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
            Comments=json_data.get("Comments"),
            DynamicSortSubtable=json_data.get("DynamicSortSubtable"),
            Id=json_data.get("Id"),
            Nat=json_data.get("Nat"),
            NatPort=json_data.get("NatPort"),
            OrigPort=json_data.get("OrigPort"),
            Policyid=json_data.get("Policyid"),
            Protocol=json_data.get("Protocol"),
            Status=json_data.get("Status"),
            Type=json_data.get("Type"),
            Uuid=json_data.get("Uuid"),
            Vdomparam=json_data.get("Vdomparam"),
            DstAddr=deserialize_list(json_data.get("DstAddr"), DstAddrDefinition),
            DstAddr6=deserialize_list(json_data.get("DstAddr6"), DstAddr6Definition),
            Dstintf=deserialize_list(json_data.get("Dstintf"), DstintfDefinition),
            NatIppool=deserialize_list(json_data.get("NatIppool"), NatIppoolDefinition),
            NatIppool6=deserialize_list(json_data.get("NatIppool6"), NatIppool6Definition),
            OrigAddr=deserialize_list(json_data.get("OrigAddr"), OrigAddrDefinition),
            OrigAddr6=deserialize_list(json_data.get("OrigAddr6"), OrigAddr6Definition),
            Srcintf=deserialize_list(json_data.get("Srcintf"), SrcintfDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DstAddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstAddrDefinition = DstAddrDefinition


@dataclass
class DstAddr6Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstAddr6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstAddr6Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstAddr6Definition = DstAddr6Definition


@dataclass
class DstintfDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DstintfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DstintfDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DstintfDefinition = DstintfDefinition


@dataclass
class NatIppoolDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NatIppoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NatIppoolDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NatIppoolDefinition = NatIppoolDefinition


@dataclass
class NatIppool6Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NatIppool6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NatIppool6Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NatIppool6Definition = NatIppool6Definition


@dataclass
class OrigAddrDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrigAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrigAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrigAddrDefinition = OrigAddrDefinition


@dataclass
class OrigAddr6Definition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_OrigAddr6Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_OrigAddr6Definition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_OrigAddr6Definition = OrigAddr6Definition


@dataclass
class SrcintfDefinition(BaseModel):
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SrcintfDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SrcintfDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SrcintfDefinition = SrcintfDefinition


