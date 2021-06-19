# TF::Databricks::SqlEndpoint

CloudFormation equivalent of databricks_sql_endpoint

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Databricks::SqlEndpoint",
    "Properties" : {
        "<a href="#autostopmins" title="AutoStopMins">AutoStopMins</a>" : <i>Double</i>,
        "<a href="#clustersize" title="ClusterSize">ClusterSize</a>" : <i>String</i>,
        "<a href="#datasourceid" title="DataSourceId">DataSourceId</a>" : <i>String</i>,
        "<a href="#enablephoton" title="EnablePhoton">EnablePhoton</a>" : <i>Boolean</i>,
        "<a href="#instanceprofilearn" title="InstanceProfileArn">InstanceProfileArn</a>" : <i>String</i>,
        "<a href="#jdbcurl" title="JdbcUrl">JdbcUrl</a>" : <i>String</i>,
        "<a href="#maxnumclusters" title="MaxNumClusters">MaxNumClusters</a>" : <i>Double</i>,
        "<a href="#minnumclusters" title="MinNumClusters">MinNumClusters</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#numclusters" title="NumClusters">NumClusters</a>" : <i>Double</i>,
        "<a href="#spotinstancepolicy" title="SpotInstancePolicy">SpotInstancePolicy</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#odbcparams" title="OdbcParams">OdbcParams</a>" : <i>[ <a href="odbcparamsdefinition.md">OdbcParamsDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Databricks::SqlEndpoint
Properties:
    <a href="#autostopmins" title="AutoStopMins">AutoStopMins</a>: <i>Double</i>
    <a href="#clustersize" title="ClusterSize">ClusterSize</a>: <i>String</i>
    <a href="#datasourceid" title="DataSourceId">DataSourceId</a>: <i>String</i>
    <a href="#enablephoton" title="EnablePhoton">EnablePhoton</a>: <i>Boolean</i>
    <a href="#instanceprofilearn" title="InstanceProfileArn">InstanceProfileArn</a>: <i>String</i>
    <a href="#jdbcurl" title="JdbcUrl">JdbcUrl</a>: <i>String</i>
    <a href="#maxnumclusters" title="MaxNumClusters">MaxNumClusters</a>: <i>Double</i>
    <a href="#minnumclusters" title="MinNumClusters">MinNumClusters</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#numclusters" title="NumClusters">NumClusters</a>: <i>Double</i>
    <a href="#spotinstancepolicy" title="SpotInstancePolicy">SpotInstancePolicy</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#odbcparams" title="OdbcParams">OdbcParams</a>: <i>
      - <a href="odbcparamsdefinition.md">OdbcParamsDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
</pre>

## Properties

#### AutoStopMins

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClusterSize

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DataSourceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnablePhoton

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceProfileArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JdbcUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxNumClusters

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinNumClusters

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NumClusters

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpotInstancePolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OdbcParams

_Required_: No

_Type_: List of <a href="odbcparamsdefinition.md">OdbcParamsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

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

