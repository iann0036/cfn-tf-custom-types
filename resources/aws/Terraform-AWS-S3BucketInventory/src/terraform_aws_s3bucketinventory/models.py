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
    Bucket: Optional[Sequence["_Bucket"]]
    Enabled: Optional[bool]
    IncludedObjectVersions: Optional[str]
    Name: Optional[str]
    OptionalFields: Optional[Sequence[str]]
    Destination: Optional[Sequence["_Destination"]]
    Filter: Optional[Sequence["_Filter"]]
    Schedule: Optional[Sequence["_Schedule"]]
    Encryption: Optional[Sequence["_Encryption"]]
    SseKms: Optional[Sequence["_SseKms"]]
    SseS3: Optional[Sequence["_SseS3"]]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            Bucket=json_data.get("Bucket"),
            Enabled=json_data.get("Enabled"),
            IncludedObjectVersions=json_data.get("IncludedObjectVersions"),
            Name=json_data.get("Name"),
            OptionalFields=json_data.get("OptionalFields"),
            Destination=json_data.get("Destination"),
            Filter=json_data.get("Filter"),
            Schedule=json_data.get("Schedule"),
            Encryption=json_data.get("Encryption"),
            SseKms=json_data.get("SseKms"),
            SseS3=json_data.get("SseS3"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Bucket:
    AccountId: Optional[str]
    BucketArn: Optional[str]
    Format: Optional[str]
    Prefix: Optional[str]
    Encryption: Optional[Sequence["_Encryption"]]

    @classmethod
    def _deserialize(
        cls: Type["_Bucket"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Bucket"]:
        if not json_data:
            return None
        return cls(
            AccountId=json_data.get("AccountId"),
            BucketArn=json_data.get("BucketArn"),
            Format=json_data.get("Format"),
            Prefix=json_data.get("Prefix"),
            Encryption=json_data.get("Encryption"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Bucket = Bucket


@dataclass
class Encryption:
    SseKms: Optional[Sequence["_SseKms"]]
    SseS3: Optional[Sequence["_SseS3"]]

    @classmethod
    def _deserialize(
        cls: Type["_Encryption"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Encryption"]:
        if not json_data:
            return None
        return cls(
            SseKms=json_data.get("SseKms"),
            SseS3=json_data.get("SseS3"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Encryption = Encryption


@dataclass
class SseKms:
    KeyId: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SseKms"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SseKms"]:
        if not json_data:
            return None
        return cls(
            KeyId=json_data.get("KeyId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SseKms = SseKms


@dataclass
class SseS3:
    IsPropertyDefined: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SseS3"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SseS3"]:
        if not json_data:
            return None
        return cls(
            IsPropertyDefined=json_data.get("IsPropertyDefined"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SseS3 = SseS3


@dataclass
class Destination:
    Bucket: Optional[Sequence["_Bucket"]]

    @classmethod
    def _deserialize(
        cls: Type["_Destination"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Destination"]:
        if not json_data:
            return None
        return cls(
            Bucket=json_data.get("Bucket"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Destination = Destination


@dataclass
class Filter:
    Prefix: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Filter"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Filter"]:
        if not json_data:
            return None
        return cls(
            Prefix=json_data.get("Prefix"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Filter = Filter


@dataclass
class Schedule:
    Frequency: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Schedule"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Schedule"]:
        if not json_data:
            return None
        return cls(
            Frequency=json_data.get("Frequency"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Schedule = Schedule


