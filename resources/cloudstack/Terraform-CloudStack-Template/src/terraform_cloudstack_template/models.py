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
    DisplayText: Optional[str]
    Format: Optional[str]
    Hypervisor: Optional[str]
    IsDynamicallyScalable: Optional[bool]
    IsExtractable: Optional[bool]
    IsFeatured: Optional[bool]
    IsPublic: Optional[bool]
    IsReady: Optional[bool]
    IsReadyTimeout: Optional[float]
    Name: Optional[str]
    OsType: Optional[str]
    PasswordEnabled: Optional[bool]
    Project: Optional[str]
    Url: Optional[str]
    Zone: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            DisplayText=json_data.get("DisplayText"),
            Format=json_data.get("Format"),
            Hypervisor=json_data.get("Hypervisor"),
            IsDynamicallyScalable=json_data.get("IsDynamicallyScalable"),
            IsExtractable=json_data.get("IsExtractable"),
            IsFeatured=json_data.get("IsFeatured"),
            IsPublic=json_data.get("IsPublic"),
            IsReady=json_data.get("IsReady"),
            IsReadyTimeout=json_data.get("IsReadyTimeout"),
            Name=json_data.get("Name"),
            OsType=json_data.get("OsType"),
            PasswordEnabled=json_data.get("PasswordEnabled"),
            Project=json_data.get("Project"),
            Url=json_data.get("Url"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


