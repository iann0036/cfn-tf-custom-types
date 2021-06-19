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
    AsPathRegex: Optional[str]
    BgpAggregate: Optional[str]
    CommunityRegex: Optional[str]
    Enable: Optional[bool]
    ExtendedCommunityRegex: Optional[str]
    FromPeers: Optional[Sequence[str]]
    Id: Optional[str]
    Med: Optional[str]
    Name: Optional[str]
    NextHops: Optional[Sequence[str]]
    RouteTable: Optional[str]
    VirtualRouter: Optional[str]
    AddressPrefix: Optional[Sequence["_AddressPrefixDefinition"]]

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
            AsPathRegex=json_data.get("AsPathRegex"),
            BgpAggregate=json_data.get("BgpAggregate"),
            CommunityRegex=json_data.get("CommunityRegex"),
            Enable=json_data.get("Enable"),
            ExtendedCommunityRegex=json_data.get("ExtendedCommunityRegex"),
            FromPeers=json_data.get("FromPeers"),
            Id=json_data.get("Id"),
            Med=json_data.get("Med"),
            Name=json_data.get("Name"),
            NextHops=json_data.get("NextHops"),
            RouteTable=json_data.get("RouteTable"),
            VirtualRouter=json_data.get("VirtualRouter"),
            AddressPrefix=deserialize_list(json_data.get("AddressPrefix"), AddressPrefixDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AddressPrefixDefinition(BaseModel):
    Exact: Optional[bool]
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddressPrefixDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddressPrefixDefinition"]:
        if not json_data:
            return None
        return cls(
            Exact=json_data.get("Exact"),
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddressPrefixDefinition = AddressPrefixDefinition


