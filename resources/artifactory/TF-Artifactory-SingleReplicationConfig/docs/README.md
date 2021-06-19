# TF::Artifactory::SingleReplicationConfig

CloudFormation equivalent of artifactory_single_replication_config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Artifactory::SingleReplicationConfig",
    "Properties" : {
        "<a href="#cronexp" title="CronExp">CronExp</a>" : <i>String</i>,
        "<a href="#enableeventreplication" title="EnableEventReplication">EnableEventReplication</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#pathprefix" title="PathPrefix">PathPrefix</a>" : <i>String</i>,
        "<a href="#repokey" title="RepoKey">RepoKey</a>" : <i>String</i>,
        "<a href="#sockettimeoutmillis" title="SocketTimeoutMillis">SocketTimeoutMillis</a>" : <i>Double</i>,
        "<a href="#syncdeletes" title="SyncDeletes">SyncDeletes</a>" : <i>Boolean</i>,
        "<a href="#syncproperties" title="SyncProperties">SyncProperties</a>" : <i>Boolean</i>,
        "<a href="#syncstatistics" title="SyncStatistics">SyncStatistics</a>" : <i>Boolean</i>,
        "<a href="#url" title="Url">Url</a>" : <i>String</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Artifactory::SingleReplicationConfig
Properties:
    <a href="#cronexp" title="CronExp">CronExp</a>: <i>String</i>
    <a href="#enableeventreplication" title="EnableEventReplication">EnableEventReplication</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#pathprefix" title="PathPrefix">PathPrefix</a>: <i>String</i>
    <a href="#repokey" title="RepoKey">RepoKey</a>: <i>String</i>
    <a href="#sockettimeoutmillis" title="SocketTimeoutMillis">SocketTimeoutMillis</a>: <i>Double</i>
    <a href="#syncdeletes" title="SyncDeletes">SyncDeletes</a>: <i>Boolean</i>
    <a href="#syncproperties" title="SyncProperties">SyncProperties</a>: <i>Boolean</i>
    <a href="#syncstatistics" title="SyncStatistics">SyncStatistics</a>: <i>Boolean</i>
    <a href="#url" title="Url">Url</a>: <i>String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### CronExp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableEventReplication

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathPrefix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepoKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SocketTimeoutMillis

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyncDeletes

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyncProperties

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SyncStatistics

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

_Required_: No

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

#### Id

Returns the <code>Id</code> value.

