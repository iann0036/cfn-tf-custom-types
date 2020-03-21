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
    AppProfileId: Optional[str]
    Description: Optional[str]
    IgnoreWarnings: Optional[bool]
    Instance: Optional[str]
    MultiClusterRoutingUseAny: Optional[bool]
    Name: Optional[str]
    Project: Optional[str]
    SingleClusterRouting: Optional[Sequence["_SingleClusterRouting"]]
    Timeouts: Optional["_Timeouts"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            AppProfileId=json_data.get("AppProfileId"),
            Description=json_data.get("Description"),
            IgnoreWarnings=json_data.get("IgnoreWarnings"),
            Instance=json_data.get("Instance"),
            MultiClusterRoutingUseAny=json_data.get("MultiClusterRoutingUseAny"),
            Name=json_data.get("Name"),
            Project=json_data.get("Project"),
            SingleClusterRouting=json_data.get("SingleClusterRouting"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class SingleClusterRouting:
    AllowTransactionalWrites: Optional[bool]
    ClusterId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SingleClusterRouting"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SingleClusterRouting"]:
        if not json_data:
            return None
        return cls(
            AllowTransactionalWrites=json_data.get("AllowTransactionalWrites"),
            ClusterId=json_data.get("ClusterId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SingleClusterRouting = SingleClusterRouting


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


