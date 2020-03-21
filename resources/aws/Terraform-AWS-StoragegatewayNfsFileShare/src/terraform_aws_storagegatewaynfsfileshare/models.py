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
    ClientList: Optional[Sequence[str]]
    DefaultStorageClass: Optional[str]
    FileshareId: Optional[str]
    GatewayArn: Optional[str]
    GuessMimeTypeEnabled: Optional[bool]
    Id: Optional[str]
    KmsEncrypted: Optional[bool]
    KmsKeyArn: Optional[str]
    LocationArn: Optional[str]
    ObjectAcl: Optional[str]
    ReadOnly: Optional[bool]
    RequesterPays: Optional[bool]
    RoleArn: Optional[str]
    Squash: Optional[str]
    Tags: Optional[Sequence["_Tags"]]
    NfsFileShareDefaults: Optional[Sequence["_NfsFileShareDefaults"]]
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
            ClientList=json_data.get("ClientList"),
            DefaultStorageClass=json_data.get("DefaultStorageClass"),
            FileshareId=json_data.get("FileshareId"),
            GatewayArn=json_data.get("GatewayArn"),
            GuessMimeTypeEnabled=json_data.get("GuessMimeTypeEnabled"),
            Id=json_data.get("Id"),
            KmsEncrypted=json_data.get("KmsEncrypted"),
            KmsKeyArn=json_data.get("KmsKeyArn"),
            LocationArn=json_data.get("LocationArn"),
            ObjectAcl=json_data.get("ObjectAcl"),
            ReadOnly=json_data.get("ReadOnly"),
            RequesterPays=json_data.get("RequesterPays"),
            RoleArn=json_data.get("RoleArn"),
            Squash=json_data.get("Squash"),
            Tags=json_data.get("Tags"),
            NfsFileShareDefaults=json_data.get("NfsFileShareDefaults"),
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
class NfsFileShareDefaults:
    DirectoryMode: Optional[str]
    FileMode: Optional[str]
    GroupId: Optional[float]
    OwnerId: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_NfsFileShareDefaults"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_NfsFileShareDefaults"]:
        if not json_data:
            return None
        return cls(
            DirectoryMode=json_data.get("DirectoryMode"),
            FileMode=json_data.get("FileMode"),
            GroupId=json_data.get("GroupId"),
            OwnerId=json_data.get("OwnerId"),
        )


# work around possible type aliasing issues when variable has same name as a model
_NfsFileShareDefaults = NfsFileShareDefaults


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


