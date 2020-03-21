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
    ApiManagementName: Optional[str]
    Buffered: Optional[bool]
    Description: Optional[str]
    Name: Optional[str]
    ResourceGroupName: Optional[str]
    ApplicationInsights: Optional[Sequence["_ApplicationInsights"]]
    Eventhub: Optional[Sequence["_Eventhub"]]
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
            ApiManagementName=json_data.get("ApiManagementName"),
            Buffered=json_data.get("Buffered"),
            Description=json_data.get("Description"),
            Name=json_data.get("Name"),
            ResourceGroupName=json_data.get("ResourceGroupName"),
            ApplicationInsights=json_data.get("ApplicationInsights"),
            Eventhub=json_data.get("Eventhub"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ApplicationInsights:
    InstrumentationKey: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ApplicationInsights"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ApplicationInsights"]:
        if not json_data:
            return None
        return cls(
            InstrumentationKey=json_data.get("InstrumentationKey"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ApplicationInsights = ApplicationInsights


@dataclass
class Eventhub:
    ConnectionString: Optional[str]
    Name: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Eventhub"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Eventhub"]:
        if not json_data:
            return None
        return cls(
            ConnectionString=json_data.get("ConnectionString"),
            Name=json_data.get("Name"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Eventhub = Eventhub


@dataclass
class Timeouts:
    Create: Optional[str]
    Delete: Optional[str]
    Read: Optional[str]
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
            Read=json_data.get("Read"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


