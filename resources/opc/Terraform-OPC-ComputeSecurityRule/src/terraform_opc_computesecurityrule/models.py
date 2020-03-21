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
    Acl: Optional[str]
    Description: Optional[str]
    DstIpAddressPrefixes: Optional[Sequence[str]]
    DstVnicSet: Optional[str]
    Enabled: Optional[bool]
    FlowDirection: Optional[str]
    Name: Optional[str]
    SecurityProtocols: Optional[Sequence[str]]
    SrcIpAddressPrefixes: Optional[Sequence[str]]
    SrcVnicSet: Optional[str]
    Tags: Optional[Sequence[str]]
    Uri: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Acl=json_data.get("Acl"),
            Description=json_data.get("Description"),
            DstIpAddressPrefixes=json_data.get("DstIpAddressPrefixes"),
            DstVnicSet=json_data.get("DstVnicSet"),
            Enabled=json_data.get("Enabled"),
            FlowDirection=json_data.get("FlowDirection"),
            Name=json_data.get("Name"),
            SecurityProtocols=json_data.get("SecurityProtocols"),
            SrcIpAddressPrefixes=json_data.get("SrcIpAddressPrefixes"),
            SrcVnicSet=json_data.get("SrcVnicSet"),
            Tags=json_data.get("Tags"),
            Uri=json_data.get("Uri"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


