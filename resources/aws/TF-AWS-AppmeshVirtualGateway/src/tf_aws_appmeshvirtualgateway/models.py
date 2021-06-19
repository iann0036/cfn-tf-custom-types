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
    Arn: Optional[str]
    CreatedDate: Optional[str]
    Id: Optional[str]
    LastUpdatedDate: Optional[str]
    MeshName: Optional[str]
    MeshOwner: Optional[str]
    Name: Optional[str]
    ResourceOwner: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    Spec: Optional[Sequence["_SpecDefinition"]]

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
            Arn=json_data.get("Arn"),
            CreatedDate=json_data.get("CreatedDate"),
            Id=json_data.get("Id"),
            LastUpdatedDate=json_data.get("LastUpdatedDate"),
            MeshName=json_data.get("MeshName"),
            MeshOwner=json_data.get("MeshOwner"),
            Name=json_data.get("Name"),
            ResourceOwner=json_data.get("ResourceOwner"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            Spec=deserialize_list(json_data.get("Spec"), SpecDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ResourceModel = ResourceModel


@dataclass
class TagsDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsDefinition = TagsDefinition


@dataclass
class TagsAllDefinition(BaseModel):
    MapKey: Optional[str]
    MapValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_TagsAllDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TagsAllDefinition"]:
        if not json_data:
            return None
        return cls(
            MapKey=json_data.get("MapKey"),
            MapValue=json_data.get("MapValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_TagsAllDefinition = TagsAllDefinition


@dataclass
class SpecDefinition(BaseModel):
    BackendDefaults: Optional[Sequence["_BackendDefaultsDefinition"]]
    Listener: Optional[Sequence["_ListenerDefinition"]]
    Logging: Optional[Sequence["_LoggingDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SpecDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SpecDefinition"]:
        if not json_data:
            return None
        return cls(
            BackendDefaults=deserialize_list(json_data.get("BackendDefaults"), BackendDefaultsDefinition),
            Listener=deserialize_list(json_data.get("Listener"), ListenerDefinition),
            Logging=deserialize_list(json_data.get("Logging"), LoggingDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SpecDefinition = SpecDefinition


@dataclass
class BackendDefaultsDefinition(BaseModel):
    ClientPolicy: Optional[Sequence["_ClientPolicyDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_BackendDefaultsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_BackendDefaultsDefinition"]:
        if not json_data:
            return None
        return cls(
            ClientPolicy=deserialize_list(json_data.get("ClientPolicy"), ClientPolicyDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_BackendDefaultsDefinition = BackendDefaultsDefinition


@dataclass
class ClientPolicyDefinition(BaseModel):
    Tls: Optional[Sequence["_TlsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ClientPolicyDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ClientPolicyDefinition"]:
        if not json_data:
            return None
        return cls(
            Tls=deserialize_list(json_data.get("Tls"), TlsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ClientPolicyDefinition = ClientPolicyDefinition


@dataclass
class TlsDefinition(BaseModel):
    Enforce: Optional[bool]
    Ports: Optional[Sequence[float]]
    Certificate: Optional[Sequence["_CertificateDefinition"]]
    Validation: Optional[Sequence["_ValidationDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TlsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TlsDefinition"]:
        if not json_data:
            return None
        return cls(
            Enforce=json_data.get("Enforce"),
            Ports=json_data.get("Ports"),
            Certificate=deserialize_list(json_data.get("Certificate"), CertificateDefinition),
            Validation=deserialize_list(json_data.get("Validation"), ValidationDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TlsDefinition = TlsDefinition


@dataclass
class CertificateDefinition(BaseModel):
    File: Optional[Sequence["_FileDefinition"]]
    Sds: Optional[Sequence["_SdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_CertificateDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CertificateDefinition"]:
        if not json_data:
            return None
        return cls(
            File=deserialize_list(json_data.get("File"), FileDefinition),
            Sds=deserialize_list(json_data.get("Sds"), SdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_CertificateDefinition = CertificateDefinition


@dataclass
class FileDefinition(BaseModel):
    CertificateChain: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FileDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FileDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateChain=json_data.get("CertificateChain"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FileDefinition = FileDefinition


@dataclass
class SdsDefinition(BaseModel):
    SecretName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SdsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SdsDefinition"]:
        if not json_data:
            return None
        return cls(
            SecretName=json_data.get("SecretName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SdsDefinition = SdsDefinition


@dataclass
class ValidationDefinition(BaseModel):
    SubjectAlternativeNames: Optional[Sequence["_SubjectAlternativeNamesDefinition"]]
    Trust: Optional[Sequence["_TrustDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ValidationDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ValidationDefinition"]:
        if not json_data:
            return None
        return cls(
            SubjectAlternativeNames=deserialize_list(json_data.get("SubjectAlternativeNames"), SubjectAlternativeNamesDefinition),
            Trust=deserialize_list(json_data.get("Trust"), TrustDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ValidationDefinition = ValidationDefinition


@dataclass
class SubjectAlternativeNamesDefinition(BaseModel):
    Match: Optional[Sequence["_MatchDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_SubjectAlternativeNamesDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SubjectAlternativeNamesDefinition"]:
        if not json_data:
            return None
        return cls(
            Match=deserialize_list(json_data.get("Match"), MatchDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_SubjectAlternativeNamesDefinition = SubjectAlternativeNamesDefinition


@dataclass
class MatchDefinition(BaseModel):
    Exact: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_MatchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_MatchDefinition"]:
        if not json_data:
            return None
        return cls(
            Exact=json_data.get("Exact"),
        )


# work around possible type aliasing issues when variable has same name as a model
_MatchDefinition = MatchDefinition


@dataclass
class TrustDefinition(BaseModel):
    Acm: Optional[Sequence["_AcmDefinition"]]
    File: Optional[Sequence["_FileDefinition"]]
    Sds: Optional[Sequence["_SdsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_TrustDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_TrustDefinition"]:
        if not json_data:
            return None
        return cls(
            Acm=deserialize_list(json_data.get("Acm"), AcmDefinition),
            File=deserialize_list(json_data.get("File"), FileDefinition),
            Sds=deserialize_list(json_data.get("Sds"), SdsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_TrustDefinition = TrustDefinition


@dataclass
class AcmDefinition(BaseModel):
    CertificateAuthorityArns: Optional[Sequence[str]]

    @classmethod
    def _deserialize(
        cls: Type["_AcmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AcmDefinition"]:
        if not json_data:
            return None
        return cls(
            CertificateAuthorityArns=json_data.get("CertificateAuthorityArns"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AcmDefinition = AcmDefinition


@dataclass
class ListenerDefinition(BaseModel):
    ConnectionPool: Optional[Sequence["_ConnectionPoolDefinition"]]
    HealthCheck: Optional[Sequence["_HealthCheckDefinition"]]
    PortMapping: Optional[Sequence["_PortMappingDefinition"]]
    Tls: Optional[Sequence["_TlsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ListenerDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ListenerDefinition"]:
        if not json_data:
            return None
        return cls(
            ConnectionPool=deserialize_list(json_data.get("ConnectionPool"), ConnectionPoolDefinition),
            HealthCheck=deserialize_list(json_data.get("HealthCheck"), HealthCheckDefinition),
            PortMapping=deserialize_list(json_data.get("PortMapping"), PortMappingDefinition),
            Tls=deserialize_list(json_data.get("Tls"), TlsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ListenerDefinition = ListenerDefinition


@dataclass
class ConnectionPoolDefinition(BaseModel):
    Grpc: Optional[Sequence["_GrpcDefinition"]]
    Http: Optional[Sequence["_HttpDefinition"]]
    Http2: Optional[Sequence["_Http2Definition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ConnectionPoolDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ConnectionPoolDefinition"]:
        if not json_data:
            return None
        return cls(
            Grpc=deserialize_list(json_data.get("Grpc"), GrpcDefinition),
            Http=deserialize_list(json_data.get("Http"), HttpDefinition),
            Http2=deserialize_list(json_data.get("Http2"), Http2Definition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ConnectionPoolDefinition = ConnectionPoolDefinition


@dataclass
class GrpcDefinition(BaseModel):
    MaxRequests: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_GrpcDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_GrpcDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxRequests=json_data.get("MaxRequests"),
        )


# work around possible type aliasing issues when variable has same name as a model
_GrpcDefinition = GrpcDefinition


@dataclass
class HttpDefinition(BaseModel):
    MaxConnections: Optional[float]
    MaxPendingRequests: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HttpDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HttpDefinition"]:
        if not json_data:
            return None
        return cls(
            MaxConnections=json_data.get("MaxConnections"),
            MaxPendingRequests=json_data.get("MaxPendingRequests"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HttpDefinition = HttpDefinition


@dataclass
class Http2Definition(BaseModel):
    MaxRequests: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_Http2Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Http2Definition"]:
        if not json_data:
            return None
        return cls(
            MaxRequests=json_data.get("MaxRequests"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Http2Definition = Http2Definition


@dataclass
class HealthCheckDefinition(BaseModel):
    HealthyThreshold: Optional[float]
    IntervalMillis: Optional[float]
    Path: Optional[str]
    Port: Optional[float]
    Protocol: Optional[str]
    TimeoutMillis: Optional[float]
    UnhealthyThreshold: Optional[float]

    @classmethod
    def _deserialize(
        cls: Type["_HealthCheckDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_HealthCheckDefinition"]:
        if not json_data:
            return None
        return cls(
            HealthyThreshold=json_data.get("HealthyThreshold"),
            IntervalMillis=json_data.get("IntervalMillis"),
            Path=json_data.get("Path"),
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
            TimeoutMillis=json_data.get("TimeoutMillis"),
            UnhealthyThreshold=json_data.get("UnhealthyThreshold"),
        )


# work around possible type aliasing issues when variable has same name as a model
_HealthCheckDefinition = HealthCheckDefinition


@dataclass
class PortMappingDefinition(BaseModel):
    Port: Optional[float]
    Protocol: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PortMappingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PortMappingDefinition"]:
        if not json_data:
            return None
        return cls(
            Port=json_data.get("Port"),
            Protocol=json_data.get("Protocol"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PortMappingDefinition = PortMappingDefinition


@dataclass
class LoggingDefinition(BaseModel):
    AccessLog: Optional[Sequence["_AccessLogDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_LoggingDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LoggingDefinition"]:
        if not json_data:
            return None
        return cls(
            AccessLog=deserialize_list(json_data.get("AccessLog"), AccessLogDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_LoggingDefinition = LoggingDefinition


@dataclass
class AccessLogDefinition(BaseModel):
    File: Optional[Sequence["_FileDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_AccessLogDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AccessLogDefinition"]:
        if not json_data:
            return None
        return cls(
            File=deserialize_list(json_data.get("File"), FileDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_AccessLogDefinition = AccessLogDefinition


