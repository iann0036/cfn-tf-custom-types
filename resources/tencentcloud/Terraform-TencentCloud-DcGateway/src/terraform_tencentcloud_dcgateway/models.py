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
    CnnRouteType: Optional[str]
    CreateTime: Optional[str]
    EnableBgp: Optional[bool]
    GatewayType: Optional[str]
    Name: Optional[str]
    NetworkInstanceId: Optional[str]
    NetworkType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CnnRouteType=json_data.get("CnnRouteType"),
            CreateTime=json_data.get("CreateTime"),
            EnableBgp=json_data.get("EnableBgp"),
            GatewayType=json_data.get("GatewayType"),
            Name=json_data.get("Name"),
            NetworkInstanceId=json_data.get("NetworkInstanceId"),
            NetworkType=json_data.get("NetworkType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


