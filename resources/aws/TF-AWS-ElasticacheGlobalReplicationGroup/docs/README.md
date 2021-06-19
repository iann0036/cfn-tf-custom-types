# TF::AWS::ElasticacheGlobalReplicationGroup

Provides an ElastiCache Global Replication Group resource, which manages replication between two or more Replication Groups in different regions. For more information, see the [ElastiCache User Guide](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Redis-Global-Datastore.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ElasticacheGlobalReplicationGroup",
    "Properties" : {
        "<a href="#globalreplicationgroupdescription" title="GlobalReplicationGroupDescription">GlobalReplicationGroupDescription</a>" : <i>String</i>,
        "<a href="#globalreplicationgroupidsuffix" title="GlobalReplicationGroupIdSuffix">GlobalReplicationGroupIdSuffix</a>" : <i>String</i>,
        "<a href="#primaryreplicationgroupid" title="PrimaryReplicationGroupId">PrimaryReplicationGroupId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ElasticacheGlobalReplicationGroup
Properties:
    <a href="#globalreplicationgroupdescription" title="GlobalReplicationGroupDescription">GlobalReplicationGroupDescription</a>: <i>String</i>
    <a href="#globalreplicationgroupidsuffix" title="GlobalReplicationGroupIdSuffix">GlobalReplicationGroupIdSuffix</a>: <i>String</i>
    <a href="#primaryreplicationgroupid" title="PrimaryReplicationGroupId">PrimaryReplicationGroupId</a>: <i>String</i>
</pre>

## Properties

#### GlobalReplicationGroupDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GlobalReplicationGroupIdSuffix

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryReplicationGroupId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ActualEngineVersion

Returns the <code>ActualEngineVersion</code> value.

#### Arn

Returns the <code>Arn</code> value.

#### AtRestEncryptionEnabled

Returns the <code>AtRestEncryptionEnabled</code> value.

#### AuthTokenEnabled

Returns the <code>AuthTokenEnabled</code> value.

#### CacheNodeType

Returns the <code>CacheNodeType</code> value.

#### ClusterEnabled

Returns the <code>ClusterEnabled</code> value.

#### Engine

Returns the <code>Engine</code> value.

#### EngineVersionActual

Returns the <code>EngineVersionActual</code> value.

#### GlobalReplicationGroupId

Returns the <code>GlobalReplicationGroupId</code> value.

#### Id

Returns the <code>Id</code> value.

#### TransitEncryptionEnabled

Returns the <code>TransitEncryptionEnabled</code> value.

