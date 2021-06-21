# DO NOT modify this file by hand, changes will be overwritten
import sys
from dataclasses import dataclass
from inspect import getmembers, isclass
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
    BaseModel,
    BaseResourceHandlerRequest,
)
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

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
class ResourceModel(BaseModel):
    tfcfnid: Optional[str]
    CertificateChain: Optional[str]
    ChangeTime: Optional[str]
    CommonName: Optional[str]
    CreateTime: Optional[str]
    Fingerprints: Optional[Sequence["_FingerprintsDefinition"]]
    Id: Optional[str]
    Labels: Optional[Sequence[str]]
    LeafCertificate: Optional[str]
    Name: Optional[str]
    NotValidAfter: Optional[str]
    PrivateKey: Optional[str]
    Status: Optional[str]
    Timeouts: Optional["_TimeoutsDefinition"]

    @classmethod
    def _deserialize(
        cls: Type["_ResourceModel"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ResourceModel"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            tfcfnid=json_data.get("tfcfnid"),
            CertificateChain=json_data.get("CertificateChain"),
            ChangeTime=json_data.get("ChangeTime"),
            CommonName=json_data.get("CommonName"),
            CreateTime=json_data.get("CreateTime"),
            Fingerprints=deserialize_list(json_data.get("Fingerprints"), FingerprintsDefinition),
            Id=json_data.get("Id"),
            Labels=json_data.get("Labels"),
            LeafCertificate=json_data.get("LeafCertificate"),
            Name=json_data.get("Name"),
            NotValidAfter=json_data.get("NotValidAfter"),
            PrivateKey=json_data.get("PrivateKey"),
            Status=json_data.get("Status"),
            Timeouts=TimeoutsDefinition._deserialize(json_data.get("Timeouts")),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class FingerprintsDefinition(BaseModel):
    Md5: Optional[str]
    Sha1: Optional[str]
    Sha256: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FingerprintsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FingerprintsDefinition"]:
        if not json_data:
            return None
        return cls(
            Md5=json_data.get("Md5"),
            Sha1=json_data.get("Sha1"),
            Sha256=json_data.get("Sha256"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FingerprintsDefinition = FingerprintsDefinition


@dataclass
class TimeoutsDefinition(BaseModel):
    Create: Optional[str]
    Delete: Optional[str]
    Update: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TimeoutsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TimeoutsDefinition"]:
        if not json_data:
            return None
        return cls(
            Create=json_data.get("Create"),
            Delete=json_data.get("Delete"),
            Update=json_data.get("Update"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TimeoutsDefinition = TimeoutsDefinition

