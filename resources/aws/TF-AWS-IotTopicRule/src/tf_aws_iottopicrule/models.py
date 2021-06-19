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
    Description: Optional[str]
    Enabled: Optional[bool]
    Id: Optional[str]
    Name: Optional[str]
    Sql: Optional[str]
    SqlVersion: Optional[str]
    Tags: Optional[Sequence["_TagsDefinition"]]
    TagsAll: Optional[Sequence["_TagsAllDefinition"]]
    CloudwatchAlarm: Optional[Sequence["_CloudwatchAlarmDefinition"]]
    CloudwatchMetric: Optional[Sequence["_CloudwatchMetricDefinition"]]
    Dynamodb: Optional[Sequence["_DynamodbDefinition"]]
    Dynamodbv2: Optional[Sequence["_Dynamodbv2Definition"]]
    Elasticsearch: Optional[Sequence["_ElasticsearchDefinition"]]
    ErrorAction: Optional[Sequence["_ErrorActionDefinition"]]
    Firehose: Optional[Sequence["_FirehoseDefinition"]]
    IotAnalytics: Optional[Sequence["_IotAnalyticsDefinition"]]
    IotEvents: Optional[Sequence["_IotEventsDefinition"]]
    Kinesis: Optional[Sequence["_KinesisDefinition"]]
    Lambda: Optional[Sequence["_LambdaDefinition"]]
    Republish: Optional[Sequence["_RepublishDefinition"]]
    S3: Optional[Sequence["_S3Definition"]]
    Sns: Optional[Sequence["_SnsDefinition"]]
    Sqs: Optional[Sequence["_SqsDefinition"]]
    StepFunctions: Optional[Sequence["_StepFunctionsDefinition"]]

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
            Description=json_data.get("Description"),
            Enabled=json_data.get("Enabled"),
            Id=json_data.get("Id"),
            Name=json_data.get("Name"),
            Sql=json_data.get("Sql"),
            SqlVersion=json_data.get("SqlVersion"),
            Tags=deserialize_list(json_data.get("Tags"), TagsDefinition),
            TagsAll=deserialize_list(json_data.get("TagsAll"), TagsAllDefinition),
            CloudwatchAlarm=deserialize_list(json_data.get("CloudwatchAlarm"), CloudwatchAlarmDefinition),
            CloudwatchMetric=deserialize_list(json_data.get("CloudwatchMetric"), CloudwatchMetricDefinition),
            Dynamodb=deserialize_list(json_data.get("Dynamodb"), DynamodbDefinition),
            Dynamodbv2=deserialize_list(json_data.get("Dynamodbv2"), Dynamodbv2Definition),
            Elasticsearch=deserialize_list(json_data.get("Elasticsearch"), ElasticsearchDefinition),
            ErrorAction=deserialize_list(json_data.get("ErrorAction"), ErrorActionDefinition),
            Firehose=deserialize_list(json_data.get("Firehose"), FirehoseDefinition),
            IotAnalytics=deserialize_list(json_data.get("IotAnalytics"), IotAnalyticsDefinition),
            IotEvents=deserialize_list(json_data.get("IotEvents"), IotEventsDefinition),
            Kinesis=deserialize_list(json_data.get("Kinesis"), KinesisDefinition),
            Lambda=deserialize_list(json_data.get("Lambda"), LambdaDefinition),
            Republish=deserialize_list(json_data.get("Republish"), RepublishDefinition),
            S3=deserialize_list(json_data.get("S3"), S3Definition),
            Sns=deserialize_list(json_data.get("Sns"), SnsDefinition),
            Sqs=deserialize_list(json_data.get("Sqs"), SqsDefinition),
            StepFunctions=deserialize_list(json_data.get("StepFunctions"), StepFunctionsDefinition),
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
class CloudwatchAlarmDefinition(BaseModel):
    AlarmName: Optional[str]
    RoleArn: Optional[str]
    StateReason: Optional[str]
    StateValue: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchAlarmDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchAlarmDefinition"]:
        if not json_data:
            return None
        return cls(
            AlarmName=json_data.get("AlarmName"),
            RoleArn=json_data.get("RoleArn"),
            StateReason=json_data.get("StateReason"),
            StateValue=json_data.get("StateValue"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchAlarmDefinition = CloudwatchAlarmDefinition


@dataclass
class CloudwatchMetricDefinition(BaseModel):
    MetricName: Optional[str]
    MetricNamespace: Optional[str]
    MetricTimestamp: Optional[str]
    MetricUnit: Optional[str]
    MetricValue: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_CloudwatchMetricDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_CloudwatchMetricDefinition"]:
        if not json_data:
            return None
        return cls(
            MetricName=json_data.get("MetricName"),
            MetricNamespace=json_data.get("MetricNamespace"),
            MetricTimestamp=json_data.get("MetricTimestamp"),
            MetricUnit=json_data.get("MetricUnit"),
            MetricValue=json_data.get("MetricValue"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_CloudwatchMetricDefinition = CloudwatchMetricDefinition


@dataclass
class DynamodbDefinition(BaseModel):
    HashKeyField: Optional[str]
    HashKeyType: Optional[str]
    HashKeyValue: Optional[str]
    Operation: Optional[str]
    PayloadField: Optional[str]
    RangeKeyField: Optional[str]
    RangeKeyType: Optional[str]
    RangeKeyValue: Optional[str]
    RoleArn: Optional[str]
    TableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_DynamodbDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_DynamodbDefinition"]:
        if not json_data:
            return None
        return cls(
            HashKeyField=json_data.get("HashKeyField"),
            HashKeyType=json_data.get("HashKeyType"),
            HashKeyValue=json_data.get("HashKeyValue"),
            Operation=json_data.get("Operation"),
            PayloadField=json_data.get("PayloadField"),
            RangeKeyField=json_data.get("RangeKeyField"),
            RangeKeyType=json_data.get("RangeKeyType"),
            RangeKeyValue=json_data.get("RangeKeyValue"),
            RoleArn=json_data.get("RoleArn"),
            TableName=json_data.get("TableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_DynamodbDefinition = DynamodbDefinition


@dataclass
class Dynamodbv2Definition(BaseModel):
    RoleArn: Optional[str]
    PutItem: Optional[Sequence["_PutItemDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_Dynamodbv2Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Dynamodbv2Definition"]:
        if not json_data:
            return None
        return cls(
            RoleArn=json_data.get("RoleArn"),
            PutItem=deserialize_list(json_data.get("PutItem"), PutItemDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_Dynamodbv2Definition = Dynamodbv2Definition


@dataclass
class PutItemDefinition(BaseModel):
    TableName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_PutItemDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_PutItemDefinition"]:
        if not json_data:
            return None
        return cls(
            TableName=json_data.get("TableName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_PutItemDefinition = PutItemDefinition


@dataclass
class ElasticsearchDefinition(BaseModel):
    Endpoint: Optional[str]
    Id: Optional[str]
    Index: Optional[str]
    RoleArn: Optional[str]
    Type: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_ElasticsearchDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ElasticsearchDefinition"]:
        if not json_data:
            return None
        return cls(
            Endpoint=json_data.get("Endpoint"),
            Id=json_data.get("Id"),
            Index=json_data.get("Index"),
            RoleArn=json_data.get("RoleArn"),
            Type=json_data.get("Type"),
        )


# work around possible type aliasing issues when variable has same name as a model
_ElasticsearchDefinition = ElasticsearchDefinition


@dataclass
class ErrorActionDefinition(BaseModel):
    CloudwatchAlarm: Optional[Sequence["_CloudwatchAlarmDefinition"]]
    CloudwatchMetric: Optional[Sequence["_CloudwatchMetricDefinition"]]
    Dynamodb: Optional[Sequence["_DynamodbDefinition"]]
    Dynamodbv2: Optional[Sequence["_Dynamodbv2Definition"]]
    Elasticsearch: Optional[Sequence["_ElasticsearchDefinition"]]
    Firehose: Optional[Sequence["_FirehoseDefinition"]]
    IotAnalytics: Optional[Sequence["_IotAnalyticsDefinition"]]
    IotEvents: Optional[Sequence["_IotEventsDefinition"]]
    Kinesis: Optional[Sequence["_KinesisDefinition"]]
    Lambda: Optional[Sequence["_LambdaDefinition"]]
    Republish: Optional[Sequence["_RepublishDefinition"]]
    S3: Optional[Sequence["_S3Definition"]]
    Sns: Optional[Sequence["_SnsDefinition"]]
    Sqs: Optional[Sequence["_SqsDefinition"]]
    StepFunctions: Optional[Sequence["_StepFunctionsDefinition"]]

    @classmethod
    def _deserialize(
        cls: Type["_ErrorActionDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_ErrorActionDefinition"]:
        if not json_data:
            return None
        return cls(
            CloudwatchAlarm=deserialize_list(json_data.get("CloudwatchAlarm"), CloudwatchAlarmDefinition),
            CloudwatchMetric=deserialize_list(json_data.get("CloudwatchMetric"), CloudwatchMetricDefinition),
            Dynamodb=deserialize_list(json_data.get("Dynamodb"), DynamodbDefinition),
            Dynamodbv2=deserialize_list(json_data.get("Dynamodbv2"), Dynamodbv2Definition),
            Elasticsearch=deserialize_list(json_data.get("Elasticsearch"), ElasticsearchDefinition),
            Firehose=deserialize_list(json_data.get("Firehose"), FirehoseDefinition),
            IotAnalytics=deserialize_list(json_data.get("IotAnalytics"), IotAnalyticsDefinition),
            IotEvents=deserialize_list(json_data.get("IotEvents"), IotEventsDefinition),
            Kinesis=deserialize_list(json_data.get("Kinesis"), KinesisDefinition),
            Lambda=deserialize_list(json_data.get("Lambda"), LambdaDefinition),
            Republish=deserialize_list(json_data.get("Republish"), RepublishDefinition),
            S3=deserialize_list(json_data.get("S3"), S3Definition),
            Sns=deserialize_list(json_data.get("Sns"), SnsDefinition),
            Sqs=deserialize_list(json_data.get("Sqs"), SqsDefinition),
            StepFunctions=deserialize_list(json_data.get("StepFunctions"), StepFunctionsDefinition),
        )


# work around possible type aliasing issues when variable has same name as a model
_ErrorActionDefinition = ErrorActionDefinition


@dataclass
class FirehoseDefinition(BaseModel):
    DeliveryStreamName: Optional[str]
    RoleArn: Optional[str]
    Separator: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_FirehoseDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_FirehoseDefinition"]:
        if not json_data:
            return None
        return cls(
            DeliveryStreamName=json_data.get("DeliveryStreamName"),
            RoleArn=json_data.get("RoleArn"),
            Separator=json_data.get("Separator"),
        )


# work around possible type aliasing issues when variable has same name as a model
_FirehoseDefinition = FirehoseDefinition


@dataclass
class IotAnalyticsDefinition(BaseModel):
    ChannelName: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IotAnalyticsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IotAnalyticsDefinition"]:
        if not json_data:
            return None
        return cls(
            ChannelName=json_data.get("ChannelName"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IotAnalyticsDefinition = IotAnalyticsDefinition


@dataclass
class IotEventsDefinition(BaseModel):
    InputName: Optional[str]
    MessageId: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_IotEventsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_IotEventsDefinition"]:
        if not json_data:
            return None
        return cls(
            InputName=json_data.get("InputName"),
            MessageId=json_data.get("MessageId"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_IotEventsDefinition = IotEventsDefinition


@dataclass
class KinesisDefinition(BaseModel):
    PartitionKey: Optional[str]
    RoleArn: Optional[str]
    StreamName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_KinesisDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_KinesisDefinition"]:
        if not json_data:
            return None
        return cls(
            PartitionKey=json_data.get("PartitionKey"),
            RoleArn=json_data.get("RoleArn"),
            StreamName=json_data.get("StreamName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_KinesisDefinition = KinesisDefinition


@dataclass
class LambdaDefinition(BaseModel):
    FunctionArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_LambdaDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_LambdaDefinition"]:
        if not json_data:
            return None
        return cls(
            FunctionArn=json_data.get("FunctionArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_LambdaDefinition = LambdaDefinition


@dataclass
class RepublishDefinition(BaseModel):
    Qos: Optional[float]
    RoleArn: Optional[str]
    Topic: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_RepublishDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_RepublishDefinition"]:
        if not json_data:
            return None
        return cls(
            Qos=json_data.get("Qos"),
            RoleArn=json_data.get("RoleArn"),
            Topic=json_data.get("Topic"),
        )


# work around possible type aliasing issues when variable has same name as a model
_RepublishDefinition = RepublishDefinition


@dataclass
class S3Definition(BaseModel):
    BucketName: Optional[str]
    Key: Optional[str]
    RoleArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_S3Definition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_S3Definition"]:
        if not json_data:
            return None
        return cls(
            BucketName=json_data.get("BucketName"),
            Key=json_data.get("Key"),
            RoleArn=json_data.get("RoleArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_S3Definition = S3Definition


@dataclass
class SnsDefinition(BaseModel):
    MessageFormat: Optional[str]
    RoleArn: Optional[str]
    TargetArn: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_SnsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SnsDefinition"]:
        if not json_data:
            return None
        return cls(
            MessageFormat=json_data.get("MessageFormat"),
            RoleArn=json_data.get("RoleArn"),
            TargetArn=json_data.get("TargetArn"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SnsDefinition = SnsDefinition


@dataclass
class SqsDefinition(BaseModel):
    QueueUrl: Optional[str]
    RoleArn: Optional[str]
    UseBase64: Optional[bool]

    @classmethod
    def _deserialize(
        cls: Type["_SqsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_SqsDefinition"]:
        if not json_data:
            return None
        return cls(
            QueueUrl=json_data.get("QueueUrl"),
            RoleArn=json_data.get("RoleArn"),
            UseBase64=json_data.get("UseBase64"),
        )


# work around possible type aliasing issues when variable has same name as a model
_SqsDefinition = SqsDefinition


@dataclass
class StepFunctionsDefinition(BaseModel):
    ExecutionNamePrefix: Optional[str]
    RoleArn: Optional[str]
    StateMachineName: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_StepFunctionsDefinition"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_StepFunctionsDefinition"]:
        if not json_data:
            return None
        return cls(
            ExecutionNamePrefix=json_data.get("ExecutionNamePrefix"),
            RoleArn=json_data.get("RoleArn"),
            StateMachineName=json_data.get("StateMachineName"),
        )


# work around possible type aliasing issues when variable has same name as a model
_StepFunctionsDefinition = StepFunctionsDefinition


