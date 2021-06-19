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
    Account: Optional[str]
    AutoRenew: Optional[bool]
    ColdStorageSize: Optional[float]
    CoreDiskSize: Optional[float]
    CoreDiskType: Optional[str]
    CoreInstanceQuantity: Optional[float]
    CoreInstanceType: Optional[str]
    DeletionProtection: Optional[bool]
    Duration: Optional[float]
    Engine: Optional[str]
    EngineVersion: Optional[str]
    Id: Optional[str]
    ImmediateDeleteFlag: Optional[bool]
    IpWhite: Optional[str]
    MaintainEndTime: Optional[str]
    MaintainStartTime: Optional[str]
    MasterInstanceQuantity: Optional[float]
    MasterInstanceType: Optional[str]
    Name: Optional[str]
    Password: Optional[str]
    PayType: Optional[str]
    SecurityGroups: Optional[Sequence[str]]
    SlbConnAddrs: Optional[Sequence["_SlbConnAddrsDefinition"]]
    Tags: Optional[Sequence["_TagsDefinition"]]
    UiProxyConnAddrs: Optional[Sequence["_UiProxyConnAddrsDefinition"]]
    VswitchId: Optional[str]
    ZkConnAddrs: Optional[Sequence["_ZkConnAddrsDefinition"]]
    ZoneId: Optional[str]
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
            Account=json_data.get("Account"),
            AutoRenew=json_data.get("AutoRenew"),
            ColdStorageSize=json_data.get("ColdStorageSize"),
            CoreDiskSize=json_data.get("CoreDiskSize"),
            CoreDiskType=json_data.get("CoreDiskType"),
            CoreInstanceQuantity=json_data.get("CoreInstanceQuantity"),
            CoreInstanceType=json_data.get("CoreInstanceType"),
            DeletionProtection=json_data.get("DeletionProtection"),
            Duration=json_data.get("Duration"),
            Engine=json_data.get("Engine"),
            EngineVersion=json_data.get("EngineVersion"),
            Id=json_data.get("Id"),
            ImmediateDeleteFlag=json_data.get("ImmediateDeleteFlag"),
            IpWhite=json_data.get("IpWhite"),
            MaintainEndTime=json_data.get("MaintainEndTime"),
            MaintainStartTime=json_data.get("MaintainStartTime"),
            MasterInstanceQuantity=json_data.get("MasterInstanceQuantity"),
            MasterInstanceType=json_data.get("MasterInstanceType"),
            Name=json_data.get("Name"),
            Password=json_data.get("Password"),
            PayType=json_data.get("PayType"),
            SecurityGroups=json_data.get("SecurityGroups"),
            SlbConnAddrs=deserialize_list(json_data.get("SlbConnAddrs"), SlbConnAddrsDefinition),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            UiProxyConnAddrs=deserialize_list(json_data.get("UiProxyConnAddrs"), UiProxyConnAddrsDefinition),
            VswitchId=json_data.get("VswitchId"),
            ZkConnAddrs=deserialize_list(json_data.get("ZkConnAddrs"), ZkConnAddrsDefinition),
            ZoneId=json_data.get("ZoneId"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SlbConnAddrsDefinition(BaseModel):
    ConnAddr: Optional[str]
    ConnAddrPort: Optional[str]
    NetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SlbConnAddrsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SlbConnAddrsDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnAddr=json_data.get("ConnAddr"),
            ConnAddrPort=json_data.get("ConnAddrPort"),
            NetType=json_data.get("NetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SlbConnAddrsDefinition = SlbConnAddrsDefinition


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
class UiProxyConnAddrsDefinition(BaseModel):
    ConnAddr: Optional[str]
    ConnAddrPort: Optional[str]
    NetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_UiProxyConnAddrsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_UiProxyConnAddrsDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnAddr=json_data.get("ConnAddr"),
            ConnAddrPort=json_data.get("ConnAddrPort"),
            NetType=json_data.get("NetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_UiProxyConnAddrsDefinition = UiProxyConnAddrsDefinition


@dataclass
class ZkConnAddrsDefinition(BaseModel):
    ConnAddr: Optional[str]
    ConnAddrPort: Optional[str]
    NetType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ZkConnAddrsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ZkConnAddrsDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnAddr=json_data.get("ConnAddr"),
            ConnAddrPort=json_data.get("ConnAddrPort"),
            NetType=json_data.get("NetType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ZkConnAddrsDefinition = ZkConnAddrsDefinition


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


