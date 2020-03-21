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
    Href: Optional[str]
    IpVersion: Optional[float]
    Network: Optional[str]
    NextHop: Optional[str]
    PrefixLength: Optional[float]
    RegionSlug: Optional[str]
    ReversePtr: Optional[str]
    Server: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Href=json_data.get("Href"),
            IpVersion=json_data.get("IpVersion"),
            Network=json_data.get("Network"),
            NextHop=json_data.get("NextHop"),
            PrefixLength=json_data.get("PrefixLength"),
            RegionSlug=json_data.get("RegionSlug"),
            ReversePtr=json_data.get("ReversePtr"),
            Server=json_data.get("Server"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


