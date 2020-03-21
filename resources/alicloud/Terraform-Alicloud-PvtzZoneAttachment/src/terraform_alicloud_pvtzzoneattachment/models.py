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
    Lang: Optional[str]
    UserClientIp: Optional[str]
    VpcIds: Optional[Sequence[str]]
    ZoneId: Optional[str]
    Vpcs: Optional[Sequence["_Vpcs"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Lang=json_data.get("Lang"),
            UserClientIp=json_data.get("UserClientIp"),
            VpcIds=json_data.get("VpcIds"),
            ZoneId=json_data.get("ZoneId"),
            Vpcs=json_data.get("Vpcs"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Vpcs:
    RegionId: Optional[str]
    VpcId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Vpcs"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Vpcs"]:
        if not json_data:
            return None
        return cls(
            RegionId=json_data.get("RegionId"),
            VpcId=json_data.get("VpcId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Vpcs = Vpcs


