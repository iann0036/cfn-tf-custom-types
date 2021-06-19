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
    Active: Optional[bool]
    Algorithm: Optional[float]
    AnswerType: Optional[str]
    Certificate: Optional[str]
    Digest: Optional[str]
    DigestType: Optional[float]
    DnsName: Optional[str]
    EmailAddress: Optional[str]
    Expiration: Optional[str]
    Expiry: Optional[float]
    Fingerprint: Optional[str]
    FingerprintType: Optional[float]
    Flags: Optional[float]
    Flagsnaptr: Optional[str]
    Hardware: Optional[str]
    Id: Optional[str]
    Inception: Optional[str]
    Iterations: Optional[float]
    Key: Optional[str]
    Keytag: Optional[float]
    Labels: Optional[float]
    Mailbox: Optional[str]
    MatchType: Optional[float]
    Name: Optional[str]
    NameServer: Optional[str]
    NextHashedOwnerName: Optional[str]
    NxdomainTtl: Optional[float]
    Order: Optional[float]
    OriginalTtl: Optional[float]
    Port: Optional[float]
    Preference: Optional[float]
    Priority: Optional[float]
    PriorityIncrement: Optional[float]
    Protocol: Optional[float]
    RecordSha: Optional[str]
    Recordtype: Optional[str]
    Refresh: Optional[float]
    Regexp: Optional[str]
    Replacement: Optional[str]
    Retry: Optional[float]
    Salt: Optional[str]
    Selector: Optional[float]
    Serial: Optional[float]
    Service: Optional[str]
    Signature: Optional[str]
    Signer: Optional[str]
    Software: Optional[str]
    Subtype: Optional[float]
    SvcParams: Optional[str]
    SvcPriority: Optional[float]
    Target: Optional[Sequence[str]]
    TargetName: Optional[str]
    Ttl: Optional[float]
    Txt: Optional[str]
    TypeBitmaps: Optional[str]
    TypeCovered: Optional[str]
    TypeMnemonic: Optional[str]
    TypeValue: Optional[float]
    Usage: Optional[float]
    Weight: Optional[float]
    Zone: Optional[str]

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
            Active=json_data.get("Active"),
            Algorithm=json_data.get("Algorithm"),
            AnswerType=json_data.get("AnswerType"),
            Certificate=json_data.get("Certificate"),
            Digest=json_data.get("Digest"),
            DigestType=json_data.get("DigestType"),
            DnsName=json_data.get("DnsName"),
            EmailAddress=json_data.get("EmailAddress"),
            Expiration=json_data.get("Expiration"),
            Expiry=json_data.get("Expiry"),
            Fingerprint=json_data.get("Fingerprint"),
            FingerprintType=json_data.get("FingerprintType"),
            Flags=json_data.get("Flags"),
            Flagsnaptr=json_data.get("Flagsnaptr"),
            Hardware=json_data.get("Hardware"),
            Id=json_data.get("Id"),
            Inception=json_data.get("Inception"),
            Iterations=json_data.get("Iterations"),
            Key=json_data.get("Key"),
            Keytag=json_data.get("Keytag"),
            Labels=json_data.get("Labels"),
            Mailbox=json_data.get("Mailbox"),
            MatchType=json_data.get("MatchType"),
            Name=json_data.get("Name"),
            NameServer=json_data.get("NameServer"),
            NextHashedOwnerName=json_data.get("NextHashedOwnerName"),
            NxdomainTtl=json_data.get("NxdomainTtl"),
            Order=json_data.get("Order"),
            OriginalTtl=json_data.get("OriginalTtl"),
            Port=json_data.get("Port"),
            Preference=json_data.get("Preference"),
            Priority=json_data.get("Priority"),
            PriorityIncrement=json_data.get("PriorityIncrement"),
            Protocol=json_data.get("Protocol"),
            RecordSha=json_data.get("RecordSha"),
            Recordtype=json_data.get("Recordtype"),
            Refresh=json_data.get("Refresh"),
            Regexp=json_data.get("Regexp"),
            Replacement=json_data.get("Replacement"),
            Retry=json_data.get("Retry"),
            Salt=json_data.get("Salt"),
            Selector=json_data.get("Selector"),
            Serial=json_data.get("Serial"),
            Service=json_data.get("Service"),
            Signature=json_data.get("Signature"),
            Signer=json_data.get("Signer"),
            Software=json_data.get("Software"),
            Subtype=json_data.get("Subtype"),
            SvcParams=json_data.get("SvcParams"),
            SvcPriority=json_data.get("SvcPriority"),
            Target=json_data.get("Target"),
            TargetName=json_data.get("TargetName"),
            Ttl=json_data.get("Ttl"),
            Txt=json_data.get("Txt"),
            TypeBitmaps=json_data.get("TypeBitmaps"),
            TypeCovered=json_data.get("TypeCovered"),
            TypeMnemonic=json_data.get("TypeMnemonic"),
            TypeValue=json_data.get("TypeValue"),
            Usage=json_data.get("Usage"),
            Weight=json_data.get("Weight"),
            Zone=json_data.get("Zone"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


