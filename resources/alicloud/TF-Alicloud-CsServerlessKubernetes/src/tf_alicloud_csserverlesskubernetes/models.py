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
    ClientCert: Optional[str]
    ClientKey: Optional[str]
    ClusterCaCert: Optional[str]
    DeletionProtection: Optional[bool]
    EndpointPublicAccessEnabled: Optional[bool]
    ForceUpdate: Optional[bool]
    Id: Optional[str]
    KubeConfig: Optional[str]
    LoadBalancerSpec: Optional[str]
    LoggingType: Optional[str]
    Name: Optional[str]
    NamePrefix: Optional[str]
    NewNatGateway: Optional[bool]
    PrivateZone: Optional[bool]
    ResourceGroupId: Optional[str]
    SecurityGroupId: Optional[str]
    ServiceCidr: Optional[str]
    ServiceDiscoveryTypes: Optional[Sequence[str]]
    SlsProjectName: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TimeZone: Optional[str]
    Version: Optional[str]
    VpcId: Optional[str]
    VswitchId: Optional[str]
    VswitchIds: Optional[Sequence[str]]
    ZoneId: Optional[str]
    Addons: Optional[Sequence["_AddonsDefinition"]]
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
            ClientCert=json_data.get("ClientCert"),
            ClientKey=json_data.get("ClientKey"),
            ClusterCaCert=json_data.get("ClusterCaCert"),
            DeletionProtection=json_data.get("DeletionProtection"),
            EndpointPublicAccessEnabled=json_data.get("EndpointPublicAccessEnabled"),
            ForceUpdate=json_data.get("ForceUpdate"),
            Id=json_data.get("Id"),
            KubeConfig=json_data.get("KubeConfig"),
            LoadBalancerSpec=json_data.get("LoadBalancerSpec"),
            LoggingType=json_data.get("LoggingType"),
            Name=json_data.get("Name"),
            NamePrefix=json_data.get("NamePrefix"),
            NewNatGateway=json_data.get("NewNatGateway"),
            PrivateZone=json_data.get("PrivateZone"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            SecurityGroupId=json_data.get("SecurityGroupId"),
            ServiceCidr=json_data.get("ServiceCidr"),
            ServiceDiscoveryTypes=json_data.get("ServiceDiscoveryTypes"),
            SlsProjectName=json_data.get("SlsProjectName"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TimeZone=json_data.get("TimeZone"),
            Version=json_data.get("Version"),
            VpcId=json_data.get("VpcId"),
            VswitchId=json_data.get("VswitchId"),
            VswitchIds=json_data.get("VswitchIds"),
            ZoneId=json_data.get("ZoneId"),
            Addons=deserialize_list(json_data.get("Addons"), AddonsDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class AddonsDefinition(BaseModel):
    Config: Optional[str]
    Disabled: Optional[bool]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AddonsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AddonsDefinition"]:
        if not json_data:
            return None
        return cls(
            Config=json_data.get("Config"),
            Disabled=json_data.get("Disabled"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AddonsDefinition = AddonsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]

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
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition

