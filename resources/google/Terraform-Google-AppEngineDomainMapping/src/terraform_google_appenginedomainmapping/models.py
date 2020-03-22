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
    DomainName: Optional[str]
    Id: Optional[str]
    Name: Optional[str]
    OverrideStrategy: Optional[str]
    Project: Optional[str]
    ResourceRecords: Optional[Sequence["_ResourceRecords"]]
    SslSettings: Optional[Sequence["_SslSettings"]]
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
            DomainName=json_data.get("DomainName"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            OverrideStrategy=json_data.get("OverrideStrategy"),
            Project=json_data.get("Project"),
            ResourceRecords=json_data.get("ResourceRecords"),
            SslSettings=json_data.get("SslSettings"),
            Timeouts=Timeouts._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ResourceRecords:
    Name: Optional[str]
    Rrdata: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceRecords"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceRecords"]:
        if not json_data:
            return None
        return cls(
            Name=json_data.get("Name"),
            Rrdata=json_data.get("Rrdata"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceRecords = ResourceRecords


@dataclass
class SslSettings:
    CertificateId: Optional[str]
    SslManagementType: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SslSettings"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SslSettings"]:
        if not json_data:
            return None
        return cls(
            CertificateId=json_data.get("CertificateId"),
            SslManagementType=json_data.get("SslManagementType"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SslSettings = SslSettings


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


