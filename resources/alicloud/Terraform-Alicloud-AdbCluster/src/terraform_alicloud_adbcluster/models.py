# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass
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
    BaseResourceHandlerRequest,
    BaseResourceModel,
)

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
class ResourceModel(BaseResourceModel):
    tfcfnid: Optional[str]
    AutoRenewPeriod: Optional[float]
    DbClusterCategory: Optional[str]
    DbClusterVersion: Optional[str]
    DbNodeClass: Optional[str]
    DbNodeCount: Optional[float]
    DbNodeStorage: Optional[float]
    Description: Optional[str]
    Id: Optional[str]
    MaintainTime: Optional[str]
    PayType: Optional[str]
    Period: Optional[float]
    RenewalStatus: Optional[str]
    SecurityIps: Optional[Sequence[str]]
    Tags: Optional[Sequence["_Tags"]]
    VswitchId: Optional[str]
    ZoneId: Optional[str]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AutoRenewPeriod=json_data.get("AutoRenewPeriod"),
            DbClusterCategory=json_data.get("DbClusterCategory"),
            DbClusterVersion=json_data.get("DbClusterVersion"),
            DbNodeClass=json_data.get("DbNodeClass"),
            DbNodeCount=json_data.get("DbNodeCount"),
            DbNodeStorage=json_data.get("DbNodeStorage"),
            Description=json_data.get("Description"),
            Id=json_data.get("Id"),
            MaintainTime=json_data.get("MaintainTime"),
            PayType=json_data.get("PayType"),
            Period=json_data.get("Period"),
            RenewalStatus=json_data.get("RenewalStatus"),
            SecurityIps=json_data.get("SecurityIps"),
            Tags=json_data.get("Tags"),
            VswitchId=json_data.get("VswitchId"),
            ZoneId=json_data.get("ZoneId"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


