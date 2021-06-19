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
    DnsName: Optional[str]
    ForceDestroy: Optional[bool]
    Id: Optional[str]
    Labels: Optional[Sequence["_LabelsDefinition"]]
    Name: Optional[str]
    NameServers: Optional[Sequence[str]]
    Project: Optional[str]
    Visibility: Optional[str]
    DnssecConfig: Optional[Sequence["_DnssecConfigDefinition"]]
    ForwardingConfig: Optional[Sequence["_ForwardingConfigDefinition"]]
    PeeringConfig: Optional[Sequence["_PeeringConfigDefinition"]]
    PrivateVisibilityConfig: Optional[Sequence["_PrivateVisibilityConfigDefinition"]]
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
            Description=json_data.get("Description"),
            DnsName=json_data.get("DnsName"),
            ForceDestroy=json_data.get("ForceDestroy"),
            Id=json_data.get("Id"),
            Labels=deserialize_list(json_data.get("Labels"), LabelsDefinition),
            Name=json_data.get("Name"),
            NameServers=json_data.get("NameServers"),
            Project=json_data.get("Project"),
            Visibility=json_data.get("Visibility"),
            DnssecConfig=deserialize_list(json_data.get("DnssecConfig"), DnssecConfigDefinition),
            ForwardingConfig=deserialize_list(json_data.get("ForwardingConfig"), ForwardingConfigDefinition),
            PeeringConfig=deserialize_list(json_data.get("PeeringConfig"), PeeringConfigDefinition),
            PrivateVisibilityConfig=deserialize_list(json_data.get("PrivateVisibilityConfig"), PrivateVisibilityConfigDefinition),
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
class DnssecConfigDefinition(BaseModel):
    Kind: Optional[str]
    NonExistence: Optional[str]
    State: Optional[str]
    DefaultKeySpecs: Optional[Sequence["_DefaultKeySpecsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_DnssecConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DnssecConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Kind=json_data.get("Kind"),
            NonExistence=json_data.get("NonExistence"),
            State=json_data.get("State"),
            DefaultKeySpecs=deserialize_list(json_data.get("DefaultKeySpecs"), DefaultKeySpecsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_DnssecConfigDefinition = DnssecConfigDefinition


@dataclass
class DefaultKeySpecsDefinition(BaseModel):
    Algorithm: Optional[str]
    KeyLength: Optional[float]
    KeyType: Optional[str]
    Kind: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DefaultKeySpecsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DefaultKeySpecsDefinition"]:
        if not json_data:
            return None
        return cls(
            Algorithm=json_data.get("Algorithm"),
            KeyLength=json_data.get("KeyLength"),
            KeyType=json_data.get("KeyType"),
            Kind=json_data.get("Kind"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DefaultKeySpecsDefinition = DefaultKeySpecsDefinition


@dataclass
class ForwardingConfigDefinition(BaseModel):
    TargetNameServers: Optional[Sequence["_TargetNameServersDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ForwardingConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ForwardingConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetNameServers=deserialize_list(json_data.get("TargetNameServers"), TargetNameServersDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ForwardingConfigDefinition = ForwardingConfigDefinition


@dataclass
class TargetNameServersDefinition(BaseModel):
    ForwardingPath: Optional[str]
    Ipv4Address: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetNameServersDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetNameServersDefinition"]:
        if not json_data:
            return None
        return cls(
            ForwardingPath=json_data.get("ForwardingPath"),
            Ipv4Address=json_data.get("Ipv4Address"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetNameServersDefinition = TargetNameServersDefinition


@dataclass
class PeeringConfigDefinition(BaseModel):
    TargetNetwork: Optional[Sequence["_TargetNetworkDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PeeringConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PeeringConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            TargetNetwork=deserialize_list(json_data.get("TargetNetwork"), TargetNetworkDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PeeringConfigDefinition = PeeringConfigDefinition


@dataclass
class TargetNetworkDefinition(BaseModel):
    NetworkUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TargetNetworkDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TargetNetworkDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkUrl=json_data.get("NetworkUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TargetNetworkDefinition = TargetNetworkDefinition


@dataclass
class PrivateVisibilityConfigDefinition(BaseModel):
    Networks: Optional[Sequence["_NetworksDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_PrivateVisibilityConfigDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PrivateVisibilityConfigDefinition"]:
        if not json_data:
            return None
        return cls(
            Networks=deserialize_list(json_data.get("Networks"), NetworksDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_PrivateVisibilityConfigDefinition = PrivateVisibilityConfigDefinition


@dataclass
class NetworksDefinition(BaseModel):
    NetworkUrl: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_NetworksDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NetworksDefinition"]:
        if not json_data:
            return None
        return cls(
            NetworkUrl=json_data.get("NetworkUrl"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NetworksDefinition = NetworksDefinition


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


