# Terraform::AWS::DbClusterSnapshot

CloudFormation equivalent of aws_db_cluster_snapshot

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DbClusterSnapshot",
    "Properties" : {
        "<a href="#dbclusteridentifier" title="DbClusterIdentifier">DbClusterIdentifier</a>" : <i>String</i>,
        "<a href="#dbclustersnapshotidentifier" title="DbClusterSnapshotIdentifier">DbClusterSnapshotIdentifier</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DbClusterSnapshot
Properties:
    <a href="#dbclusteridentifier" title="DbClusterIdentifier">DbClusterIdentifier</a>: <i>String</i>
    <a href="#dbclustersnapshotidentifier" title="DbClusterSnapshotIdentifier">DbClusterSnapshotIdentifier</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### DbClusterIdentifier

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbClusterSnapshotIdentifier

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AllocatedStorage

Returns the &lt;code&gt;AllocatedStorage&lt;/code&gt; value.

#### AvailabilityZones

Returns the &lt;code&gt;AvailabilityZones&lt;/code&gt; value.

#### DbClusterSnapshotArn

Returns the &lt;code&gt;DbClusterSnapshotArn&lt;/code&gt; value.

#### Engine

Returns the &lt;code&gt;Engine&lt;/code&gt; value.

#### EngineVersion

Returns the &lt;code&gt;EngineVersion&lt;/code&gt; value.

#### KmsKeyId

Returns the &lt;code&gt;KmsKeyId&lt;/code&gt; value.

#### LicenseModel

Returns the &lt;code&gt;LicenseModel&lt;/code&gt; value.

#### Port

Returns the &lt;code&gt;Port&lt;/code&gt; value.

#### SnapshotType

Returns the &lt;code&gt;SnapshotType&lt;/code&gt; value.

#### SourceDbClusterSnapshotArn

Returns the &lt;code&gt;SourceDbClusterSnapshotArn&lt;/code&gt; value.

#### Status

Returns the &lt;code&gt;Status&lt;/code&gt; value.

#### StorageEncrypted

Returns the &lt;code&gt;StorageEncrypted&lt;/code&gt; value.

#### VpcId

Returns the &lt;code&gt;VpcId&lt;/code&gt; value.

