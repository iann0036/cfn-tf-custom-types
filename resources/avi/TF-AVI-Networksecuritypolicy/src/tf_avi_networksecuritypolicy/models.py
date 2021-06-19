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
    CloudConfigCksum: Optional[str]
    CreatedBy: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    IpReputationDbRef: Optional[str]
    Name: Optional[str]
    TenantRef: Optional[str]
    Uuid: Optional[str]
    Markers: Optional[Sequence["_MarkersDefinition"]]
    Rules: Optional[Sequence["_RulesDefinition"]]

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
            CloudConfigCksum=json_data.get("CloudConfigCksum"),
            CreatedBy=json_data.get("CreatedBy"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            IpReputationDbRef=json_data.get("IpReputationDbRef"),
            Name=json_data.get("Name"),
            TenantRef=json_data.get("TenantRef"),
            Uuid=json_data.get("Uuid"),
            Markers=deserialize_list(json_data.get("Markers"), MarkersDefinition),
            Rules=deserialize_list(json_data.get("Rules"), RulesDefinition),
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
class RulesDefinition(BaseModel):
    Action: Optional[str]
    Age: Optional[float]
    CreatedBy: Optional[str]
    Enable: Optional[bool]
    Index: Optional[float]
    Log: Optional[bool]
    Name: Optional[str]
    Match: Optional[Sequence["_MatchDefinition"]]
    RlParam: Optional[Sequence["_RlParamDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_RulesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RulesDefinition"]:
        if not json_data:
            return None
        return cls(
            Action=json_data.get("Action"),
            Age=json_data.get("Age"),
            CreatedBy=json_data.get("CreatedBy"),
            Enable=json_data.get("Enable"),
            Index=json_data.get("Index"),
            Log=json_data.get("Log"),
            Name=json_data.get("Name"),
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
            RlParam=deserialize_list(json_data.get("RlParam"), RlParamDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_RulesDefinition = RulesDefinition


@dataclass
class MatchDefinition(BaseModel):
    ClientIp: Optional[Sequence["_ClientIpDefinition"]]
    ClientPort: Optional[Sequence["_ClientPortDefinition"]]
    IpReputationType: Optional[Sequence["_IpReputationTypeDefinition"]]
    Microservice: Optional[Sequence["_MicroserviceDefinition"]]
    VsPort: Optional[Sequence["_VsPortDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientIp=deserialize_list(json_data.get("ClientIp"), ClientIpDefinition),
            ClientPort=deserialize_list(json_data.get("ClientPort"), ClientPortDefinition),
            IpReputationType=deserialize_list(json_data.get("IpReputationType"), IpReputationTypeDefinition),
            Microservice=deserialize_list(json_data.get("Microservice"), MicroserviceDefinition),
            VsPort=deserialize_list(json_data.get("VsPort"), VsPortDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class ClientIpDefinition(BaseModel):
    GroupRefs: Optional[Sequence[str]]
    MatchCriteria: Optional[str]
    Addrs: Optional[Sequence["_AddrsDefinition"]]
    Prefixes: Optional[Sequence["_PrefixesDefinition"]]
    Ranges: Optional[Sequence["_RangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientIpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientIpDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupRefs=json_data.get("GroupRefs"),
            MatchCriteria=json_data.get("MatchCriteria"),
            Addrs=deserialize_list(json_data.get("Addrs"), AddrsDefinition),
            Prefixes=deserialize_list(json_data.get("Prefixes"), PrefixesDefinition),
            Ranges=deserialize_list(json_data.get("Ranges"), RangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientIpDefinition = ClientIpDefinition


@dataclass
class AddrsDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddrsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddrsDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddrsDefinition = AddrsDefinition


@dataclass
class PrefixesDefinition(BaseModel):
    Mask: Optional[float]
    IpAddr: Optional[Sequence["_IpAddrDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrefixesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrefixesDefinition"]:
        if not json_data:
            return None
        return cls(
            Mask=json_data.get("Mask"),
            IpAddr=deserialize_list(json_data.get("IpAddr"), IpAddrDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrefixesDefinition = PrefixesDefinition


@dataclass
class IpAddrDefinition(BaseModel):
    Addr: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IpAddrDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpAddrDefinition"]:
        if not json_data:
            return None
        return cls(
            Addr=json_data.get("Addr"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpAddrDefinition = IpAddrDefinition


@dataclass
class RangesDefinition(BaseModel):
    End: Optional[float]
    Start: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RangesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RangesDefinition"]:
        if not json_data:
            return None
        return cls(
            End=json_data.get("End"),
            Start=json_data.get("Start"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RangesDefinition = RangesDefinition


@dataclass
class ClientPortDefinition(BaseModel):
    MatchCriteria: Optional[str]
    Ports: Optional[Sequence[float]]
    Ranges: Optional[Sequence["_RangesDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientPortDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            Ports=json_data.get("Ports"),
            Ranges=deserialize_list(json_data.get("Ranges"), RangesDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientPortDefinition = ClientPortDefinition


@dataclass
class IpReputationTypeDefinition(BaseModel):
    MatchOperation: Optional[str]
    ReputationTypes: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_IpReputationTypeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IpReputationTypeDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchOperation=json_data.get("MatchOperation"),
            ReputationTypes=json_data.get("ReputationTypes"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IpReputationTypeDefinition = IpReputationTypeDefinition


@dataclass
class MicroserviceDefinition(BaseModel):
    GroupRef: Optional[str]
    MatchCriteria: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_MicroserviceDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MicroserviceDefinition"]:
        if not json_data:
            return None
        return cls(
            GroupRef=json_data.get("GroupRef"),
            MatchCriteria=json_data.get("MatchCriteria"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MicroserviceDefinition = MicroserviceDefinition


@dataclass
class VsPortDefinition(BaseModel):
    MatchCriteria: Optional[str]
    Ports: Optional[Sequence[float]]

    @classmethod
    def _deserialize(
        cls: Type["_VsPortDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_VsPortDefinition"]:
        if not json_data:
            return None
        return cls(
            MatchCriteria=json_data.get("MatchCriteria"),
            Ports=json_data.get("Ports"),
        )


# work around possible type aliasing issues when variable has same name as a model
_VsPortDefinition = VsPortDefinition


@dataclass
class RlParamDefinition(BaseModel):
    BurstSize: Optional[float]
    MaxRate: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_RlParamDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RlParamDefinition"]:
        if not json_data:
            return None
        return cls(
            BurstSize=json_data.get("BurstSize"),
            MaxRate=json_data.get("MaxRate"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RlParamDefinition = RlParamDefinition


