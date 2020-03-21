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
    Name: Optional[str]
    ReceivingRecords: Optional[Sequence["_ReceivingRecords"]]
    Region: Optional[str]
    SendingRecords: Optional[Sequence["_SendingRecords"]]
    SmtpLogin: Optional[str]
    SmtpPassword: Optional[str]
    SpamAction: Optional[str]
    Wildcard: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Name=json_data.get("Name"),
            ReceivingRecords=json_data.get("ReceivingRecords"),
            Region=json_data.get("Region"),
            SendingRecords=json_data.get("SendingRecords"),
            SmtpLogin=json_data.get("SmtpLogin"),
            SmtpPassword=json_data.get("SmtpPassword"),
            SpamAction=json_data.get("SpamAction"),
            Wildcard=json_data.get("Wildcard"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ReceivingRecords:
    Priority: Optional[str]
    RecordType: Optional[str]
    Valid: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ReceivingRecords"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ReceivingRecords"]:
        if not json_data:
            return None
        return cls(
            Priority=json_data.get("Priority"),
            RecordType=json_data.get("RecordType"),
            Valid=json_data.get("Valid"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ReceivingRecords = ReceivingRecords


@dataclass
class SendingRecords:
    Name: Optional[str]
    RecordType: Optional[str]
    Valid: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SendingRecords"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SendingRecords"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            RecordType=json_data.get("RecordType"),
            Valid=json_data.get("Valid"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SendingRecords = SendingRecords


