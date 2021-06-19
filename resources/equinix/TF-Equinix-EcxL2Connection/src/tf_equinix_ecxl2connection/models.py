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
    AuthorizationKey: Optional[str]
    DeviceInterfaceId: Optional[float]
    DeviceUuid: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    NamedTag: Optional[str]
    Notifications: Optional[Sequence[str]]
    PortUuid: Optional[str]
    ProfileUuid: Optional[str]
    ProviderStatus: Optional[str]
    PurchaseOrderNumber: Optional[str]
    RedundancyType: Optional[str]
    RedundantUuid: Optional[str]
    SellerMetroCode: Optional[str]
    SellerRegion: Optional[str]
    Speed: Optional[float]
    SpeedUnit: Optional[str]
    Status: Optional[str]
    Uuid: Optional[str]
    VlanCtag: Optional[float]
    VlanStag: Optional[float]
    ZsidePortUuid: Optional[str]
    ZsideVlanCtag: Optional[float]
    ZsideVlanStag: Optional[float]
    AdditionalInfo: Optional[Sequence["_AdditionalInfoDefinition"]]
    SecondaryConnection: Optional[Sequence["_SecondaryConnectionDefinition"]]
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
            AuthorizationKey=json_data.get("AuthorizationKey"),
            DeviceInterfaceId=json_data.get("DeviceInterfaceId"),
            DeviceUuid=json_data.get("DeviceUuid"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            NamedTag=json_data.get("NamedTag"),
            Notifications=json_data.get("Notifications"),
            PortUuid=json_data.get("PortUuid"),
            ProfileUuid=json_data.get("ProfileUuid"),
            ProviderStatus=json_data.get("ProviderStatus"),
            PurchaseOrderNumber=json_data.get("PurchaseOrderNumber"),
            RedundancyType=json_data.get("RedundancyType"),
            RedundantUuid=json_data.get("RedundantUuid"),
            SellerMetroCode=json_data.get("SellerMetroCode"),
            SellerRegion=json_data.get("SellerRegion"),
            Speed=json_data.get("Speed"),
            SpeedUnit=json_data.get("SpeedUnit"),
            Status=json_data.get("Status"),
            Uuid=json_data.get("Uuid"),
            VlanCtag=json_data.get("VlanCtag"),
            VlanStag=json_data.get("VlanStag"),
            ZsidePortUuid=json_data.get("ZsidePortUuid"),
            ZsideVlanCtag=json_data.get("ZsideVlanCtag"),
            ZsideVlanStag=json_data.get("ZsideVlanStag"),
            AdditionalInfo=deserialize_list(json_data.get("AdditionalInfo"), AdditionalInfoDefinition),
            SecondaryConnection=deserialize_list(json_data.get("SecondaryConnection"), SecondaryConnectionDefinition),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class AdditionalInfoDefinition(BaseModel):
    Name: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AdditionalInfoDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AdditionalInfoDefinition"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AdditionalInfoDefinition = AdditionalInfoDefinition


@dataclass
class SecondaryConnectionDefinition(BaseModel):
    AuthorizationKey: Optional[str]
    DeviceInterfaceId: Optional[float]
    DeviceUuid: Optional[str]
    Name: Optional[str]
    PortUuid: Optional[str]
    ProfileUuid: Optional[str]
    SellerMetroCode: Optional[str]
    SellerRegion: Optional[str]
    Speed: Optional[float]
    SpeedUnit: Optional[str]
    VlanCtag: Optional[float]
    VlanStag: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_SecondaryConnectionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SecondaryConnectionDefinition"]:
        if not json_data:
            return None
        return cls(
            AuthorizationKey=json_data.get("AuthorizationKey"),
            DeviceInterfaceId=json_data.get("DeviceInterfaceId"),
            DeviceUuid=json_data.get("DeviceUuid"),
            Name=json_data.get("Name"),
            PortUuid=json_data.get("PortUuid"),
            ProfileUuid=json_data.get("ProfileUuid"),
            SellerMetroCode=json_data.get("SellerMetroCode"),
            SellerRegion=json_data.get("SellerRegion"),
            Speed=json_data.get("Speed"),
            SpeedUnit=json_data.get("SpeedUnit"),
            VlanCtag=json_data.get("VlanCtag"),
            VlanStag=json_data.get("VlanStag"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SecondaryConnectionDefinition = SecondaryConnectionDefinition


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


