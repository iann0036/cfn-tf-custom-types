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
    AutoCreateRoutes: Optional[bool]
    ExportCustomRoutes: Optional[bool]
    ImportCustomRoutes: Optional[bool]
    Name: Optional[str]
    Network: Optional[str]
    PeerNetwork: Optional[str]
    State: Optional[str]
    StateDetails: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AutoCreateRoutes=json_data.get("AutoCreateRoutes"),
            ExportCustomRoutes=json_data.get("ExportCustomRoutes"),
            ImportCustomRoutes=json_data.get("ImportCustomRoutes"),
            Name=json_data.get("Name"),
            Network=json_data.get("Network"),
            PeerNetwork=json_data.get("PeerNetwork"),
            State=json_data.get("State"),
            StateDetails=json_data.get("StateDetails"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


