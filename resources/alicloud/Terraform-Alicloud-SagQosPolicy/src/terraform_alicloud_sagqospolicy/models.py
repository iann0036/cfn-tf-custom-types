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
    DestCidr: Optional[str]
    DestPortRange: Optional[str]
    EndTime: Optional[str]
    IpProtocol: Optional[str]
    Name: Optional[str]
    Priority: Optional[float]
    QosId: Optional[str]
    SourceCidr: Optional[str]
    SourcePortRange: Optional[str]
    StartTime: Optional[str]

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
            DestCidr=json_data.get("DestCidr"),
            DestPortRange=json_data.get("DestPortRange"),
            EndTime=json_data.get("EndTime"),
            IpProtocol=json_data.get("IpProtocol"),
            Name=json_data.get("Name"),
            Priority=json_data.get("Priority"),
            QosId=json_data.get("QosId"),
            SourceCidr=json_data.get("SourceCidr"),
            SourcePortRange=json_data.get("SourcePortRange"),
            StartTime=json_data.get("StartTime"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


