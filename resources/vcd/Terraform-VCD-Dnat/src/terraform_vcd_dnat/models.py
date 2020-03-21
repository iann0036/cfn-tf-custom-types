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
    Description: Optional[str]
    EdgeGateway: Optional[str]
    ExternalIp: Optional[str]
    IcmpSubType: Optional[str]
    InternalIp: Optional[str]
    NetworkName: Optional[str]
    NetworkType: Optional[str]
    Org: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    TranslatedPort: Optional[float]
    Vdc: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Description=json_data.get("Description"),
            EdgeGateway=json_data.get("EdgeGateway"),
            ExternalIp=json_data.get("ExternalIp"),
            IcmpSubType=json_data.get("IcmpSubType"),
            InternalIp=json_data.get("InternalIp"),
            NetworkName=json_data.get("NetworkName"),
            NetworkType=json_data.get("NetworkType"),
            Org=json_data.get("Org"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            TranslatedPort=json_data.get("TranslatedPort"),
            Vdc=json_data.get("Vdc"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


