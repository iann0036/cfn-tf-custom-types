# TF::Artifactory::ReplicationConfig

CloudFormation equivalent of artifactory_replication_config

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Artifactory::ReplicationConfig",
    "Properties" : {
        "<a href="#cronexp" title="CronExp">CronExp</a>" : <i>String</i>,
        "<a href="#enableeventreplication" title="EnableEventReplication">EnableEventReplication</a>" : <i>Boolean</i>,
        "<a href="#repokey" title="RepoKey">RepoKey</a>" : <i>String</i>,
        "<a href="#replications" title="Replications">Replications</a>" : <i>[ <a href="replicationsdefinition.md">ReplicationsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Artifactory::ReplicationConfig
Properties:
    <a href="#cronexp" title="CronExp">CronExp</a>: <i>String</i>
    <a href="#enableeventreplication" title="EnableEventReplication">EnableEventReplication</a>: <i>Boolean</i>
    <a href="#repokey" title="RepoKey">RepoKey</a>: <i>String</i>
    <a href="#replications" title="Replications">Replications</a>: <i>
      - <a href="replicationsdefinition.md">ReplicationsDefinition</a></i>
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

#### RepoKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Replications

_Required_: No

_Type_: List of <a href="replicationsdefinition.md">ReplicationsDefinition</a>

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

