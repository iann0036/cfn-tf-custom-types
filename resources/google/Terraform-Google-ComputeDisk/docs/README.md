# Terraform::Google::ComputeDisk

CloudFormation equivalent of google_compute_disk

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::ComputeDisk",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#image" title="Image">Image</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#physicalblocksizebytes" title="PhysicalBlockSizeBytes">PhysicalBlockSizeBytes</a>" : <i>Double</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
        "<a href="#snapshot" title="Snapshot">Snapshot</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>,
        "<a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>" : <i>[ &lt;a href=&#34;diskencryptionkey.md&#34;&gt;DiskEncryptionKey&lt;/a&gt;, ... ]</i>,
        "<a href="#sourceimageencryptionkey" title="SourceImageEncryptionKey">SourceImageEncryptionKey</a>" : <i>[ &lt;a href=&#34;sourceimageencryptionkey.md&#34;&gt;SourceImageEncryptionKey&lt;/a&gt;, ... ]</i>,
        "<a href="#sourcesnapshotencryptionkey" title="SourceSnapshotEncryptionKey">SourceSnapshotEncryptionKey</a>" : <i>[ &lt;a href=&#34;sourcesnapshotencryptionkey.md&#34;&gt;SourceSnapshotEncryptionKey&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::ComputeDisk
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#image" title="Image">Image</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#physicalblocksizebytes" title="PhysicalBlockSizeBytes">PhysicalBlockSizeBytes</a>: <i>Double</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>Double</i>
    <a href="#snapshot" title="Snapshot">Snapshot</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
    <a href="#diskencryptionkey" title="DiskEncryptionKey">DiskEncryptionKey</a>: <i>
      - &lt;a href=&#34;diskencryptionkey.md&#34;&gt;DiskEncryptionKey&lt;/a&gt;</i>
    <a href="#sourceimageencryptionkey" title="SourceImageEncryptionKey">SourceImageEncryptionKey</a>: <i>
      - &lt;a href=&#34;sourceimageencryptionkey.md&#34;&gt;SourceImageEncryptionKey&lt;/a&gt;</i>
    <a href="#sourcesnapshotencryptionkey" title="SourceSnapshotEncryptionKey">SourceSnapshotEncryptionKey</a>: <i>
      - &lt;a href=&#34;sourcesnapshotencryptionkey.md&#34;&gt;SourceSnapshotEncryptionKey&lt;/a&gt;</i>
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

#### Image

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

#### PhysicalBlockSizeBytes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Snapshot

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiskEncryptionKey

_Required_: No

_Type_: List of &lt;a href=&#34;diskencryptionkey.md&#34;&gt;DiskEncryptionKey&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceImageEncryptionKey

_Required_: No

_Type_: List of &lt;a href=&#34;sourceimageencryptionkey.md&#34;&gt;SourceImageEncryptionKey&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceSnapshotEncryptionKey

_Required_: No

_Type_: List of &lt;a href=&#34;sourcesnapshotencryptionkey.md&#34;&gt;SourceSnapshotEncryptionKey&lt;/a&gt;

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

#### LabelFingerprint

Returns the &lt;code&gt;LabelFingerprint&lt;/code&gt; value.

#### LastAttachTimestamp

Returns the &lt;code&gt;LastAttachTimestamp&lt;/code&gt; value.

#### LastDetachTimestamp

Returns the &lt;code&gt;LastDetachTimestamp&lt;/code&gt; value.

#### SelfLink

Returns the &lt;code&gt;SelfLink&lt;/code&gt; value.

#### SourceImageId

Returns the &lt;code&gt;SourceImageId&lt;/code&gt; value.

#### SourceSnapshotId

Returns the &lt;code&gt;SourceSnapshotId&lt;/code&gt; value.

#### Users

Returns the &lt;code&gt;Users&lt;/code&gt; value.

