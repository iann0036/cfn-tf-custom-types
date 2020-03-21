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
    Cutoff: Optional[float]
    DecayHalfLifeReachable: Optional[float]
    DecayHalfLifeUnreachable: Optional[float]
    Enable: Optional[bool]
    MaxHoldTime: Optional[float]
    Name: Optional[str]
    Reuse: Optional[float]
    Template: Optional[str]
    TemplateStack: Optional[str]
    VirtualRouter: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Cutoff=json_data.get("Cutoff"),
            DecayHalfLifeReachable=json_data.get("DecayHalfLifeReachable"),
            DecayHalfLifeUnreachable=json_data.get("DecayHalfLifeUnreachable"),
            Enable=json_data.get("Enable"),
            MaxHoldTime=json_data.get("MaxHoldTime"),
            Name=json_data.get("Name"),
            Reuse=json_data.get("Reuse"),
            Template=json_data.get("Template"),
            TemplateStack=json_data.get("TemplateStack"),
            VirtualRouter=json_data.get("VirtualRouter"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


