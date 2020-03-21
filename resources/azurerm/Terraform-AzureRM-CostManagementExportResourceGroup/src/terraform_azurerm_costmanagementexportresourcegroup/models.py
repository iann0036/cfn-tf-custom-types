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
    Active: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    RecurrencePeriodEnd: Optional[str]
    RecurrencePeriodStart: Optional[str]
    RecurrenceType: Optional[str]
    ResourceGroupId: Optional[str]
    DeliveryInfo: Optional[Sequence["_DeliveryInfo"]]
    Query: Optional[Sequence["_Query"]]
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
            Active=json_data.get("Active"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            RecurrencePeriodEnd=json_data.get("RecurrencePeriodEnd"),
            RecurrencePeriodStart=json_data.get("RecurrencePeriodStart"),
            RecurrenceType=json_data.get("RecurrenceType"),
            ResourceGroupId=json_data.get("ResourceGroupId"),
            DeliveryInfo=json_data.get("DeliveryInfo"),
            Query=json_data.get("Query"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class DeliveryInfo:
    ContainerName: Optional[str]
    RootFolderPath: Optional[str]
    StorageAccountId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DeliveryInfo"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DeliveryInfo"]:
        if not json_data:
            return None
        return cls(
            ContainerName=json_data.get("ContainerName"),
            RootFolderPath=json_data.get("RootFolderPath"),
            StorageAccountId=json_data.get("StorageAccountId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DeliveryInfo = DeliveryInfo


@dataclass
class Query:
    TimeFrame: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Query"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Query"]:
        if not json_data:
            return None
        return cls(
            TimeFrame=json_data.get("TimeFrame"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Query = Query


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


