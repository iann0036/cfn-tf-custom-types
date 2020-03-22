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
    Backend: Optional[str]
    DbName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    RotationPeriod: Optional[float]
    RotationStatements: Optional[Sequence[str]]
    Username: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Backend=json_data.get("Backend"),
            DbName=json_data.get("DbName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RotationPeriod=json_data.get("RotationPeriod"),
            RotationStatements=json_data.get("RotationStatements"),
            Username=json_data.get("Username"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


