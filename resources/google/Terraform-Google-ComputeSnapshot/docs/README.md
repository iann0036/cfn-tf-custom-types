# Terraform::Google::ComputeSnapshot

CloudFormation equivalent of google_compute_snapshot

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeSnapshot",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#sourcedisk" title="SourceDisk">SourceDisk</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#snapshotencryptionkey" title="SnapshotEncryptionKey">SnapshotEncryptionKey</a>" : <i>[ &lt;a href=&#34;snapshotencryptionkey.md&#34;&gt;SnapshotEncryptionKey&lt;/a&gt;, ... ]</i>,
        "<a href="#sourcediskencryptionkey" title="SourceDiskEncryptionKey">SourceDiskEncryptionKey</a>" : <i>[ &lt;a href=&#34;sourcediskencryptionkey.md&#34;&gt;SourceDiskEncryptionKey&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeSnapshot
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#sourcedisk" title="SourceDisk">SourceDisk</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#snapshotencryptionkey" title="SnapshotEncryptionKey">SnapshotEncryptionKey</a>: <i>
      - &lt;a href=&#34;snapshotencryptionkey.md&#34;&gt;SnapshotEncryptionKey&lt;/a&gt;</i>
    <a href="#sourcediskencryptionkey" title="SourceDiskEncryptionKey">SourceDiskEncryptionKey</a>: <i>
      - &lt;a href=&#34;sourcediskencryptionkey.md&#34;&gt;SourceDiskEncryptionKey&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDisk

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotEncryptionKey

_Required_: No

_Type_: List of &lt;a href=&#34;snapshotencryptionkey.md&#34;&gt;SnapshotEncryptionKey&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDiskEncryptionKey

_Required_: No

_Type_: List of &lt;a href=&#34;sourcediskencryptionkey.md&#34;&gt;SourceDiskEncryptionKey&lt;/a&gt;

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

#### CreationTimestamp

Returns the &lt;code&gt;CreationTimestamp&lt;/code&gt; value.

#### DiskSizeGb

Returns the &lt;code&gt;DiskSizeGb&lt;/code&gt; value.

#### LabelFingerprint

Returns the &lt;code&gt;LabelFingerprint&lt;/code&gt; value.

#### Licenses

Returns the &lt;code&gt;Licenses&lt;/code&gt; value.

#### SelfLink

Returns the &lt;code&gt;SelfLink&lt;/code&gt; value.

#### SnapshotId

Returns the &lt;code&gt;SnapshotId&lt;/code&gt; value.

#### SourceDiskLink

Returns the &lt;code&gt;SourceDiskLink&lt;/code&gt; value.

#### StorageBytes

Returns the &lt;code&gt;StorageBytes&lt;/code&gt; value.

