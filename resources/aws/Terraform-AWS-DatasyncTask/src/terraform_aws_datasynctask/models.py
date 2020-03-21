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
    Arn: Optional[str]
    CloudwatchLogGroupArn: Optional[str]
    DestinationLocationArn: Optional[str]
    Name: Optional[str]
    SourceLocationArn: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    Options: Optional[Sequence["_Options"]]
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
            Arn=json_data.get("Arn"),
            CloudwatchLogGroupArn=json_data.get("CloudwatchLogGroupArn"),
            DestinationLocationArn=json_data.get("DestinationLocationArn"),
            Name=json_data.get("Name"),
            SourceLocationArn=json_data.get("SourceLocationArn"),
            Tags=json_data.get("Tags"),
            Options=json_data.get("Options"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class Tags:
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tags"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tags"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tags = Tags


@dataclass
class Options:
    Atime: Optional[str]
    BytesPerSecond: Optional[float]
    Gid: Optional[str]
    Mtime: Optional[str]
    PosixPermissions: Optional[str]
    PreserveDeletedFiles: Optional[str]
    PreserveDevices: Optional[str]
    Uid: Optional[str]
    VerifyMode: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Options"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Options"]:
        if not json_data:
            return None
        return cls(
            Atime=json_data.get("Atime"),
            BytesPerSecond=json_data.get("BytesPerSecond"),
            Gid=json_data.get("Gid"),
            Mtime=json_data.get("Mtime"),
            PosixPermissions=json_data.get("PosixPermissions"),
            PreserveDeletedFiles=json_data.get("PreserveDeletedFiles"),
            PreserveDevices=json_data.get("PreserveDevices"),
            Uid=json_data.get("Uid"),
            VerifyMode=json_data.get("VerifyMode"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Options = Options


@dataclass
class Timeouts:
    Create: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Timeouts"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Timeouts"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Timeouts = Timeouts


