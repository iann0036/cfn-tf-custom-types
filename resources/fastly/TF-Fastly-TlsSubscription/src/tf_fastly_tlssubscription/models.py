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
    CertificateAuthority: Optional[str]
    CommonName: Optional[str]
    ConfigurationId: Optional[str]
    CreatedAt: Optional[str]
    Domains: Optional[Sequence[str]]
    ForceDestroy: Optional[bool]
    ForceUpdate: Optional[bool]
    Id: Optional[str]
    ManagedDnsChallenge: Optional[Sequence["_ManagedDnsChallengeDefinition"]]
    ManagedHttpChallenges: Optional[Sequence["_ManagedHttpChallengesDefinition"]]
    State: Optional[str]
    UpdatedAt: Optional[str]

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
            CertificateAuthority=json_data.get("CertificateAuthority"),
            CommonName=json_data.get("CommonName"),
            ConfigurationId=json_data.get("ConfigurationId"),
            CreatedAt=json_data.get("CreatedAt"),
            Domains=json_data.get("Domains"),
            ForceDestroy=json_data.get("ForceDestroy"),
            ForceUpdate=json_data.get("ForceUpdate"),
            Id=json_data.get("Id"),
            ManagedDnsChallenge=deserialize_list(json_data.get("ManagedDnsChallenge"), ManagedDnsChallengeDefinition),
            ManagedHttpChallenges=deserialize_list(json_data.get("ManagedHttpChallenges"), ManagedHttpChallengesDefinition),
            State=json_data.get("State"),
            UpdatedAt=json_data.get("UpdatedAt"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class ManagedDnsChallengeDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedDnsChallengeDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedDnsChallengeDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedDnsChallengeDefinition = ManagedDnsChallengeDefinition


@dataclass
class ManagedHttpChallengesDefinition(BaseModel):
    RecordName: Optional[str]
    RecordType: Optional[str]
    RecordValues: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_ManagedHttpChallengesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ManagedHttpChallengesDefinition"]:
        if not json_data:
            return None
        return cls(
            RecordName=json_data.get("RecordName"),
            RecordType=json_data.get("RecordType"),
            RecordValues=json_data.get("RecordValues"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ManagedHttpChallengesDefinition = ManagedHttpChallengesDefinition


