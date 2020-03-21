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
    Cidr: Optional[str]
    Dpd: Optional[bool]
    EspLifetime: Optional[float]
    EspPolicy: Optional[str]
    Gateway: Optional[str]
    IkeLifetime: Optional[float]
    IkePolicy: Optional[str]
    IpsecPsk: Optional[str]
    Name: Optional[str]
    Project: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Cidr=json_data.get("Cidr"),
            Dpd=json_data.get("Dpd"),
            EspLifetime=json_data.get("EspLifetime"),
            EspPolicy=json_data.get("EspPolicy"),
            Gateway=json_data.get("Gateway"),
            IkeLifetime=json_data.get("IkeLifetime"),
            IkePolicy=json_data.get("IkePolicy"),
            IpsecPsk=json_data.get("IpsecPsk"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


